
############################################################################   ##############################################################################
#                                ENGLISH                                   #   #                                 FRANÇAIS                                   #
############################################################################   ##############################################################################
#                                                                          #   #                                                                            #
#   Crypton is a free encryption software that aims to hide a string       #   #   Crypton est un logiciel de cryptage gratuit ayant pour but de cacher     #
#   by modifying it.                                                       #   #   une chaîne de caractères en la modifiant                                 #
#   Copyright (C) 2017  Alves Antonin & De Freitas Laura                   #   #   Copyright (C) 2017  Alves Antonin & De Freitas Laura                     #
#                                                                          #   #                                                                            #
#   This program is free software: you can redistribute it and/or modify   #   #   Ce programme est un logiciel gratuit : vous pouvez le redistribuer       #
#   it under the terms of the GNU General Public License 3 or later, as    #   #   et/ou le modifier en respectant les termes de la GNU General Public      #
#   published by the Free Software Foundation.                             #   #   License 3 ou plus, comme publiée par la Free Software Foundation.        #
#                                                                          #   #                                                                            #
#   This program is distributed in the hope that it will be useful,        #   #   Ce programme est distribué avec l'espoir qu'il soit util mais SANS       #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of         #   #   AUCUNE GARANTIE; sans même la garantie implicite de COMMERCIALISATION    #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #   #   ou D'ADAPTATION A UN USAGE PARTICULIER. Voir la GNU General Public       #
#   GNU General Public License for more details.                           #   #   License pour plus de détails.                                            #
#                                                                          #   #                                                                            #
#   A copy of the GNU General Public License is provided along with this   #   #   Une copie de la GNU General Public License est fournie avec ce           #
#   program in the file LICENSE.txt.                                       #   #   programme dans le fichier LICENSE.txt. Vous pouvez aussi la lire         #
#   You can also read it at <http://www.gnu.org/licenses/gpl-3.0.txt>.     #   #   à cette adresse <http://www.gnu.org/licenses/gpl-3.0.txt>.               #
#                                                                          #   #                                                                            #
#   BUG REPORT AND OTHER REQUESTS:                                         #   #   POUR REPORTER UN BUG OU POUR TOUTE AUTRE DEMANDE:                        #
#   Alves Antonin: <sir.ramalla@gmail.com>                                 #   #   Alves Antonin: <sir.ramalla@gmail.com>                                   #
#                                                                          #   #                                                                            #
############################################################################   ##############################################################################




#......Importation des modules
from tkinter import *
from tkinter.messagebox import *


#...............................DEFINITION DES FONCTIONS DU PROGRAMME........................................#

"""........On a donc les fonctions de CRYPTAGE, de DECRYPTAGE et les fonctions COMMUNES............"""

#....................FONCTION CRYPTAGE....................#

def SelectionCryptage():    # On a appuyé sur le bouton Cryptage
# On ferme la fenetre de selection, puis on ecrit "cryptage" dans le fichier texte "Fichier1.txt".

    FenetreSelection.destroy()
    monFichier = open("Fichier1.txt", "w")
    monFichier.write("cryptage")
    monFichier.close


def CréationCryptageEvent(event): # On a appuyé sur le touche Enter de clavier
    # On nous redirige vers CréationCryptage
    CréationCryptage()


def CréationCryptage(): # On créer le Cryptage
# On utilise la methode qui est detaillée dans la synthèse

      texte=Texte.get()
      clef = creationClef(Clef.get() ,texte)

      i = 0
      texteCrypté =""
      while i < len(texte):
        texteCrypté = str(texteCrypté + cryptage(texte[i] ,clef[i]))
        i+=1

      # On fait apparaitre une fenetre pop-up pour indiquer ou se trouve le résultat
      showinfo('Cryptage','Le texte Crypter se trouve dans\n ./FichierCrypté')

      # On ouvre le fichier "FichierCrypté.txt" pour y ecrire le résultat
      x = open("FichierCrypté.txt","w")
      x.write(texteCrypté)
      x.close()
      Mafenetre.destroy()


