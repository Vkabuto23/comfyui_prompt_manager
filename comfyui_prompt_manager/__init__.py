# __init__.py
from .PMSaveNode import PMSaveNode
from .PMLoadNode import PMLoadNode

NODE_CLASS_MAPPINGS = {
    "PMSaveNode": PMSaveNode,
    "PMLoadNode": PMLoadNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PMSaveNode": "💾 PM Save",
    "PMLoadNode": "📂 PM Load",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
