import os

from config.paths import PLAYERS_TXT_PATH
from file_handler.read import get_content


def check_login(login: str, file_path: str = PLAYERS_TXT_PATH) -> bool:
    logins = []
    file_content = get_content()
    file_lines = file_content.split("\n")
    for _login in file_lines:
        logins.append(_login.split(":")[0])
    return login in logins


def register_user(new_user_login: str, cash: int = 0) -> None:
    with open(PLAYERS_TXT_PATH, "a") as file:
        file.write(f"{new_user_login}:{cash}\n")


def update_cash(user: str, new_cash: int):
    content = get_content()
    new_content = ""
    content = content.split("\n")
    for row in content:
        if ":" in row:
            login, cash = row.split(":")
            if login == user:
                new_content += f"{login}:{int(cash) + int(new_cash)}\n"
            else:
                new_content += f"{login}:{cash}\n"

    with open(PLAYERS_TXT_PATH, "w") as file:
        file.write(f"{new_content}\n")


def get_user_cash(user: str) -> int:
    content = get_content()
    content = content.split("\n")
    for row in content:
        login, cash = row.split(":")
        if login == user:
            return int(cash)


def registration() -> str:
    player_login = input("Пожалуйста введите ваш логин: ")
    if check_login(login=player_login):
        user_cash = get_user_cash(user=player_login)
        print(f"ПРИВЕТСТВУЕМ ВАС СНОВА, {player_login}!!!!! ВАШ ТЕКУЩИЙ БАЛАНС - {user_cash}")
        player_cash_answer = input("Хотите пополнить счет? (да/нет): ").lower()
        if player_cash_answer == "да":
            update_cash(user=player_login, new_cash=int(input("На сколько вы хотите пополнить счет? ")))
    else:
        print("ВЫ НЕ ЗАРЕГИСТРИРОВАНЫ!!!")
        register_user(new_user_login=player_login, cash=int(input("На сколько вы хотите пополнить счет? ")))
    return player_login
