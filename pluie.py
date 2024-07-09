import pygame as py

import monstre
from masque import Masque
from pillule import Pillule
from monstre import Corona_vert, Boss, Corona_rouge

class Pluie:
    def __init__(perso, jeu):
        perso.pourcent = 0
        perso.pourcent_vitesse = 20
        perso.pillules = py.sprite.Group() # Groupe de sprite
        perso.masques = py.sprite.Group() # Groupe de sprite
        perso.jeu = jeu

    def ajout_pourcent(perso):
        perso.pourcent += perso.pourcent_vitesse / 100

    def max_barre(perso):
        return perso.pourcent >= 100 # Définition du pourcentage maximal de la barre d'événements

    def reset_pourcent(perso):
        perso.pourcent = 0

    def pluies(perso):
        perso.pillules.add(Pillule(perso)) # Regroupement des pillules dans un sprite
        perso.masques.add(Masque(perso)) # Regroupement des masques dans un sprite

    def pluie_objet(perso):
        if perso.max_barre():
            perso.pluies()
            perso.reset_pourcent()
            perso.jeu.spawn_monstre(Corona_vert)

    def maj_barre(perso, surface):
        perso.ajout_pourcent()
        perso.pluie_objet()
        # Barre noire
        py.draw.rect(surface, (0, 0, 0), [0, surface.get_height() - 10, surface.get_width(), 10])
        # Barre rouge
        py.draw.rect(surface, (187, 11, 11), [0, surface.get_height() - 10, (surface.get_width() / 100) * perso.pourcent, 10])
