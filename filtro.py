def filtro(command,deletion):
    lista = list(command.split(" "))
    stopwords = ["translate","plot","ratings"]
    stopwords.append(deletion)
    for word in list(lista):
        if word in stopwords:
            lista.remove(word)
    comando = ' '.join(str(e) for e in lista)
    return comando