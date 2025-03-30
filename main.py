from Utilits.file_handler import update_cash, registration, get_user_cash
from session import player_loop, dealer_loop

if __name__ == '__main__':
    # регистрация
    player_login = registration()

    play_more = "да"
    while play_more == "да":
        player_bet = int(input("Введите ставку: "))
        while player_bet > get_user_cash(player_login):
            print("но но но мистер фиш")
            player_bet = int(input("Введите ставку: "))
        # Цикл игрока
        player_points = player_loop()
        if player_points == 21:
            update_cash(user=player_login, new_cash=player_bet)
            print("ВЫ ВЫЙГРАЛИ")
        elif player_points > 21:
            print("ВЫ ПРОИГРАЛИ")
            update_cash(user=player_login, new_cash=-player_bet)
        else:
            # Цикл дилера
            dealer_points = dealer_loop(player_points=player_points)
            if dealer_points > 21:
                print("ВЫ ВЫЙГРАЛИ")
                update_cash(user=player_login, new_cash=player_bet)
            elif dealer_points > player_points:
                print("ВЫ ПРОИГРАЛИ")
                update_cash(user=player_login, new_cash=-player_bet)
        print(get_user_cash(player_login))
        play_more = input("Хотите играть дальше? (да/нет): ").lower()
