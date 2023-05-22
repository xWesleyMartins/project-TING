import sys


def is_txt_file(path_file: str) -> bool:
    return path_file.split(".")[-1] == "txt"


def txt_importer(path_file: str):
    txt_stderr = sys.stderr
    if not is_txt_file(path_file):
        print("Formato inválido", file=txt_stderr)
        return []
    try:
        with open(path_file) as file:
            content = file.read()
            return content.split("\n")
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=txt_stderr)
