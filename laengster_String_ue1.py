def longster_string(*values):
    laengster_String = 0
    for value in values:
        if (len(str(value))>len(str(laengster_String))):
            laengster_String = value
    return laengster_String

print(longster_string("sometimes","you","eat","the","bear"))
print(longster_string("python","is","superb"))