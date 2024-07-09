import pygame as py # On importe le module pygame il est donc juste recupéré
from pygame import mixer
from jeu import Jeu

py.init() # Charge les composants qui sont à l'intérieur du module pygame

clock = py.time.Clock() # Définir une clock
FPS = 60

py.display.set_caption("CORONED") # Permet de nommer la fenêtre d'exécution
logo_jeu = py.image.load("images/logo_coroned.png")
py.display.set_icon(logo_jeu)

fenetre = py.display.set_mode((1080,720)) # Permet de définir la dimension de la fenêtre, en premier argument la largeur puis en deux la hauteur

fond_jeu = py.image.load("images/hopital.png") # On crée une variable fond_jeu et on charge l'image de l'hopital
fond_jeu = py.transform.scale(fond_jeu, (1080, 720)) # Taille du fond d'écran

fond_menu = py.image.load("images/bg_menu.jpg") # On crée une variable fond_menu et on charge bg_menu.jpg depuis images
fond_texte = py.image.load("images/fond_texte.png") # On crée une variable fond_texte et on charge fond_texte.jpg depuis images
fond_fin = py.image.load("images/bg_fin.jpg")

bouton_menu = py.image.load("images/bouton.png") # On crée une variable fond menu et on charge bouton.png depuis images

bouton_menu_rect = bouton_menu.get_rect() # Raccourci

bouton_menu_rect.x = (fenetre.get_width() // 4) # Coordonnées du bouton (abscisses)
bouton_menu_rect.y = (fenetre.get_height() // 2) # Coordonnées du bouton (ordonnées)

jeu = Jeu() # Permet de charger la classe Jeu

mixer.music.load("musiques/musique_lucien.wav") # Importation de la musique
mixer.music.play(-1) # Lancement continu de la musique de fond

fenetre.blit(fond_menu, (0, 0))
fenetre.blit(bouton_menu, (0, 0))

running = True # On crée une variable running pour savoir si notre programme fonctionne ou non

while running: # Boucle d'exécution : tant que running est vrai, le programme fonctionne

    if jeu.menu:
        fenetre.blit(fond_menu, (0, 0))
        fenetre.blit(bouton_menu, (0, 0))

        for event in py.event.get(): # Permet de récupérer les infos du joueur
            if event.type == py.QUIT: # Si le joueur ferme la fenetre alors le programme s'arrete
                running = False
                py.quit() # On dit a pygame de quitter l'application de notre jeu

            elif event.type == py.MOUSEBUTTONDOWN:  # Lance le jeu si le joueur clique
                if py.mouse.get_pos()[0] > 303 and py.mouse.get_pos()[0] < 779 and py.mouse.get_pos()[1] > 464 and py.mouse.get_pos()[1] < 566:
                    jeu.debut()

    elif jeu.est_joue: # Vérifie si notre jeu a commencé
        fenetre.blit(fond_jeu, (0, 0)) # Blit permet d'injecter une image dans une partie spécifique de la fenêtre
        fenetre.blit(fond_texte, (0, 0))
        fenetre.blit(fond_texte, (900, 0))
        jeu.maj(fenetre) # Lance les instructions de la partie

    else: # Vérifie si le jeu n'a pas commencé
        fenetre.blit(fond_fin, (0, 0))
        jeu.affiche_score_fin(fenetre)

        for event in py.event.get(): # Permet de récupérer les infos du joueur
            if event.type == py.QUIT: # Si le joueur ferme la fenetre alors le programme s'arrete
                running = False
                py.quit()
            elif event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    jeu.score = 0
                    jeu.level = 1
                    jeu.level1 = True
                    jeu.debut()

# Si le joueur ferme la fenêtre
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
            py.quit()
# Détecte la pression d'une touche du clavier
        elif event.type == py.KEYDOWN:
            jeu.entree[event.key] = True

        elif event.type == py.KEYUP:
            jeu.entree[event.key] = False
# Détecte le placement du curseur de la souris, ainsi que son clic
        elif event.type == py.MOUSEBUTTONDOWN: # Clic sur la souris
            if py.mouse.get_pos()[0] > jeu.joueur.rect.x + 213:
                #print(py.mouse.get_pos())  # position de la soucis pour l'equation cartesienne
                #print(jeu.joueur.rect.x, jeu.joueur.rect.y)

                a = ((py.mouse.get_pos()[1] - (jeu.joueur.rect.y + 176)) / (py.mouse.get_pos()[0] - (213 + jeu.joueur.rect.x)))
                #print(a)
                x = 15
                y = -(a * x)
                jeu.joueur.lancement_tir(x, y)

            elif py.mouse.get_pos()[0] < jeu.joueur.rect.x + 213:
                #print(jeu.joueur.rect.x, jeu.joueur.rect.y)
                #print(py.mouse.get_pos())
                a = (((jeu.joueur.rect.y + 176) - py.mouse.get_pos()[1]) / ((jeu.joueur.rect.x + 213) - (py.mouse.get_pos()[0])))
                #print(a)
                x = -15
                y = -(a * x)
                jeu.joueur.lancement_tir(x, y)
    py.display.flip() # Permet de mettre à jour la fenêtre

    # Fixer le nombre de FPS sur la clock
    clock.tick(FPS)


