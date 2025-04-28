"""
Projet Arbre binaire de recherche, ici représenté par un visual novel nommé The Apocalypse
fait par Hana Badreddine
Le jeu possède un menu composé d'une page crédit,
une page regle et une page jeu
"""

import pygame, sys   #importation des modules necessaire

pygame.init()      #initialise pygame

screen = pygame.display.set_mode((700,400))    #crée une fenetre de 500 par 375 pixel
pygame.display.set_caption("The Apocalypse")       #définie le titre de la fenetre

main_font = pygame.font.Font("RetroGaming.ttf", 23)   #importation d'une police d'écriture

background = pygame.image.load("menu.png")   #importation de l'image de fond du menu
background_rect = background.get_rect(topleft=(0,0))     #définie le point d'ancrage de l'image
backgroundpng = pygame.image.load("menupng.png")   #importation de l'image de fond du menu
backgroundpng_rect = background.get_rect(topleft=(0,0))     #définie le point d'ancrage de l'image




icon = pygame.image.load("icon.png")     #importation de l'image icon
pygame.display.set_icon(icon)                  #définie l'icon


class Button():       #debut de la classe
    def __init__(self, image, x_pos, y_pos, text_input):   #constructeur auquelle on passe 4 parametres (ses coordonnées x et y et le nom du bouton)
        self.image = image    # Passe les paramètres dans des arguments pour les réutiliser dans la classe
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))     #définie le point d'ancrage de l'image par les coordonées attitré dans les arguments
        self.text_input = text_input    # Passe le paramètre dans un argument pour le réutiliser dans la classe
        self.text = main_font.render(self.text_input, True, "white")   #definie le texte avec sa couleur
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))   #définie le point d'ancrage du texte par les coordonées attitré dans les arguments

    def update(self):      #crée la méthode update
        screen.blit(self.image, self.rect)   #affiche l'image sur l'écran
        screen.blit(self.text, self.text_rect)   #affiche le texte sur l'écran

    def checkForInput(self, position): #crée la méthode checkForInput
        return position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom)  # retourne la position de la souris ; tupple = (x,y); tupple[0]= x; tupple[1]=y        

    def changeColor(self, position):   #crée la méthode changeColor
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):  #si les coordonnées de la souris sont situé ou se trouve l'image
            self.text = main_font.render(self.text_input, True, "black")  # le texte deviens noir
        else:
            self.text = main_font.render(self.text_input, True, "white")  #sinon le texte reste blanc




button_surface = pygame.image.load("button.png")  #importation de l'image des boutons


buttonStart = Button(button_surface, 360, 155, "Start Game") #objet permettant l'exécution de la classe bouton avec ses parametres

buttonRules = Button(button_surface, 360, 207, "Game Rules")

buttonCredits = Button(button_surface, 360, 310, "Credits")

buttonCharacters = Button(button_surface, 360, 258, "Characters")

buttonReturn = Button(button_surface, 360, 370, "Return")





#buttonP_Retour = Button(button_surface_for_p, 280, 68,"")

run = True
state = "menu"

while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()
            
        if event.type == pygame.MOUSEBUTTONDOWN :
            
            if state == "menu" and buttonStart.checkForInput(pygame.mouse.get_pos()):
                state = "playing"
                
            if state == "menu"  and buttonRules.checkForInput(pygame.mouse.get_pos()):
                state = "rules"
                
            if state == "menu"  and buttonCredits.checkForInput(pygame.mouse.get_pos()):
                state = "credits"
                
            if state == "menu"  and buttonCharacters.checkForInput(pygame.mouse.get_pos()):
                state = "characters"
                
            if (state == "rules" or state == "credits" or state == "characters" ) and buttonReturn.checkForInput(pygame.mouse.get_pos()):
                state = "menu"
                
                        
                

    screen.fill((255, 255, 255))
    
    if state == "menu":
        screen.blit(background, (background_rect))
        screen.blit(backgroundpng, (backgroundpng_rect))

        buttonStart.update()
        buttonStart.changeColor(pygame.mouse.get_pos())

        buttonRules.update()
        buttonRules.changeColor(pygame.mouse.get_pos())
    
        buttonCredits.update()
        buttonCredits.changeColor(pygame.mouse.get_pos())
        
        buttonCharacters.update()
        buttonCharacters.changeColor(pygame.mouse.get_pos())
             
          
                
    if state == "rules":      
        screen.blit(background, (background_rect))
        screen.blit(backgroundpng, (backgroundpng_rect))
        imageRules = pygame.image.load("rules.png")
        imageRules_rect = imageRules.get_rect(topleft=(0,0))
        screen.blit(imageRules, (imageRules_rect))
        imageRulespng = pygame.image.load("rulespng.png")
        imageRulespng_rect = imageRulespng.get_rect(topleft=(0,0))
        screen.blit(imageRulespng, (imageRulespng_rect))
        buttonReturn.update()
        buttonReturn.changeColor(pygame.mouse.get_pos())
        
    if state == "characters":
        screen.blit(background, (background_rect))
        screen.blit(backgroundpng, (backgroundpng_rect))
        imageCharacters = pygame.image.load("characters.png")
        imageCharacters_rect = imageCharacters.get_rect(topleft=(0,0))
        screen.blit(imageCharacters, (imageCharacters_rect))
        imageCharacterspng = pygame.image.load("characterspng.png")
        imageCharacterspng_rect = imageCharacterspng.get_rect(topleft=(0,0))
        screen.blit(imageCharacterspng, (imageCharacterspng_rect))
        buttonReturn.update()
        buttonReturn.changeColor(pygame.mouse.get_pos())
        
        
    if state == "credits":
        screen.blit(background, (background_rect))
        screen.blit(backgroundpng, (backgroundpng_rect))
        imageCredits = pygame.image.load("credits.png")
        imageCredits_rect = imageCredits.get_rect(topleft=(0,0))
        screen.blit(imageCredits, (imageCredits_rect))
        imageCreditspng = pygame.image.load("creditspng.png")
        imageCreditspng_rect = imageCreditspng.get_rect(topleft=(0,0))
        screen.blit(imageCreditspng, (imageCreditspng_rect))
        buttonReturn.update()
        buttonReturn.changeColor(pygame.mouse.get_pos())



    if state == "playing":
        import game


    if state == "GoMenu":
        screen.blit(GoMenubackground, (GoMenubackground_rect))
        for event in events:
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE:
                    state = "menu"



    pygame.display.update()

