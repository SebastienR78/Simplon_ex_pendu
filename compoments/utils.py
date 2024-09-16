# from WordDictionnary import RandomWord

import WordDictionnary as dictio
import re


def SecretWord():
    myWordSelected = dictio.RandomWord()
    print("selected : ",myWordSelected)
    symbol = "_"
    mySecretWord = re.sub('[A-Za-zÀ-ú]', symbol, myWordSelected)
    return mySecretWord

print(SecretWord())