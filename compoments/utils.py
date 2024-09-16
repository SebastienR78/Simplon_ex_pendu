import re


def SecretWord(w):
    symbol = "_"
    mySecretWord = re.sub('[A-Za-zÀ-ú]', symbol, w)
    return mySecretWord