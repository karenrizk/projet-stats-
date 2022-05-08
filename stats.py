
import tkinter as tk 
import random as rd
import csv



#Longueur et largeur de notre canvas
longueur = 600
largeur = 600

#l'initialisation de nos listes vides
listX = []
listY = []
lx=[]
ly=[]


#Variable pour le fichier ville virgule
list10=[]
list12=[]

nb_10=[]
nb_12=[]

hab_10=[]
hab_12=[]






# Liste de couleurs
c = ['deepskyblue3', 'peachpuff', 'salmon', 'mediumorchid', 'darkturquoise', 'lawngreen', 'gold', 'blue', 'green',
     'red', 'black']

#Variables Globales     
a = 0
b = 0
v = "green"

def file_cvs():
    """Prendre le fichier cvs villes_virgules et extraire les 2 listes entières"""
    filename = open('villes_virgule.csv','r')

    file=csv.DictReader(filename)

    for col in file:
        nb_10.append(col["nb_hab_2010"])
        nb_12.append(col["nb_hab_2012"])

    for i in range(len(nb_10)):
        nb_12[i]=float(nb_12[i])
        if nb_10[i]<=500:
            hab_10.append(nb_10[i])
        else:
            continue

    for i in range(len(nb_12)):
        nb_12[i]=float(nb_12[i])
        if nb_12[i]<=500:
            hab_12.append(nb_12[i])
        else:
            continue

    print('nb_hab_2010:',hab_10)
    print('nb_hab_2012:',hab_12)

    filename.close()

def trace_Nuage100():
    """Tracer le nuage de point des 100 premières valeurs du fichier """
    x = 0
    y = 0
    rayon = 2

    for i in range(100):
        list10.append(nb_10[i])
        list12.append(nb_12[i])

    for i in range(len(list10)):
        x = list10[i]
        y = list12[i]
        cercle = canvas.create_oval((x - rayon,y - rayon), (x + rayon,y + rayon), fill='red')

def trace_Nuage_n():
    """Trace nuage de la fonction villes_virgules en rentrant un nombre n"""
    n= int(input('rentrez le nombre de valeurs que vous voulez prendre en compte'))
    x = 0
    y = 0
    rayon = 2

    for i in range(100):
        list10.append(nb_10[i])
        list12.append(nb_12[i])

    for i in range(len(list10)):
        x = list10[i]
        y = list12[i]
        cercle = canvas.create_oval((x - rayon,y - rayon), (x + rayon,y + rayon), fill='red')


def cree_fichier_alea(nbr, nomfichier):
    """creation d'un fichier de texte, qui donnera sur des lignes
    2 nombres flottants aleatoires entre 0 et 500."""
    nbrcloud = open(nomfichier, "w")
    for i in range(nbr * 2):
        if i % 2 == 0:
            k = rd.randrange(start=0, stop=500) + rd.random()
            nbrcloud.write(str(k) + " ")
        else:
            k = rd.randrange(start=0, stop=500) + rd.random()
            nbrcloud.write(str(k) + "\n")
    nbrcloud.close()


def lit_fichier(nomfichier):
    """lit un fichier sur le disque dur et renvera 2 listes
    premiere liste la premiere colonne et la deuxieme
    liste les ordonnees"""
    fic = open(nomfichier, "r")
    list = []
    liste = []
    for ligne in fic:
        list = ligne.split()
        liste.append(list)

    for i in range(len(liste)):
        for j in range(2):
            if j % 2 == 0:
                listX.append(liste[i][j])
            else:
                listY.append(liste[i][j])
            
    for i in range(len(listX)):
        listX[i] = float(listX[i])

    for i in range(len(listY)):
        listY[i] = float(listY[i])

    fic.close()
    
    print("La taille de la liste est ",len(listX))
    return listX, listY

def trace_Nuage(nomfichier):
    """trace un nuage de point des points de la fonction lit_fichier """
    x = 0
    y = 0
    l1=list(listX)
    l2=list(listY)
    rayon = 2
    l="red"

    for i in range(11):
        l=rd.choice(c)

    for i in range(len(l1)):
        x = l1[i]
        y = l2[i]
        cercle = canvas.create_oval((x - rayon,y - rayon), (x + rayon,y + rayon),
                                    fill=l)     
    print("il y a ",(len(l1)),"points")                                                          
    return (len(l1))



def trace_droite(a, b):
    global v,ligne
    """elle prend 2 arguments de nombres flottants
    a: le coefficiant directeur de la droite et
    b: l'ordonnée 1a l'origine.
    Representation entre 2 points
    de cette droite."""
    x1, y1 = 0, b  # on a l'ordonnee a l'origine qui sert de premier point
    x2, y2 = len(listX), a * len(listX) + b  # on calcule l'emplacement du dernier point
    ligne=canvas.create_line((x1, y1), (x2, y2), fill=v)


# Calculs statistiques"
def moyenne(listX):
    """Prend une liste de reels et calcul leur moyenne
    retourne la moyenne"""
    moy = 0
    serieX=list(listX)
    for i in range(len(listX)):
        moy +=listX[i]
    moy /= len(listX)
    return moy


