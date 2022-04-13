from asyncore import write
import tkinter as tk 
import random as rd
from urllib.parse import ParseResultBytes 









# Outils
def cree_fichier_alea(nb,nomfichier):
    """nom d'un fichier sur le disque dur, fonction ouvre et lit ce fichier """
    nbrcloud = open("nbrcloud","w")
    nbrcloud=write


def lit_fichier(nomfic):
    """fichier contient les coordonnees des point d'un nuage """
    pass


def trace_Nuage(nomf):
    pass


def trace_droite(a,b):
    pass







# Calculs statistiques"
def moyenne(serie):
    pass


def variance(serie):
    pass


def covariance(serieX, serieY):
    pass


def correlation(serieX,serieY):
    pass


def forteCorrelation(serieX,serieY):
    pass

def droite_reg(serieX,serieY):
    pass









#Fonction fenetre graphique 
def Tracerdroite():
    pass

def autrecouleur():
    pass


def quitter():
    pass





#fenetre graphique
racine = tk.Tk()
racine.title("projet stats")
canvas = tk.Canvas(racine, width=1000, height=1000, bg='black')
tracerdroite = tk.Button(racine, text="Tracer la droite", command=Tracerdroite)
Autrecouleur=tk.Button(racine,text="Autre couleur",command=autrecouleur )
Quitter=tk.Button(racine,text="Quitter", command=quitter)





canvas.grid()
tracerdroite.grid()
Autrecouleur.grid()
Quitter.grid()


racine.mainloop()