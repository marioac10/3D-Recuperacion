#Mario Edmundo Ac Hernandez
#No. Control: 18390055
#Programa para plotear un plano(Triangular) y el hit point, asi como sus respectivos triangulos y
#el calculo de sus area para saber si el hit point esta dentro o fuera

#Profe no pude realizar que es programa finalizara presionando la tecla Esc, solo pude escribiendo esc.
import matplotlib.pyplot as plt 
import numpy as np
from math import sin, cos, radians,sqrt
#import keyboard

#Coordenadas globales
xg=[]
yg=[]
zg=[]
#Cordenadas centrales
xc=80
yc=40
zc=40
#Plano del sistema y hitpoint
x=[]
y=[]
z=[]

def plotTriangleLine(x,y,z,xg,yg,zg,hpx,hpy):#Funcion para plotear el Plano(Triangular) y el hitpoint

    plt.axis([0,250,200,0])#Definimos el tamaño de la ventana
    plt.axis('on')
    plt.grid(True)

    #Ejes X Y 
    plt.plot([8,240],[8,8],color='k')
    plt.text(120,5.5,'X')
    plt.plot([8,8],[8,190],color='k')
    plt.text(3,80,'Y')

    x=[40,30,80,hpx]#Llenamos los vectores con el hitpoint
    y=[60,10,60,hpy]
    z=[0,0,0,0]

    for i in range(len(x)):#Llenamos los vectores globales
        xg.append(x[i]+xc)
        yg.append(y[i]+yc)
        zg.append(z[i]+zc)

    AA,AA1,AA2=plotHitpoint(x,y,z)

    plt.text(xg[0],yg[0],'0')
    plt.text(xg[1],yg[1],'1')
    plt.text(xg[2],yg[2],'2')
    plt.text(xg[3],yg[3],'3')
    plt.text(xg[3]+4,yg[3]+4,'Hitpoint')
    plt.title("Triangular Plane And Hitpoint")
    
    plt.plot([xg[0],xg[1]],[yg[0],yg[1]],color='k')#Ploteamos el Plano Base(Triangulo A)
    plt.plot([xg[1],xg[2]],[yg[1],yg[2]],color='k')
    plt.plot([xg[2],xg[0]],[yg[2],yg[0]],color='k')
    plt.text(xg[0]+10,yg[0]-15,'A',color ='k')

    plt.plot([xg[0],xg[1]],[yg[0],yg[1]],color='purple')#Ploteamos el Triangulo A1
    plt.plot([xg[1],xg[3]],[yg[1],yg[3]],color='purple')
    plt.plot([xg[3],xg[0]],[yg[3],yg[0]],color='purple')
    plt.text(xg[1]-5,yg[1]+30,'A1',color ='purple')

    plt.plot([xg[0],xg[2]],[yg[0],yg[2]],color='g')#Ploteamos el triangulo A2
    plt.plot([xg[2],xg[3]],[yg[2],yg[3]],color='g')
    plt.plot([xg[3],xg[0]],[yg[3],yg[0]],color='g')
    plt.text(xg[2]-27,yg[2]+7,'A2',color ='g')

    #ETIQUETAS DE LAS AREAS
    plt.text(15,150,'El area del Triangulo A es: ' + str(AA),color ='k')
    plt.text(15,160,'El area del Triangulo A1 es: ' + str(AA1),color='purple')
    plt.text(15,170,'El area del Triangulo A2 es: ' + str(AA2),color ='g')
    Total=AA1+AA2
    plt.text(15,180,'La suma del area de los Triangulos A1+A2= ' + str(Total))

    #Calculamos si el Hitpoint está dentro o fuera del límite
    if(AA1+AA2 > AA):
        plt.text(15,25,'El Hitpoint esta fuera del límite',color ='k')
        plt.scatter(xg[3],yg[3],s=22,color='orange') #Pintamos el hitpoint
    elif (AA1+AA2 < AA):
        plt.text(15,25,'El Hitpoint esta dentro del límite',color ='k')
        plt.scatter(xg[3],yg[3],s=22,color='blue') #Pintamos el hitpoint 

    plt.show()


def plotHitpoint(x,y,z):#Calculamos cada una de las areas de los triangulos con el Hitpoint
    #Triangulo A
    #Distance point 0 to 1
    a=x[1]-x[0]
    b=y[1]-y[0]
    c=z[1]-z[0]
    D1=sqrt(a*a+b*b+c*c) 
    #Distance point 1 to 2
    a=x[2]-x[1]
    b=y[2]-y[1]
    c=z[2]-z[1]
    D2=sqrt(a*a+b*b+c*c) 
    #Distance point 2 to 0
    a=x[2]-x[0]
    b=y[2]-y[0]
    c=z[2]-z[0]
    D3=sqrt(a*a+b*b+c*c) 

    s1 = (D1+D2+D3)/2 #Calculamos el semiperimetro del triangulo A
    A1 = sqrt(s1*(s1-D1)*(s1-D2)*(s1-D3))

    #Triangulo A1
    #Distance point 0 to 1
    a=x[1]-x[0]
    b=y[1]-y[0]
    c=z[1]-z[0]
    D11=sqrt(a*a+b*b+c*c) 
    #_____distance point 1 to 3
    a=x[3]-x[1]
    b=y[3]-y[1]
    c=z[3]-z[1]
    D22=sqrt(a*a+b*b+c*c) 
    #_____distance point 3 to 0
    a=x[3]-x[0]
    b=y[3]-y[0]
    c=z[3]-z[0]
    D33=sqrt(a*a+b*b+c*c)  

    s2 = (D11+D22+D33)/2 #Calculamos el semiperimetro del triangulo A1
    A2 = sqrt(s2*(s2-D11)*(s2-D22)*(s2-D33))  

    #Triangulo A2
    #__Distance point 0 to 2
    a=x[2]-x[0]
    b=y[2]-y[0]
    c=z[2]-z[0]
    D111=sqrt(a*a+b*b+c*c) 
    #__Distance point 2 to 3
    a=x[3]-x[2]
    b=y[3]-y[2]
    c=z[3]-z[2]
    D222=sqrt(a*a+b*b+c*c) 
    #__Distance point 3 to 0
    a=x[3]-x[0]
    b=y[3]-y[0]
    c=z[3]-z[0]
    D333=sqrt(a*a+b*b+c*c) 

    s3 = (D111+D222+D333)/2 #Calculamos el semiperimetro del triangulo A2
    A3 = sqrt(s3*(s3-D111)*(s3-D222)*(s3-D333))

    return A1,A2,A3

#Pedimimos al usuario que ingrese las coordenas del Hitpoint y luego ploteamos
while True:
    axis=input('Presione una tecla para ingresar la coordenadas del Hitpoint o escriba esc para salir: ')
    if axis=='esc':
        break
    elif axis!="":
        hpx=(float(input('Coordenada X: ')))
        hpy=(float(input('Coordenada Y: ')))
        plotTriangleLine(x,y,z,xg,yg,zg,hpx,hpy)



