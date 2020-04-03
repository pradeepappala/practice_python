def set_bit(n):
    res = n
    res |= res >> 1
    res |= res >> 2
    res |= res >> 4
    res |= res >> 8
    res |= res >> 16
    return (res + 1) >> 1


# Complete the counterGame function below.
def counter_game_util(n):
    if n == 1:
        return 0
    if not (n & (n - 1)):
        return counter_game_util(n >> 1) + 1
    else:
        return counter_game_util(n - set_bit(n)) + 1


def counter_game(n):
    res = counter_game_util(n)
    return 'Louise' if res % 2 else 'Richard'


if __name__ == '__main__':

    result = counter_game(6)

    print(result + '\n')
