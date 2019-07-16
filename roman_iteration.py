# List of supported numerals

DIGITS = [

        ('M', 1000, 900),

        ('D', 500, 400),

        ('C', 100, 90),

        ('L', 50, 40),

        ('X', 10, 9),

        ('V', 5, 4),

        ('I', 1, 1),

    ]


# Reverse mapping from value to numeral.

TO_DIGIT = {value: character for character, value, _ in DIGITS}


def checkio(number):

    """Return number (an integer in [1, 3999]) as Roman numerals."""

    result = ''

    # Work from largest to smallest

    for digit, value, limit in DIGITS:

        while number >= limit:

            # Handle the special case of subtracting smaller numerals.

            if number < value:

                delta = value - limit

                result += TO_DIGIT[delta]

                number += delta

            result += digit

            number -= value

    return result

    

if __name__ == '__main__':

    assert checkio(6) == 'VI', 'First'

    assert checkio(76) == 'LXXVI', 'Second'

    assert checkio(499) == 'CDXCIX', 'Third'

    assert checkio(3888) == 'MMMDCCCLXXXVIII', 'Fourth'

    print('All ok')