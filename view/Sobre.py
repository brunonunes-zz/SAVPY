# -*- coding: utf-8 -*-
'''
Created on 19/08/2009

@author: Administrador
'''
import sys
try:
    
    import pygtk
    pygtk.require('2.0')
    import gtk
    import gtk.glade
    

except:
    print ' Erro Ao Carregar um dos Import9'
    sys.exit(1)

class Sobre(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
       #O arquivo glade
        self.arquivoglade="Projects\sobre\sobre.glade"
        #Rereentacao do arquivo xml
        self.xml = gtk.glade.XML(self.arquivoglade)
       #Componentes da Janela TelaPrincipal
        self.sobre = self.xml.get_widget('sobre')
        #self.telaprincipal.set_title('Testando Titulo')
        #botao sair#
        self.buttonFechar=self.xml.get_widget('buttonFechar')
        self.fixed1=self.xml.get_widget('fixed1')
        self.image1=self.xml.get_widget('image1')
        self.image1.set_from_file('python.jpg')
        #icone
        self.statusIcon = gtk.StatusIcon()
        self.statusIcon.set_from_file( "Civic.jpg")
        self.statusIcon.set_visible(True)
        
        
    
         # Autoconnect Signals and Callbacks
        self.xml.signal_autoconnect(self)
        #self.buttonFechar.connect('clicked',self.on_buttonFechar_clicked)

        self.sobre.show_all()  
        gtk.main() 
        
    def on_buttonFechar_clicked (self,widget):
        print'buttonFechar'  
        self.sobre.hide()
        gtk.main_quit()
    def on_sobre_destroy (self,widget):
        gtk.main_quit()
   
   
if __name__ == '__main__':

    s = Sobre()


