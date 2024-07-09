import pygame as py
from tir import Tir
import animation

class Joueur(animation.SpriteAnime): # Pour que pygame prend en compte joueur en tant que composé dans le jeu il faut le transformer en sprite
    def __init__(perso, jeu): # init qui va être appelé au chargement de notre classe Joueur qui permettra de charger les caractétistiques de notre joueur
        super().__init__("medecin") # Appel d'une superclasse
        perso.jeu = jeu
        perso.vie = 100 # Vie du joueur
        perso.max_vie = 100 # Limite max de la vie du joueur
        perso.attaque = 20 # Dégats d'attaque de notre perso
        perso.vitesse = 12 # Vitesse du déplacement de notre perso
        perso.tirs = py.sprite.Group() # Regroupement de tous les tirs dans un sprite
        perso.rect = perso.image.get_rect() # On récupère les coordonnées de l'image
        perso.rect.x = 400 # On place le perso sur l'axe des abscisses
        perso.rect.y = 400 # On place le perso sur l'axe des ordonnées
        perso.saut = 20
        perso.nombre_saut = 0
        perso.double_saut_valeur = 20
        perso.double_saut = False
        perso.a_saute = False
        perso.CD = 0

    def sauter(perso):
        if perso.a_saute:
            perso.rect.y -= perso.saut
            perso.saut -= 1
            if perso.saut < -20:
                perso.a_saute = False
                perso.saut = 20
        if perso.double_saut:
            perso.rect.y -= perso.double_saut_valeur
            perso.double_saut_valeur -= 1
            if perso.double_saut_valeur < -20:
                perso.double_saut = False
                perso.double_saut_valeur = 20

    def degats(perso, compteur):
        if perso.vie - compteur > compteur:
            perso.vie -= compteur
        else:
            perso.jeu.fin_jeu()

    def maj_animation(perso):
        perso.anime()

    def maj_barre_vie(perso, surface):
        couleur_barre = (91, 211, 30) # Couleur de la barre de vie
        couleur_fond = (120, 123, 118)  # Couleur de l'arrière plan de la barre de vie

        position_barre = [perso.rect.x + 100, perso.rect.y - 10, perso.vie, 7] # Coordonnées de la barre de vie
        position_fond = [perso.rect.x + 100, perso.rect.y - 10, perso.max_vie, 7] # Coordonnées de l'arrière plan de la barre de vie

        py.draw.rect(surface, couleur_fond, position_fond)  # Dessin de l'arrière plan de la barre de vie
        py.draw.rect(surface, couleur_barre, position_barre) # Dessin de la barre de vie

    def cooldown(perso): #Fonction pour définir un temps d'arrêt entre chaque tir
        if perso.CD >= 3:
            perso.CD = 0
        elif perso.CD > 0:
            perso.CD += 1

    def lancement_tir(perso, x, y):
        perso.cooldown()
        if perso.CD == 0: #Si le cooldown est nul, un tir s'ajoute et le cooldown est égal à 1
            perso.lancement_animation()
            perso.tirs.add(Tir(perso, x, y))
            perso.CD = 1

    def deplacement_droite(perso):
        if not perso.jeu.verif_collision(perso, perso.jeu.monstres): #Si le joueur n'est pas en collision avec un monstre
            perso.rect.x += perso.vitesse #Alors le perso peut se déplacer vers la droite

    def deplacement_gauche(perso):
        if not perso.jeu.verif_collision(perso, perso.jeu.monstres): #Si le joueur n'est pas en collision avec un monstre
            perso.rect.x -= perso.vitesse #Alors le perso peut se déplacer vers la gauche
