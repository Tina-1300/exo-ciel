user_price_ht = float(input("Entrez le prix ht : "))
user_tva = float(input("Entrez la tva : "))

def calculer_montant_ttc(prix_ht, tva) :
  montant_ttc = prix_ht * (1 + (tva / 100))
  return round(montant_ttc, 2)

prix_ht = user_price_ht #20
tva = user_tva #20

print(f"Le montant TTC est : {calculer_montant_ttc(prix_ht, tva)}")