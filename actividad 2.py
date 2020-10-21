from numpy import linalg

def tabla(X,TABLA,aNorm):

    for i in range(1,30):
        x=X[0]; y=X[1]; z=X[2]
        F=[(((x-4)**2)+((y+9)**2)+((z)**2)-14.04**2),(((x-7)**2)+((y+8)**2)+((z)**2)-14.59**2),(((x-8)**2)+((y+2)**2)+((z)**2)-12.96**2)]
        J=[[2*(x-4),2*(y+9),2*(z)],[2*(x-2),2*(y+8),3*(z)],[4*(x-8),2*(y+2),2*(z)]]
        DX=-linalg.solve(J,F)
        X=X+DX
        if linalg.norm(F)< aNorm:
            TABLA.append([X[0],X[1],X[2]])
            print "Posicion (x,y,z) ="
            TABLA[0][0]=int(TABLA[0][0])
            TABLA[0][1]=int(TABLA[0][1])
            TABLA[0][2]=int(TABLA[0][2])
            print TABLA
            break


X = [1,1,1]
TABLA = []
aNorm = 1e-15
tabla(X,TABLA,aNorm)