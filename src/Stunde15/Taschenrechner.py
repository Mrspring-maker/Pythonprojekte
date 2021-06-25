class taschenrechner:

    def __init__(self,x,y,ersteZahl,zweiteZahl):
        self.x = x
        self.y = y
        self.ersteZahl = ersteZahl
        self.zweiteZahl = zweiteZahl

    def abfragezahlen(self):
        ersteZahl = int(input("Nenne deine 1 Zahl: "))
        zweiteZahl = int(input("Nenne deine 2 Zahl: "))
        return ersteZahl, zweiteZahl


    def abfrage_benutzer(self):
        abfarge = input("Was möchtest du rechen? ")
        if abfarge == ("+"):
            add(x, y)
        elif abfarge == ("-"):
            sub(x, y)
        elif abfarge == ("*"):
            mult(x, y)
        elif abfarge == (":"):
            division(x, y)
        elif abfarge == ("%"):
            modulo(x, y)
        elif abfarge == ("="):
            sum(x, y)
        else:
            myquit




    def add(self):
        print(ersteZahl + zweiteZahl)


    def sub(self):
        print(ersteZahl - zweiteZahl)


    def mult(self):
        print(ersteZahl * zweiteZahl)


    def division(self):
        print(ersteZahl / zweiteZahl)


    def modulo(self):
        print(ersteZahl % zweiteZahl)

    def sum(self):
        # For loop
        erg = 0
        for n in range(self):
            #print(n)
            erg += n
        print(erg)

    def myquit(self):
        quit()


rechner = taschenrechner()
x, y = rechner.abfragezahlen()
rechner.abfrage_benutzer(x, y)



