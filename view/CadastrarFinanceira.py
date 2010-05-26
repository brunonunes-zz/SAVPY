# -*- coding: utf-8 -*-
'''
Created on 19/08/2009

@author: Administrador
'''
import sys
try:

    import pygtk
    pygtk.require('2.0')
    import datetime
    import gtk
    import gtk.glade
    import MySQLdb
    import os.path
    
except:
    print ' Erro Ao Carregar um dos Importkj'
    sys.exit(1)

class CadastrarFinanceira(object):
    def __init__(self):           

        self.host= "localhost"
        self.user= "root"
        self.passwd= "carros"
        self.database = "agenciaBeta1"
        
      
        
        #Setando a variavel com o arquivo glade
        self.arquivoglade = "Projects\cadastrar_financeira\cadastrar_financeira.glade"
        #Extraindo conteudo XML do arquivo
        self.xml = gtk.glade.XML(self.arquivoglade)        
        #Componentes da Janela CadastrarSenha
        self.cadastrar_financeira=self.xml.get_widget('cadastrar_financeira')
        self.buttonSalvar=self.xml.get_widget('buttonSalvar')
        self.buttonFechar=self.xml.get_widget('buttonFechar')
        self.entryCodigo=self.xml.get_widget('entryCodigo')
        self.entryNome=self.xml.get_widget('entryNome')
        self.entryLocal=self.xml.get_widget('entryLocal')
        self.entryCidade=self.xml.get_widget('entryCidade')
        self.entryCep=self.xml.get_widget('entryCep')
        self.entryCnpj=self.xml.get_widget('entryCnpj')
        self.entryTelefone1=self.xml.get_widget('entryTelefone1')
        self.entryTelefone2=self.xml.get_widget('entryTelefone2')
        self.entryCelular=self.xml.get_widget('entryCelular')
        self.entryEmail=self.xml.get_widget('entryEmail')
        
        # Autoconnect Signals and Callbacks
        self.xml.signal_autoconnect(self)
        
        #self.buttonSalvar.connect('clicked',self.on_buttonSalvar_clicked)

        #self.buttonFechar.connect('clicked',self.on_buttonFechar_clicked)
        #aparecer todos os omponentes dessa tela
        self.cadastrar_financeira.show_all() 

        #chama o metodo criar tabela
        self.criartabela()    
        gtk.main()
     
    def criartabela(self):
             
                    conexao = MySQLdb.connect(host="localhost", user="root",passwd="carros", db="agenciaBeta1")
                    cursor = conexao.cursor()
                    
                    sql = """create table cf(
                             codigofinanceira int(10) PRIMARY KEY AUTO_INCREMENT NOT NULL UNIQUE,
                             nome varchar(50) not null,
                             local varchar(60) not null,
                             cidade varchar(50),
                             cep varchar(10),
                             cnpj varchar(20),
                             telefone1 varchar(11),
                             telefone2 varchar(11),
                             celular varchar(11),
                             email varchar(50),
                             data varchar(20))"""

                    try:     
                            print  ' j   j   '
                            cursor.execute(sql)
                            conexao.commit()
                            
                    except MySQLdb.Error, e:
                    
                       if e.args[0] == 1050:                     
                         print  'Tratando o erro'
                         
                    #gtk.main()
    def on_buttonSalvar_clicked (self,*args):
        print'buttonSalvar'
        
        if (self.entryNome.props.text == "" or self.entryLocal.props.text== "" or self.entryCidade.props.text == "" or self.entryCep.props.text== "" or self.entryTelefone1.props.text== "" ):
        
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Por favor Preencha Todos os Campos')
            msg.run()
            msg.destroy()
            print 'g'
            
        else:
            
            nome = self.entryNome.props.text
            local= self.entryLocal.props.text
            cidade= self.entryCidade.props.text
            cep= self.entryCep.props.text
            cnpj=self.entryCnpj.props.text
            telefone1=self.entryTelefone1.props.text
            telefone2=self.entryTelefone2.props.text
            celular=self.entryCelular.props.text
            email=self.entryEmail.props.text
            data1 = datetime.datetime.now().date().isoformat()
            data =  '/'.join(data1.split('-')[::-1])
        
       
            " Limpando os campos "
            self.entryNome.props.text = ""
            self.entryLocal.props.text = ""
            self.entryCidade.props.text = ""
            self.entryCep.props.text = ""
            self.entryCnpj.props.text = ""
            self.entryTelefone1.props.text = ""
            self.entryTelefone2.props.text = ""
            self.entryCelular.props.text = ""
            self.entryEmail.props.text = ""
            
            #gravando dados no Banco
            sql = "insert into cf(nome,local, cidade, cep, cnpj, telefone1, telefone2, celular, email,data) values('" + nome + "','" + local + "', '" + cidade  + "', '" + cep + "','" + cnpj  + "', '" + telefone1  + "', '" + telefone2 + "','" + celular + "','" + email + "','" + data  + "')"
            self.conexao=MySQLdb.connect(self.host,self.user,self.passwd,self.database)
            self.cursor = self.conexao.cursor()
            self.cursor.execute(sql)
            self.conexao.commit()#Para enviar tudo para o Banco
            
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Cadastrado Com Sucesso')
            msg.run()
            msg.destroy()
        #gtk.main()
        

    def on_buttonFechar_clicked (self,*args):
        print'buttonFechar'
        self.cadastrar_financeira.hide()
        gtk.main_quit()
    def on_cadastrar_financeira_destroy(self,*args):
        print 'hi'
        gtk.main_quit()

        
if __name__ == '__main__':

    cf = CadastrarFinanceira()
