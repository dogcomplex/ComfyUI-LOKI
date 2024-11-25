import re
from torch import Tensor

import os
import cv2


UNARY_COMMANDS = ["DOWN", "LEFT", "RIGHT", "UP", "ACTION-A", "ACTION-B", "START", "INSTINCT"]
FUNCTION_COMMANDS = ["REMEMBER", "REPLACE-JOURNAL", "DRAW", "THOUGHTS", "HELP"]

UNARY_MAPPINGS = [0, 1, 2, 3, 4, 5, 6, 7] # very specific hacky mapping to action codes for gameboy emulator
# note 7 is actually pass action, they dont implement SELECT lol

# special commands
# REMEMBER: writes to journal, appends an entry to journal string
# REPLACE-JOURNAL: replaces entire journal string
# THOUGHTS: writes to feedback string, appends an entry to feedback string
# DRAW: direct comfyui command to draw a picture immediately
# HELP: writes to feedback string with emphasis


class SplitCommand:
  def __init__(self):
        pass

  @classmethod
  def INPUT_TYPES(cls):
    return {
      "required": {
        "command": ("STRING", {"multiline": False}),
      }
    }

  RETURN_TYPES = ("STRING", "STRING")
  RETURN_NAMES = ("command", "input")
  FUNCTION = "split_command"
  CATEGORY = "Text Processing"

  def split_command(self, command):
      """
      Processes a command and its input, if any, and returns the command and input as separate strings.

      Parameters:
      - command (str): The command to process.

      Returns:
      - tuple: A tuple containing the command and its input, if any.
      """
      # Split the command and its input
      # note: it may or may not have an input in brackets
      input = ""
      if '(' in command and ')' in command:
          command, input = command.split('(', 1)
          input = input[:-1]
      return (command, input)


class ProcessCommand:
    
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
      return {
        "required": {
          "command": ("STRING", {"multiline": False}),
          "journal": ("STRING", {"multiline": True, "default": ""}),
          "feedback": ("STRING", {"multiline": True, "default": ""}),
          "prompt": ("STRING", {"multiline": True, "default": ""})
        }
      }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("command_code", "journal", "feedback", "prompt")
    FUNCTION = "process_command"
    CATEGORY = "Text Processing"
    OUTPUT_IS_LIST = (False, False, False, False)
    INPUT_IS_LIST = False

    def process_command(self, command, journal="", feedback="", prompt=""):
        """
        Processes a command and its input, if any, and returns the processed command.
        Extremely specialized to a niche application

        Parameters:
        - command (str): The command to process.
        - input (str): The input to the command, if any.

        Returns:
        - str: The processed command.
        """
        # Process the command and its input
        if command in UNARY_COMMANDS:
            return (UNARY_MAPPINGS[UNARY_COMMANDS.index(command)], journal, feedback, prompt)
        command, input = SplitCommand.split_command(self, command)
        if command in FUNCTION_COMMANDS:
          if command == "REMEMBER":
              journal += "- " + input + "\n"
          elif command == "REPLACE-JOURNAL":
              journal = input
          elif command == "THOUGHTS":
              feedback += input + "\n"
          elif command == "DRAW":
              prompt = input
          elif command == "HELP":
              feedback += "HELP(" + input + ")\n"
          else:
              pass
        else:
            pass
        return (-1, journal, feedback, prompt)

class ProcessCommands:
    
    def __init__(self):
        pass
  
    @classmethod
    def INPUT_TYPES(cls):
      return {
        "required": {
          "commands": ("STRING", {"multiline": True, "forceInput": True}),
          "journal": ("STRING", {"multiline": True, "default": ""}),
          "feedback": ("STRING", {"multiline": True, "default": ""}),
          "prompt": ("STRING", {"multiline": True, "default": ""})
        }
      }
  
    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("command_codes", "journal", "feedback", "prompt")
    FUNCTION = "process_commands"
    CATEGORY = "Text Processing"
    OUTPUT_IS_LIST = (False, False, False, False)
    INPUT_IS_LIST = True
  
    def process_commands(self, commands, journal="", feedback="", prompt=""):
        """
        Processes a list of commands and returns the processed commands.

        Parameters:
        - commands (list): A list of commands to process.

        Returns:
        - list: A list of processed commands.
        """
        pc = ProcessCommand()
        command_codes = []
        for command in commands:
            command_code, journal, feedback, prompt = pc.process_command(command, journal, feedback, prompt)
            command_codes.append(command_code)
        # filter -1 commands
        command_codes = list(filter(lambda x: x != -1, command_codes))
        command_codes = list(map(str, command_codes))
        # very counter-intuitive but we seemingly have to join these?
        return (' '.join(command_codes), ''.join(journal), ''.join(feedback), ''.join(prompt),)

class ParseCommands:
  
  def __init__(self):
      pass

  @classmethod
  def INPUT_TYPES(cls):
    return {
      "required": {
        "text": ("STRING", {"multiline": True})
      }
    }

  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("commands",)
  FUNCTION = "parse_commands"
  CATEGORY = "Text Processing"
  
  OUTPUT_IS_LIST = (True,)

  def parse_commands(self, text):
      """
      Parses the input text and extracts valid commands, including those with text inputs within brackets.

      Parameters:
      - text (str): The input text containing commands.

      Returns:
      - list: A list of valid commands found in the input text, preserving their order.
      """
      # Prepare regex pattern to match both types of commands
      # This pattern looks for either a unary command or a function command with its arguments
      # a unary command will be standalone, while a function command will either have its arguments in brackets or after a colon
      # OR a function command will have its arguments after a colon, ending in newline
      pattern = r"(?P<command>" + "|".join(UNARY_COMMANDS) + r")"
      pattern += r"|(?P<command2>" + "|".join(FUNCTION_COMMANDS) + r")"
      pattern += r" ?\((?P<args>[^\)]+)\)| ?: ?\n?(?P<args2>[^\n]+)"

      # Initialize the result list
      result = []

      # Find all matches using the combined pattern
      matches = re.finditer(pattern, text)

      # Process each match
      for match in matches:
          # Get the command and arguments from the match
          command = match.group("command") or match.group("command2")
          args = match.group("args") or match.group("args2")

          # If the command is a unary command, add it to the result list
          if command in UNARY_COMMANDS:
              result.append(command)
          # If the command is a function command, add it to the result list with its arguments
          elif command in FUNCTION_COMMANDS:
              result.append(command + "(" + args + ")")

      # Return the result list
      return (result,)

    
