import random
def Tableau(NbPt):
    liste=[]
    for i in range (NbPt):
        a=random.randint(0,20)
        b=random.randint(0,20)
        if a!=b :
            for i in range (len(liste)):
                if liste[i]!=a and liste[i]!=b :
                    liste.append(Point(a,b))
    return liste
