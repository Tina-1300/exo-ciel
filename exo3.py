from math import pi


user_rayon = float(input("Entrez vôtre rayon : "))

rayon = user_rayon

def volume_sphere(rayon=rayon) -> float:
    return (4*pi/3)* rayon**3

volume = f"Le volume de la sphère de rayon {rayon} cm est de {volume_sphere()} cm cube"

print(volume)