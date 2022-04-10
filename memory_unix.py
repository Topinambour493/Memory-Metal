def waitclic():
    """ attend que l'utilisateur clique gauche, et renvoie les coordonnées du point cliqué. ferme le programme si clic sur croix"""
    continuer = 1
    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit(0)
            if event.type== MOUSEBUTTONDOWN:
                if event.button==1:
                    return event.pos

def clic():
    """ferme le programme si clic sur croix"""
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit(0)

def rectangle(x1,y1,x3,y3,couleur):
    """rectangle (centre du rectangle,longueur segment horizontaux,longueur segments verticaux,couleur, )"""
    x2,y2=x3,y1
    x4,y4=x1,y3
    pygame.draw.line(screen,couleur,(x1-2,y1),(x2,y2),6)
    pygame.draw.line(screen,couleur,(x2,y2-2),(x3,y3),6)
    pygame.draw.line(screen,couleur,(x3+3,y3),(x4,y4),6)
    pygame.draw.line(screen,couleur,(x4,y4+3),(x1,y1),6)
    pygame.display.flip()

def choix_menu_principale(x,y):
    if 496<x<780 and 176<y<259:
        return 1
    elif 471<x<801 and 319<y<403:
        return 2
    elif 485<x<784 and 472<y<559:
        return 3
    else:
        return 0

def changement_parametre_menu1(x,y):
    global nb_joueurs,type_partie,ok
    if 184<x<476 and 179<y<281:
        nb_joueurs=2
    elif 488<x<780 and 179<y<281:
        nb_joueurs=3
    elif 794<x<1086 and 179<y<281:
        nb_joueurs=4
    elif 142<x<627 and 368<y<470:
        type_partie="2 cartes identiques"
    elif 640<x<1125 and 368<y<470:
        type_partie="2 cartes différentes"
    elif 392<x<877 and 483<y<585:
        type_partie="3 cartes différentes"
    elif 965<x<1210 and 502<y<615:
        ok=1

def affichage_parametre_menu1():
    window.blit(menu1,(0,0))
    if nb_joueurs==2:
        rectangle(184,179,476,281,noir)
    elif nb_joueurs==3:
        rectangle(488,179,780,281,noir)
    else:
        rectangle(794,179,1086,281,noir)
    if type_partie=="2 cartes identiques":
        rectangle(142,368,627,470,noir)
    elif type_partie=="2 cartes différentes":
        rectangle(640,368,1125,470,noir)
    else:
        rectangle(392,483,877,585,noir)
    pygame.display.flip()

def changement_parametre_menu_binaire(x,y):
    global nb_cartes,type_cartes,ok
    if 239<x<361 and 176<y<279:
        nb_cartes=8
    elif 373<x<495 and 176<y<279:
        nb_cartes=12
    elif 507<x<629 and 176<y<279:
        nb_cartes=14
    elif 641<x<763 and 176<y<279:
        nb_cartes=16
    elif 775<x<897 and 176<y<279:
        nb_cartes=18
    elif 909<x<1031 and 176<y<279:
        nb_cartes=24
    elif 142<x<627 and 368<y<470:
        type_cartes="logo-musique"
    elif 640<x<1125 and 368<y<470:
        type_cartes="musique-album"
    elif 392<x<877 and 483<y<585:
        type_cartes="logo-album"
    elif 965<x<1210 and 502<y<615:
        ok=1

def affichage_parametre_menu_binaire():
    window.blit(menu_binaire,(0,0))
    if nb_cartes==8:
        rectangle(239,176,361,279,noir)
    elif nb_cartes==12:
        rectangle(373,176,495,279,noir)
    elif nb_cartes==14:
        rectangle(507,176,629,279,noir)
    elif nb_cartes==16:
        rectangle(641,176,763,279,noir)
    elif nb_cartes==18:
        rectangle(775,176,897,279,noir)
    else:
        rectangle(909,176,1031,279,noir)
    if type_cartes=="logo-musique":
        rectangle(142,368,627,470,noir)
    elif type_cartes=="musique-album":
        rectangle(640,368,1125,470,noir)
    else:
        rectangle(392,483,877,585,noir)
    pygame.display.flip()

