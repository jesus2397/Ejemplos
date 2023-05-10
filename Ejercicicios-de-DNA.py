

def resumen(cadena):

    ultima_base=cadena[0]
    contador=0
    cadena_resumen=''

    for base in cadena:
        if base==ultima_base:
            contador+=1
        else:
            cadena_resumen+= ultima_base+str(contador)
            contador=1
            ultima_base=base

    reversa=cadena[::-1]
    ultima_reversa=reversa[0]

    for base in reversa:
        if base==ultima_reversa:
            contador+1
    cadena_resumen+= ultima_reversa + str(contador)
    return cadena_resumen


#cadena="AAATTGGGGAAAGCCTTTTT"
#print(resumen(cadena))

def reversa_resumen(cadena):
    salida = ""
    i=0
    for i in range(0,len(cadena),2):
        multiplicar=cadena[i]*int(cadena[i+1])
        salida+=multiplicar

    return salida


#cadena="A3T2G4A3G1C2T5"
#print(reversa_resumen(cadena))

#Splicing de intrones

def intrones(secuencia):

    secuencias={}

    primer_exon=secuencia[0:63]
    segundo_exon=secuencia[91:len(secuencia)]
    intron=secuencia[64:90]
    region_codificante=primer_exon+segundo_exon
    secuencia_resaltada=primer_exon+intron.lower()+segundo_exon

    contador=0
    for base in region_codificante:

        if base =="G" or base=="C":
            contador+=1

    porcentaje=(contador/len(region_codificante))*100

    secuencias["Region codificante"]=region_codificante
    secuencias["Porcentaje GC"]=porcentaje
    secuencias["Secuencia resaltada"]=secuencia_resaltada


    with open("secuencias.fa","w") as file: #Devolver un archivo fasta
        file.write(">exon_1\n")
        file.write(primer_exon )
        file.write("\n")
        file.write(">exon_2\n")
        file.write(segundo_exon)


    return file


#secuencia="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

#print(intrones(secuencia))

import re

def RNA_a_proteina(fichero_cadena):
    genetic_code={                #Se define la variable "genetic_code" que es un diccionario donde se recogen las equivalencias de cada codon
        "UUU": "F",    #con el aminoacido que se corresponde.
        "UUC": "F",
        "UUA": "L",
        "UUG": "L",
        "UCU": "S",
        "UCC": "S",
        "UCA": "S",
        "UCG": "S",
        "UAU": "Y",
        "UAC": "y",
        "UAA": "-STOP-",
        "UAG": "-STOP-",
        "UGU": "C",
        "UGC": "C",
        "UGA": "-STOP-",
        "UGG": "W",
        "CUU": "L",
        "CUC": "L",
        "CUA": "L",
        "CUG": "L",
        "CCU": "P",
        "CCC": "P",
        "CCA": "P",
        "CCG": "P",
        "CAU": "H",
        "CAC": "H",
        "CAA": "Q",
        "CAG": "Q",
        "CGU": "R",
        "CGC": "R",
        "CGA": "R",
        "CGG": "R",
        "AUU": "I",
        "AUC": "I",
        "AUA": "I",
        "AUG": "M",
        "ACU": "T",
        "ACC": "T",
        "ACA": "T",
        "ACG": "T",
        "AAU": "N",
        "AAC": "N",
        "AAA": "K",
        "AAG": "K",
        "AGU": "S",
        "AGC": "S",
        "AGA": "R",
        "AGG": "R",
        "GUU": "V",
        "GUC": "V",
        "GUA": "V",
        "GUG": "V",
        "GCU": "A",
        "GCC": "A",
        "GCA": "A",
        "GCG": "A",
        "GAU": "D",
        "GAC": "D",
        "GAA": "E",
        "GAG": "E",
        "GGU":"G",
        "GGC":"G",
        "GGA":"G",
        "GGG": "G"}
    


    fasta=open(fichero_cadena,'r')
    DNA = fasta.readlines()



    cadena=""
    cadena_mRNA=""
    for lines in DNA:
        if lines[0]!=">": 
           cadena = cadena + lines.rstrip()

           
    for base in cadena:
        if base=="T":
            cadena_mRNA+="U"
        else:
            cadena_mRNA+=base


    proteina=""
    for base in range(0,len(cadena_mRNA),3):
        if cadena_mRNA[base:base+3] in genetic_code:
            proteina=proteina+genetic_code[cadena_mRNA[base:base+3]]
    
    return proteina

    


RNA="sequence.fasta"

print(RNA_a_proteina(RNA))