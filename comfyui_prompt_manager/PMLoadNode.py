# PMLoadNode.py
import os
from .utils import get_prompts_dir


class PMLoadNode:
    """
    • Показывает выпадающий список всех .txt в  <ComfyUI-root>/prompts
    • При выборе читает содержимое и:
        – выводит строку prompt_text на выход
        – отображает текст внутри ноды (overlay)
    """

    CATEGORY      = "Prompt Manager"
    NODE_TITLE    = "PM Load"

    RETURN_TYPES  = ("STRING", "NODE_OVERLAY")
    RETURN_NAMES  = ("prompt_text", "overlay")
    FUNCTION      = "load"
    OUTPUT_NODE   = True       # ← заставляет ComfyUI рисовать overlay внутри ноды

    WRITEABLE     = ["file_name"]
    INPUT_LABELS  = {"file_name": "file_name"}

    # -------- dropdown со списком файлов ---------------------------------
    @classmethod
    def INPUT_TYPES(cls):
        prompt_dir = get_prompts_dir()
        files = sorted(
            f for f in os.listdir(prompt_dir) if f.lower().endswith(".txt")
        ) or ["< no .txt files >"]

        # tuple → ComfyUI превращает параметр в выпадающий список
        return {"required": {"file_name": (files,)}}
    # ---------------------------------------------------------------------

    def load(self, file_name: str):
        """
        • Если файла нет (или placeholder), отдаёт пустую строку.
        • overlay содержит {'text': текст, 'image': None} – ComfyUI покажет
          его внутри ноды после любого запуска графа или при Auto Queue.
        """
        prompt_dir = get_prompts_dir()
        path = os.path.join(prompt_dir, file_name)

        text = ""
        if os.path.isfile(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    text = f.read()
            except Exception as e:
                print(f"[PMLoadNode] Can't read {path}: {e}")

        overlay = {"text": text, "image": None}
        return (text, overlay)
