import random

from config.cards import CARDS


def player_loop() -> int:
    """цикл игрока"""
    player_points = 0
    player_cards = []
    player_answer = "нет"
    while player_answer != "да":
        random_card_name = random.choice(list(CARDS.keys()))
        if "Т" in random_card_name:
            player_points += 11 if player_points <= 10 else 1
        player_cards.append(random_card_name)
        player_points += CARDS[random_card_name]
        print(f"Карты игрока:{player_cards}")
        print(f"Очки игрока:{player_points}")
        del CARDS[random_card_name]
        if player_points >= 21:
            break
        player_answer = input("Закончить набор? (да/нет): ").lower()
    print()
    return player_points


def dealer_loop(player_points: int) -> int:
    """цикл дилера"""
    dealer_points = 0
    dealer_cards = []
    while dealer_points < player_points and dealer_points < 21:
        random_card_name = random.choice(list(CARDS.keys()))
        if "Т" in random_card_name:
            dealer_points += 11 if dealer_points <= 10 else 1
        dealer_cards.append(random_card_name)
        dealer_points += CARDS[random_card_name]
        print(f"Карты дилера:{dealer_cards}")
        print(f"Очки дилера:{dealer_points}")
        del CARDS[random_card_name]
    return dealer_points