class ReplaceViaDictionary:
  
  def __init__(self):
      pass

  @classmethod
  def INPUT_TYPES(cls):
    return {
      "required": {
        "text": ("STRING", {"multiline": True}),
        "dictionary": ("STRING", {"multiline": True})
      },
      "optional": {
        "separator": ("STRING", {"multiline": True, "default": "_$_"})
      }
    }

  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("text",)
  FUNCTION = "replace_via_dictionary"
  CATEGORY = "Text Processing"

  def replace_via_dictionary(self, text, dictionary="", separator="_$_"):
      """
      Replaces the keys in the text with the corresponding values in the dictionary.
      The keys are surrounded by the separator.
      Dictionary format: key1==value1|key2==value2|...|keyN==valueN
      """
      dictionary = dictionary.split("|")
      dictionary = {k.split("==")[0]: k.split("==")[1] for k in dictionary}
      for key in dictionary:
          text = text.replace(separator + key + separator, dictionary[key])
      return (text,)


class ListToString:
  
  def __init__(self):
      pass

  @classmethod
  def INPUT_TYPES(cls):
    return {
      "required": {
        "list": ("STRING", {"multiline": False, "forceInput": True}),
      },
      "optional": {
        "separator": ("STRING", {"multiline": True, "default": ", "})
      }
    }

  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("text",)
  FUNCTION = "list_to_string"
  CATEGORY = "Text Processing"
  OUTPUT_IS_LIST = (False,)
  INPUT_IS_LIST = True

  def list_to_string(self, list=[], separator=[]):
      text = ""
      default_separator = ", "
      if separator == []:
          separator = default_separator
      else:
          separator = str(separator[0])
      # list and separator are lists 
      for item in list:
          text += str(item) + separator
      text = text[:-len(separator)]
      return (text,)

class StringToList:
  
  def __init__(self):
      pass

  @classmethod
  def INPUT_TYPES(cls):
    return {
      "required": {
        "text": ("STRING", {"multiline": False, "forceInput": True}),
      },
      "optional": {
        "separator": ("STRING", {"multiline": True, "default": ", "})
      }
    }

  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("list",)
  FUNCTION = "string_to_list"
  CATEGORY = "Text Processing"
  OUTPUT_IS_LIST = (True,)
  INPUT_IS_LIST = False

  def string_to_list(self, text, separator="_$_"):
      list = text.split(separator)
      return (list,)


class SaveImageOverwrite:
   
  def __init__(self):
       pass
   
  @classmethod
  def INPUT_TYPES(cls):
    return {
      "required": {
        "image": ("IMAGE", {"forceInput": True}),
        "filename": ("STRING", {"multiline": False}),
        "overwrite": ("BOOLEAN", {"default": False})
      }
    }

  RETURN_TYPES = ("IMAGE",)
  RETURN_NAMES = ("image",)
  FUNCTION = "save_image_overwrite"
  CATEGORY = "Image Processing"
  OUTPUT_IS_LIST = (False,)
  INPUT_IS_LIST = False
  OUTPUT_NODE = True


  def save_image_overwrite(self, images: Tensor, filename, overwrite=False):
      # image is a tensor, might be just a single image
      if os.path.exists(filename) and not overwrite:
          return (image,)
      if images is None:
          print(f"Warning: trying to save {filename}, but no images were provided")
          return

      counter = 1
      for image in images:
          i = 255. * image.cpu().numpy()
          img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
          metadata = None
          if embed_metadata:
              metadata = PngInfo()
              if prompt is not None:
                  metadata.add_text("prompt", json.dumps(prompt))
              if extra_pnginfo is not None:
                  for x in extra_pnginfo:
                      metadata.add_text(x, json.dumps(extra_pnginfo[x]))

          file = f"{filename}-{counter}.png" if counter > 1 else f"{filename}.png"
          counter = counter + 1

          img.save(os.path.join(full_path, file), pnginfo=metadata, compress_level=4)


   

# A dictionary that contains all nodes you want to export with their names
NODE_CLASS_MAPPINGS = {
    "ReplaceViaDictionary": ReplaceViaDictionary,
    "SplitCommand": SplitCommand,
    "ProcessCommand": ProcessCommand,
    "ProcessCommands": ProcessCommands,
    "ParseCommands": ParseCommands,
    "ListToString": ListToString,
    "StringToList": StringToList,
    "SaveImageOverwrite": SaveImageOverwrite
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "ReplaceViaDictionary": "Replace via Dictionary",
    "SplitCommand": "Split Command",
    "ProcessCommand": "Process Command",
    "ProcessCommands": "Process Commands",
    "ParseCommands": "Parse Commands",
    "ListToString": "List to String",
    "StringToList": "String to List",
    "SaveImageOverwrite": "Save Image Overwrite"
}
