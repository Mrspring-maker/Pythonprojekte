from input import Input

class ZuweiserRechenmodul:
    def __init__(self):
        i = Input()
        self.eins = i.Zahl1
        self.zwei = i.Zahl2
        self.zeichen = i.Zeichen

    def ausgabe(self):
        print(self.eins,self.zeichen, self.zwei)
        print("=")
    def abfrage_benutzer(self):
        if self.zeichen == ("+"):
            return(self.eins+self.zwei)
        elif self.zeichen == ("-"):
            return(self.eins-self.zwei)
        elif self.zeichen == ("*"):
            return(self.eins*self.zwei)
        elif self.zeichen == (":"):
            return (self.eins/self.zwei)
        else:
            quit()


zr = ZuweiserRechenmodul()
zr.ausgabe()
zr.abfrage_benutzer()
print(zr.abfrage_benutzer())



