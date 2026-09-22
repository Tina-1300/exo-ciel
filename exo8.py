
user = int(input("Entrez le nombre : "))

factorial = lambda n: n * factorial(n-1) if n != 0 else 1

print(f"factorielle de {user} est {factorial(user)}")  

