# -*- coding: utf-8 -*-
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

except:
    print ' Erro Ao Carregar um dos Import1'
    sys.exit(1)
    
#CLASSE RESPONSÁVEL PELA AUTENTICAÇÃO DA SENHA E NOME DO VENDEDOR E GERENTE.

class PermissaoUsuario(object):
    def __init__(self):
        self.host= "localhost"
        self.user= "root"
        self.passwd= "carros"
        self.database = "agenciaBeta1"
        #Setando a variavel com o arquivo glade
        self.arquivoglade = "Projects\permissao_usuario\permissao_usuario.glade"
        print 'plo'
        #Extraindo conteudo XML do arquivo
        self.xml = gtk.glade.XML(self.arquivoglade)    
        print 'gugu'    
       #Componentes da Janela PermissaoUsuario
        self.permissao_usuario=self.xml.get_widget('permissao_usuario')
        self.buttonOk= self.xml.get_widget('buttonOk')
        self.buttonCancelar=self.xml.get_widget('buttonCancelar')
        self.entryNome=self.xml.get_widget('entryNome')
        self.entrySenha=self.xml.get_widget('entrySenha')
        
        #torna o caracter da caixa senha invisivel para o cliente
        self.entrySenha.set_visibility(False)              
        #referente ao link do botao ao metodo 
        #self.buttonOk.connect('clicked',self.on_buttonOk_clicked)
        #self.buttonCancelar.connect('clicked',self.on_buttonCancelar_clicked)
        
        #mostra todos os compoentes que tem na tela       
        self.permissao_usuario.show_all()  
        
        # Comboxbox
        self.cbxSistema = self.xml.get_widget('comboboxEscolha1')
        
        # Preparar a Caixa Comboxbox para selecao
        
        # Componente ListStore para armazenar as retas
        store = gtk.ListStore(str)
        store.append(["Escolha Opcao"])
        store.append(["Gerente"])
        store.append(["Vendedor"])

        # Celula texto para nossa Caixa de Selecao
        celula = gtk.CellRendererText()
        # Associa o ListStore a Caixa de Selecao
        self.cbxSistema.set_model(store)
        # Associa a celula a caixa de selecao
        self.cbxSistema.pack_start(celula, True)
        self.cbxSistema.add_attribute(celula, 'text', 0)
        
        # Coloca o foco no Selecionar
        self.cbxSistema.set_active(0)

        # Autoconnect Signals and Callbacks
        self.xml.signal_autoconnect(self)
        #faz com que a tela fique em loop ate que feche.
        self.criardatabase()
        gtk.main()
        
    #cria a BASE de DADOS (POR SER A PRIMEIRA TELA A APARECER ELA AUTOMATICAMENTE CRIA ESSA BASE DE DADOS)
    def criardatabase(self):
       print           'HHJJ'
       if not os.path.exists('agenciaBeta1.db'):
            try:
                    #verifica se o data base nomeado acima ja foi criado 
                    
                    conexao = MySQLdb.connect(self.host,self.user,self.passwd,self.database )
                    print ' Banco de Dados existente'
                        
                  
            except MySQLdb.Error, e:
                    #caso nao foi criado cria o database e a tabela referete a ele
                    
                if e.args[0] == 1049:

                    conexao = MySQLdb.connect(self.host,self.user,self.passwd)
                    cursor = conexao.cursor()    
                    cursor.execute('create database %s' %self.database)  
                    cursor.close()
                    print 'Banco de Dados criado com sucesso'
                    
                gtk.main()
            
    def on_buttonOk_clicked (self,widget):
        print'buttonOk2'
        #digita o nome e senha 
        n= self.entryNome.props.text
        s= self.entrySenha.props.text
        print n     
        print s
        #faz a ligacao com o banco
        self.conexao=MySQLdb.connect(self.host,self.user,self.passwd,self.database)
        cursor = self.conexao.cursor()
        # se o nome e a senha digitado for igual ao que esta 
        #cadastrado no banco de dados entra no sistema.
        
        #pega o que foi selecionado no combobox
        combo = self.cbxSistema.get_active_text()
        if combo=="Escolha Opcao":
            msg = gtk.MessageDialog(None,0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Escolha Vendedor ou Gerente Para Acessar Sistema.')
            msg.set_position(gtk.WIN_POS_CENTER)
            msg.run()
            msg.destroy()
                
        if combo =="Gerente":
            
            if cursor.execute("select * from gere where nome='%s' and senha='%s'" %(n,s)):
                cursor.fetchall()
                self.permissao_usuario.destroy()
                t=TelaPrincipalGerente()
                print 'g'
            else:
                self.entrySenha.props.text = ""
                msg = gtk.MessageDialog(None,0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Nome ou Senha Incorreto.')
                msg.set_position(gtk.WIN_POS_CENTER)
                msg.run()
                msg.destroy()
       
        if combo =="Vendedor":
            
            if cursor.execute("select * from cs where nome='%s' and senha='%s'" %(n,s)):
                cursor.fetchall()
                self.permissao_usuario.destroy()
                
                t=TelaPrincipalVendedor()

            else:
                self.entrySenha.props.text = ""
                msg = gtk.MessageDialog(None,0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Nome ou Senha Incorreto.')
                msg.set_position(gtk.WIN_POS_CENTER)
                msg.run()
                msg.destroy()
        
        #gtk.main()   
    def on_buttonCancelar_clicked (self,widget):
        print'buttonFechar1'
        self.permissao_usuario.hide()
        gtk.main_quit()
        
    def on_permissao_usuario_destroy (self,widget):
        gtk.main_quit()
       
if __name__ == '__main__':

    p = PermissaoUsuario()
    
    