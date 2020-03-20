import sys

try:
    for line in sys.stdin:
        line = line.strip()
        line = line.split(',')
        if len(line) == 15:
            genero = line[1]
            estado = line[14]
            if genero == 'male' or genero == 'female':
                if estado == "deceased":
                    print(genero)

except:
    pass

 