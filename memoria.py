import xml.etree.ElementTree as ET
import ast

class Extra(object):

    instructivo = False
    ejemplo = False
    log = False
    visor = False
    cerrado = False
    pruebas = False
    proceso = 0

    def leer_documento(self):
        documento = open('propiedades.txt')
        propiedades = documento.readlines()
        documento.close()
        print(type(propiedades[0]))
        print(len(propiedades))
        print(propiedades[0])

    def sobreescribir_documento(self):
        pass

    def leer_xml(self):
        tree = ET.parse('propiedades.xml')
        root = tree.getroot()
        for child in root.findall('propiedades'):
            self.instructivo = child.find('instructivo').text
            self.ejemplo = ast.literal_eval(child.find('ejemplo').text)
            self.log = ast.literal_eval(child.find('log').text)
            self.proceso = int(child.find('proceso').text)
            self.cerrado = ast.literal_eval(child.find('cerrado').text)
            self.pruebas = ast.literal_eval(child.find('pruebas').text)

    def leer_proceso_xml(self):
        tree = ET.parse('propiedades.xml')
        root = tree.getroot()
        for child in root.findall('propiedades'):
            self.proceso = child.find('proceso').text
            self.cerrado = bool(child.find('cerrado').text)

    def verificar_variables(self):
        print (":::instructivo:::")
        print (self.instructivo)
        print (":::ejemplo:::")
        print (self.ejemplo)
        print (":::log:::")
        print (self.log)
        print (":::cerrado:::")
        print (self.cerrado)
        print (":::pruebas:::")
        print (self.pruebas)
        print (":::proceso:::")
        print (self.proceso)

    def insertar_proceso_xml(self,numero_proceso):
        tree = ET.parse('propiedades.xml')
        root = tree.getroot()
        for proceso in root.iter('proceso'):
            new_proceso = int(numero_proceso)
            proceso.text = str(new_proceso)
            proceso.set('update','yes')
        tree.write('propiedades.xml')

