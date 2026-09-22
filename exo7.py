def calculer_montant_ttc(prix_ht, tva) :
  montant_ttc = prix_ht * (1 + (tva / 100))
  return round(montant_ttc, 2)

prix_ht = 20
tva = 20

print(f"Le montant TTC est : {calculer_montant_ttc(prix_ht, tva)}")