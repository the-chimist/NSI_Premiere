import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import pi,cos

#On crée la figure une fois puis on la modifie régulièrement dans le temps
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
fig.show()

#Conditions de la simulation
c = 340.
T = 1/1000.
dt = T/10.
xmax=3.
ig=0
ir=0

#Création de la liste des valeurs de x
x=[i*xmax/1000. for i in range(1000)]

def f(x,t,c,T):
    return cos(2*pi*(t/T-x/(c*T)))
    
def anime(i):
    global c,T,dt,xmax,ig,ir,x    

    #Création de la liste des valeurs de y à l'instant i*dt
    y=[]
    for j in range(1000):
        y.append(f(x[j],i*dt,c,T))

    #On efface le graphique précédent
    ax1.clear() 

    #On trace le nouveau graphique
    ax1.plot(x,y,"blue",label="t = {:.3f}s".format(i*dt))
    
    #Si le point rouge sort de l'écran, il repart à gauche et on synchronise avec le vert
    if c*(i-ir)*dt>xmax:
        ir=i
        ig=ir

    #On trace les points
    ax1.plot([c*(i-ir)*dt],[f(c*(i-ir)*dt,i*dt,c,T)],"o",color="red")
    if c*(i-ig)*dt+c*T<xmax:
        ax1.plot([c*(i-ig)*dt+c*T],[f(c*(i-ig)*dt+c*T,i*dt,c,T)],"o",color="green")

    #On ajoute la légende et la grandeur sur l'axe des abscisses
    ax1.legend(loc='upper right',framealpha=1.)
    plt.xlabel("distance (m)")

simulation=animation.FuncAnimation(fig,anime,interval=50) #appelle la fonction anime toutes les 50 ms avec un indice i de plus en plus grand
