def calcule_addition(prix, pourboire=15):return float(prix) * (pourboire / 100) + float(prix)
print(f"Le montant total de vôtre addition est {calcule_addition(15.0, 10)}")