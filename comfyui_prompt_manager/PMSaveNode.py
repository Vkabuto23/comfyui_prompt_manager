# PMSaveNode.py
import os
from .utils import get_prompts_dir


class PMSaveNode:
    CATEGORY      = "Prompt Manager"
    NODE_TITLE    = "PM Save"
    RETURN_TYPES  = ("STRING",)
    RETURN_NAMES  = ("prompt_text",)
    FUNCTION      = "process"

    WRITEABLE     = ["prompt", "name", "save_prompt"]
    INPUT_LABELS  = {"prompt": "prompt",
                     "name": "name",
                     "save_prompt": "save_prompt"}

    # ── входы ─────────────────────────────────────────────────────
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # большое текстовое окно на 5 строк
                "prompt": ("STRING", {
                    "default": "",
                    "multiline": True,
                    "lines": 5,
                }),
                "name": ("STRING", {"default": ""}),
                # настоящий тумблер-switch, без порта-слота
                "save_prompt": ("BOOLEAN", {
                    "default": False,
                    "forceInput": False,   # ← не выводить вход
                }),
            }
        }
    # ─────────────────────────────────────────────────────────────

    def process(self, prompt: str, name: str, save_prompt: bool):
        """
        • Всегда возвращает prompt.
        • Если save_prompt == True и name непустой – сохраняет
          prompts/<name>.txt.
        """
        if save_prompt and name.strip():
            try:
                path = os.path.join(get_prompts_dir(), f"{name}.txt")
                with open(path, "w", encoding="utf-8") as f:
                    f.write(prompt)
            except Exception as e:
                print(f"[PMSaveNode] error saving prompt: {e}")

        return (prompt,)
