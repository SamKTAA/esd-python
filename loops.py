def multiplie(a, b):
    """
    Multiplie deux nombres par additions successives.
    """
    x = 0
    for i in range(b):
        x += a
    return x

def puissance(base, exposant):
    """
    Calcule la puissance d'un nombre par multiplication successives.
    """
    x = 1
    for i in range(exposant):
        x = multiplie(x, base)
    return x

print(multiplie(12,5))
print(puissance(12,6))
   