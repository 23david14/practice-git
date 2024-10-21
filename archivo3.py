print("3er archivo como nuestra tercera estrella")

def suma(n1, n2):
    result = n1 + n2
    return result

def division(n1, n2):
    try:
        result = n1 / n2
    except:
        return "Error, número no divisible entre 0"

    return result

n1 = int(input("Ingrese un número: "))
n2 = int(input("Ingrese un número: "))

print(suma(2, 2))
print(division(n1, n2))