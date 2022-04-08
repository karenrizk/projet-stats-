import tkinter as tk 
import random as rd
from urllib.parse import ParseResultBytes 





def cree_fichier_alea(nb,nomfichier):
    pass


def lit_fichier(nomfic):
    pass


def trace_Nuage(nomf):
    pass


def trace_droite(a,b):
    pass


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


def Tracerdroite():
    pass





racine = tk.Tk()
racine.title("projet stats")
canvas = tk.Canvas(racine, width=1000, height=1000, bg='black')
tracerdroite = tk.Button(racine, text="Tracer la droite", command=Tracerdroite)
