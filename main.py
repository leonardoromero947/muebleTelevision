#DOCUMENTO INICIAL DE FUNCIONAMIENTO
import ejecutor as EJT
import time
import seguro as SEG

class Main(object):
    switch = EJT.Ejecutor()
    seguros = SEG.Seguro_acciones()

m = Main()
m.switch.iniciar()

