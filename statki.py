import random
class OceanWar:
    def __init__(self, dimension=6, all_ships=3):
        self.dimension = dimension
        self.ships = []
        self.all_ships = all_ships
        self.hidden_map = [['~'] * dimension for _ in range(dimension)]
        self.deploy_ships()
        self.attack_map = [['~'] * dimension for _ in range(dimension)]
    def map_presentation(self, map_grid):
        # Wyświetlanie planszy z numerami wierszy,kolumn
        print("   " + " ".join(str(i) for i in range(self.dimension)))
        for idx, line in enumerate(map_grid):
            print(f"{idx:2} " + " ".join(line))
        print()
    def deploy_ships(self):
        # Rozmieszczanie statków
        while len(self.ships) < self.all_ships:
            x, y = random.randint(0, self.dimension - 1), random.randint(0, self.dimension - 1)
            if (x, y) not in self.ships:
                self.ships.append((x, y))
                self.hidden_map[x][y] = 'B'
    def get_coordinates(self):
        # Pobieranie współrzędnych od gracza i sprawdzanie czy trafiono statek
        while True:
            try:
                x, y = map(int, input("Podaj wiersz i kolumnę, oddzielone spacją: ").split())
                if (x, y) in self.ships:
                    print("Trafiony!")
                    self.attack_map[x][y] = 'X'
                    self.ships.remove((x, y))
                    if not self.ships:
                        print("Gratulacje! Zatopiłeś wszystkie statki!")
                        return True
                else:
                    if self.attack_map[x][y] == '~':
                        print("Tym razem nie udało ci się!")
                        self.attack_map[x][y] = 'M'
                    else:
                        print("Atakowałeś już to pole.")
                return False
            except ValueError:
                print("Dane są błędne. Podaj dwa numery oddzielone spacją.")
            except IndexError:
                print(f"Podaj liczby w zakresie 0-{self.dimension - 1}.")
    def begin_game(self):
        print("Witaj w Bitwie Statków!")
        while True:
            self.map_presentation(self.attack_map)
            if self.get_coordinates():
                break
        print("Zatop ukryte statki")
        self.map_presentation(self.hidden_map)

if __name__ == "__main__":
    try:
        dimension = int(input("Podaj rozmiar planszy: "))
    except ValueError:
        print("Nieprawidłowe dane. Podaj liczbę całkowitą.")
        dimension = 6  # Ustawienie domyślnej wartości
    try:
        all_ships = int(input("Podaj liczbę statków: "))
    except ValueError:
        print("Nieprawidłowe dane. Podaj liczbę całkowitą.")
        all_ships = 3  # Ustawienie domyślnej wartości

    game = OceanWar(dimension, all_ships)
    game.begin_game()
