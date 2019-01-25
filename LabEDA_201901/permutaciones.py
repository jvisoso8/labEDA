## Permutaciones
##
import sys
def permutacion(p,ind,k,n,cuantas):
    ## k es el siguiente lugar a llenar
    if k <= n:
        ##
        ## busco el siguiente valor que no se ha ocupado
        ##
        for t in range(1,n+1):
            if ind[t] == 0:
                ind[t] = 1
                p[k] = t
                permutacion(p,ind,k+1,n,cuantas)
                ind[t] = 0
    else:
        cuantas[0] = cuantas[0] + 1
        print(str(cuantas[0]) + "   " + str(p[1:]))
                    
def main(n):
    p = [0] * (n+1)
    ind = p[:]
    cuantas = [0]
    permutacion(p,ind,1,n,cuantas)
    
print(sys.argv)
n = 6
if len(sys.argv) > 1:
  print("El segundo argumento es " + sys.argv[1])
  n = int(sys.argv[1])
main(n)