def moyenne(listY):
    """Prend une liste de reels et calcul leur moyenne
    retourne la moyenne"""
    moy = 0
    for i in range(len(listY)):
        moy += listY[i]
    moy /= len(listY)
    return moy


def variance(listX):
    """prend egalement une liste de reels et calcul la variance
    retourne la variance"""
    var = 0
    moy = moyenne(listX)
    for i in range(len(listX)):
        var += (listX[i] - moy) ** 2
    var /= len(listX)
    return (var)


def variance(listY):
    """prend egalement une liste de reels et calcul la variance
    retourne la variance"""
    var = 0
    moy = moyenne(listY)
    for i in range(len(listY)):
        var += (listY[i] - moy) ** 2
    var /= len(listY)
    return (var)


def covariance(listX, listY):
    """2 listes de reels representent 2 variables statistiques
     renvoie la covariance de ces deux variables """
    moyX, moyY = moyenne(listX), moyenne(listY)
    cov = 0
    for i in range(len(listX)):
        cov += (listX[i] - moyX) * (listY[i] - moyY)
    cov /= len(listX)
    return (cov)


def correlation(listX, listY):
    """prend comme argument 2 listes de reels et retourne
    leur coefficient de correlation linéaire """
    cov = covariance(listX, listY)
    varX, varY = variance(listX), variance(listY)
    cor = cov / ((varX * varY) ** (1 / 2))
    return (cor)


def forteCorrelation(listX, listY):
    """prend 2 listes de reels et decide de combien
    elles sont correlees"""

    cor = correlation(listX, listY)
    if cor >= 0.8 and cor <= 1:
        return True
    elif cor <= -0.8 and cor >= -1:
        return True
    else:
        return False


def droite_reg(listX, listY):
    global a, b
    """calcul les coefficients de la droite 
    elle les retournera sous forme d'un tuple (coeff_dir, ord_orig)"""
    if forteCorrelation(listX, listY) == True:
        a = covariance(listX, listY) / variance(listX)
        b = moyenne(listY) - (a * moyenne(listX))
    else:
        print("la correlation des points entre elle n'est pas assez forte afin de modeliser une droite de regression")    
    tuple_test = (coeff_dir, ord_orig) = (a, b)
    return tuple_test


# fenetre graphique.


def autrecouleur():
    global v,ligne
    """Lorsqu'on clique une choisie une autre couleur pour la droite """
    c_choice = rd.choice(c)
    v = c_choice
    canvas.itemconfig(ligne,fill=v)

def marchebouton():
    """change la configuration du point """
    if Dessin['text']=="Dessin":
        Dessin['text']="Arret"
        
    
    else:
        Dessin['text']="Dessin"  
 


def dessinpt(event):
    """Prend les coordonnées des clics et puis calcul la correlation et dessine la droite"""
    if Dessin['text']=="Arret":
        x, y = event.x, event.y
        rond=canvas.create_oval((x-3,y-3),((x+3),(y+3)),fill="red",width=2)
        lx.append(x)
        ly.append(y)
    else:
        tracerdroite.configure(command=lambda test1 = droite_reg(list_testx,list_testy):trace_droite(*test1))
 
    
    if forteCorrelation(lx,ly)==True:
        list_X,list_Y=lx,ly
        tracerdroite.configure(command=lambda test2=droite_reg(list_X,list_Y): trace_droite(*test2))
    else:
        print("il n'ya pas de forte correlation entre les points")
        tracerdroite.configure(command=lambda test1 = droite_reg(list_testx,list_testy):trace_droite(*test1))




# fenetre graphique
racine = tk.Tk()
racine.title("projet stats")
canvas = tk.Canvas(racine, width=largeur, height=longueur, bg='black')
cree_fichier_alea(nbr,nomfichier)#veuiller ecrire le nom du fichier et le nombre de ligne si vous ne souhaitez pas créer un fichier aléatoire veuillez mettre un # avant
list_testx, list_testy = lit_fichier(nomfichier) #veuiller ici le nom du fichier avec des guillemets 
tracerdroite = tk.Button(racine, text="Tracer la droite", command=lambda test1 = droite_reg(list_testx,list_testy)  : trace_droite(*test1))
Autrecouleur = tk.Button(racine, text="Autre couleur", command=autrecouleur)
Quitter = tk.Button(racine, text="Quitter", command=canvas.quit)
Dessin = tk.Button(racine,text= " Dessin", command=marchebouton)

trace_Nuage(nomfichier) #veuiller ecrire le nom du fichier à utiliser

#file_cvs()
#trace_Nuage100()
#trace_Nuage_n()
#correlation(hab_10,hab_12)
#forteCorrelation(hab_10,hab_12)


canvas.bind('<Button-1>',dessinpt)
Dessin.grid()
tracerdroite.grid()
Autrecouleur.grid()
Quitter.grid()
canvas.grid()


racine.mainloop()

