notes = [12, 15, 10, 17, 4, 2]

# Calcul de la moyenne

def moyenne_non_ponderer(notes):
    return sum(notes) / len(notes)

print(f"La moyenne est : {moyenne_non_ponderer(notes)}")
