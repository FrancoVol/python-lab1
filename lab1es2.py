print("Insert the string:")
string = input()
if len(string) < 2:
    print("La stringa inserita non è valida. Il risultato è:   ")
else:
    print("Il risultato è: " + string[0] + string[1] + string[len(string)-2] + string[len(string)-1])