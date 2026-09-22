user_price = float(input("Entrez le prix : "))
user_pourboire = float(input("Entrez la valeur du pourboire : "))

def calcule_addition(prix, pourboire):return float(prix) * (pourboire / 100) + float(prix)
print(f"Le montant total de vôtre addition est {calcule_addition(user_price, user_pourboire)}")