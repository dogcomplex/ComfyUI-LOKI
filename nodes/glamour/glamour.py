# glamour.py - LOKI Script layer for Glamour node functionality

import argparse
import os
import sys

# Determine the parent directory of the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
# Add the parent directory (ComfyUI-LOKI/nodes) to sys.path
# This allows importing from sibling directories like 'glamour'
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Try importing the utility function
try:
    from glamour.glamour_utils import GlamourImageManager
except ImportError as e:
    print(f"Error importing GlamourImageManager: {e}")
    print("Please ensure the script is run from within the ComfyUI-LOKI directory structure,")
    print("or that ComfyUI-LOKI/nodes is in your PYTHONPATH.")
    GlamourImageManager = None # Indicate failure

def check_image(image_id, node_type):
    """Checks the status of a specific glamour image."""
    if not GlamourImageManager:
        print("GlamourImageManager could not be loaded. Cannot check image.")
        return

    print(f"--- Checking Glamour Image ---")
    print(f"  Image ID: {image_id}")
    print(f"  Node Type: {node_type if node_type else 'N/A'}")
    try:
        path = GlamourImageManager.get_image_path(image_id, node_type)
        abs_path = os.path.abspath(path)
        exists = os.path.exists(abs_path)
        print(f"  Resolved Path: {abs_path}")
        print(f"  Exists: {exists}")
        if exists:
            timestamp = os.path.getmtime(abs_path)
            print(f"  Last Modified Timestamp: {timestamp}")
            size = os.path.getsize(abs_path)
            print(f"  Size (bytes): {size}")
        else:
             print(f"  Reason: File not found at the expected location.")

    except Exception as e:
        print(f"  Error during check: {e}")
    print(f"-----------------------------")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="LOKI Glamour Script Utilities. Provides command-line access to check Glamour image assets.",
        epilog="Example: python glamour.py --check my_node_output_001 --type SaveImageNode"
    )
    parser.add_argument(
        "--check",
        metavar="IMAGE_ID",
        required=True,
        help="Check status of a Glamour image by its base ID (e.g., the output filename without extension)."
    )
    parser.add_argument(
        "--type",
        metavar="NODE_TYPE",
        default=None,
        help="Optional: Node type associated with the image ID (used for potential type-specific subdirectories)."
    )

    args = parser.parse_args()

    if GlamourImageManager: # Proceed only if import was successful
        check_image(args.check, args.type)
    else:
        # Error message already printed during import attempt
        sys.exit(1) # Exit with error code 