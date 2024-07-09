import pygame as py

# Permet de répartir les instructions dans différentes classes
class Tir(py.sprite.Sprite):
    def __init__(perso, joueur, x, y):
        super().__init__() # Appel d'une superclasse
        perso.vitessex = x
        perso.vitessey = y
        perso.joueur = joueur
        perso.tirs = py.sprite.Group() # Regroupement de tous les tirs
        perso.image = py.image.load("images/seringue.png") # Chargement de l'image
        perso.image = py.transform.scale(perso.image, (160, 80)) # Réuction de la taille de l'image
        perso.rect = perso.image.get_rect()
        perso.rect.x = joueur.rect.x + 150 # Placement initial de la seringue sur l'axe des x
        perso.rect.y = joueur.rect.y + 90 # Placement initial de la seringue sur l'axe des y
        perso.origine_image = perso.image # On garde l'image d'origine qui va nous servir par la suite
        perso.angle = 0

    def rotation(perso): # Rotation de la seringue
        perso.angle += 10
        perso.image = py.transform.rotozoom(perso.origine_image, perso.angle, 1) # Donne l'image avec la rotation argument 1 de notre image d'origine, angle de départ
        perso.rect = perso.image.get_rect(center=perso.rect.center) # Récupération des coordonnées et centrage de l'image

    def suppression(perso):
        perso.joueur.tirs.remove(perso) # Suppression de la seringue

    def deplacement(perso):
        perso.rect.x += perso.vitessex
        perso.rect.y -= perso.vitessey
        perso.rotation()

        for monstre in perso.joueur.jeu.verif_collision(perso, perso.joueur.jeu.monstres): # Vérifie si la seringue est entrée en collision avec un groupe de monstres
            perso.suppression() # Suppression de la seringue
            monstre.degats(perso.joueur.attaque) # Attaque du joueur

        if perso.rect.x > 1080: # Vérifie si la seringue n'est plus sur l'écran
            perso.suppression() # Suppression de la seringue