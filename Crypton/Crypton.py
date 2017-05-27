
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

def SelectionCryptageEvent(event):
    SelectionCryptage()

def SelectionCryptage():
    FenetreSelection.destroy()
    monFichier = open("Fichier1.txt", "w")
    monFichier.write("cryptage")
    monFichier.close


def CréationCryptageEvent(event):
    CréationCryptage()


def CréationCryptage():
      texte=Texte.get()
      clef = creationClef(Clef.get() ,texte)

      i = 0
      texteCrypté =""
      while i < len(texte):
        texteCrypté = str(texteCrypté + cryptage(texte[i] ,clef[i]))
        i+=1

      showinfo('Cryptage','Le texte Crypter se trouve dans\n./FichierCrypté')


      x = open("FichierCrypté.txt","w")
      x.write(texteCrypté)
      x.close()
      Mafenetre.destroy()


def cryptage(lettre1 ,lettre2):

    possibilité = "abcdefghijklmnopqrstuvwxyzéèàçùêûîôïë .,;:!?'ABCDEFGHIJKLMNOPQRSTUVWXYZÈÉÊŒÙÎÔÛÄËÏÖÜÀÆÇÂº¤£$}{[])("

    nombre1 = possibilité.find(lettre1)
    nombre2 = possibilité.find(lettre2)

    nombreFinal = nombre1 + nombre2

    lettreFinale = possibilité[nombreFinal]
    return(lettreFinale)

def SelectionDécryptageEvent(event):
    SelectionDécryptage()

def SelectionDécryptage():
    FenetreSelection.destroy()
    monFichier = open("Fichier1.txt", "w")
    monFichier.write("décryptage")
    monFichier.close


def CréationDécryptageEvent(event):
    CréationDécryptage()


def CréationDécryptage():

    texte=Texte.get()
    clef = creationClef(Clef.get() ,texte)

    i = 0
    texteDécrypté =""
    while i < len(texte):
        texteDécrypté = str(texteDécrypté + décryptage(texte[i] ,clef[i]))
        i+=1

    showinfo('Décryptage','Le texte Décrypter se trouve dans\n./FichierDécrypté')

    x = open("FichierDécrypté.txt","w")
    x.write(texteDécrypté)
    x.close()
    Mafenetre2.destroy()


def décryptage(lettre1 ,lettre2):

    possibilité = "abcdefghijklmnopqrstuvwxyzéèàçùêûîôïë .,;:!?'ABCDEFGHIJKLMNOPQRSTUVWXYZÈÉÊŒÙÎÔÛÄËÏÖÜÀÆÇÂº¤£$}{[])("

    nombre1 = possibilité.find(lettre1)
    nombre2 = possibilité.find(lettre2)

    nombreFinal = nombre1 - nombre2
    lettreFinale = possibilité[nombreFinal]

    return(lettreFinale)


def creationClef(clef ,texte):
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


def VerificationEvent(event):
    Verification()

def Verification():

    if Motdepasse.get() == 'crypton':

        Mafenetre.destroy()
        monFichier = open("Fichier1.txt", "w")
        monFichier.write("yes")
        monFichier.close
    else:

        showwarning('Résultat','Mot de passe incorrect.\nVeuillez recommencer !')
        Motdepasse.set('')


def Licence():

    Fenetre = Tk()
    Fenetre.geometry("190x230+425+200")
    Fenetre.title("Info")
    Fenetre.iconbitmap("Zicon clé.ico")
    Label1 = Label(Fenetre, text="Programme Crypton\nProjet ISN 2017 \n\n Créé par Laura De Freitas &\nAntonin Alves")
    Label1.pack(pady = 8)
    Label2 = Label(Fenetre, text="Licence GNU GPL\nGeneral Public License\nVoir detail dans le doc Licence.txt")
    Label2.pack()
    Label3 = Label(Fenetre, text=("Ce programme est fournis\nsans garantie de fonctionnement"))
    Label3.pack(pady = 8)
    Quit = Button(Fenetre, text=("Quit"), command=Fenetre.destroy, width=13,cursor = "sizing")
    Quit.pack()




#.............................................DEBUT DU PROGRAMME..................................................#


Mafenetre = Tk()
Mafenetre.title('Identification requise')
Mafenetre.geometry("300x80+450+200")
Mafenetre.iconbitmap("Zicon cadena.ico")

Label1 = Label(Mafenetre, text = 'Mot de passe ')
Label1.pack(side = LEFT, padx = 5, pady = 5)

Motdepasse= StringVar()
Champ = Entry(Mafenetre, textvariable= Motdepasse, show='*', bg ='white', fg='black')
Champ.focus_set()
Champ.pack(side = LEFT, padx = 5, pady = 5)

Bouton = Button(Mafenetre, text ='Valider', command = Verification,cursor = "sizing")
Bouton.pack(side = LEFT, padx = 5, pady = 5)

