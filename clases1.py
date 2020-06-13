class Coche:
    tanque = True
    motorencendido = False

    def arranca(self, *args):
        if sum(args) > 20:
            self.motorencendido = True

    def status(self):
        if (self.motorencendido):
            return "arrancado"
        else:
            return "no arranca"
Skyline = Coche()
Skyline.arranca(23, 0)
print(Skyline.status())