def cryptage(lettre1 ,lettre2):  # On crypte le texte lettre par lettre
# On utilise la methode qui est detaillée dans la synthèse

    possibilité = "abcdefghijklmnopqrstuvwxyzéèàçùêûîôïë .,;:!?'ABCDEFGHIJKLMNOPQRSTUVWXYZÈÉÊŒÙÎÔÛÄËÏÖÜÀÆÇÂº¤£$}{[])("

    nombre1 = possibilité.find(lettre1)
    nombre2 = possibilité.find(lettre2)

    nombreFinal = nombre1 + nombre2

    lettreFinale = possibilité[nombreFinal]
    return(lettreFinale)


#....................FONCTION DECRYPTAGE....................#

def SelectionDécryptage():    # On a appuyé sur le bouton Décryptage
# On ferme la fenetre de selection, puis on ecrit "décryptage" dans le fichier texte "Fichier1.txt".

    FenetreSelection.destroy()
    monFichier = open("Fichier1.txt", "w")
    monFichier.write("décryptage")
    monFichier.close


def CréationDécryptageEvent(event): # On a appuyé sur le touche Enter de clavier
    # On nous redirige vers CréationDécryptage
    CréationDécryptage()


def CréationDécryptage(): # On créer le Décryptage
# On utilise la methode qui est detaillée dans la synthèse

    texte=Texte.get()
    clef = creationClef(Clef.get() ,texte)

    i = 0
    texteDécrypté =""
    while i < len(texte):
        texteDécrypté = str(texteDécrypté + décryptage(texte[i] ,clef[i]))
        i+=1

    # On fait apparaitre une fenetre pop-up pour indiquer ou se trouve le résultat
    showinfo('Décryptage','Le texte Décrypter se trouve dans\n ./FichierDécrypté')

    # On ouvre le fichier "FichierDécrypté.txt" pour y ecrire le résultat
    x = open("FichierDécrypté.txt","w")
    x.write(texteDécrypté)
    x.close()
    Mafenetre2.destroy()


def décryptage(lettre1 ,lettre2): #On décrypte le texte lettre par lettre
# On utilise la methode qui est detaillée dans la synthèse
    possibilité = "abcdefghijklmnopqrstuvwxyzéèàçùêûîôïë .,;:!?'ABCDEFGHIJKLMNOPQRSTUVWXYZÈÉÊŒÙÎÔÛÄËÏÖÜÀÆÇÂº¤£$}{[])("

    nombre1 = possibilité.find(lettre1)
    nombre2 = possibilité.find(lettre2)

    nombreFinal = nombre1 - nombre2
    lettreFinale = possibilité[nombreFinal]

    return(lettreFinale)


#....................FONCTION COMMUNES....................#

def creationClef(clef ,texte):# Création de la clef de cryptage
# On agrandit la clef pour qu'elle soit aussi grande que le texte

    i = 0
    m = int(round(len(texte)/len(clef),0))
    test = clef
    while i < m:
        x = 0
        i +=1
        while x < len(clef):
            test = test + clef[x]
            x +=1
    return(test)


def VerificationEvent(event): # On a appuyé sur le touche Enter de clavier
    # On nous redirige vers Verification
    Verification()

def Verification(): #Simple verification de mot de passe
# Le mot de passe est Crypton

    if Motdepasse.get() == 'crypton':
        # le mot de passe est correct : on ecrit "yes" dans le fichier "Fichier1.txt"
        Mafenetre.destroy()
        monFichier = open("Fichier1.txt", "w")
        monFichier.write("yes")
        monFichier.close
    else:
        # le mot de passe est incorrect : on affiche une boîte de dialogue
        showwarning('Résultat','Mot de passe incorrect.\nVeuillez recommencer !')
        Motdepasse.set('')


def Licence(): # Une fenetre Tkinter basique pour donner quelque info sur le programme

    Fenetre = Tk()
    Fenetre.geometry("190x250+425+200")
    Fenetre.iconbitmap("Zicon clé.ico")
    Label1 = Label(Fenetre, text="\nProgramme Crypton\nProjet ISN 2017 \n\n Créé par Laura De Freitas &\nAntonin Alves")
    Label1.pack(pady = 8)
    Label2 = Label(Fenetre, text="Licence GNU GPL\nGeneral Public License\nVoir detail dans le doc Licence.txt")
    Label2.pack()
    Label3 = Label(Fenetre, text=("Ce programme est fournis\nsans garantie de fonctionnement"))
    Label3.pack(pady = 8)
    Quit = Button(Fenetre, text=("Quit"), command=Fenetre.destroy, width=13,cursor = "sizing")
    Quit.pack()


