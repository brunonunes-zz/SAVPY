'''
Created on 06/08/2009

@author: Administrador
'''
import sys
try:
    import pygtk
    import gtk
    pygtk.require('2.0')
    import gtk
    import gtk.glade
    sys.path.append("C:\\Documents and Settings\\Administrador\\workspace\\agencia\\src\\view")
    from CadastrarVeiculo import *
    
except :
    
    print ' Erro Ao Carregar um dos Import 3'
    sys.exit(1)
    
class ControllerCadastrarVeiculo(object):
    '''
    classdocs
    '''    
         
    def __init__(self):
        '''
        Constructor
        '''
        print 'gugu'
         
       # print'buttonSalvar'
        #gtk.main()
        
  
    
    