from .scribe_node import Scribe

# Using information from scribe_name.md and scribe.json
NODE_CLASS_MAPPINGS = {
    "✍️Scribe (LOKI)": Scribe
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "✍️Scribe (LOKI)": "✍️ Scribe Workflow Documenter (LOKI)"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

# Print a message to the console when the node is loaded
print("\n----------------------------------------")
print("🦊 LOKI: Loaded Scribe node")
print("    [✓] Class: Scribe")
print("    [✓] Display Name: ✍️ Scribe Workflow Documenter (LOKI)")
print("----------------------------------------\n") 