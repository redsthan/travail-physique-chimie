import matplotlib.pyplot as plt
import math

x=[0]*8
y=[58.80,57.58,53.90,47.78,39.20,28.28,14.70,0]
t=list(map(lambda x: x/2, range(8)))
vx=[0]*8
vy=[(y[i]-y[i-1])/(t[i]-t[i-1]) for i in range(1,len(t))]
echelle=2.3

print("\n".join(["A la hauteur {} m, la vitesse atteinte par Laso Schaller est d'environ {} km/h".format(y[i+1],round(-3.6*vy[i]*100)/100) for i in range(len(t)-1)]))


plt.title("évolution de la vitesse du plongeur")
plt.xlabel("temps (s)")
plt.ylabel("vitesse (m/s)")
plt.scatter(list(t[1::]),list(map(lambda x:-x, vy)),c="purple", marker='+')
plt.axis([0,4,0,40])

plt.show()


for i in range(len(t)):
    plt.close("all")
    
    for it in range(i):
        plt.arrow(0,y[it+1],0,vy[it]/echelle,head_width=0.025,head_length=0.5,length_includes_head=True)
    
    plt.title("chronophotographie d'un plongeur")
    plt.xlabel("déplacement horizontal (m)")
    plt.ylabel("déplacement vertical (m)")
    plt.scatter(x,y,c="red", marker='+')
    plt.axis([-1,1,-30,60])
    
    plt.pause(1)

    plt.show()