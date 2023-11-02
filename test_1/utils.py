DIVIDERS = ("(", "[", "*")


def clean_string(string: str) -> str:
    # removing useless symbols
    new_string = string.strip()
    for divider in DIVIDERS:
        if divider in new_string:
            new_string = new_string.split(divider)[0]

    # replacing symbols
    new_string = new_string.casefold()
    new_string = new_string.replace("-", "_")
    new_string = new_string.replace(",", "")
    new_string = new_string.replace(".", "")
    return new_string


def clean_strings(strings: list[str]) -> list[str]:
    """
    Removes case
    Leaving everything before "(", "[", "*"
    Replaces "-" to "_", "," and "." to "",
    :param strings:
    :return:
    """

    result = []
    for string in strings:
        # removing useless symbols
        new_string = clean_string(string)
        result.append(new_string)
    return result
