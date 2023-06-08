from string import *
#from Numeric import *
import random


def llenarMatriz(tam,p):
    matriz = []
    for i in range(tam):
        col = []
        for j in range(tam):
            rnd = random.randrange(0,99)
            if rnd < p:
                col.append(1)
            else:
                col.append(0)
            if j==tam-1 :
                col[j] = 2
        matriz.append(col)
    return matriz



#--------------.ma---------------------------------

codigoCD = open("codigo.ma",'w')
tam = 100

dato = """[top]\n""" 
dato = dato + """components : perco\n"""
dato = dato + """\n"""
dato = dato + """[perco]\n"""
dato = dato + """type : cell\n"""
dato = dato + """width : %i\n"""%tam
dato = dato + """height : %i\n"""%tam
dato = dato + """delay : transport\n"""
dato = dato + """defaultDelayTime : 500\n"""
dato = dato + """border : nowrapped\n""" 
dato = dato + """neighbors : perco(-1,-1)  perco(-1,0) perco(-1,1)\n"""
dato = dato + """neighbors : perco(0,-1)   perco(0,0)  perco(0,1)\n"""
dato = dato + """neighbors : perco(1,-1)   perco(1,0)  perco(1,1)\n"""
dato = dato + """initialvalue : 0\n"""
codigoCD.write(dato)
#codigoCD.write("\n")
matriz = llenarMatriz(tam,41)
for i in range(len(matriz)):
    colum = ""
    for j in range(len(matriz[i])):
        colum = colum + """%s"""%matriz[i][j]
    codigoCD.write("initialrowvalue :  %i     %s\n"%(i, colum))
codigoCD.write("localtransition : perco-rule\n")
codigoCD.write("\n")
codigoCD.write("[perco-rule]\n")
codigoCD.write("rule : 0 100 { (0,0) = 8 and falsecount = 8} \n")
codigoCD.write("rule : 8 100 { (0,0) = 7}\n")
codigoCD.write("rule : 7 100 { (0,0) = 6}\n")
codigoCD.write("rule : 6 100 { (0,0) = 5}\n")
codigoCD.write("rule : 5 100 { (0,0) = 4}\n")
codigoCD.write("rule : 4 100 { (0,0) = 3}\n")
codigoCD.write("rule : 3 100 { (0,0) = 2}\n")
codigoCD.write("rule : 2 100 { (0,0) = 1 and (statecount(2) > 0 or statecount(3) > 0 or statecount(4) > 0)} \n")
codigoCD.write("rule : 1 100 { (0,0) = 1 } \n")
codigoCD.write("rule : 0 100 { t } \n")

codigoCD.close()
print "Listo"


