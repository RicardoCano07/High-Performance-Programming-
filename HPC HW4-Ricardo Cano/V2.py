from pylab import *
import sympy as sy
import matplotlib.pyplot as plt
import numpy as np

@profile
def HenonMap(x,y,a,b,alpha,beta):
    return a- alpha*x**2+b*y, beta*x

@profile
 
def myfunction():
	#Map dependent parameters
	a = 1.4
	b = 0.3
	alpha=1
	beta=1
	
	iterates = 1000
	# Initial Condition
	xtemp = 0.1
	ytemp = 0.1
	
	x = [xtemp]
	y = [ytemp]
	
	for n in range(0,iterates):
		xtemp, ytemp = HenonMap(xtemp,ytemp,a,b,alpha,beta)
		x.append( xtemp )
		y.append( ytemp )
	
	# Plot the time series
	plt.plot(x,y,'k.')
	plt.savefig("Solucion.png",dpi=300)
	show()

	a = 1
	b = 1
	alpha=0.2
	beta=1.01
	
	R=100
	p=4
	q=4
	npoints=200
	dp=4/npoints
	dq=-4/npoints
	pgrid=[]
	qgrid=[]
	matriz=[]
	for i in range (npoints):
		pgrid.append(i*dp)
	#pgrid=np.linspace(0,4,npoints)
	
	for j in range(npoints):
		qgrid.append(j*dq)
    	#qgrid=np.linspace(-4,0,npoints)

	for i in range(npoints):
		matriz.append([])
		for j in range(npoints):
			matriz[i].append(0)
        	#values=np.zeros([npoints,npoints])
	for i in range(npoints):
		for j in range(npoints):
			xtemp = pgrid[i]
			ytemp = qgrid[j]
			aux=0
			while (xtemp**2+ytemp**2)<R:
				xtemp, ytemp = HenonMap(xtemp,ytemp,a,b,alpha,beta)
				if aux>1000:
					break
				aux+=1
			matriz[i][j]=aux
	plt.imshow(matriz, interpolation='nearest', cmap=cm.hot)
	plt.savefig("HenonMap.png",dpi=300)
	show()

myfunction()