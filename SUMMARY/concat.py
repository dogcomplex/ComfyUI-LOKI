import os
import sys
import json
from datetime import datetime

# Define encodings globally for use in multiple functions
encodings = ['utf-8', 'latin-1', 'cp1252']

if len(sys.argv) != 2:
    print("Usage: python concat.py <config_key>")
    sys.exit(1)

config_path = sys.argv[1]

if os.path.isdir(config_path):
    print(f"Error: Configuration path '{config_path}' is a directory. Please provide a path to a JSON configuration file.")
    sys.exit(1)

with open(config_path, 'r') as config_file:
    configs = json.load(config_file)

config = configs['concat']

excluded_files = config["excluded_files"]
excluded_files_with_tree = config["excluded_files_with_tree"]
excluded_file_types = tuple(config["excluded_file_types"])
# Convert excluded folder names to lowercase for case-insensitive comparison
excluded_folders = [ef.lower() for ef in config.get("excluded_folders", [])]
excluded_contents_folder = [ecf.lower() for ecf in config.get("excluded_contents_folder", [])]
target_folder = configs["target"]
output_folder = "SUMMARY/summaries" # Hardcoded to ensure output to SUMMARY/summaries
original_config_output_folder = configs.get("output") # Keep original for potential logging if needed
if original_config_output_folder != output_folder:
    print(f"INFO: Overriding output folder from config ('{original_config_output_folder}') to '{output_folder}'")
name = configs["name"]

# Helper function to get file size in characters
def get_file_size_chars(file_path):
    global encodings
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                return len(f.read())
        except UnicodeDecodeError:
            continue
        except OSError:  # Handles FileNotFoundError, PermissionError, etc.
            return 0  # Cannot read or access, count as 0 chars
    return 0  # All decodings failed or file is empty/unreadable

# Recursive helper for generating tree summary
def _generate_summary_recursive_helper(current_path, indent):
    global excluded_files, excluded_file_types, excluded_folders # Use global config lists
    
    child_lines = []
    current_dir_total_chars = 0

    try:
        items = sorted(os.listdir(current_path))
    except OSError:
        return [], 0 # Cannot list directory

    for item_name in items:
        item_full_path = os.path.join(current_path, item_name)

        if os.path.isdir(item_full_path):
            item_name_lower = item_name.lower() # Get lowercase of the directory name itself

            # First, check if the directory name itself is in the excluded_folders list
            if item_name_lower in excluded_folders:
                continue

            # Case-insensitive check for excluded folders based on full path components
            path_components_lower = [comp.lower() for comp in item_full_path.split(os.path.sep)]
            if any(excluded_folder_lower in path_components_lower for excluded_folder_lower in excluded_folders):
                continue

            sub_child_lines, sub_dir_chars = _generate_summary_recursive_helper(
                item_full_path,
                indent + 4
            )
            child_lines.append(f"{' ' * indent}+-- {item_name} ({sub_dir_chars} chars)")
            if sub_child_lines: # Only extend if there are actual child lines
                child_lines.extend(sub_child_lines)
            current_dir_total_chars += sub_dir_chars
        else:  # It's a file
            if any(item_name.endswith(ext) for ext in excluded_file_types) or \
               item_name in excluded_files: # Exclude based on type or specific file name
                continue

            chars_in_file = get_file_size_chars(item_full_path)
            child_lines.append(f"{' ' * indent}+-- {item_name} ({chars_in_file} chars)")
            current_dir_total_chars += chars_in_file
            
    return child_lines, current_dir_total_chars

# Main function to generate the complete tree summary string
def generate_tree_summary(root_dir_path):
    root_folder_name = os.path.basename(os.path.abspath(root_dir_path)) # Get a clean name for the root
    
    child_lines, total_project_chars = _generate_summary_recursive_helper(
        root_dir_path,
        0  # Start indent at 0 for items directly under root_dir
    )
    
    summary_string = f"+-- {root_folder_name} ({total_project_chars} chars)\n"
    summary_string += "\n".join(child_lines)
    return summary_string