#.............................................DEBUT DU PROGRAMME..................................................#

""" Fenetre qui demande le mot de passe"""

# Ouverture premiere fenetre (Titre, Dimension,icon)
Mafenetre = Tk()
Mafenetre.title('Identification requise')
Mafenetre.geometry("300x80+450+200")
Mafenetre.iconbitmap("Zicon cadena.ico")

# Ajout de texte dans la fenetre
Label1 = Label(Mafenetre, text = 'Mot de passe ')
Label1.pack(side = LEFT, padx = 5, pady = 5)

# Ajout d'un champ dans lequel il sera possible d'ecrire
Motdepasse= StringVar()
Champ = Entry(Mafenetre, textvariable= Motdepasse, show='*', bg ='white', fg='maroon')
Champ.focus_set()
Champ.pack(side = LEFT, padx = 5, pady = 5)

# Ajout d'un boutton qui redirigera vers la fonction Verification
Bouton = Button(Mafenetre, text ='Valider', command = Verification)
Bouton.pack(side = LEFT, padx = 5, pady = 5)

# Ajout d'un evenement , lorsque l'on appui sur la touche entrer on nous redirigera vers la fonction VerificationEvent
Mafenetre.bind('<Return>',VerificationEvent)

# Comme une parenthese on indique que les caracteristique de la fenetre s'arrettent là
Mafenetre.mainloop()


# On ouvre le fichier "Fichier1.txt" et on lit ce qu'il y a dedans
monFichier = open("Fichier1.txt", "r")
contenu1 = monFichier.read()
monFichier = open("Fichier1.txt", "w")
monFichier.write(" ")
monFichier.close()

