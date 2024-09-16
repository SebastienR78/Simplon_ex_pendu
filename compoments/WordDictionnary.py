import random

myWordList =[
    'Amoureux', 'Baladeur', 'Bavarder', 'Bonbonne', 'Cadratin',
    'Capuchet', 'Cendrier', 'Chiffons', 'Cloportes', 'Comédien',
    'Cravate', 'Dérision', 'Disputer', 'Douanier', 'Éclectif',
    'Exploits', 'Fabuleux', 'Fourrure', 'Galeries', 'Goudrons',
    'Habituel', 'Haletant', 'Historié', 'Hurlante', 'Inédites',
    'Joueurse', 'Jumelage', 'Labyrint', 'Larguées',
    'Maquette', 'Mélodies', 'Modestes', 'Nombrils', 'Nourries',
    'Observer', 'Optimisé', 'Ouverture', 'Parlante', 'Polisson',
    'Rassurer', 'Romances', 'Rutilant', 'Sapajous', 'Silicone',
    'Tentures', 'Tintamar', 'Tourment', 'Triomphe', 'Vibrants'
]

def RandomWord():
    word = random.choice(myWordList)
    return word
