#exercice 2
myTable=[5,7,3,9,2]

for i in range(len(myTable)-1):
    chiffrechoisit=myTable[i]
    chiffresuivant=i+1
    chiffrecomparé=myTable[chiffresuivant]
    if (chiffrechoisit>chiffrecomparé):
        
        stock=myTable[i]
        myTable[i]=myTable[chiffresuivant]
        myTable[chiffresuivant]=stock
print(myTable)