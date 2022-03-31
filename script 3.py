import matplotlib.pyplot as plt # importation de la bibliothèque des représentations graphiques
x=[0,0,0,0,0,0,0,0] # dans une liste nommée x, entrer les abscisses du point mobile séparés d’une virgule. 
y=[58.80,57.58,53.90,47.78,39.20,28.28,14.70,0] # dans une liste nommée y, entrer les ordonnées du point mobile séparés d’une virgule. Les valeurs décimales utilisent le point.
t=[0,0.5,1,1.5,2,2.5,3,3.5]
vx=[0,0,0,0,0,0,0,0]
vy=[]

for i in range (len(t)-1): # len donne le nombre d’éléments d’une liste
    vy.append((y[i+1]-y[i])/(t[i+1]-t[i]))# append permet d’ajouter des #éléments dans une liste existante

plt.title("chronophotographie d'un plongeur")
plt.xlabel("déplacement horizontal (m)")
plt.ylabel("déplacement vertical (m)")

plt.scatter(x,y,c="blue", marker='+')

plt.axis([-1,1,0,60])
plt.show()