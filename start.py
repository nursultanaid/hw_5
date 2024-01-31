
from logic import play_casino_game
from decouple import config

MY_MONEY = 1000

if __name__ == "__main__":
    print(f"Добро пожаловать в казино! Ваш начальный капитал: {MY_MONEY}$")
    play_casino_game(MY_MONEY)

