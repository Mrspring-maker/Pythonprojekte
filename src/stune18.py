class MyClass:
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


klasse = MyClass
zeile =  klasse.nummer_linien
wörter = klasse.nummer_wörter
zeichen = klasse.nummer_zeichen



print("Zeilen:",zeile, "Wörter:", wörter, "Zeichen:",zeichen)

