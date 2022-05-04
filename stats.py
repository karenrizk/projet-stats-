from asyncore import write
import tkinter as tk 
import random as rd
from urllib.parse import ParseResultBytes 









# Outils

def cree_fichier_alea(nbr,nomfichier):
    """creation d'un fichier de texte, qui donnera sur des lignes 
    2 nombres flottants aleatoires entre 0 et 500."""
    nbrcloud = open(nomfichier,"w")
    for i in range(nbr*2):
        if i%2==0:
            k = rd.randrange(start=0,stop=500)+rd.random()
            nbrcloud.write(str(k) + " ")
        else :
            k = rd.randrange(start=0,stop=500)+rd.random()
            nbrcloud.write(str(k)+"\n")
    nbrcloud.close() 


def lit_fichier(nomfichier):
    """lit un fichier sur le disque dur et renvera 2 listes 
    premiere liste la premiere colonne et la deuxieme 
    liste les ordonnees"""
    fic = open(nomfichier,"r")
    list=[]
    liste=[]
    listX = []
    listY = []
    for ligne in fic:
        list=ligne.split()
        liste.append(list)
   
    for i in range(len(liste)):
        for j in range(2):
            if j%2==0:
                listX.append(liste[i][j])
            else:
                listY.append(liste[i][j])

    for i in range (len(listX)):
        listX[i]=float(listX[i])
    
    for i in range (len(listY)):   
        listY[i]=float(listY[i])
    fic.close()
    return listX,listY



def trace_Nuage(nomf):
    """trace un nuage de point des points de la fonction lit_fichier """
    pass


def trace_droite(a,b):
    """elle prend 2 arguments de nombres flottants
    a: le coefficiant directeur de la droite et
    b: l'ordonnée 1a l'origine.
    Rrepresentstion entre 2 points
    de cette droite."""
    pass







# Calculs statistiques"
def moyenne(serie):
    """Prend une liste de reels et calcul leur moyenne
    retourne la moyenne"""
    pass


def variance(serie):
    """prend egalement une liste de reels et calcul la variance
    retourne la variance"""
    pass


def covariance(serieX, serieY):
    """2 listes de reels representent 2 variables statistiques
     renvoie la covariance de ces deux variables """
    
    pass


def correlation(serieX,serieY):
    """prend comme argument 2 listes de reels et retourne
    leur ocefficient de correlation linéaire """

    pass


def forteCorrelation(serieX,serieY):
    """prend 2 listes de reels et decide de combien 
    elles sont correlees"""
    pass

def droite_reg(serieX,serieY):
    """calcul les coefficients de la droite 
    elle les retournera sous forme d'un tuple (coeff_dir, ord_orig)"""
    pass









#Fonction fenetre graphique 
def Tracerdroite():
    """Boutton lorsqu'on clique dessus, une ligne coloree apparait"""
    pass

def autrecouleur():
    """Lorsqu'on clique une choisie une autrevcouleur pour la droite """
    pass


def quitter():
    """Permet de fermer la fenetre entierement"""
    pass





#fenetre graphique
racine = tk.Tk()
racine.title("projet stats")
canvas = tk.Canvas(racine, width=1000, height=1000, bg='black')
tracerdroite = tk.Button(racine, text="Tracer la droite", command=Tracerdroite)
Autrecouleur=tk.Button(racine,text="Autre couleur",command=autrecouleur )
Quitter=tk.Button(racine,text="Quitter", command=quitter)





tracerdroite.grid(row=1, column=0)
Autrecouleur.grid(row=2,column=0)
Quitter.grid(row=3,column=0)
canvas.grid(rowspan=3,column=1)



racine.mainloop()