
def count_substring(cadena,motivo):
    contador=0
    base=0

    for base in range(len(cadena)):
        if cadena[base:base+len(motivo)]==motivo:
            contador=contador+1

    return contador


cadena="ATGATATATATATGATA"

motivo="AT"

print(count_substring(cadena,motivo))
