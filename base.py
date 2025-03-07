class Gramata:
    def __init__(self, nosaukums, lapaspuse ):
        self.nosaukums = nosaukums
        self.lapaspuse = lapaspuse
    def paradi_info(self):
      print("Gramatas nosaukums: " + self.nosaukums) 
      print("Gramatas lapaspuse: " + str(self.lapaspuse))

g1 = Gramata ("Sākums", 51)
g2 = Gramata("Asas", 53)
g1.paradi_info()
g2.paradi_info()