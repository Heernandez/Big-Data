import sys

salida = {}


for line in sys.stdin:
    line = line.strip()
    
    if  line in salida :
        salida[line]+= 1
    else:
        salida[line] = 0
            
for i in salida.keys():
    print(i ," : ",salida[i])
    