def changement_parametre_menu_classique(x,y):
    global nb_cartes,type_cartes,ok
    if 239<x<361 and 176<y<279:
        nb_cartes=8
    elif 373<x<495 and 176<y<279:
        nb_cartes=12
    elif 507<x<629 and 176<y<279:
        nb_cartes=14
    elif 641<x<763 and 176<y<279:
        nb_cartes=16
    elif 775<x<897 and 176<y<279:
        nb_cartes=18
    elif 909<x<1031 and 176<y<279:
        nb_cartes=24
    elif 142<x<627 and 368<y<470:
        type_cartes="musique"
    elif 640<x<1125 and 368<y<470:
        type_cartes="album"
    elif 392<x<877 and 483<y<585:
        type_cartes="logo"
    elif 965<x<1210 and 502<y<615:
        ok=1

def affichage_parametre_menu_classique():
    window.blit(menu_classique,(0,0))
    if nb_cartes==8:
        rectangle(239,176,361,279,noir)
    elif nb_cartes==12:
        rectangle(373,176,495,279,noir)
    elif nb_cartes==14:
        rectangle(507,176,629,279,noir)
    elif nb_cartes==16:
        rectangle(641,176,763,279,noir)
    elif nb_cartes==18:
        rectangle(775,176,897,279,noir)
    else:
        rectangle(909,176,1031,279,noir)
    if type_cartes=="musique":
        rectangle(142,368,627,470,noir)
    elif type_cartes=="album":
        rectangle(640,368,1125,470,noir)
    else:
        rectangle(392,483,877,585,noir)
    pygame.display.flip()

def changement_parametre_menu_ternaire(x,y):
    global nb_cartes,type_cartes,ok
    if 239<x<361 and 295<y<398:
        nb_cartes=9
    elif 373<x<495 and 295<y<398:
        nb_cartes=12
    elif 507<x<629 and 295<y<398:
        nb_cartes=15
    elif 641<x<763 and 295<y<398:
        nb_cartes=18
    elif 775<x<897 and 295<y<398:
        nb_cartes=21
    elif 909<x<1031 and 295<y<398:
        nb_cartes=24
    elif 965<x<1210 and 502<y<615:
        ok=1

def affichage_parametre_menu_ternaire():
    window.blit(menu_ternaire,(0,0))
    if nb_cartes==9:
        rectangle(239,295,361,398,noir)
    elif nb_cartes==12:
        rectangle(373,295,495,398,noir)
    elif nb_cartes==15:
        rectangle(507,295,629,398,noir)
    elif nb_cartes==18:
        rectangle(641,295,763,398,noir)
    elif nb_cartes==21:
        rectangle(775,295,897,398,noir)
    else:
        rectangle(909,295,1031,398,noir)
    pygame.display.flip()

def lance_credits():
    musique_credits.play(loops=0, maxtime=0, fade_ms=0)
    for i in range (891):
        window.blit(image_credits,(0,-i))
        pygame.display.flip()
        pygame.time.delay(13)
        clic()
    for i in range (891,4170):
        window.blit(image_credits,(0,-i))
        window.blit(image_musique_album,(0,0))
        pygame.display.flip()
        pygame.time.delay(13)
        clic()
    for i in range (4170,4480):
        window.blit(image_credits,(0,-i))
        window.blit(image_musique_album,(0,4170-i))
        pygame.display.flip()
        pygame.time.delay(13)
        clic()

def cartes_partie(artistes,types):
    """arstistes correspond au nombres d'artistes différents durant la partie et types correspond aux differents types de cartes utilisés"""
    global total_cartes,total_cartes2,total_groupes,total_musique_groupes
    ensemble=list(zip(total_cartes,total_cartes2,total_groupes,total_musique_groupes))
    random.shuffle(ensemble)
    ensemble=ensemble[:artistes]
    cartes,cartes2,groupes,musique_groupes=zip(*ensemble)
    cartes,cartes2,total_groupes,total_musique_groupes=list(cartes),list(cartes2),list(groupes),list(musique_groupes)
    cartes_,cartes2_=[],[]
    for i in range(artistes):
        for v in range(len(types)):
            cartes_.append(cartes[i][types[v]-1])
            cartes2_.append(cartes2[i][types[v]-1])
    ensemble=list(zip(cartes_,cartes2_))
    random.shuffle(ensemble)
    cartes,cartes2=zip(*ensemble)
    cartes,cartes2=list(cartes),list(cartes2)
    return cartes,cartes2,groupes,musique_groupes

