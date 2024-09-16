import matplotlib.pyplot as plt

def afficher_pendu(nb_erreurs):
    """
    Affiche le pendu en fonction du nombre d'erreurs.
    """
    plt.figure()  # Crée une nouvelle figure
    # Dessine la potence
    plt.plot([0, 1], [0, 0], 'k')  # Base
    plt.plot([0.5, 0.5], [0, 1], 'k')  # Poteau vertical
    plt.plot([0.5, 1], [1, 1], 'k')  # Barre horizontale
    plt.plot([1, 1], [0.9, 0.8], 'k')  # Corde
    # Dessine le corps du pendu en fonction du nombre d'erreurs
    if nb_erreurs > 0:  # Tête
        cercle = plt.Circle((1, 0.75), 0.1, color='k', fill=False)
        plt.gca().add_patch(cercle)
    if nb_erreurs > 1:  # Corps
        plt.plot([1, 1], [0.7, 0.5], 'k')
    if nb_erreurs > 2:  # Bras gauche
        plt.plot([1, 0.9], [0.65, 0.55], 'k')
    if nb_erreurs > 3:  # Bras droit
        plt.plot([1, 1.1], [0.65, 0.55], 'k')
    if nb_erreurs > 4:  # Jambe gauche
        plt.plot([1, 0.9], [0.5, 0.4], 'k')
    if nb_erreurs > 5:  # Jambe droite
        plt.plot([1, 1.1], [0.5, 0.4], 'k')
    # Paramètres d'affichage
    plt.axis('off')  # Cache les axes
    plt.xlim(-0.2, 1.4)  # Ajuste les limites de l'axe x
    plt.ylim(-0.2, 1.2)  # Ajuste les limites de l'axe y
    plt.gca().set_aspect('equal')  # Maintient l'aspect proportionnel
    plt.show()  # Affiche le pendu