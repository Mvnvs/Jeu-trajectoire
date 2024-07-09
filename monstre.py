import pygame as py
import random
import animation
import jeu
from joueur import Joueur

class Monstre(animation.SpriteAnime):
    def __init__(perso, jeu, nom):
        super().__init__(nom)
        perso.jeu = jeu
        perso.vie = 100 # Vie du monstre
        perso.max_vie = 100 # Vie max du monstre
        perso.attaque = 1 # Attaque du monstre
        perso.rect = perso.image.get_rect() # Récupère les coordonnées de l'image
        perso.rect.x = 930 + random.randint(50, 300) # Placement initial aléatoire du monstre sur l'axe des x
        perso.rect.y = random.randint(50, 550) # Placement initial aléatoire du monstre sur l'axe des y
        perso.vitesse = 2 # Vitesse du monstre
        perso.lancement_animation()

    def degats(perso, compteur):
        perso.vie -= compteur

        if perso.vie <= 0: # Vérifier si son nombre de point de vie est inférieur ou égal à 0
            perso.rect.x = 1000 + random.randint(50, 300) # Réapparition comme un nouveau monstre
            perso.rect.y = random.randint(50, 550)
            perso.vitesse = 2
            perso.vie = perso.max_vie
            perso.jeu.score += 1

    def maj_animation(perso):
        perso.anime(boucle=True)

    def maj_barre_vie(perso, surface):
        couleur_barre = (91, 211, 30) # Couleur barre de vie
        couleur_fond = (120, 123, 118)  # Couleur arrière plan barre de vie
# Défini la position de notre jauge de vie ainsi que sa largeur
        position_barre = [perso.rect.x + 2, perso.rect.y - 10, perso.vie, 5]
        position_fond = [perso.rect.x + 2, perso.rect.y - 10, perso.max_vie, 5]

        py.draw.rect(surface, couleur_fond, position_fond)  # Dessin de l'arrière plan de la barre de vie
        py.draw.rect(surface, couleur_barre, position_barre) # Dessin de la barre de vie

    def suppression(perso):
        perso.jeu.monstres.remove(perso)  # Supprime le monstre

    def deplacement_monstre(perso):
        # Déplacement réalisé seulement s'il n'y a pas de collision avec le joueur
        if not perso.jeu.verif_collision(perso, perso.jeu.joueurs):
            perso.rect.x -= perso.vitesse # Déplacement du monstre de droite à gauche

        # Si le monstre est en collision avec le joueur
        else:
            perso.jeu.joueur.degats(perso.attaque) # Attaque le joueur

        if perso.rect.x < -80: # Si le monstre est en dehors de la fenêtre, il est supprimé et un autre apparaît
            perso.jeu.score -= 1
            perso.suppression()
            perso.jeu.spawn_monstre(Corona_vert)

class Corona_vert(Monstre): # Définir une classe pour le corona_vert
    def __init__(perso, jeu):
        super().__init__(jeu, "corona_vert")

class Boss(animation.SpriteAnime): # Définir une classe pour le boss
    def __init__(perso, jeu):
        super().__init__("boss")
        perso.jeu = jeu
        perso.vie = 200  # Vie du monstre
        perso.max_vie = 200  # Vie max du monstre
        perso.rect = perso.image.get_rect()  # Récupère les coordonnées de l'image
        perso.rect.x = 800  # Placement initial aléatoire du monstre sur l'axe des x
        perso.rect.y = 400  # Placement initial aléatoire du monstre sur l'axe des y
        perso.boss_en_vie = True

    def suppression(perso):
        perso.jeu.monstres.remove(perso)  # Supprime le monstre

    def degats(perso, compteur):
        perso.vie -= compteur

        if perso.vie <= 0:  # Vérifier si son nombre de point de vie est inférieur ou égal à 0
            perso.suppression()
            perso.jeu.score += 10

    def maj_animation(perso):
        perso.anime()

    def maj_barre_vie(perso, surface):
        couleur_barre = (91, 211, 30)  # Couleur barre de vie
        couleur_fond = (120, 123, 118)  # Couleur arrière plan barre de vie

        # Défini la position de notre jauge de vie ainsi que sa largeur
        position_barre = [perso.rect.x + 50, perso.rect.y - 10, perso.vie, 5]
        position_fond = [perso.rect.x + 50, perso.rect.y - 10, perso.max_vie, 5]

        py.draw.rect(surface, couleur_fond, position_fond)  # Dessin de l'arrière plan de la barre de vie
        py.draw.rect(surface, couleur_barre, position_barre)  # Dessin de la barre de vie

    def deplacement_monstre(perso):
        pass

class Corona_rouge(animation.SpriteAnime): # Définir une classe pour le corona_vert
    def __init__(perso, jeu):
        super().__init__("corona_rouge")
        a = (((jeu.joueur.rect.y) - 250) / ((jeu.joueur.rect.x) - 800))
        x = - random.randint(5, 10)
        y = -(a * x)
        perso.vitessex = x
        perso.vitessey = y
        perso.jeu = jeu
        perso.vie = 100  # Vie du monstre
        perso.max_vie = 100  # Vie max du monstre
        perso.attaque = 3  # Attaque du monstre
        perso.rect = perso.image.get_rect()  # Récupère les coordonnées de l'image
        perso.rect.x = 800 # Placement initial du monstre sur l'axe des x
        perso.rect.y = 400 # Placement initial du monstre sur l'axe des y
        perso.lancement_animation()

    def degats(perso, compteur):
        perso.vie -= compteur

        if perso.vie <= 0:  # Vérifier si son nombre de point de vie est inférieur ou égal à 0
            perso.rect.x = 800  # Placement initial du monstre sur l'axe des x
            perso.rect.y = 400  # Placement initial du monstre sur l'axe des y
            perso.vie = perso.max_vie
            perso.jeu.score += 1

    def maj_animation(perso):
        perso.anime(boucle=True)

    def maj_barre_vie(perso, surface):
        couleur_barre = (91, 211, 30)  # Couleur barre de vie
        couleur_fond = (120, 123, 118)  # Couleur arrière plan barre de vie
        # Défini la position de notre jauge de vie ainsi que sa largeur
        position_barre = [perso.rect.x + 2, perso.rect.y - 10, perso.vie, 5]
        position_fond = [perso.rect.x + 2, perso.rect.y - 10, perso.max_vie, 5]

        py.draw.rect(surface, couleur_fond, position_fond)  # Dessin de l'arrière plan de la barre de vie
        py.draw.rect(surface, couleur_barre, position_barre)  # Dessin de la barre de vie

    def suppression(perso):
        perso.jeu.monstres.remove(perso)  # Supprime le monstre

    def deplacement_monstre(perso):
        # Déplacement réalisé seulement s'il n'y a pas de collision avec le joueur
        if not perso.jeu.verif_collision(perso, perso.jeu.joueurs):
            # Déplacement du monstre de droite à gauche
            perso.rect.x += perso.vitessex
            perso.rect.y -= perso.vitessey

        # Si le monstre est en collision avec le joueur
        else:
            perso.jeu.joueur.degats(perso.attaque)  # Attaque le joueur

        if perso.rect.x < -80:  # Si le monstre est en dehors de la fenêtre, il est supprimé et un autre apparaît
            perso.suppression()
            perso.jeu.spawn_monstre(Corona_rouge)