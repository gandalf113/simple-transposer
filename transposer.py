gamma = ('C', 'D', 'E', 'F', 'G', 'A', 'H')


# nuty - lista nut, które chcesz poddać transpozycji
# n - o ile chcesz przesunąć każdy akord
def transpose(nuty, n):
    # Lista ztranspozowanych nut
    nowe_nuty = []

    for nuta in nuty:
        # Znajdź indeks danej nuty (np. E ma indeks 2)
        index = gamma.index(nuta)

        # Stranspozuj nute
        # Modulo jest po to żeby wrócić na początek listy jeśli nowy indeks będzie większy niż długość listy
        transpozowana_nuta = gamma[(index + n) % len(gamma)]

        # Dodaj ją do listy
        nowe_nuty.append(transpozowana_nuta)

    # Zwróć liste transpozowanych nut
    return nowe_nuty


nutki = ['C', 'D', 'G', 'C']
print(transpose(nutki, 1))
print(transpose(nutki, 5))
print(transpose(nutki, -2))
