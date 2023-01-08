import re

def regex_plz_ort(wort):
    pattern = re.compile(r"[0-9]{5}[A-Za-z s]*|[1-9]{1}[0-9]{3}[A-Za-z s]*")
    match = pattern.match(wort)
    if match:
        return str(match.group()) +  ": Ausdruck ist korrekt"
    return str(wort) + ": Ausdruck ist nicht korrekt"
    
print(regex_plz_ort("0123 Entenhausen"))
print(regex_plz_ort("A123 Mittelerde"))

print(regex_plz_ort("6020 Innsbruck"))
print (regex_plz_ort("1020 Wien"))
print(regex_plz_ort("8060 Bad Gastein"))
print(regex_plz_ort("08080 Fugging"))

def regex_telefonn(wort):
    pattern = re.compile(r"[+]{1}[^(0)]{1}[0-9]{0,2}[-][^(0)][0-9]{2,5}[-][^(0)][0-9]{5,9}")
    match = pattern.match(wort)
    if match:
        return str(match.group()) + ": Ausdruck ist korrekt"
    return str(wort) + ": Ausdruck ist nicht korrekt"

print(regex_telefonn("+43-5372-71819314"))
print(regex_telefonn("+1-234-56789012"))

print(regex_telefonn("+43 5372 71819314"))
print(regex_telefonn("+01-012-0123456"))
