def iif(cond,vt,vf):
    if cond:
        res = vt
    else:
        res = vf
    return res    
# --------------------------------------------------------------------------------------------------    
class Contabilidad:
    def __init__(self, empresa, ejercicio):
        self.empresa   = empresa
        self.ejercicio = ejercicio
        self.lisPartes=[0,1,2,3,4,5] # sacrifico la referencia del lugar 0
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

    def incidePoliza(self, poliza):
        #
        # verificando que la póliza esté cuadrada y que cada una de las cuentas involucradas existan
        #
        sc = 0.0
        sa = 0.0
        ban = True
        for m in poliza.colMovtos:
            ban = ban and self.valida(m.numCta)
            if m.tipoMov == "C":
                sc += m.monto
            else:
                sa += m.monto
        if sc == sa and ban:
            self.incideMovtos(poliza)
        return ban    

    def valida(self,numCta):
        numId = numCta // 100000
        ban = False
        if 1 <= numId and numId <= 5:
            ban = self.lisPartes[numId].verificaCta(numCta)
        return ban
    
    def incideMovtos(self,poliza):
        for m in poliza.colMovtos:
            numCta = m.numCta
            numId = numCta // 100000
            if 1 <= numId and numId <= 5:
               self.lisPartes[numId].incideMovto(m)
    
    def __str__(self):
        cadena = "Contabilidad de " + self.empresa + " para el ejercicio " + str(self.ejercicio)
        for k in range(1,6):
          cadena += '\n' + str(self.lisPartes[k])

        return cadena
# --------------------------------------------------------------------------------------------------    
class parteContable:
    def __init__(self,numId,nombreParte,natParte):
        self.id     = numId
        self.nombre = nombreParte
        self.nat    = natParte
        self.colCtas = {}
    def altaCta(self,numCta,nombreCta,naturaleza):
        # print( str(self) +  ": altaCta(str(numCta)" + "," +nombreCta + " ...(" + naturaleza+")")
        cta = self.colCtas.get(numCta)
        if cta == None:
          self.colCtas.update({numCta:cuentaT(numCta,nombreCta,naturaleza)})
    def verificaCta(self,numCta):
        return self.colCtas.get(numCta) != None
    def incideMovto(self,m):
        self.colCtas.get(m.numCta).incideMovto(m)
    def __str__(self):
        cadena = self.nombre + " "*20
        cadena =  "ParteContable " + str(self.id) + " " + cadena[0:10] + " ... (" + self.nat +  ")"
        for x in self.colCtas.values():
            cadena += '\n     ' + str(x)
        return cadena    
# ----------------------------------------------------------------------------------------------------
class cuentaT:
    def __init__(self,numCta,nombreCta,natCta):
        self.numCta = numCta
        self.nombre = nombreCta
        self.nat    = natCta
        self.colMovtos = []
    def incideMovto(self,movto):
        self.colMovtos.append(movto)
    def __str__(self):
         movtoSaldo = self.saldo()
         cad = self.nombre + " " * 30
         cadena = str(self.numCta) + " ... " + cad[0:20] + " (" + self.nat + ")" + \
                  iif(self.nat == "A","         "," ") + str(movtoSaldo.monto)
         return cadena
    def saldo(self):
        sc = 0.0
        sa = 0.0
        for m in self.colMovtos:
            if m.tipoMov == "C":
                sc += m.monto
            else:
                sa += m.monto
        if self.nat == "D":
             movtoSaldo = Movto(0,0,"C",sc - sa)
        else:
             movtoSaldo = Movto(0,0,"A",sa - sc)
        return movtoSaldo    
# ------------------------------------------------------------------------------------------------------
class Movto:
    def __init__(self,numPoliza, numCta, tipoMov, monto ):
        self.numPoliza = numPoliza
        self.numCta    = numCta
        self.tipoMov   = tipoMov
        self.monto     = monto
    def __str__(self):
        cadena =  str(self.numPoliza) + " ... " + str(self.numCta) + "(" + self.tipoMov + ")  "
        if self.tipoMov == "A": # Abono
            cadena += " " * 10
        cadena += str(self.monto)
        return cadena
    
# ------------------------------------------------------------------------------------------------------
class Poliza:
    def __init__(self,numPoliza, nomPoliza, fecha ): # fecha como AAAAMMDD (numérico)
        self.numPoliza = numPoliza
        self.nomPoliza = nomPoliza
        self.fecha     = fecha
        self.colMovtos =[]
    def cargo(self,numCta,monto):
        self.colMovtos.append(Movto(self.numPoliza,numCta,"C",monto))
    def abono(self,numCta,monto):
        self.colMovtos.append(Movto(self.numPoliza,numCta,"A",monto))
                       
    def __str__(self):
        cadena =  str(self.numPoliza) + " ... " + self.nomPoliza + "   " + str(self.fecha)
        for x in self.colMovtos:
           cadena += "\n" + " " * 4 + str(x)
        return cadena
            


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


print("\n"+str(conta)+"\n\n")

pol1 = Poliza(1,"Constitución de la Empresa",20190121)
pol1.cargo(100100,10000)
pol1.abono(300000,10000)

print(str(pol1))
conta.incidePoliza(pol1)

print("\n"+str(conta)+"\n\n")

pol2 = Poliza(2,"Compra de mercancía por 3000 pagados al contado",20190122)
pol2.cargo(100200,3000)
pol2.abono(100100,3000)

print(str(pol2))
conta.incidePoliza(pol2)

print("\n"+str(conta)+"\n\n")

pol3 = Poliza(3,"Venta al contado por 1500 de mercancía que costó 1000",20190122)
pol3.abono(100200,1000)
pol3.cargo(500100,1000)
pol3.abono(400100,1500)
pol3.cargo(100100,1500)

print(str(pol3))
conta.incidePoliza(pol3)

print("\n"+str(conta)+"\n\n")

#
# ========================== FIN DEL SCRIPT PRINCIPAL =====================

