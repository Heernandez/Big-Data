import sys

salida = {}

for line in sys.stdin:
    line = line.strip()
    entidad, presupuestoInicial = line.split(',')
    if entidad in salida :
        salida[entidad]+= round(float(presupuestoInicial))
    else:
        salida[entidad] = round(float(presupuestoInicial))


for entidad in salida.keys():  
    print(entidad ," : Presupuesto Inicial para el 2016 : ", salida[entidad])
    





