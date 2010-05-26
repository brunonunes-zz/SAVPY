# -*- coding: utf-8 -*-
'''
Created
'''
'''
Created on 23/07/2009

@author: Gustavo,Bruno,Eduardo
'''

import sys
try:
    
    import pygtk
    pygtk.require('2.0')
    import gtk
    import gtk.glade
    import MySQLdb 
    from TelaPrincipalGerente import *
    from TelaPrincipalVendedor import *
    from Sobre import *
except:
    print ' Erro Ao Carregar um dos Import18'
    sys.exit(1)

class LoggofUsuario(object):
    def __init__(self):
        self.host= "localhost"
        self.user= "root"
        self.passwd= "carros"
        self.database = "agenciaBeta1"
        #self.tg=TelaPrincipalGerente()
        #Setando a variavel com o arquivo glade
        self.arquivoglade = "Projects\loggof_usuario\loggof_usuario.glade"
        print 'plo'
        #Extraindo conteudo XML do arquivo
        self.xml = gtk.glade.XML(self.arquivoglade)    
        print 'gugu'    
       #Componentes da Janela PermissaoUsuario
        self.loggof_usuario=self.xml.get_widget('loggof_usuario')
        self.buttonOk= self.xml.get_widget('buttonOk')
        self.buttonCancelar=self.xml.get_widget('buttonCancelar')
        self.entryNome=self.xml.get_widget('entryNome')
        self.entrySenha=self.xml.get_widget('entrySenha')
        self.entry1=self.xml.get_widget('entry1')
        #self.buttonOk.connect('clicked',self.on_buttonOk_clicked)
        #self.buttonCancelar.connect('clicked',self.on_buttonCancelar_clicked)
               
        self.entrySenha.set_visibility(False)              
             # Comboxbox
        self.combobox1 = self.xml.get_widget('combobox1')
        
        # Preparar a Caixa Comboxbox para selecao
        # Componente ListStore para armazenar as retas
        store = gtk.ListStore(str)
        store.append(["Escolha Opcao"])
        store.append(["Gerente"])
        store.append(["Vendedor"])
        # Celula texto para nossa Caixa de Selecao
        print 'teste'
        celula = gtk.CellRendererText()
        # Associa o ListStore a Caixa de Selecao
        self.combobox1.set_model(store)
        # Associa a celula a caixa de selecao
        self.combobox1.pack_start(celula, True)
        self.combobox1.add_attribute(celula, 'text', 0)
        # Coloca o foco no -Selecionar-
        self.combobox1.set_active(0)
        print 'teste2'
                
      
        #============================================================================
       # Autoconnect Signals and Callbacks
        self.xml.signal_autoconnect(self)
        
        
        self.loggof_usuario.show_all()  
        gtk.main() 
    
    def on_buttonOk_clicked (self,widget):
        print'buttonOk1'
        
        #digita o nome e senha 
        n= self.entryNome.props.text
        s= self.entrySenha.props.text


        #faz a ligacao com o banco
        self.conexao=MySQLdb.connect(self.host,self.user,self.passwd,self.database)
        cursor = self.conexao.cursor()
        # se o nome e a senha digitado for igual ao que esta 
        #cadastrado no banco de dados entra no sistema.
        combo = self.combobox1.get_active_text()
        
        if combo=="Escolha Opcao":
            msg = gtk.MessageDialog(None,0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Escolha Vendedor ou Gerente Para Acessar Sistema.')
            msg.run()
            msg.destroy()
            
        if combo =="Gerente":
            
            if cursor.execute("select * from gere where nome='%s' and senha='%s'" %(n,s)):
                cursor.fetchall()
                self.loggof_usuario.destroy()
                t= TelaPrincipalGerente() 
                print 'gege'

                
            else:
                self.entrySenha.props.text = ""
                msg = gtk.MessageDialog(None,0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Nome ou Senha Incorreto.')
                msg.run()
                msg.destroy()
        print 'testando' 

        print 'i'     
        if combo =="Vendedor":
            
            if cursor.execute("select * from cs where nome='%s' and senha='%s'" %(n,s)):
                cursor.fetchall()
                self.loggof_usuario.destroy()
                print 'veve'
                tt=TelaPrincipalVendedor()

            else:
                self.entrySenha.props.text = ""
                msg = gtk.MessageDialog(None,0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Nome ou Senha Incorreto.')
                msg.run()
                msg.destroy()
        
        #gtk.main()   
    def on_buttonCancelar_clicked (self,widget):
        print'buttonFechar1'
        self.loggof_usuario.hide()
        gtk.main_quit()
        
    def on_loggof_usuario_clicked (self,widget):
        print 'testeando'
        gtk.main()
    def on_loggof_usuario_destroy (self,widget):
        gtk.main_quit()

       
if __name__ == '__main__':

    t = LoggofUsuario()
    
    