import pygame as py
import csv
from joueur import Joueur
from monstre import Monstre, Corona_vert, Boss, Corona_rouge
from pluie import Pluie


class Jeu:
    def __init__(perso):
        perso.est_joue = False # Définir si notre jeu a commencé ou non
        perso.menu = True
        perso.joueurs = py.sprite.Group() # Permet de créer un groupe de sprite
        perso.joueur = Joueur(perso) # Génération de la classe Joueur
        perso.joueurs.add(perso.joueur) # Ajoute la classe Joueur dans le groupe de sprite
        perso.pluie = Pluie(perso)
        perso.monstres = py.sprite.Group() # Groupe de monstre
        perso.entree = {}
        perso.collision_sol = False
        perso.score = 0
        perso.level = 1
        perso.level1 = True
        perso.level2 = True
        perso.compteur_double_saut = False

    def debut(perso):
        perso.menu = False
        perso.est_joue = True
        py.display.flip()
        perso.spawn_monstre(Corona_vert) # Fait apparaitre un monstre en début de partie
        perso.spawn_monstre(Corona_vert)

    def fin_jeu(perso):
        perso.monstres = py.sprite.Group()
        perso.joueur.vie = perso.joueur.max_vie
        perso.menu = False
        perso.est_joue = False
        perso.joueurs = py.sprite.Group()
        perso.joueur = Joueur(perso)
        perso.joueurs.add(perso.joueur)
        perso.pluie = Pluie(perso)
        perso.monstres = py.sprite.Group()
        perso.entree = {}
        perso.collision_sol = False

    def affiche_score(perso, fenetre):
        texte = py.font.SysFont("scoreboard", 30)  # Création de la police du texte
        score_texte = texte.render(f"Score : {perso.score}", 1, (0, 0, 0))  # Paramètrage du texte du score
        fenetre.blit(score_texte, (45, 38))  # Affichage du score

    def affiche_score_fin(perso, fenetre):
        texte2 = py.font.SysFont("scoreboard", 30)  # Création de la police du texte
        score_texte2 = texte2.render(f"SCORE FINAL : {perso.score}", 1, (255, 255, 255))  # Paramètrage du texte du score
        fenetre.blit(score_texte2, (45, 38))  # Affichage du score

        with open("Base_de_donnees.csv", 'r') as csv_file: # Création meilleur score
            reader = csv.reader(csv_file)
            firstline = True
            for row in reader:
                if firstline:
                    firstline = False
                    continue
                score_max = int(row[0])
        if perso.score > score_max:
            with open("Base_de_donnees.csv", mode='w', newline="") as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=',')
                csv_writer.writerow(["Donnée"])
                csv_writer.writerow({perso.score})
        texte3 = py.font.SysFont("scoreboard", 30)  # Création de la police du texte
        score_texte3 = texte3.render(f"MEILLEUR SCORE : {score_max}", 1,(255, 255, 255))  # Paramètrage du texte du score
        fenetre.blit(score_texte3, (830, 38))  # Affichage du score

    def affiche_level(perso, fenetre):
        texte4 = py.font.SysFont("scoreboard", 30)  # Création de la police du texte
        score_texte4 = texte4.render(f"Level : {perso.level}", 1, (0, 0, 0))  # Paramètrage du texte du score
        fenetre.blit(score_texte4, (950, 38))  # Affichage du score

    def maj(perso, fenetre):
        fenetre.blit(perso.joueur.image, perso.joueur.rect)
        if perso.level1:
            if perso.score == 20:
                perso.level += 1
                perso.spawn_monstre(Boss)
                perso.spawn_monstre(Corona_rouge)
                perso.level1 = False
        if perso.level2:
            if perso.score == 50:
                perso.level += 1
                perso.spawn_monstre(Boss)
                perso.spawn_monstre(Corona_rouge)
                perso.spawn_monstre(Corona_rouge)
                perso.level2 = False
        if perso.score < 0:
            perso.score += 1
            perso.fin_jeu()

        perso.affiche_score(fenetre)

        perso.affiche_level(fenetre)

        perso.joueur.maj_barre_vie(fenetre)  # Appel de la barre de vie du joueur

        perso.pluie.maj_barre(fenetre) # Appel de la barre d'événement

        perso.joueur.maj_animation() # Actualiser l'animation du joueur

        for tir in perso.joueur.tirs:
            tir.deplacement()

        for monstre in perso.monstres:
            monstre.deplacement_monstre()
            monstre.maj_barre_vie(fenetre)
            monstre.maj_animation()

        for pillule in perso.pluie.pillules:
            pillule.chute()

        for masque in perso.pluie.masques:
            masque.chute()

        perso.joueur.tirs.draw(fenetre) # Dessine le groupe de sprite des tirs sur notre surface fenetre

        perso.monstres.draw(fenetre) # Dessine le groupe de sprite des monstres sur notre surface fenetre

        perso.pluie.pillules.draw(fenetre) # Dessine le groupe de sprite des pillules sur notre surface fenetre

        perso.pluie.masques.draw(fenetre) # Dessine le groupe de sprite des masques sur notre surface fenetre

        perso.joueur.sauter() # Appel la fonction sauter

        if perso.entree.get(py.K_d) and perso.joueur.rect.x < 820:
            perso.joueur.deplacement_droite()
            if perso.entree.get(py.K_z):
                perso.joueur.a_saute = True

        elif perso.entree.get(py.K_q) and perso.joueur.rect.x > 0:
            perso.joueur.deplacement_gauche()
            if perso.entree.get(py.K_z):
                perso.joueur.a_saute = True

        elif perso.entree.get(py.K_z):  # Si le joueur appuie sur la touche Z et que le perso est dans la fenêtre
            if perso.joueur.rect.y == 400:
                perso.compteur_double_saut = True
            perso.joueur.a_saute = True  # Alors le perso saute
            if perso.compteur_double_saut and perso.joueur.rect.y <= 380:
                perso.joueur.double_saut = True
                perso.compteur_double_saut = False

        elif perso.entree.get(py.K_d) and perso.entree.get(py.K_z):
            perso.joueur.a_saute = True

        elif perso.entree.get(py.K_q) and perso.entree.get(py.K_z):
            perso.joueur.a_saute = True

        py.display.flip() # Mise à jour de la fenêtre

    def verif_collision(perso, sprite, groupe): # py.sprite.collide_mask c'est le masque de collision, hitbox
        return py.sprite.spritecollide(sprite, groupe, False, py.sprite.collide_mask) # Renvoi le résultat d'une comparaison de collision entre le sprite et le groupe de sprite

    def spawn_monstre(perso, nom_classe_monstre):
        perso.monstres.add(nom_classe_monstre.__call__(perso)) # Ajoute la classe Monstre dans un groupe de sprite pour rassembler tous les monstres
