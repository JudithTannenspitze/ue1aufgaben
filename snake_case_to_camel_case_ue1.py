def snake_case_to_camel_case(word):
    zusammengesetzter_string = ""
    splitWord = word.split("_")
    for value in splitWord:
        zusammengesetzter_string = zusammengesetzter_string + value.capitalize()
    first_capital_letter = zusammengesetzter_string[1:len(zusammengesetzter_string)]
    first_letter = zusammengesetzter_string[0].lower()
    zusammengesetzt = first_letter + first_capital_letter
    return zusammengesetzt

print(snake_case_to_camel_case("this_is_snake_case"))
print(snake_case_to_camel_case("name"))
print(snake_case_to_camel_case("hallo_welt"))