def phrase():
    """phrase permet de créer une phrase affichable par pygame, ici on crée la phrase qui liste les groupes utilisés durant la partie"""
    texte="groupes utilisées durant la partie:"
    texte=texte+" "+groupes[0]
    for i in range (1,(len(groupes)-1)):
        texte=texte+", "+groupes[i]
    texte=texte+" et "+groupes[(len(groupes)-1)]
    return texte

def affichage_partie(nb_cartes,x,y,longueur):
    window.blit(fond,(0,0))
    for j in range (len(joueurs)):
        texte1=police1.render(joueurs[j][0],1,joueurs[j][1])
        window.blit(texte1,joueurs[j][2])
    texte2=police2.render(phrase(),1,noir)
    window.blit(texte2,(5,118))
    i=0
    x_=x
    while i<nb_cartes:
        if cartes2[i]!="trouvé":
            window.blit(dos,(x_,y))
        x_=x_+156
        i=i+1
        if i%longueur==0:
            y=y+156
            x_=x

def affichage_joueurs_et_scores():
    window.blit(demi_fond,(0,0))
    for j in range (len(joueurs)):
        texte1=police1.render(joueurs[j][0],1,joueurs[j][1])
        window.blit(texte1,joueurs[j][2])
    texte2=police2.render(phrase(),1,noir)
    window.blit(texte2,(5,118))

def lance_musique():
    for i in range (len(groupes)):
        if cartes2[indice]==groupes[i]:
            musique_groupes[i].play(loops=0, maxtime=0, fade_ms=0)

def click_carte(clickX,clickY,cartes,x,y,longueur):
    lignes=cartes/longueur
    y_=y
    p=900
    i=0
    while i<lignes and p==900:
        if y_<=clickY<=y_+146:
            p=i
        else:
            y_=y_+156
            i=i+1
    if p==900:
        return -1,0
    x_=x
    c=900
    i=0
    while i<longueur and c==900:
        if x_<=clickX<=x_+146:
            c=i
        else:
            x_=x_+156
            i=i+1
    if c==900:
        return -1,0
    test=(x_,y_) in positions
    if test==True:
        return -1,0
    indice_carte=c+p*longueur
    if cartes2[indice_carte]=="trouvé":
        return -1,0
    return indice_carte,(x_,y_)

def joueur_et_fonds_suivant():
    for j in range((len(joueurs)-1)):
        if joueur==joueurs[j]:
            return joueurs[j+1],fonds[j+1],demi_fonds[j+1]
    return joueurs[0],fonds[0],demi_fonds[0]

def score_augmente():
    score_actuel=scores.index(joueur[0])
    return scores[score_actuel+1]

def type(type_cartes):
    if type_cartes=="musique":
        return 3,3
    elif type_cartes=="logo":
        return 2,2
    elif type_cartes=="album":
        return 1,1
    elif type_cartes=="logo-musique":
        return 2,3
    elif type_cartes=="musique-album":
        return 3,1
    elif type_cartes=="logo-album":
        return 2,1
    else:
        return 1,2,3

def parametres_cartes(nb_cartes):
    """en changeant la taille du tableau "cartes", on change le nombre total de cartes affichés, en changeant la longueur,on change la capacité de chaque ligne.En changeant x et y, on change la position de la premiere carte(coin haut-gauche de la carte)"""
    """parametres en fonction de la partie:
    8,328,234,4
    9,406,156,3
    12,328,156,4
    14,94,234,7
    15,250,156,5
    16,16,234,8
    18,156,156,6
    21,94,156,7
    24,16,156,8"""
    if nb_cartes==8:
        return 8,328,234,4
    elif nb_cartes==9:
        return 9,406,156,3
    elif nb_cartes==12:
        return 12,328,156,4
    elif nb_cartes==14:
        return 14,94,234,7
    elif nb_cartes==15:
        return 15,250,156,5
    elif nb_cartes==16:
        return 16,16,234,8
    elif nb_cartes==18:
        return 18,156,156,6
    elif nb_cartes==21:
        return 21,94,156,7
    else:
        return 24,16,156,8

