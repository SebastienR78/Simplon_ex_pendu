import compoments.utils as utils
import compoments.WordDictionnary as dictio
import re


myWord = dictio.RandomWord()
print(myWord)

def pendu(OneWord):
    Sword = utils.SecretWord(myWord)
    print(Sword)
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    nbCaract = len(OneWord)
    nbTent= 0
    reussite = False
    while  nbTent < nbCaract  and  reussite == False  :
        print(f"veuillez trouver le mot secret :{Sword}?. Il vous reste {nbCaract-nbTent} ")
        lettre = input('Veuillez rentrer une lettre : ')
        if lettre.isnumeric():
            print('Rentrer une lettre')
        elif regex.search(lettre) != None:
            print('Ceci n\'est pas une lettre')
        else :
            if lettre.lower() not in OneWord.lower() :
                print('La lettre n\'est pas dans le mot !' )
                nbTent +=1
            else :
                print('Bravo! votre lettre est  dans le mot')
                for index in range(len(OneWord)):
                    if OneWord[index].lower() == lettre.lower():
                        print(Sword)
                        s = list(Sword)
                        s[index] = OneWord[index]
                        Sword = "".join(s)
                        if "_" not in Sword:
                            reussite = True
    if reussite == False:
        print(f"PERDU, le mot était : {myWord}")
    else:
        print(f"bravo, le mot est donc : {myWord}")
pendu(myWord)



