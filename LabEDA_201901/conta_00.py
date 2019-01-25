class Contabilidad:
    def __init__(self, empresa, ejercicio):
        self.empresa   = empresa
        self.ejercicio = ejercicio
        self.lisPartes=[0,1,2,3,4,5]
        self.lisPartes[1] = parteContable(1,"Activo"  ,"D")
        self.lisPartes[2] = parteContable(2,"Pasivo"  ,"A")
        self.lisPartes[3] = parteContable(3,"Kapital" ,"A")
        self.lisPartes[4] = parteContable(4,"Ingresos","A")
        self.lisPartes[5] = parteContable(5,"Egresos" ,"D")

    def altaCta(self,numCta,nombreCta,naturaleza):
        #print("Contabilidad: altaCta("+str(numCta)+","+nombreCta+" ...(" + naturaleza+")")
        numId = numCta // 100000
        if numId < 1 or numId > 5:
            print("¿Apuntaste las placas de la combi?")
        else:
            self.lisPartes[numId].altaCta(numCta,nombreCta,naturaleza)       
    def __str__(self):
        cadena = "Contabilidad de " + self.empresa + " para el ejercicio " + str(self.ejercicio)
        for k in range(1,6):
          cadena += '\n' + str(self.lisPartes[k])

        return cadena
    
class parteContable:
    def __init__(self,numId,nombreParte,natParte):
        self.id     = numId
        self.nombre = nombreParte
        self.nat    = natParte
    def altaCta(self,numCta,nombreCta,naturaleza):
        print( str(self) +  ": altaCta(str(numCta)" + "," +nombreCta + " ...(" + naturaleza+")")
    def __str__(self):
        cadena = self.nombre + "          "
        return "ParteContable " + str(self.id) + " " + cadena[0:10] + " ... (" + self.nat +  ")"


#
# ================================== Script principal ================================
#

conta = Contabilidad("MiEmpre S.A.",2019)

conta.altaCta(100100,"Bancos"             ,"D")
conta.altaCta(100200,"Inventario"         ,"D")
conta.altaCta(200100,"Proveedores"        ,"A")
conta.altaCta(300000,"Kapital"            ,"A")
conta.altaCta(400100,"Ventas"             ,"A")
conta.altaCta(500100,"Costo de lo Vendido","D")

print("\n"+str(conta))



