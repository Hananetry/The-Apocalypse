import pygame
import sys
import time

pygame.init()


screen = pygame.display.set_mode((700, 400))
pygame.display.set_caption("The Apocalypse")

main_font = pygame.font.Font("RetroGaming.ttf", 16)   #importation d'une police d'écriture

icon = pygame.image.load("icon.png")     #importation de l'image icon
pygame.display.set_icon(icon)                  #définie l'icon

imagebarre = pygame.image.load("barreTexte.PNG")
imagebarre_rect = imagebarre.get_rect(topleft=(0,0))


def quit():
    pygame.quit()
    sys.exit()
    

def fin():
    indiceboom = 1
    while True :
        if indiceboom >= 5 :
            quit()
        boom = pygame.image.load( "boom"+str(indiceboom)+".png")
        screen.blit(boom, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    indiceboom +=1
        pygame.display.update() 

#Parole est une classe permettant de definir une action du visual novel (image, texte et option)


class Parole():
    def __init__(self, image: str, texte: str, choix = False, optGauche = "", optDroite = ""):
        self.image = image
        self.texte = texte
        self.choix = choix
        self.optGauche = optGauche
        self.optDroite = optDroite

    def getImage(self):
        return self.image
    
    def getTexte(self):
        return self.texte

    def getoptGauche(self):
        if self.choix == True :
            return self.optGauche
    
    def getoptDroite(self):
        if self.choix == True :
            return self.optDroite


class Noeud:
    def __init__(self, racine, gauche=None, droite=None):
        self.racine = racine
        self.gauche = gauche
        self.droite = droite

    def __repr__(self):
        resultat = ""           #initialisation dela chaine de caractère à return
        if self.racine != None:
            resultat+=str(self.racine)
        if self.gauche != None: #ne pas afficher les none
            resultat+=","
            resultat+=str(self.gauche)
        if self.droite != None:
            resultat+=","
            resultat+=str(self.droite)
        return resultat

    def taille(self):
        if self == None:
            return 0
        else:
            return 1 + self.taille(self.gauche) + self.taille(self.droite)

    def ajouter(self,v):
        n = self                      #n est l'arbre
        est_insere = False            #booléen de condition d'arrêt
        while not est_insere :        
            if v == n.racine:              #condition d'arrêt
                est_insere = True     #fin
                                        #sinon, si la condition d'arrêt n'est pas vérifiée
            elif v < n.racine:             #si la valeur est plus petite que le noeud étudié
                if n.gauche != None:      #s'il a une suite à ce noeud
                    n = n.gauche          #on étudie cette suite, la condition n'est pas vérifié, la boucle reprends
                else:                 #si on a atteint une feuille
                    n.gauche= Noeud(v)    #notre feuille prends comme fils notre valeur
                    est_insere = True #la condition est vérifiée
            else:                     #sinon, si la valeur était plus grande que le noeud étudié
                if n.droite != None:      #s'il y a une suite à ce noeud
                    n = n.droite          #on étudie la suite
                else:                 #si on a atteint une feuille
                    n.droite = Noeud(v)   #cette feuille prends comme fil notre valeur
                    est_insere = True #la condition est vérifiée

    def insere_tout(self, vals):
        for v in vals:
            self.ajouter(v)
            
    def avancer(self, choix):
        if choix == False:
            
            if self.gauche is not None :
                self.racine = self.gauche.racine
                self.droite = self.gauche.droite
                self.gauche = self.gauche.gauche
                
            else :
                fin()


        else :
            
            if self.droite is not None :
                self.racine = self.droite.racine
                self.gauche = self.droite.gauche
                self.droite = self.droite.droite
                
            else :
                fin()
 
        
        

class Scene():
    def __init__(self, listeParole, id):
        self.listeParole = listeParole
        self.id = id

    def __repr__(self) -> str:
        return str(self.id)

    #equal ==
    def __eq__(self, __o):
        return self.id == __o.id

    #less than <
    def __lt__(self, __o):
        return self.id < __o.id

    #greater than >
    def __gt__(self, __o):
        return self.id > __o.id

    #lesser or equal <=
    def __le__(self, __o):
        return self == __o or self < __o

    #greater or equal >=
    def __ge__(self, __o):
        return self == __o or self > __o

    #not equal !=
    def __ne__(self, __o):
        return type(self) is not type(__o)

scene11 = Scene([Parole("11-0", "The earth is still in a apocalyptic state. Its been 2 years already."), Parole("11-1", "You wake up alone like usuall but you are a little confuse... "), Parole("11-1", "how are you ?", True, "Tired but okay", "Sick and hungry")], 11)
scene6 = Scene([Parole("6-0", "You have a bad headache and a weird feeling haunt you"), Parole("6-1", "For a moment you though you had change. And became like THEM."), Parole("6-1", "Suddenly you hear a loud noise coming from downstairs"), Parole("6-1", "But... you are suppose to be alone !"), Parole("6-1", "How ? Like.... how ? You are scared."), Parole("6-1", "What do you do ?", True, "Stay in your room", "Go see what it is")], 6)
scene17 = Scene([Parole("17-0", "You are feeling a bit dizzy"), Parole("17-0", "But things are starting to go back as it was"), Parole("17-0", "It is like................. rrrrrrrrrh rrrrrrhhh rrrrrhhh"), Parole("17-0", "Rrrrrhhh noise rhhhhh downstairs rrrrrrh"), Parole("17-0", "Stay rrrrrrhhhhh or go rrrrhhhhh ?", True, "Go downstairs", "Stay here")], 17)

scene3 = Scene([Parole("3-0", "Maybe staying in your room isnt a bad idea."),Parole("3-0", "It feel safer to hide than exposing you to the danger."),Parole("3-0", "At least it is what you think. It might be nothing, just an open window") ,Parole("3-0", "But you still have a weird feeling... Is it paranoïa ?"),Parole("3-0", "Are you going crazy ? Would you even know if you did ?"),Parole("3-0", "And again you hear the noise but this time is getting closer"),Parole("3-0", "Maybe a weapon could help ?", True, "Grab your knife", "Doesn't need one")], 3)
scene8 = Scene([Parole("8-0", "Your choice is made. You take your gun and go downstairs"), Parole("8-1", "The stairs are squeaking. Its okay... take a deep breath..."), Parole("8-2", "You enter the Kitchen..."), Parole("8-3", "Oh shit ! A dead !"), Parole("8-3", "What do you do ?", True, "Shot them", "Take a step closer")], 8)
scene14 = Scene([Parole("14-0", "Rrrrrrhhhh hungry rrrhhhhh noise rrrrrrrhhhhh"), Parole("14-1", "Rrrrrhhhhh rrrhhhhh Kitchen rrrrrhhhhh rrrrhhhh'"), Parole("14-2", "Rrrrrhhhh Human rrrrhhh bad rrrrrhhhhhh", True, "Don't move", "Attack")], 14)

scene21 = Scene([Parole("21-0", "Rrrrrrhhhh tired rrrrrrhhhhhh dont move rrrrrrhhhhhh stay here "), Parole("21-0", "Noise back rrrrrrh rrrrrrhhhhh coming rrrrrrhhhh here rrrrrhhhh  "), Parole("21-0", "close now rrrrrrrhhhh door open rrrrrrhhhhh scary human !", True, "Attack", "Stay still")], 21)
scene1 = Scene([Parole("1-0", "You grab your knife quickly and look at the ennemi."), Parole("1-1", "Obviously it as to be a dead one. But this one is strange..."), Parole("1-1", "This dead... it looks like YOU..."), Parole("1-2", "They approach you and attack you."), Parole("1-3", "And with fear in your eyes, you didn’t move, not even a step")], 1)
scene4 = Scene([Parole("4-0", "It’s not like a weapon could really help. You’ve been tired lately."), Parole("4-1", "You look at them while they are getting in the room."), Parole("4-2", "And smile while they attack you."), Parole("4-3", "Maybe this is peace.")], 4)

scene7 = Scene([Parole("7-0", "You try to shoot them but close your eyes while you do it."), Parole("7-1", "You missed them. Your gun fall. They are getting closer. "), Parole("7-2", "And for the first time in a while, you have hope.")], 7)
scene9 = Scene([Parole("9-0", "You are not a great shooter. So you take a step toward them..."), Parole("9-1", "But at the exact same time they do the same.")], 9)
scene12 = Scene([Parole("12-0", "Rrrrhhhh friends ?"), Parole("12-1", "Rrrrrhhhhh scared rrrrrhhhh gun rrrrrhhh")], 12)

scene16 = Scene([Parole("16-0", "RRRRRHHHH RRRRHHH bad human rrrrrrhhhh kill them"), Parole("16-1", "Rhhhhhrhrhrhhhh gun hurt rrrrrhhhrhrrrhh")], 16)
scene18 = Scene([Parole("18-0", "Rrrrhhhhh bad rrrrrhhhhhh human"), Parole("18-1", "rhhhhrrrrrhh gun rrrrrrrrrhhhhhh")], 18)
scene23 = Scene([Parole("23-0", "Rrrrrrhhhhh scared like you rrhhh stay still rhhhhh human nice ?"), Parole("23-1", "Rrrrrhhhhhh rhhhhh oh rrrrhhhhh gun...")], 23)



deroulement = [scene6, scene17,scene3, scene8, scene14, scene21, scene1, scene4, scene7, scene9, scene12, scene16, scene18, scene23]



visualNovel = Noeud(scene11)
visualNovel.insere_tout(deroulement)








def afficherChoix(surface, parole):
    global choixUtilisateur
    textGauche = main_font.render(parole.getoptGauche(), True, (255, 255, 255))
    textDroit = main_font.render(parole.getoptDroite(), True, (255, 255, 255))
    surface.blit(textGauche, (125, 340))
    surface.blit(textDroit, (350, 340))
    

#Change la couleur de notre choix
    if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP :
            if event.key == pygame.K_LEFT:
                choixUtilisateur = False
                    
            if event.key ==pygame.K_RIGHT:
                choixUtilisateur = True
                
    if choixUtilisateur == False :
        textGauche = main_font.render(parole.getoptGauche(), True, (139, 0, 0))
        surface.blit(textGauche, (125, 340))
        
    else :
        textDroit = main_font.render(parole.getoptDroite(), True, (139, 0, 0))
        surface.blit(textDroit, (350, 340))

def afficherParole(surface, parole: Parole):
    bg = pygame.image.load(parole.getImage() + ".png")
    surface.blit(bg, (0, 0))
    
    surface.blit(imagebarre, imagebarre_rect)

    
    text = main_font.render(parole.getTexte(), True, (255, 255, 255))
    surface.blit(text, (25, 365))

def afficherScene(fenetre, scene, indiceDialogue):
    dialogue = scene.listeParole[indiceDialogue]
    afficherParole(fenetre, dialogue)
    afficherChoix(fenetre, dialogue)
    

        

       
indicePourLeDialogue = 0
choixUtilisateur = False

while True:

    
    for event in pygame.event.get():
        scene = visualNovel.racine
        if indicePourLeDialogue >= len(scene.listeParole):
            visualNovel.avancer(choixUtilisateur)
            indicePourLeDialogue = 0
        afficherScene(screen, scene, indicePourLeDialogue)
        
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                indicePourLeDialogue += 1

        
        
    
        if event.type == pygame.QUIT:
            quit()
            

            
    
    
    

    

    pygame.display.update()






