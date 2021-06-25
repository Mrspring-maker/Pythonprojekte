from input import Input

# Abspeicherung der Variablen

inputs = Input()
x = inputs.Zahl1
y = inputs.Zahl2
abfrage = inputs.Zeichen

print(x, abfrage, y)
print("=")

def abfrage_benutzer(x, y):
    if abfrage == ("+"):
       return(x+y)
    elif abfrage == ("-"):
        return(x-y)
    elif abfrage == ("*"):
       return(x*y)
    elif abfrage == (":"):
        return (x/y)
    else:
        quit()



ergebniss = abfrage_benutzer(x,y)


print(ergebniss)