Mafenetre.bind('<Return>',VerificationEvent)

Mafenetre.mainloop()

monFichier = open("Fichier1.txt", "r")
contenu1 = monFichier.read()
monFichier = open("Fichier1.txt", "w")
monFichier.write(" ")
monFichier.close()

if contenu1 == "yes":


    FenetreSelection = Tk()
    FenetreSelection.title('Crypton')
    FenetreSelection.geometry("225x320+450+200")
    FenetreSelection.iconbitmap("Zicon clé.ico")


    photo = PhotoImage(file="Zcadena2.png")

    canvas = Canvas(FenetreSelection,width=100, height=60)
    canvas.create_image(52,10,anchor = N,image=photo)
    canvas.pack(side=TOP, padx = 10, pady = 10)

    Label1 = Label(FenetreSelection, text = '***** Bienvenu ! *****')
    Label1.pack(side = TOP , pady = 12)
    Label2 = Label(FenetreSelection, text = 'Que voulez vous que je fasse ?')
    Label2.pack(side = TOP , padx = 0, pady = 8)

    Cryptage = Button(FenetreSelection, text='Crypter un texte ',command = SelectionCryptage, width = 30,cursor = "sizing")
    Cryptage.pack(side = TOP ,padx = 0, pady = 0)

    Décryptage = Button(FenetreSelection, text='Décrypter un texte',command = SelectionDécryptage, width = 30,cursor = "sizing")
    Décryptage.pack( padx = 0, pady = 12)

    Licence = Button(FenetreSelection, text='A propos du programme...',command = Licence,width = 30,cursor = "sizing")
    Licence.pack( padx =0, pady = 12)

    Quit = Button(FenetreSelection, text=("Quitter"), command=FenetreSelection.destroy, width=13,cursor = "sizing")
    Quit.pack()

    FenetreSelection.mainloop()

    monFichier = open("Fichier1.txt", "r")
    selection = monFichier.read()
    monFichier = open("Fichier1.txt", "w")
    monFichier.close()

    if selection == "cryptage":

      Mafenetre = Tk()
      Mafenetre.geometry("400x150+450+200")
      Mafenetre.title('Crypton')
      Mafenetre.iconbitmap("Zicon clé.ico")

      Label1 = Label(Mafenetre, text = 'Entrer le texte à crypter...                           Entrer la clef de cryptage...')
      Label1.pack(side = TOP)
      Label2 = Label(Mafenetre,text = '   (clef de cryptage en minuscule et sans caractères spéciaux)')
      Label2.pack(side= TOP)
      Texte= StringVar()
      Champ = Entry(Mafenetre, textvariable= Texte, bg ='bisque', fg='maroon')
      Champ.focus_set()
      Champ.pack(side = LEFT, padx = 5, pady = 5)
      Clef = StringVar()
      Champ = Entry(Mafenetre, textvariable= Clef, bg ='bisque', fg='maroon')
      Champ.focus_set()
      Champ.pack(side = RIGHT, padx = 5, pady = 5)

      Quit = Button(Mafenetre, text=("Quit"), command=Mafenetre.destroy, width=13,cursor = "sizing")
      Quit.pack(side = BOTTOM, padx = 5, pady = 5)

      Bouton = Button(Mafenetre, text ='Valider', command=CréationCryptage, width=11,cursor = "sizing")
      Bouton.pack(side = BOTTOM , padx = 5, pady = 5)

      Mafenetre.bind('<Return>',CréationCryptageEvent)


      Mafenetre.mainloop()


    elif selection == "décryptage":

     Mafenetre2 = Tk()
     Mafenetre2.geometry("400x150+450+200")
     Mafenetre2.title('Crypton')
     Mafenetre2.iconbitmap("Zicon clé.ico")

     Label1 = Label(Mafenetre2, text = 'Entrer le texte à décrypter...                           Entrer la clef de décryptage...')
     Label1.pack(side = TOP)

     Texte= StringVar()
     Champ = Entry(Mafenetre2, textvariable= Texte, bg ='bisque', fg='maroon')
     Champ.focus_set()
     Champ.pack(side = LEFT, padx = 5, pady = 5)
     Clef = StringVar()
     Champ = Entry(Mafenetre2, textvariable= Clef, bg ='bisque', fg='maroon')
     Champ.focus_set()
     Champ.pack(side = RIGHT, padx = 5, pady = 5)

     Quit = Button(Mafenetre2, text=("Quit"), command=Mafenetre2.destroy, width=13,cursor = "sizing")
     Quit.pack(side = BOTTOM)

     Bouton = Button(Mafenetre2, text ='Valider', command = CréationDécryptage, width=11,cursor = "sizing")
     Bouton.pack(side = BOTTOM, padx = 5, pady = 5)

     Mafenetre2.bind('<Return>',CréationDécryptageEvent)

     Mafenetre2.mainloop()