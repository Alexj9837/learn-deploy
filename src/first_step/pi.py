from importlib.resources import files


def _load_pi_digits() -> str:
    raw = files("first_step").joinpath("pi_to_100000").read_text()
    # Remove "3.", spaces, and newlines — keep only the digit characters
    return raw.replace(".", "", 1).replace(" ", "").replace("\n", "")


_PI_DIGITS: str = _load_pi_digits()


def find__first_in_pi(n: int, start: int | None = None) -> int | None:
    position = _PI_DIGITS.find(str(n), start or 0)
    return position if position != -1 else None


def find_all_pos_in_pi(n: int) -> list[int]:
    positions: list[int] = []
    pattern = str(n)
    start = 0
    while True:
        pos = _PI_DIGITS.find(pattern, start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + 1
    return positions
