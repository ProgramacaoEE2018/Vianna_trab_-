import statistics
print ("Quantas Ve's foram feitas?\n")

a=input()
b=int(a)
print ("digite as notas das VE's\n")
meuVetor = []
for i in range(b):
    c=input()
    aux=float(c)
    meuVetor.append(aux)
    
mediaVE=statistics.mean(meuVetor)

print ("digite sua nota na VC\n")
e=input()
aux2=float(e)

print ("sua media de ve foi:")
print(mediaVE)
print("\n")
print ("voce precisa dessa nota para a final:")
precisafinal=(aux2+mediaVE)/2
if (10-precisafinal<=4):
    precisafinal=4
else:
    precisafinal=10-(aux2+mediaVE)/2
    
print(precisafinal)
