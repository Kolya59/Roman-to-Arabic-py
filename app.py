import re

# Pattern for Roman numbers (between 1 and 3999)
roman_pattern = r"\bM{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})\b"
# Numeric value of a Roman numeral
trans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


# Convert roman substring to arabic one
# TODO Remove it
# Why matched type is str instead re.Match? Fuck you, that's why
def roman_to_arabic(matched: re.Match) -> str:
    # Some magic which converts re.Match to string
    roman = matched.group()
    # Some magic which saves you from exception
    if roman == '':
        return ''
    # Convert roman numbers to the number frequency
    # for example: "MMM" -> [1000,1000,1000]
    values = [trans[r] for r in roman]
    # Some magic which convert numbers frequencies to one number
    # https://codereview.stackexchange.com/a/141413
    return '{0}'.format(sum(
        val if val >= next_val else -val
        for val, next_val in zip(values[:-1], values[1:])
    ) + values[-1])


if __name__ == '__main__':
    # Read string from keyboard
    print('Enter the text with roman numbers and wait for a miracle')
    s = input()
    # Replace each matched roman substring to arabic one
    res = re.sub(roman_pattern, roman_to_arabic, s)
    # Print result
    print("Original: {0}\n\nReplaced: {1}".format(s, res))
