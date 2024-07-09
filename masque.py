import pygame as py
import random

class Masque(py.sprite.Sprite):
    def __init__(perso, pluie):
        super().__init__()
        perso.image = py.image.load("images/masque.png") # On charge masque.png depuis images et l'attribue à une variable
        perso.image = py.transform.scale(perso.image, (120, 60)) # Réduction de la taille de l'image
        perso.rect = perso.image.get_rect() # Récupération la position
        perso.vitesse = random.randint(3, 5) # Vitesse aléatoire des masques
        perso.rect.x = random.randint(20, 800) # Déplace le perso sur l'axe des x de facon aléatoire
        perso.rect.y = - random.randint(0, 800) # Déplace le perso sur l'axe des y de facon aléatoire
        perso.pluie = pluie

    def suppression(perso):
        perso.pluie.masques.remove(perso) # Supprime le masque

    def chute(perso):
        perso.rect.y += perso.vitesse
        if perso.rect.y >= 650: # Si le masque touche le sol
            perso.suppression()
        if perso.pluie.jeu.verif_collision(perso, perso.pluie.jeu.joueurs): # Vérifie la collision entre le perso et le masque
            perso.suppression() # Supprime si collision
            if perso.pluie.jeu.joueur.vie < perso.pluie.jeu.joueur.max_vie:
                perso.pluie.jeu.joueur.vie += 20 # Augmente la vie du joueur si celle-ci n'est pas maximale
