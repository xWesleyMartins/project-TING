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
    result = []
    for index in range(instance.__len__()):
        current = instance.search(index)
        lines_occurencies = []
        for i in range(current["qtd_linhas"]):
            line = current["linhas_do_arquivo"][i]
            if word.lower() in line.lower():
                line_dict = {"linha": i + 1, "conteudo": line}
                lines_occurencies.append(line_dict)
        if any(lines_occurencies):
            file_dict = {
                "palavra": word,
                "arquivo": current["nome_do_arquivo"],
                "ocorrencias": lines_occurencies,
            }
            result.append(file_dict)
    return result