def classement_joueurs():
    for i in range (1,nb_joueurs):
        while i>0 and joueurs[i][0]>joueurs[i-1][0]:
            joueurs[i],joueurs[i-1]=joueurs[i-1],joueurs[i]
            i=i-1
    return joueurs

def joueurs_medailles(classement):
    medailles_possibles=["ore","argent","bronze"]
    score_joueur_précédent=classement[0][0]
    classement[0][0]=medailles_possibles[0]
    i=1
    while i<nb_joueurs and len(medailles_possibles)>1:
        print(nb_joueurs,classement)
        score=classement[i][0]
        if score==score_joueur_précédent:
            classement[i][0]=medailles_possibles[0]
        else:
            del medailles_possibles[0]
            classement[i][0]=medailles_possibles[0]
        score_joueur_précédent=score
        i=i+1
    médaillés=classement[:i]
    return médaillés

def distribution_des_medailles():
    classement=classement_joueurs()
    médaillés=joueurs_medailles(classement)
    for i in range (len(médaillés)):
        if médaillés[i][0]=="ore":
            window.blit(ore,(médaillés[i][2][0]+35,médaillés[i][2][1]+70))
        elif médaillés[i][0]=="argent":
            window.blit(argent,(médaillés[i][2][0]+35,médaillés[i][2][1]+70))
        else:
            window.blit(bronze,(médaillés[i][2][0]+35,médaillés[i][2][1]+70))
    pygame.display.flip()

def choix_fin_partie():
    choix=0
    while choix==0:
        X,Y=waitclic()
        if 71<X<416 and 523<Y<606:
            return 1
        elif 635<X<1200 and 523<Y<606:
            return 0

################################
# DEBUT DU PROGRAMME PRINCIPAL #
################################

import random
import pygame
from pygame.locals import *
pygame.init()


#ouverture de la fenêtre graphique
window = pygame.display.set_mode((1270,630))
screen= pygame.display.get_surface()

