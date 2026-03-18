# word=input("Entrez un mot svp")
# charac=input("Entrez un charactere svp")
# i=0
# last_charact = ""
# while word[i:] != last_charact :
#         i+=1
#         last_charact=charac
#         if
# print(i+1)

mot = input("introduisez un mot : ")
c = input("Introduisez une lettre : ")

estP = False
i=0

while i<len(mot) and estP == False:
    if mot[i]==c:
        estP=True
    i+=1

if estP:
    print("Présent")
else:
    print("Absent")