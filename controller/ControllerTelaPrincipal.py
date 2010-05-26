# -*- coding: utf-8 -*-
'''
Created on 28/07/2009

@author: Administrador
'''
import sys
try:
    import pygtk
    import gtk
    pygtk.require('2.0')
    import gtk
    import gtk.glade
    #o c diz que o controller faz liacao com o view e o model
    sys.path.append("C:\\Documents and Settings\\Administrador\\workspace\\agencia\\src\\view")
    #from TelaPrincipal import *
    from PermissaoUsuario import *
    #from CadastrarCliente import *
except :#MySQLdb.Error, e:
    
    print ' Erro Ao Cargregar um dos Import'
    sys.exit(1)
class ControllerTelaPrincipal(object):
    
    '''
    Agora atraves dos arquivos que fazem parte da camada Controller,
    voce faz as chamadas as funcionalidades da camada Model da sua aplicacao.
    Vale lembrar que o codigo da camada Model deve ser inteiramente independente
    das camadas View e Cveontroller. Assim voce tera os controladores das janelas 
    acessando as funcionalidades dos controladores da aplicacao e esses acessando
    o modelo da aplicacao.
    '''

   
    
    def __init__(self):
        '''
        Constructor
        '''
        #instanciei a class Tela principal para pegar todas as funcionalidades que estao dentro dela
    print'gugu'
    p=PermissaoUsuario()
    
    
     
        