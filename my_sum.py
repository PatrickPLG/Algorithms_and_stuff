# Returnerer summen af en række tal
def my_sum(number_list):
    result = 0
    for x in number_list:
        # Operatoren += bruges til lægge tal til result
        result += x
    return result


# Simpel test af sum-funktionen
print(my_sum([100, 23, 89, 42, 5]))
