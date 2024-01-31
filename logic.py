import random
# from decouple import config

# MY_MONEY = int(config('MY_MONEY'))


MY_MONEY = 1000
def play_casino_game(starting_money):
    MY_MONEY = starting_money
    slots = list(range(1, 11))

    def play_game(amount, chosen_slot):
        winning_slot = random.choice(slots)

        if chosen_slot == winning_slot:
            return amount * 2
        else:
            return -amount

    while MY_MONEY > 0:
        print(f"Ваш текущий капитал: {MY_MONEY}$")

        bet = int(input("Сделайте ставку: "))

        if bet > MY_MONEY:
            print("Недостаточно средств. Попробуйте заново")
            continue

        chosen_slot = int(input("Выберите слот от 1 до 10: "))

        if chosen_slot not in slots:
            print("Некорректный выбор слота. Попробуйте снова.")
            continue

        result = play_game(bet, chosen_slot)
        MY_MONEY += result
        print("Баланс: {}".format(MY_MONEY))

        if MY_MONEY <= 0:
            print("Игра окончена. Вы проиграли все деньги.")
            break

        play_again = input("Хотите ли вы сыграть еще? (yes/no): ")
        if play_again.lower() != 'yes':
            break

    if MY_MONEY > 0:
        print("Вы выиграли! Поздравляю!")
    else:
        print("Вы проиграли. Удачи в следующий раз!")

