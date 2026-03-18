# Demandez un nombre entier `a l’utilisateur.
# Tant que ce nombre n’est pas compris entre 1 et 10 (inclus), affichez un message
# d’erreur et redemandez-le.
# Une fois la valeur valide obtenue, affichez : "Valeur accept´ee : X"
# N’utilisez pas break — la condition du while doit tout g´erer.

n=int(input("Entrez un chiffre svp : "))
while n < 0 or n > 10 :
    print("erreur, recommencez.")
    n = int(input("Entrez un chiffre svp : "))
print(f"Valeur acceptée : {n}")