##chargement des imgages
menu_principale=pygame.image.load("images\images_generales\menu_principale.png").convert()
menu1=pygame.image.load("images\images_generales\menu1.png").convert()
menu_binaire=pygame.image.load("images\images_generales\menu_binaire.png").convert()
menu_classique=pygame.image.load("images\images_generales\menu_classique.png").convert()
menu_ternaire=pygame.image.load("images\images_generales\menu_ternaire.png").convert()
musique=pygame.image.load("images\images_generales\carte_musique.png").convert()
image_credits=pygame.image.load("images\images_generales\credits.png").convert()
image_musique_album=pygame.image.load("images\images_generales\image_musique_album.png").convert()
dos=pygame.image.load("images\images_generales\carte_dos.png").convert()
j1=pygame.image.load("images\images_generales\j1.png").convert()
j2=pygame.image.load("images\images_generales\j2.png").convert()
j3=pygame.image.load("images\images_generales\j3.png").convert()
j4=pygame.image.load("images\images_generales\j4.png").convert()
j1_=pygame.image.load("images\images_generales\j1_.png").convert()
j2_=pygame.image.load("images\images_generales\j2_.png").convert()
j3_=pygame.image.load("images\images_generales\j3_.png").convert()
j4_=pygame.image.load("images\images_generales\j4_.png").convert()
ore=pygame.image.load("images\images_generales\or.png").convert_alpha()
argent=pygame.image.load("images\images_generales\argent.png").convert_alpha()
bronze=pygame.image.load("images\images_generales\bronze.png").convert_alpha()
fin_partie=pygame.image.load("images\images_generales\fin_partie.png").convert_alpha()
alestorm1=pygame.image.load("images\albums\alestorm_album.png").convert()
alestorm2=pygame.image.load("images\logos\alestorm_logo.png").convert()
arch_enemy1=pygame.image.load("images\albums\arch_enemy_album.png").convert()
arch_enemy2=pygame.image.load("images\logos\arch_enemy_logo.png").convert()
children1=pygame.image.load("images\albums\children_album.png").convert()
children2=pygame.image.load("images\logos\children_logo.png").convert()
deicide1=pygame.image.load("images\albums\deicide_album.png").convert()
deicide2=pygame.image.load("images\logos\deicide_logo.png").convert()
dream_theater1=pygame.image.load("images\albums\dream_theater_album.png").convert()
dream_theater2=pygame.image.load("images\logos\dream_theater_logo.png").convert()
ghost1=pygame.image.load("images\albums\ghost_album.png").convert()
ghost2=pygame.image.load("images\logos\ghost_logo.png").convert()
gojira1=pygame.image.load("images\albums\gojira_album.png").convert()
gojira2=pygame.image.load("images\logos\gojira_logo.png").convert()
in_flames1=pygame.image.load("images\albums\in_flames_album.png").convert()
in_flames2=pygame.image.load("images\logos\in_flames_logo.png").convert()
korn1=pygame.image.load("images\albums\korn_album.png").convert()
korn2=pygame.image.load("images\logos\korn_logo.png").convert()
korpiklaani1=pygame.image.load("images\albums\korpiklaani_album.png").convert()
korpiklaani2=pygame.image.load("images\logos\korpiklaani_logo.png").convert()
machine_head1=pygame.image.load("images\albums\machine_head_album.png").convert()
machine_head2=pygame.image.load("images\logos\machine_head_logo.png").convert()
maiden1=pygame.image.load("images\albums\maiden_album.png").convert()
maiden2=pygame.image.load("images\logos\maiden_logo.png").convert()
megadeth1=pygame.image.load("images\albums\megadeth_album.png").convert()
megadeth2=pygame.image.load("images\logos\megadeth_logo.png").convert()
metallica1=pygame.image.load("images\albums\metallica_album.png").convert()
metallica2=pygame.image.load("images\logos\metallica_logo.png").convert()
municipale_waste1=pygame.image.load("images\albums\municipale_waste_album.png").convert()
municipale_waste2=pygame.image.load("images\logos\municipale_waste_logo.png").convert()
pantera1=pygame.image.load("images\albums\pantera_album.png").convert()
pantera2=pygame.image.load("images\logos\pantera_logo.png").convert()
rise1=pygame.image.load("images\albums\rise_album.png").convert()
rise2=pygame.image.load("images\logos\rise_logo.png").convert()
sabaton1=pygame.image.load("images\albums\sabaton_album.png").convert()
sabaton2=pygame.image.load("images\logos\sabaton_logo.png").convert()
slayer1=pygame.image.load("images\albums\slayer_album.png").convert()
slayer2=pygame.image.load("images\logos\slayer_logo.png").convert()
slipknot1=pygame.image.load("images\albums\slipknot_album.png").convert()
slipknot2=pygame.image.load("images\logos\slipknot_logo.png").convert()
tool1=pygame.image.load("images\albums\tool_album.png").convert()
tool2=pygame.image.load("images\logos\tool_logo.png").convert()
ultra_vomit1=pygame.image.load("images\albums\ultra_vomit_album.png").convert()
ultra_vomit2=pygame.image.load("images\logos\ultra_vomit_logo.png").convert()

