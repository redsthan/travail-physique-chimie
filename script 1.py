import matplotlib.pyplot as plt # importation de la bibliothèque des représentations graphiques
x=[0,0,0,0,0,0,0,0] # dans une liste nommée x, entrer les abscisses du point mobile séparés d’une virgule. 
y=[58.80,57.58,53.90,47.78,39.20,28.28,14.70,0] # dans une liste nommée y, entrer les ordonnées du point mobile séparés d’une virgule. Les valeurs décimales utilisent le point.

plt.scatter(x,y) # trace un graphique point par point

plt.show() # indispensable pour que la fenêtre graphique s’affiche.