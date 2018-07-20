def print_first_word(words):
    """Prints the first word after popping it off."""
    kata = sorted(words.split(' '))
    word = kata.pop(0)
    print word

nama = "Reza Azzu"
print_first_word(nama)
