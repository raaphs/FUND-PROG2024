def mediaUnisinos(grauA, grauB):
    mediaFinal = grauA + (grauB * 2)/3
    return mediaFinal

#EXECUTANDO
grauA = 7.4
grauB = 9.2
resultadoFinal = mediaUnisinos(grauA, grauB)
print("Resultado do Grau Final:", resultadoFinal)