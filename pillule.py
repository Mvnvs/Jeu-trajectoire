import pygame as py
import random

class Pillule(py.sprite.Sprite):
    def __init__(perso, pluie):
        super().__init__()
        perso.image = py.image.load("images/pillule.png") # Charge pillule.png depuis images
        perso.image = py.transform.scale(perso.image, (120, 60)) # Réduction de la taille d'image
        perso.rect = perso.image.get_rect() # Récupère les positions de l'image
        perso.vitesse = random.randint(3, 5) # Vitesse aléatoire des pillules
        perso.rect.x = random.randint(20, 800) # Déplace sur l'axe des x de facon aléatoire
        perso.rect.y = - random.randint(0, 800) # Déplace sur l'axe des y de facon aléatoire
        perso.pluie = pluie

    def suppression(perso):
        perso.pluie.pillules.remove(perso) # Supprime la pillule

    def chute(perso):
        perso.rect.y += perso.vitesse
        if perso.rect.y >= 650: # Si la pillule touche le sol
            perso.suppression() # Alors elle est supprimée
        if perso.pluie.jeu.verif_collision(perso, perso.pluie.jeu.joueurs): # Vérifie la collision entre le perso et la pillule
            perso.suppression() # Suppression de la pillule
            perso.pluie.jeu.joueur.degats(20) # Baisse la vie du joueur de 20 points