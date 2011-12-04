# Create your views here.
import urllib
from xml.dom import minidom
from django.http import HttpResponse
import os.path
import xml.etree.cElementTree as ET
from mmap import mmap,ACCESS_READ
from xlrd import open_workbook
import csv

def obtenerTodosHDI(self,idioma):
    XML_URL = 'http://www.fao.org/countryprofiles/geoinfo/ws/countryStatistics/HDI/'
    
    paises = leerXML(self)
   
    respuesta="<Datos>"    
    
    for pais in paises:
        url = XML_URL + pais[0] + "/" + idioma
        tree = ET.parse(urllib.urlopen(url))
        for tag in tree.getiterator("HDI"):
            valor=tag.findtext("Total")
            if valor==None:
                valor="N/A"
                            
            respuesta=respuesta+"<Pais name="+"'"+pais[1]+"'"+" value="+"'"+valor+"'"+"><HDI>"+valor+"</HDI></Pais>"
    
    respuesta =respuesta+ "</Datos>"
    
    return HttpResponse(respuesta, mimetype = 'application/xml')


def obtenerTodosGDP(self,idioma):
    XML_URL = 'http://www.fao.org/countryprofiles/geoinfo/ws/countryStatistics/GDP/'
    
    paises = leerXML(self)
   
    respuesta="<Datos>"    
    
    for pais in paises:
        url = XML_URL + pais[0] + "/" + idioma
        tree = ET.parse(urllib.urlopen(url))
        for tag in tree.getiterator("GDP"):
            
            valor1=tag.findtext("GDPTotalInCurrentPrices")
            if valor1==None:
                valor1="N/A"
            
            valor2=tag.findtext("GDPUnit")
            if valor2==None:
                valor2="N/A"
                
            valor3=tag.findtext("GDPYear")
            if valor3==None:
                valor3="N/A"
                            
            respuesta=respuesta+"<Pais name="+"'"+pais[1]+"'"+" value="+"'"+valor1+"'"+"><GDP>"+valor1+"</GDP><Unidad>"+valor2+"</Unidad><Anyo>"+valor3+"</Anyo></Pais>" 
    
    respuesta =respuesta+ "</Datos>"
    
    print respuesta
    
    return HttpResponse(respuesta, mimetype = 'application/xml')



def leerXML(self):
    dom = minidom.parse(os.path.join(os.path.dirname(__file__),"tablapaises.xml"))
    respuesta=[]
    
    for node in dom.getElementsByTagName('li'):
        pais=[]
        pais.append(node.getAttribute('id'))
        pais.append(node.getAttribute('name'))
        pais.append(node.getAttribute('value'))
        respuesta.append(pais)
    return respuesta


def leerCSV(self):
    
    respuesta="<Datos>" 
    
    spamReader = csv.reader(open(os.path.join(os.path.dirname(__file__),'Indice_de_percepcion_de_corrupcion_-_Paises_mas_corruptos.csv'), 'rU'))
    contador = 1
    for row in spamReader:
        if contador>3 and contador % 2 ==1:        
            linea=row[0]            
            string = linea[1:-1].split(',')
            respuesta=respuesta+"<Pais name="+ string[1]+ " value=" + string[2]+ " ranking=" + '"' +string[0]+'"'+"><INDICE>" +string[2]+"</INDICE><Ranking>"+'"'+string[0]+'"'+"</Ranking></Pais>"
        contador = contador+1   
    respuesta =respuesta+ "</Datos>"
    print respuesta
    
    return HttpResponse(respuesta, mimetype='application/xml')