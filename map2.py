import sys

try:
    for line in sys.stdin:
        line = line.strip()
        line = line.split(',')
        if len(line) == 13:
            anho = line[0]
            entidad = line[1]
            presupuestoInicial = line[4]
            if anho == '2016':
                
                print('%s,%s' %(entidad,presupuestoInicial))
        

except:
    pass

