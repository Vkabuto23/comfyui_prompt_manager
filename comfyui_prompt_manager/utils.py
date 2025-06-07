# utils.py
import os

def get_prompts_dir() -> str:
    """
    Возвращает абсолютный путь к общей папке prompts.
    Создаёт её, если она ещё не существует.
    """
    base = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    prompts_dir = os.path.join(base, "prompts")
    os.makedirs(prompts_dir, exist_ok=True)
    return prompts_dir
