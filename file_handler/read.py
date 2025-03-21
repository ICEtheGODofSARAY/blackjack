from config.paths import PLAYERS_TXT_PATH


def get_content(path: str = PLAYERS_TXT_PATH) -> str:
    with open(path, 'r') as file:
        content = file.read()
        return content
