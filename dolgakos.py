nevek=['Tibi','Évi','sanyi','karcsi','lili']
nemek=[1,2,1,1,2]
fiu_nevek=['tibi','sanyi','karcsi']
lany=['évi','lili']
fiuk=1
lany=2
for i in range(len(nevek)):
    print (nevek [i])
    
fiu_nevek=[]
for i in range(len(nevek)):
    if nemek[i]==1:
        fiu_nevek.append(nevek[i])
print (fiu_nevek)
print(len(fiu_nevek))
print(f"{len(fiu_nevek)/len(nevek)*100}% a fiúk aránya.")