##chargement des musiques
musique_credits=pygame.mixer.Sound("musiques\joe_la_mouk_connard_de_hippy.wav")
alestorm3=pygame.mixer.Sound("musiques\alestorm_alestorm.wav")
arch_enemy3=pygame.mixer.Sound("musiques\arch_enemy_the_world_is_yours.wav")
children3=pygame.mixer.Sound("musiques\children_silent_night_bodom_night.wav")
deicide3=pygame.mixer.Sound("musiques\deicide_homage_for_satan.wav")
dream_theater3=pygame.mixer.Sound("musiques\dream_theater_lost_not_forgotten.wav")
ghost3=pygame.mixer.Sound("musiques\ghost_year_zero.wav")
gojira3=pygame.mixer.Sound("musiques\gojira_ocean_planet.wav")
in_flames3=pygame.mixer.Sound("musiques\in_flames_follow_me.wav")
korn3=pygame.mixer.Sound("musiques\korn_hypocrites.wav")
korpiklaani3=pygame.mixer.Sound("musiques\korpiklaani_ammanhauta.wav")
machine_head3=pygame.mixer.Sound("musiques\machine_head_halo.wav")
maiden3=pygame.mixer.Sound("musiques\maiden_the_trooper.wav")
megadeth3=pygame.mixer.Sound("musiques\megadeth_hangar_18.wav")
metallica3=pygame.mixer.Sound("musiques\metallica_nothing_else_matters.wav")
municipale_waste3=pygame.mixer.Sound("musiques\municipal_waste_the_fatal_feast.wav")
pantera3=pygame.mixer.Sound("musiques\pantera_drag_the_waters.wav")
rise3=pygame.mixer.Sound("musiques\rise_here_comes_the_boom.wav")
sabaton3=pygame.mixer.Sound("musiques\sabaton_great_war.wav")
slayer3=pygame.mixer.Sound("musiques\slayer_raining_blood.wav")
slipknot3=pygame.mixer.Sound("musiques\slipknot_before_i_forget.wav")
tool3=pygame.mixer.Sound("musiques\tool_lateralus.wav")
ultra_vomit3=pygame.mixer.Sound("musiques\ultra_vomit_pipi_vs_caca.wav")

#definitions des couleurs
vert=(0,247,43)
bleu=(0,36,247)
jaune=(255,255,23)
rouge=(224,0,6)
noir=(0,0,0)

#definition des scores possibles
scores=("0","1","2","3","4","5","6","7","8","9","10","11","12")
#preparation de la police des textes
police1=pygame.font.SysFont("Sans-serif",170,bold=False,italic=False)
police2=pygame.font.SysFont("DejaVu Sans",14,bold=False,italic=False)

##DEBUT PROGRAMME

