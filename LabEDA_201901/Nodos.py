# -*- coding: utf-8 -*-
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.sig  = None
    def agregaAlFinal(self,dato):
        if self.sig != None:
           self.sig.agregaAlFinal(dato)
        else:
           self.sig = Nodo(dato)
    def __str__(self):
       sal = " -> " + str(self.dato)
       if self.sig != None:
           sal = sal + str(self.sig)
       return sal    
class AsaNodos:
    def __init__(self,nombre):
        self.nombre = nombre
        self.prim = None
    def agregaAlFinal(self,dato):
        if self.prim == None:
            self.prim = Nodo(dato)
        else:
            self.prim.agregaAlFinal(dato)
    def agregaAlInicio(self,dato):
        t = self.prim
        self.prim = Nodo(dato)
        self.prim.sig = t
    def __str__(self):
        sal = "Lista de Nodos " + self.nombre + " "
        if self.prim == None:
            sal = sal + " vacìa"
        else:
            sal = sal + str(self.prim)
        return sal

def main():
  lis = AsaNodos("La lista...")
  lis.agregaAlFinal("Rafael")
  lis.agregaAlFinal(24)
  print(str(lis))

main()  
