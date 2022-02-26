class Transposer:
    gamma = ('C', 'D', 'E', 'F', 'G', 'A', 'H')

    def __init__(self, nuty, n):
        self.nuty = nuty
        self.n = n

    # nuty - lista nut, które chcesz poddać transpozycji
    # n - o ile chcesz przesunąć każdy akord
    def transpose(self):
        # Lista ztranspozowanych nut
        nowe_nuty = []

        for nuta in self.nuty:
            # Znajdź indeks danej nuty (np. E ma indeks 2)
            index = self.gamma.index(nuta)

            # Stranspozuj nute
            # Modulo jest po to żeby wrócić na początek listy jeśli nowy indeks będzie większy niż długość listy
            transpozowana_nuta = self.gamma[(index + self.n) % len(self.gamma)]

            # Dodaj ją do listy
            nowe_nuty.append(transpozowana_nuta)

        # Zwróć liste transpozowanych nut
        return nowe_nuty


if __name__ == '__main__':
    transposer = Transposer(['C', 'D', 'G', 'C'], 5)
    print(transposer.transpose())