# Si dedans il y a ecrit 'yes' on ouvre une seconde fenetre (sachant que la precedente sera deja fermée)
if contenu1 == "yes":

    """Fenetre Principale ou l'on va choisir ce que l'on voudras faire"""

    # Ouverture premiere fenetre (Titre, Dimension, icon)
    FenetreSelection = Tk()
    FenetreSelection.title('Cryptage ou Décryptage...')
    FenetreSelection.geometry("225x320+450+200")
    FenetreSelection.iconbitmap("Zicon clé.ico")

    #On ouvre une image pour povoir l'utiliser
    photo = PhotoImage(file="Zcadena2.png")

    #On met l'image sur la fenetre de Selection (taille, marge, position)
    canvas = Canvas(FenetreSelection,width=100, height=60)
    canvas.create_image(52,10,anchor = N,image=photo)
    canvas.pack(side=TOP, padx = 10, pady = 10)

    # Ajout de texte dans la fenetre
    Label1 = Label(FenetreSelection, text = '***** Bienvenu ! *****')
    Label1.pack(side = TOP , pady = 12)
    Label2 = Label(FenetreSelection, text = 'Que voulez vous que je fasse ?')
    Label2.pack(side = TOP , padx = 0, pady = 8)

    # Ajout d'un boutton qui redirigera vers la fonction SelectionCryptage
    Cryptage = Button(FenetreSelection, text='Crypter un texte ',command = SelectionCryptage, width = 30,cursor = "sizing")
    Cryptage.pack(side = TOP ,padx = 0, pady = 0)

    # Ajout d'un boutton qui redirigera vers la fonction SelectionDécryptage
    Décryptage = Button(FenetreSelection, text='Décrypter un texte',command = SelectionDécryptage, width = 30,cursor = "sizing")
    Décryptage.pack( padx = 0, pady = 12)

    # Ajout d'un boutton qui redirigera vers la fonction Licence
    Licence = Button(FenetreSelection, text='A propos du programme...',command = Licence,width = 30,cursor = "sizing")
    Licence.pack( padx =0, pady = 12)

    # Ajout d'un boutton qui Ferme la fenetre
    Quit = Button(FenetreSelection, text=("Quitter"), command=FenetreSelection.destroy, width=13,cursor = "sizing")
    Quit.pack()

    # Comme une parenthese on indique que les caracteristique de la fenetre s'arrettent là
    FenetreSelection.mainloop()

    # On ouvre une fois de plus le fichier 'Fichier1.txt' et on lit son contenu
    monFichier = open("Fichier1.txt", "r")
    selection = monFichier.read()
    monFichier = open("Fichier1.txt", "w")
    monFichier.close()


    # Si il y est ecrit 'cryptage' alors on ouvre une nouvelle fenetre (la precedente s'etant encore fermée)
    if selection == "cryptage":

      """Fenetre où l'on rentrera les info pour le cryptage"""

      # Ouverture premiere fenetre (Titre, Dimension, icon)
      Mafenetre = Tk()
      Mafenetre.geometry("400x150+450+200")
      Mafenetre.title('Cryptage')
      Mafenetre.iconbitmap("Zicon clé.ico")

      # Ajout de texte dans la fenetre
      Label1 = Label(Mafenetre, text = 'Entrer le texte à crypter...                           Entrer la clef de cryptage...\n\n(clef en minuscule et sans caractères spéciaux)')
      Label1.pack(side = TOP)

      # Ajout de deux champ dans lequel il sera possible d'ecrire le texte a crypté ainsi que la clef de cryptage
      Texte= StringVar()
      Champ = Entry(Mafenetre, textvariable= Texte, bg ='bisque', fg='maroon')
      Champ.focus_set()
      Champ.pack(side = LEFT, padx = 5, pady = 5)
      Clef = StringVar()
      Champ = Entry(Mafenetre, textvariable= Clef, bg ='bisque', fg='maroon')
      Champ.focus_set()
      Champ.pack(side = RIGHT, padx = 5, pady = 5)

      # Ajout d'un boutton qui Ferme la fenetre
      Quit = Button(Mafenetre, text=("Quit"), command=Mafenetre.destroy, width=13,cursor = "sizing")
      Quit.pack(side = BOTTOM, padx = 5, pady = 5)

      # Ajout d'un boutton qui redirigera vers la fonction CéationCryptage
      Bouton = Button(Mafenetre, text ='Valider', command=CréationCryptage, width=11,cursor = "sizing")
      Bouton.pack(side = BOTTOM , padx = 5, pady = 5)

      # Ajout d'un evenement , lorsque l'on appui sur la touche entrer on nous redirigera vers la fonction CréationCryptageEvent
      Mafenetre.bind('<Return>',CréationCryptageEvent)
      Mafenetre.mainloop()

      # Comme une parenthese on indique que les caracteristique de la fenetre s'arrettent là
      Mafenetre.mainloop()


    # Si il y est ecrit 'décryptage' alors on ouvre une nouvelle fenetre (la precedente s'etant encore fermée)
    elif selection == "décryptage":

     """Fenetre où l'on rentrera les info pour le décryptage"""

     # Ouverture premiere fenetre (Titre, Dimension, icon)
     Mafenetre2 = Tk()
     Mafenetre2.geometry("400x150+450+200")
     Mafenetre2.title('Décryptage')
     Mafenetre2.iconbitmap("Zicon clé.ico")

     # Ajout de texte dans la fenetre
     Label1 = Label(Mafenetre2, text = 'Entrer le texte à décrypter...                           Entrer la clef de décryptage...')
     Label1.pack(side = TOP)

     # Ajout de deux champ dans lequel il sera possible d'ecrire le texte a décrypté ainsi que la clef de cryptage
     Texte= StringVar()
     Champ = Entry(Mafenetre2, textvariable= Texte, bg ='bisque', fg='maroon')
     Champ.focus_set()
     Champ.pack(side = LEFT, padx = 5, pady = 5)
     Clef = StringVar()
     Champ = Entry(Mafenetre2, textvariable= Clef, bg ='bisque', fg='maroon')
     Champ.focus_set()
     Champ.pack(side = RIGHT, padx = 5, pady = 5)

     # Ajout d'un boutton qui Ferme la fenetre
     Quit = Button(Mafenetre2, text=("Quit"), command=Mafenetre2.destroy, width=13,cursor = "sizing")
     Quit.pack(side = BOTTOM)

     # Ajout d'un boutton qui redirigera vers la fonction CéationCryptage
     Bouton = Button(Mafenetre2, text ='Valider', command = CréationDécryptage, width=11,cursor = "sizing")
     Bouton.pack(side = BOTTOM, padx = 5, pady = 5)

     # Ajout d'un evenement , lorsque l'on appui sur la touche entrer on nous redirigera vers la fonction CréationCryptageEvent
     Mafenetre2.bind('<Return>',CréationDécryptageEvent)
     Mafenetre2.mainloop()

     # Comme une parenthese on indique que les caracteristique de la fenetre s'arrettent là
     Mafenetre2.mainloop()