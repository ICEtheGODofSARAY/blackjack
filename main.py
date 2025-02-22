import random

cards = ["2ч", "2б", "2п", "2к", "3ч", "3б", "3п", "3к", "4ч", "4б", "4п", "4к", "5ч", "5б",
         "5п", "5к", "6ч", "6б", "6п", "6к", "7ч", "7б", "7п", "7к", "8ч", "8б", "8п", "8к", "9ч", "9б", "9п", "9к",
         "10ч", "10б", "10п", "10к", "Вч", "Вб", "Вп", "Вк", "Дч", "Дб", "Дп", "Дк", "Кч", "Кб", "Кп", "Кк", "Тч", "Тб",
         "Тп", "Тк"]

player_points = 0
dealer_points = 0
player_answer = "нет"
while player_points < 21:
    if player_points < 21:
        a = random.choice(cards)
        player_cards = [a]
        if a == "2ч" or "2б" or "2п" or "2к":
            player_points += 2
        elif a == "3ч" or "3б" or "3п" or "3к":
            player_points += 3
        elif a == "4ч" or "4б" or "4п" or "4к":
            player_points += 4
        elif a == "5ч" or "5б" or "5п" or "5к":
            player_points += 5
        elif a == "6ч" or "6б" or "6п" or "6к":
            player_points += 6
        elif a == "7ч" or "7б" or "7п" or "7к":
            player_points += 7
        elif a == "8ч" or "8б" or "8п" or "8к":
            player_points += 8
        elif a == "9ч" or "9б" or "9п" or "9к":
            player_points += 9
        elif a == "10ч" or "10б" or "10п" or "10к":
            player_points += 10
        elif a == "Вч" or "Вб" or "Вп" or "Вк" or "Дч" or "Дб" or "Дп" or "Дк" or "Кч" or "Кб" or "Кп" or "Кк":
            player_points += 10
        elif a == "Тч" or "Тб" or "Тп" or "Тк":
            if player_points <= 10:
                player_points += 11
            else:
                player_points += 1
        print(player_cards)
        print(player_points)
    if dealer_points < 21:
        a = random.choice(cards)
        dealer_cards = [a]
        if a == "2ч" or "2б" or "2п" or "2к":
            dealer_points += 2
        elif a == "3ч" or "3б" or "3п" or "3к":
            dealer_points += 3
        elif a == "4ч" or "4б" or "4п" or "4к":
            dealer_points += 4
        elif a == "5ч" or "5б" or "5п" or "5к":
            dealer_points += 5
        elif a == "6ч" or "6б" or "6п" or "6к":
            dealer_points += 6
        elif a == "7ч" or "7б" or "7п" or "7к":
            dealer_points += 7
        elif a == "8ч" or "8б" or "8п" or "8к":
            dealer_points += 8
        elif a == "9ч" or "9б" or "9п" or "9к":
            dealer_points += 9
        elif a == "10ч" or "10б" or "10п" or "10к":
            dealer_points += 10
        elif a == "Вч" or "Вб" or "Вп" or "Вк" or "Дч" or "Дб" or "Дп" or "Дк" or "Кч" or "Кб" or "Кп" or "Кк":
            dealer_points += 10
        elif a == "Тч" or "Тб" or "Тп" or "Тк":
            if dealer_points <= 10:
                dealer_points += 11
            else:
                dealer_points += 1
        print(dealer_cards)
        print(dealer_points)
        player_answer = input("Закончить набор? ")


if player_points == 21 or dealer_points > 21:
    print("ВЫ ВЫЙГРАЛИ")
elif dealer_points == 21 or player_points > 21:
    print("ВЫ ПРОИГРАЛИ")
