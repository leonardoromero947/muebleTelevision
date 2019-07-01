#DOCUMENTO INICIAL DE FUNCIONAMIENTO
import ejecutor as EJT
#import time
import raspardino_response as RDNR
import armado_mueble as A
#import switchs as SW
#import raspardino_response as R

class Main(object):
    switch = EJT.Ejecutor()

    def prueba(self):
        a = A.Armado_mueble()
        arduino = RDNR.Raspardino()
        print("Opciones")
        print("c = puerta proceso cerrar")
        print("a = puerta proceso abrir")
        print("s = seguro de puerta cerrar")
        print("x = seguro de puerta abrir")
        continuar = raw_input("Seleccion deseada?")
        if continuar in ('c', 'C'):
            a.puerta1_cerrar()
        else:
            if continuar in ('a', 'A'):
                a.puerta1_abrir()
            else:
                if continuar in ('s', 'S'):
                    print (arduino.espruino_cmd('w').strip())
                else:
                    if continuar in ('x', 'X'):
                        print (arduino.espruino_cmd('y').strip())
m = Main()
#m.prueba()
m.switch.iniciar()
#sts = SW.Switch()

#while True:
 #   arduino = R.Raspardino()
  #  comando =raw_input("teclee un comando")
   # arduino.llamada(comando)
#    print(sts.status_2A())
#    print(sts.status_2D())
#    time.sleep(2)
#a = A.Armado_mueble()
#a.puerta1_cerrar()

#arduino = RDNR.Raspardino()
#time.sleep(5)
#print (arduino.espruino_cmd('x').strip())
#sprint (arduino.espruino_cmd('x').strip())
#time.sleep(5)
#print (arduino.espruino_cmd('y').strip())
#print (arduino.espruino_cmd('z').strip())

#while True:
    #time.sleep(5)
    #switch = SW.Switch()
    #print(switch.status_2A())
    #print("ESTATUS")
    #print ("2A"+str(arduino.traductor(arduino.espruino_cmd('a').strip())))
    #print ("2D"+str(arduino.traductor(arduino.espruino_cmd('d').strip())))
    #print ("2H"+str(arduino.traductor(arduino.espruino_cmd('h').strip())))
    #print ("2E"+str(arduino.traductor(arduino.espruino_cmd('e').strip())))
    #continuar = raw_input("Ejecutar programa? S/N")
    #print(arduino.get_status_2A())
    #print(arduino.get_status_2D())

    #print (arduino.get_status_2H())