def print_file_tree(root_dir, indent=0, result=""):
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        if os.path.isdir(item_path):
            item_lower = item.lower() # Get lowercase of the directory name itself

            # First, check if the directory name itself is in the excluded_folders list
            if item_lower in excluded_folders:
                continue

            # Case-insensitive check for excluded folders based on full path components
            # This is more for nested excluded folders or if excluded_folders contains paths like 'some/folder_to_exclude'
            path_components_lower = [comp.lower() for comp in item_path.split(os.path.sep)]
            if any(excluded_folder in path_components_lower for excluded_folder in excluded_folders):
                continue
            
            # Special handling for __tests__ might still be relevant if it's only in excluded_contents_folder
            if item == "__tests__":
                result += " " * indent + "+-- " + item + "\n"
                for test_file in os.listdir(item_path):
                    if os.path.isfile(os.path.join(item_path, test_file)):
                        if not test_file.endswith(excluded_file_types) and test_file not in excluded_files:
                            result += " " * (indent + 4) + "+-- " + test_file + "\n"
            else:
                print("file: ", item_path)
                result += " " * indent + "+-- " + item + "\n"
                result = print_file_tree(item_path, indent + 4, result)
        else:
            if not item.endswith(excluded_file_types) and item not in excluded_files:
                result += " " * indent + "+-- " + item + "\n"
    return result

def concatenate_files(root_dir):
    result = ''
    global encodings
    
    combined_excluded_folders = excluded_folders + excluded_contents_folder

    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Modify dirnames in-place to prevent os.walk from traversing into excluded directories
        # This checks direct folder names for exclusion.
        dirnames[:] = [d for d in dirnames if d.lower() not in combined_excluded_folders]

        # Additionally, check if the current dirpath itself is part of an excluded path structure.
        # This handles cases where an excluded folder might be deeper in the path (e.g., 'some_dir/exclude_this').
        # However, with the dirnames[:] modification above for direct names, this primarily acts as a safeguard
        # for paths that might match excluded_folders pattern like 'foo/bar' rather than just 'bar'.
        path_components_lower = [comp.lower() for comp in dirpath.split(os.path.sep)]
        # Check against 'excluded_folders' for structural path exclusion (like .git/logs should be skipped if .git is excluded)
        # and against 'combined_excluded_folders' if we also want to skip contents of folders listed only in 'excluded_contents_folder'
        # For concatenating content, if the folder is in combined_excluded_folders, we skip its files.
        if any(excluded_folder in path_components_lower for excluded_folder in combined_excluded_folders):
            continue

        for filename in filenames:
            if not any(filename.endswith(ext) for ext in excluded_file_types) and filename not in excluded_files + excluded_files_with_tree:
                file_path = os.path.join(dirpath, filename)
                relative_path = os.path.relpath(file_path, start=os.getcwd())
                
                file_content = None
                for encoding in encodings:
                    try:
                        with open(file_path, 'r', encoding=encoding) as f:
                            file_content = f.read()
                            break
                    except UnicodeDecodeError:
                        continue
                
                if file_content is not None:
                    header_path = os.path.join(target_folder, relative_path)
                    result += f"{header_path}\n{file_content}\n\n"
                else:
                    header_path = os.path.join(target_folder, relative_path)
                    result += f"{header_path}\n```\nUnable to decode file content.\n```\n"
    return result

base_prompt = """Here is the file tree and contents of all files in the project:
"""

if __name__ == "__main__":
    root_dir = target_folder
    result = "target_folder: " +  target_folder + "/" + "\n"

    tree = print_file_tree(root_dir, 0 ,result)
    concatenated_content = concatenate_files(root_dir) # Renamed 'result' to 'concatenated_content' to avoid clash
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S.%f')[:-3]
    
    # Main output file
    output_filename = f"{timestamp}_{name}.txt"
    print("output_filename: ", output_filename)
    print("output_folder: ", output_folder)
    output_path = os.path.join(output_folder, output_filename)
    print("output_path: ", output_path) # Corrected print statement

    os.makedirs(output_folder, exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.write(base_prompt + tree + concatenated_content)

    # Generate and write tree summary
    print("Generating tree summary...")
    tree_summary_content = generate_tree_summary(root_dir)
    summary_output_filename = f"{timestamp}_{name}_summary.txt"
    summary_output_path = os.path.join(output_folder, summary_output_filename)
    
    print(f"Saving tree summary to: {summary_output_path}")
    with open(summary_output_path, 'w', encoding='utf-8') as summary_file:
        summary_file.write(tree_summary_content)
    
    print("Tree summary generated successfully.")