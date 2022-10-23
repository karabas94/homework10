"""
Написать функцию цензор. На вход функция получает имя файла и список слов для замены, функция ничего не возвращает,
но в результате ее работы необходимо создать файл, в котором слова из списка заменены шаблоном(звездочками например)
"""


def censor(filename: str, blacklist: list):
    """This function is censor. Function have file with text and list of string
    with bad words which will be replaced by stars and create censored file"""
    for word in blacklist:
        with open(filename, "r") as file:
            read_text = file.read().replace(word, "*" * len(word))
        with open(filename, "w") as file:
            file.write(read_text)
        with open("censor_text.txt", "w") as file:
            file.write(read_text)


li = ["Russia", "Belarus", "Lukashenko"]
censor("text.txt", li)
