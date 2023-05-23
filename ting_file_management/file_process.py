from ting_file_management.file_management import txt_importer
import sys


def file_exists_in_queue(path_file, queue):
    return any(item["nome_do_arquivo"] == path_file for item in queue)


def process(path_file, instance):
    if file_exists_in_queue(path_file, instance.queue):
        return None

    data = txt_importer(path_file)

    obj = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data,
    }

    instance.enqueue(obj)

    print(f"{obj}", file=sys.stdout)


def remove(instance):
    if instance:
        queue_item = instance.dequeue()["nome_do_arquivo"]
        message = f"Arquivo {queue_item} removido com sucesso"
        print(message)
    else:
        print("Não há elementos")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
