from math import pi

rayon:int = 14

def volume_sphere(rayon=rayon) -> float:
    return (4*pi/3)* rayon**3

volume = f"Le volume de la sphère de rayon {rayon} cm est de {volume_sphere()} cm cube"

print(volume)