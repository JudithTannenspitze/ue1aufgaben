def check_palindrom(word):
    umgedrehter_string = word[::-1]
    if (word.lower() == umgedrehter_string.lower()):
        return str(word) + ": " + str(True)
    return str(word) + ": " + str(False)


print( check_palindrom("Otto"))
print(check_palindrom("Anna"))
print(check_palindrom("Reliefpfeiler"))
print(check_palindrom("Racecar"))

print(check_palindrom("Palindrom"))
print(check_palindrom("Haus"))
print(check_palindrom("Auto"))