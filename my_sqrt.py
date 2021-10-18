REPETITIONS = 100000

# Returnerer kvadratroden af et tal
def my_sqrt(S):
    #Sætter kvadratroden til et input
    S = float(input("Kvadratrod af: "))
    x_n1 = (len(str(S)) / 2)
    for i in range(REPETITIONS):
        # Sæt x_n til x_n1
        x_n = x_n1
        # Beregn x_n1 via formlen
        x_n1 = (x_n+S/x_n)/2
    return x_n1


# Simpel test af my_sqrt
print(my_sqrt(100))