jouer=1
while jouer==1:
    #menu
    pygame.mixer.stop()
    window.blit(menu_principale,(0,0))
    pygame.display.flip()
    menu=0
    while menu==0:
        clickX,clickY=waitclic()
        menu=choix_menu_principale(clickX,clickY)
    if menu==1:
        nb_joueurs=2
        type_partie="2 cartes identiques"
        affichage_parametre_menu1()
        ok=0
        while ok==0:
            clickX,clickY=waitclic()
            changement_parametre_menu1(clickX,clickY)
            affichage_parametre_menu1()
        if type_partie=="2 cartes différentes":
            nb_cartes=12
            X=2
            type_cartes="musique-album"
            affichage_parametre_menu_binaire()
            ok=0
            while ok==0:
                clickX,clickY=waitclic()
                changement_parametre_menu_binaire(clickX,clickY)
                affichage_parametre_menu_binaire()
        elif type_partie=="2 cartes identiques":
            nb_cartes=12
            X=2
            type_cartes="album"
            affichage_parametre_menu_classique()
            ok=0
            while ok==0:
                clickX,clickY=waitclic()
                changement_parametre_menu_classique(clickX,clickY)
                affichage_parametre_menu_classique()
        else:
            nb_cartes=12
            X=3
            type_cartes="album-musique-logo"
            affichage_parametre_menu_ternaire()
            ok=0
            while ok==0:
                clickX,clickY=waitclic()
                changement_parametre_menu_ternaire(clickX,clickY)
                affichage_parametre_menu_ternaire()
        jouer_partie=1
        while jouer_partie==1:
            ##chargement des tableaux
            total_cartes=[[alestorm1,alestorm2,musique],[arch_enemy1,arch_enemy2,musique],[children1,children2,musique],[deicide1,deicide2,musique],[dream_theater1,dream_theater2,musique],[ghost1,ghost2,musique],[gojira1,gojira2,musique],[in_flames1,in_flames2,musique],[korn1,korn2,musique],[korpiklaani1,korpiklaani2,musique],[machine_head1,machine_head2,musique],[maiden1,maiden2,musique],[megadeth1,megadeth2,musique],[metallica1,metallica2,musique],[municipale_waste1,municipale_waste2,musique],[pantera1,pantera2,musique],[rise1,rise2,musique],[sabaton1,sabaton2,musique],[slayer1,slayer2,musique],[slipknot1,slipknot2,musique],[tool1,tool2,musique],[ultra_vomit1,ultra_vomit2,musique]]

            total_cartes2=[["alestorm","alestorm","alestorm"],["arch enemy","arch enemy","arch enemy"],["children of bodom","children of bodom","children of bodom"],["deicide","deicide","deicide"],["dream theater","dream theater","dream theater"],["ghost","ghost","ghost"],["gojira","gojira","gojira"],["in flames","in flames","in flames"],["korn","korn","korn"],["korpiklaani","korpiklaani","korpiklaani"],["machine head","machine head","machine head"],[" iron maiden"," iron maiden"," iron maiden"],["megadeth","megadeth","megadeth"],["metallica","metallica","metallica"],["municipale waste","municipale waste","municipale waste"],["pantera","pantera","pantera"],["rise of the northstar","rise of the northstar","rise of the northstar"],["sabaton","sabaton","sabaton"],["slayer","slayer","slayer"],["slipknot","slipknot","slipknot"],["tool","tool","tool"],["ultra vomit","ultra vomit","ultra vomit"]]

            total_groupes=["alestorm","arch enemy","children of bodom","deicide","dream theater","ghost","gojira","in flames","korn","korpiklaani","machine head"," iron maiden","megadeth","metallica","municipale waste","pantera","rise of the northstar","sabaton","slayer","slipknot","tool","ultra vomit"]

            total_musique_groupes=[alestorm3,arch_enemy3,children3,deicide3,dream_theater3,ghost3,gojira3,in_flames3,korn3,korpiklaani3,machine_head3,maiden3,megadeth3,metallica3,municipale_waste3,pantera3,rise3,sabaton3,slayer3,slipknot3,tool3,ultra_vomit3]
            ##preparation des parametres de la partie
            nb_cartes,x,y,longueur=parametres_cartes(nb_cartes)
            total_joueurs=[["0",rouge,(105,20)],["0",bleu,(1110,20)],["0",jaune,(305,20)],["0",vert,(905,20)]]
            joueurs=total_joueurs[:nb_joueurs]
            joueur=joueurs[0]
            total_fonds=[j1,j2,j3,j4]
            fonds=total_fonds[:nb_joueurs]
            fond=fonds[0]
            total_demi_fonds=[j1_,j2_,j3_,j4_]
            demi_fonds=total_demi_fonds[:nb_joueurs]
            demi_fond=demi_fonds[0]
            types=type(type_cartes)
            cartes,cartes2,groupes,musique_groupes=0,0,0,0
            cartes,cartes2,groupes,musique_groupes=cartes_partie(int(nb_cartes/len(types)),types)
            pygame.mixer.stop()
            affichage_partie(nb_cartes,x,y,longueur)
            pygame.display.flip()
            ##début partie
            while cartes2.count("trouvé")!=nb_cartes:
                paire=[0,0,0]
                positions=[0,0,0]
                for a in range (X):
                    indice=-1
                    while indice==-1:
                        clickX,clickY=waitclic()
                        indice,pos=click_carte(clickX,clickY,nb_cartes,x,y,longueur)
                    if a==0:
                        affichage_partie(nb_cartes,x,y,longueur)
                    paire[a],positions[a]=cartes2[indice],pos
                    pygame.mixer.stop()
                    if cartes[indice]==musique:
                        lance_musique()
                    window.blit(cartes[indice],(pos))
                    pygame.display.flip()
                    if cartes[indice]==musique:
                        lance_musique()
                if paire.count(paire[0])==X:
                    joueur[0]=score_augmente()
                    for f in range (X):
                        indice=cartes2.index(paire[0])
                        cartes2[indice]="trouvé"
                else:
                    joueur,fond,demi_fond=joueur_et_fonds_suivant()
                affichage_joueurs_et_scores()
                pygame.display.flip()
            window.blit(fin_partie,(0,0))
            distribution_des_medailles()
            jouer_partie=choix_fin_partie()
    elif menu==2:
        lance_credits()
    elif menu==3:
        jouer=0
pygame.quit()
exit(0)






































