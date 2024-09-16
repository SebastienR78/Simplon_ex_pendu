import random

# myWordList =[
#     'Amoureux', 'Baladeur', 'Bavarder', 'Bonbonne', 'Cadratin',
#     'Capuchet', 'Cendrier', 'Chiffons', 'Cloportes', 'Comédien',
#     'Cravate', 'Dérision', 'Disputer', 'Douanier', 'Éclectif',
#     'Exploits', 'Fabuleux', 'Fourrure', 'Galeries', 'Goudrons',
#     'Habituel', 'Haletant', 'Historié', 'Hurlante', 'Inédites',
#     'Joueurse', 'Jumelage', 'Labyrint', 'Larguées',
#     'Maquette', 'Mélodies', 'Modestes', 'Nombrils', 'Nourries',
#     'Observer', 'Optimisé', 'Ouverture', 'Parlante', 'Polisson',
#     'Rassurer', 'Romances', 'Rutilant', 'Sapajous', 'Silicone',
#     'Tentures', 'Tintamar', 'Tourment', 'Triomphe', 'Vibrants'
# ]

myWordList =[
    'Banane', 'Poulpe', 'Tomate', 'Crayon', 'Oiseau',
    'Loutre', 'Gaufre', 'Vallon', 'Chasse', 'Bateau',
    'Ballon', 'Soleil', 'Orange', 'Gâteau', 'Carafe',
    'Valise', 'Poulet', 'Rapide', 'Tendre', 'Cloche',
    'Puzzle', 'Glande', 'Ciment', 'Tableau', 'Coyote',
    'Bonbon', 'Fourmi', 'Bureau', 'Garçon', 'Siffle',
    'Froide', 'Muscle', 'Cactus', 'Beurre', 'Eponge',
    'Papier', 'Travail', 'Niveau', 'Plante', 'Vivier',
    'Forage', 'Ramper', 'Courir', 'Bander', 'Parler',
    'Pample', 'Bourse', 'Mouton', 'Rouage', 'Fermer'
]

def RandomWord():
    word = random.choice(myWordList)
    return word
