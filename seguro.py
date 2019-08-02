import time
import switchs as SW
import memoria as MEM
class Seguro_acciones(object):

    switch = SW.Switch()
    memoria = MEM.Extra()

    def activar_seguro(self):
        inicio_tiempo = time.time()
        while True:
            if(self.switch.status_seguro_fisico()):
                tiempo_final = time.time()
                segundo = round(tiempo_final - inicio_tiempo,2)
                print(segundo)
                if (segundo >= 5):
                    print("ACCION SEGUROS")
                    self.memoria.seguro()
                    break
            else:
                break
