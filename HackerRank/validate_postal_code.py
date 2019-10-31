import re
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

regex_integer_in_range = r"^[1-9]\d{5}$"  # Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"  # Do not delete 'r'.


def is_valid_code(s):
    return (bool(re.match(regex_integer_in_range, s))
            and len(re.findall(regex_alternating_repetitive_digit_pair, s)) < 2)


def main():
    s = ['100000', '999999', '123456', '987654', '012345', '1234567', '101234', '101232', '110000']
    for i in s:
        logger.info("{}, {}".format(i, is_valid_code(i)))


if __name__ == '__main__':
    main()
