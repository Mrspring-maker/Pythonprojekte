source = ('myfile.txt')
destination = ('/Users/lennardfruhling/test.text')


class Stunde18_2:
  file = open("myfile.txt","r")

  nummer_linien = 0
  nummer_wörter = 0
  nummer_zeichen = 0

  def __init__(self,file,nummer_linien,nummer_wörter,nummer_zeichen):
    for line in file:
      line = line.strip("\n")
      words = line.split()
      nummer_linien += 1
      nummer_wörter += len(words)
      nummer_zeichen += len(line)

  file.close()
Aufgabe2 = Stunde18_2
zeile =  Aufgabe2.nummer_linien
wörter = Aufgabe2.nummer_wörter
zeichen = Aufgabe2.nummer_zeichen
print("Zeilen:",zeile, "Wörter:", wörter, "Zeichen:",zeichen)

class Sunde18_3:
    def copy(s,d):
        f1 = open(s,'r')
        f2 = open(d,'w')
        data = f1.read()
        f2.write(data)
        f1.close()
        f2.close()

source = ('myfile.txt')
destination = ('/Users/lennardfruhling/test.text')

Aufgabe3 = Sunde18_3
Aufgabe3.copy(source,destination)

















