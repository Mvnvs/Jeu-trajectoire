import pygame as py

class SpriteAnime(py.sprite.Sprite):
    def __init__(perso, nom_sprite):
        super().__init__()
        perso.image = py.image.load(f"images/{nom_sprite}.png")
        perso.image_actuelle = 0 # Commencer l'animation à l'image 0
        perso.images = animations.get(nom_sprite)
        perso.animation = False

    def lancement_animation(perso): # Définir une méthode pour démarrer l'animation
        perso.animation = True

    def anime(perso, boucle=False): # Définir une méthode pour animer le sprite
        if perso.animation: # Vérifier si l'animation est active

            perso.image_actuelle += 1 # Passer à l'image suivante

            if perso.image_actuelle >= len(perso.images): # Vérifier si on a atteint la fin de l'animation
                perso.image_actuelle = 0 # Remettre l'animation au départ

                if boucle is False: # Vérifier si l'animation n'est pas en mode boucle
                    perso.animation = False # Désactivation de l'animation

            perso.image = perso.images[perso.image_actuelle]  # Modifier l'image précédente par la suivante


def maj_animation_images(nom_sprite):
    images = []
    chemin = f"images/{nom_sprite}/{nom_sprite}"

    for num in range(1, 18):
        chemin_image = chemin + str(num) + ".png"
        images.append(py.image.load(chemin_image)) # Chargement des images et ajout dans la liste

    return images # Renvoyer le contenu de la liste d'images

# Définir un dictionnaire qui va contenir les images chargées de chaque sprite
animations = {
    "corona_vert": maj_animation_images("corona_vert"),
    "medecin": maj_animation_images("medecin"),
    "boss": maj_animation_images("boss"),
    "corona_rouge": maj_animation_images("corona_rouge")
}