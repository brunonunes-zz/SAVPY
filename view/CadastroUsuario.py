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
    import os.path
except:
    print ' Erro Ao Carregar um dos Import37'
    sys.exit(1)

class CadastroUsuario(object):
    def __init__(self):
        self.host= "localhost"
        self.user= "root"
        self.passwd= "carros"
        self.database = "agenciaBeta1"
        #Setando a variavel com o arquivo glade
        self.arquivoglade = "Projects\cadastro_usuario\cadastro_usuario.glade"
        #Extraindo conteudo XML do arquivo
        self.xml = gtk.glade.XML(self.arquivoglade)        
        #Componentes da Janela CadastrarSenha
        self.cadastro_usuario=self.xml.get_widget('cadastro_usuario')
        self.buttonOk=self.xml.get_widget('buttonOk')
        self.buttonFechar=self.xml.get_widget('buttonFechar')
        self.entryNome=self.xml.get_widget('entryNome')
        self.entrySenha=self.xml.get_widget('entrySenha')
        #esconde o que foi  digitado
        self.entrySenha.set_visibility(False)
        self.entryConfirmar=self.xml.get_widget('entryConfirmar')
        #esconde o que foi  digitado
        self.entryConfirmar.set_visibility(False)       
        
        #=========================================================
        # Comboxbox
        self.comboboxEscolha2 = self.xml.get_widget('comboboxEscolha2')
        # Preparar a Caixa Comboxbox para selecao
        # Componente ListStore para armazenar as retas
        store = gtk.ListStore(str)
        store.append(["Escolha Opcao"])
        store.append(["Gerente"])
        store.append(["Vendedor"])
        # Celula texto para nossa Caixa de Selecao
        celula = gtk.CellRendererText()
        # Associa o ListStore a Caixa de Selecao
        self.comboboxEscolha2.set_model(store)
        # Associa a celula a caixa de selecao
        self.comboboxEscolha2.pack_start(celula, True)
        self.comboboxEscolha2.add_attribute(celula, 'text', 0)
        # Coloca o foco no primeiro item do combobox
        self.comboboxEscolha2.set_active(0)
        #============================================================================
       # Autoconnect Signals and Callbacks
        self.xml.signal_autoconnect(self)
        #self.buttonOk.connect('clicked',self.on_buttonOk_clicked)
        #self.buttonFechar.connect('clicked',self.on_buttonFechar_clicked)
        self.cadastro_usuario.show_all()     
        self.criartabela()
        gtk.main()
       
    def criartabela(self):
        
         if  not os.path.exists('agenciaBeta1.db'):
                  
                    conexao = MySQLdb.connect(host="localhost", user="root",passwd="carros", db="agenciaBeta1")
                    cursor = conexao.cursor()
                    
                    sql = """create table cs(
                            codigo int(10) PRIMARY KEY AUTO_INCREMENT NOT NULL UNIQUE ,
                            nome  varchar(20) not null,
                            senha varchar(8) not null,
                            confirmar varchar(8) not null)"""
                    
                    sql1="""create table gere(
                            codigogerente int(10) PRIMARY KEY AUTO_INCREMENT NOT NULL UNIQUE,
                            nome  varchar(20) not null,
                            senha varchar(8) not null,
                            confirmar varchar(8) not null)"""
                    try:
                     
                            print ' testando 1'      

                            cursor.execute(sql)
                            cursor.execute(sql1)
                            conexao.commit()
                            print 'testando i'
                            
                    except MySQLdb.Error, e:
                    
                       if e.args[0] == 1050:                     
                         print  'Tratando o erro'
       
    def on_buttonOk_clicked (self,widget):
        print'buttonSalvar'
        combo2 = self.comboboxEscolha2.get_active_text()
        if combo2 =="Vendedor":
            
            if (self.entryNome.props.text == "" or self.entrySenha.props.text  == "" or self.entryConfirmar.props.text  == "" ):
            
                msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Por favor preencha todos os campos')
                resposta=msg.run()
                msg.destroy()
                
            else:
                
                nome = self.entryNome.props.text
                senha= self.entrySenha.props.text
                confirmar=self.entryConfirmar.props.text
                
                " Limpando os campos "
                self.entryNome.props.text=""
                self.entrySenha.props.text = ""
                self.entryConfirmar.props.text = ""
                if (senha==confirmar):
                 #gravando dados no Banco
                    sql = "insert into cs(nome, senha, confirmar) values('" + nome + "','" + senha + "', '" + confirmar  + "')"
                    self.conexao=MySQLdb.connect(self.host,self.user,self.passwd,self.database)
                    self.cursor = self.conexao.cursor()
                    self.cursor.execute(sql)
                    self.conexao.commit()#Para enviar tudo para o Banco
                    
                    msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Cadastrado Com Sucesso')
                    msg.run()
                    msg.destroy()
                else:
                    msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Erro na Confirmacao de Senha:') 
                    msg.run()
                    msg.destroy()
                            
        if combo2 =="Gerente":
            
            if ( self.entryNome.props.text == "" or self.entrySenha.props.text  == "" or self.entryConfirmar.props.text  == "" ):
            
                msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Por favor preencha todos os campos')
                resposta=msg.run()
                msg.destroy()
                
            else:
                
                
                nome = self.entryNome.props.text
                senha= self.entrySenha.props.text
                confirmar=self.entryConfirmar.props.text
                
                " Limpando os campos "
                self.entryNome.props.text=""
                self.entrySenha.props.text = ""
                self.entryConfirmar.props.text = ""
                if (senha==confirmar):
                 #gravando dados no Banco
                    sql = "insert into gere(nome, senha, confirmar) values('" + nome + "','" + senha + "', '" + confirmar  + "')"
                    self.conexao=MySQLdb.connect(self.host,self.user,self.passwd,self.database)
                    self.cursor = self.conexao.cursor()
                    self.cursor.execute(sql)
                    self.conexao.commit()#Para enviar tudo para o Banco
                    
                    msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Cadastrado Com Sucesso')
                    msg.run()
                    msg.destroy()
                else:
                    msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Erro na Confirmacao de Senha:') 
                    msg.run()
                    msg.destroy()        
                    
        #gtk.main()
      
    def on_buttonFechar_clicked (self,widget):
        print'buttonFechar'
        self.cadastro_usuario.hide()
        gtk.main_quit()
        
    def on_cadastro_usuario_destroy(self,widget):
        print 'k'
        gtk.main_quit()

if __name__ == '__main__':

    cs = CadastroUsuario()
