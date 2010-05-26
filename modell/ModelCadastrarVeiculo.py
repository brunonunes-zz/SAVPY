'''
Created on 06/08/2009

@author: Administrador
'''
import sys
try:

    import pygtk
    pygtk.require('2.0')
    import gtk
    import gtk.glade
    #sys.path.append("C:\\Documents and Settings\\Administrador\\workspace\\agencia\\src\\view")
    #from ControllerCadastrarVeiculo import *
except:
    print ' Erro Ao Carregar um dos Import2'
    sys.exit(1)
    
class ModelCadastrarVeiculo(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        print'eu'
    
        gtk.main()
   
    
    
    
#ccz=ControllerCadastrarVeiculo()
