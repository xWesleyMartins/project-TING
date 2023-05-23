def exists_word(word, instance):
    result = [
        {
            "palavra": word,
            "arquivo": queue["nome_do_arquivo"],
            "ocorrencias": [
                {"linha": index + 1}
                for index, phrase in enumerate(queue["linhas_do_arquivo"])
                if word.casefold() in phrase.casefold()
            ],
        }
        for queue in instance.queue
        if any(
            word.casefold() in phrase.casefold()
            for phrase in queue["linhas_do_arquivo"]
        )
    ]
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
