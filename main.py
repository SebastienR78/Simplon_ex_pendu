import compoments.utils as utils
import compoments.WordDictionnary as dictio
import compoments.graph as graph
import re
import unidecode # https://www.geeksforgeeks.org/how-to-remove-string-accents-using-python-3/

def isLetter(c):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if c.isnumeric():
        print('Rentrer une lettre')
        return False
    elif regex.search(c) is not None:
        print('Ceci n\'est pas une lettre')
        return False
    else:
        return True
def loopTestUserLetter(OneWord, Sword):
    nbTent= 0
    reussite = False
    while  nbTent < len(OneWord)  and  not reussite  :
        print(f"veuillez trouver le mot secret :{Sword}?. Il vous reste {len(OneWord)-nbTent} ")
        lettre = input('Veuillez rentrer une lettre : ')
        if isLetter(lettre):
            if lettre.lower() not in OneWord.lower() :
                print('La lettre n\'est pas dans le mot !' )
                nbTent +=1
                graph.afficher_pendu(nbTent)
            else :
                print('Bravo! votre lettre est  dans le mot')
                for index in range(len(OneWord)):
                    # sup la Case et les accents pour tester
                    if unidecode.unidecode(OneWord[index].lower()) == unidecode.unidecode(lettre.lower()):
                        s = list(Sword)
                        s[index] = OneWord[index]
                        Sword = "".join(s)
                        if "_" not in Sword:
                            reussite = True
    return reussite

myWord = dictio.RandomWord()
print(myWord)

def pendu(OneWord):
    Sword = utils.SecretWord(myWord)
    print(Sword)
    reussite = loopTestUserLetter(OneWord, Sword)
    if not reussite:
        result = f" PERDU, le mot était : {myWord} "
        print("")
        print(f'{result :=^80}')
        print("")
    else:
        result = f" BRAVO, le mot est donc : {myWord} "
        print("")
        print(f'{result :=^80}')
        print("")
pendu(myWord)



