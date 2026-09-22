

user = int(input("Entrer vôtre nombre : "))

def check(num) -> str:
    if num % 2 == 0:
        return "Paire"
    else:
        return "Impaire"


print(f"vôtre nombre {user} est {check(user)}")
