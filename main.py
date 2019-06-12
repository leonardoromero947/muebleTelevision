#DOCUMENTO INICIAL DE FUNCIONAMIENTO
import ejecutor as EJT
import time
import raspardino_response as RDNR
import switchs as SW

class Main(object):
    switch = EJT.Ejecutor()

m = Main()
m.switch.iniciar()

#arduino = RDNR.Raspardino()
#time.sleep(5)
#print (arduino.espruino_cmd('w').strip())
#print (arduino.espruino_cmd('x').strip())
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