import sys

salida = {}


for line in sys.stdin:
    line = line.strip()
    edad, diag = line.split('\t')
    if diag in salida :
        salida[diag].append(edad)
    else:
        salida[diag] = []
        salida[diag].append(edad)

           
for i in salida.keys():
    sum = 0
    edades = salida[i]
    for n in edades:
        sum += int(n)
    
    print(i ," : ",round(sum/len(edades)))
    





