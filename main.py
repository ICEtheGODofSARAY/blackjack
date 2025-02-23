import random

cards = ["2ч", "2б", "2п", "2к", "3ч", "3б", "3п", "3к", "4ч", "4б", "4п", "4к", "5ч", "5б",
         "5п", "5к", "6ч", "6б", "6п", "6к", "7ч", "7б", "7п", "7к", "8ч", "8б", "8п", "8к", "9ч", "9б", "9п", "9к",
         "10ч", "10б", "10п", "10к", "Вч", "Вб", "Вп", "Вк", "Дч", "Дб", "Дп", "Дк", "Кч", "Кб", "Кп", "Кк", "Тч", "Тб",
         "Тп", "Тк"]

player_points = 0
dealer_points = 0
dealer_cards = []
player_cards = []
player_answer = "нет"
while player_points < 21:

    if player_points < 21:
        a = random.choice(cards)
        player_cards.append(a)
        if a == "2ч" or a == "2б" or a == "2п" or a == "2к":
            player_points += 2
        elif a == "3ч" or a == "3б" or a == "3п" or a == "3к":
            player_points += 3
        elif a == "4ч" or a == "4б" or a == "4п" or a == "4к":
            player_points += 4
        elif a == "5ч" or a == "5б" or a == "5п" or a == "5к":
            player_points += 5
        elif a == "6ч" or a == "6б" or a == "6п" or "6к":
            player_points += 6
        elif a == "7ч" or a == "7б" or a == "7п" or a == "7к":
            player_points += 7
        elif a == "8ч" or a == "8б" or a == "8п" or a == "8к":
            player_points += 8
        elif a == "9ч" or a == "9б" or a == "9п" or a == "9к":
            player_points += 9
        elif a == "10ч" or a == "10б" or a == "10п" or a == "10к":
            player_points += 10
        elif (a == "Вч" or a == "Вб" or a == "Вп" or a == "Вк" or a == "Дч" or a == "Дб" or a == "Дп" or a == "Дк"
              or a == "Кч" or a == "Кб" or a == "Кп" or a == "Кк"):
            player_points += 10
        elif a == "Тч" or a == "Тб" or a == "Тп" or a == "Тк":
            if player_points <= 10:
                player_points += 11
            else:
                player_points += 1
        print(player_cards)
        print(player_points)
    if dealer_points < 21:
        a = random.choice(cards)
        dealer_cards.append(a)
        if a == "2ч" or a == "2б" or a == "2п" or a == "2к":
            dealer_points += 2
        elif a == "3ч" or a == "3б" or a == "3п" or a == "3к":
            dealer_points += 3
        elif a == "4ч" or a == "4б" or a == "4п" or a == "4к":
            dealer_points += 4
        elif a == "5ч" or a == "5б" or a == "5п" or a == "5к":
            dealer_points += 5
        elif a == "6ч" or a == "6б" or a == "6п" or a == "6к":
            dealer_points += 6
        elif a == "7ч" or a == "7б" or a == "7п" or a == "7к":
            dealer_points += 7
        elif a == "8ч" or a == "8б" or a == "8п" or a == "8к":
            dealer_points += 8
        elif a == "9ч" or a == "9б" or a == "9п" or a == "9к":
            dealer_points += 9
        elif a == "10ч" or a == "10б" or a == "10п" or a == "10к":
            dealer_points += 10
        elif (a == "Вч" or a == "Вб" or a == "Вп" or a == "Вк" or a == "Дч" or a == "Дб" or a == "Дп" or a == "Дк"
              or a == "Кч" or a == "Кб" or a == "Кп" or a == "Кк"):
            dealer_points += 10
        elif a == "Тч" or a == "Тб" or a == "Тп" or a == "Тк":
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
