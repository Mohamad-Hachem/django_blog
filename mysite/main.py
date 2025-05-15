def is_ISBN_10(code: str) -> bool:
    if len(code) != 10:
        return False

    total = 0
    for i in range(9):
        if not code[i].isdigit():
            return False
        total += (i + 1) * int(code[i])

    check = total % 11
    last_char = code[9]

    if check == 10:
        return last_char == 'X'
    return last_char.isdigit() and check == int(last_char)


def is_ISBN_13(code: str) -> bool:
    if len(code) != 13 or not code.isdigit():
        return False

    total = 0
    for i in range(12):
        digit = int(code[i])
        if i % 2 == 0:
            total += digit
        else:
            total += 3 * digit

    check_digit = (10 - (total % 10)) % 10
    return check_digit == int(code[12])


def solve(incoming: str) -> bool:
    cleaned = incoming.replace(' ', '').replace('-', '')
    if len(cleaned) == 10:
        return is_ISBN_10(cleaned)
    elif len(cleaned) == 13:
        return is_ISBN_13(cleaned)
    return False


print(solve('978-1-56619-909-2'))