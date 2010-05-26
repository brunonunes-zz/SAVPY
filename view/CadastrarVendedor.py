# -*- coding: utf-8 -*-

'''
Created on 17/08/2009

@author: Gustavo
'''
#-*- coding:utf-8 -*- 

import sys
try:

    import pygtk
    pygtk.require('2.0')
    import gtk
    import gtk.glade
    import MySQLdb
    import datetime
    import os.path
    from CadastroUsuario import *
    

except:
    print ' Erro Ao Carregar um dos Import76'
    sys.exit(1)

class CadastrarVendedor(object):
    def __init__(self):
        
        self.host= "localhost"
        self.user= "root"
        self.passwd= "carros"
        self.database = "agenciaBeta1"
        #Setando a variavel com o arquivo glade
        self.arquivoglade = "Projects\cadastro_vendedor\cadastro_vendedor.glade"
        #Extraindo conteudo XML do arquivo
        self.xml = gtk.glade.XML(self.arquivoglade)        
        #Componentes da Janela CadastrarSenha
        self.cadastro_vendedor=self.xml.get_widget('cadastro_vendedor')
        self.buttonSalvar=self.xml.get_widget('buttonSalvar')
        self.buttonFechar=self.xml.get_widget('buttonFechar')
        self.entrySetor=self.xml.get_widget('entrySetor')
        self.entryNome=self.xml.get_widget('entryNome')
        self.comboEstadoCivil=self.xml.get_widget('comboEstadoCivil')
        self.entryEndereco=self.xml.get_widget('entryEndereco')
        self.entryNumero=self.xml.get_widget('entryNumero')
        self.entryBairro=self.xml.get_widget('entryBairro')
        self.entryCidade=self.xml.get_widget('entryCidade')
        self.entryCep=self.xml.get_widget('entryCep')
        self.comboUf=self.xml.get_widget('comboUf')
        self.entryEmail=self.xml.get_widget('entryEmail')
        self.entryNascimento=self.xml.get_widget('entryNascimento')
        self.entryCpf=self.xml.get_widget('entryCpf')
        self.entryRg=self.xml.get_widget('entryRg')
        self.entryDddResidencial=self.xml.get_widget('entryDddResidencial')
        self.entryResidencial=self.xml.get_widget('entryResidencial')
        self.entryDddCelular=self.xml.get_widget('entryDddCelular')
        self.entryCelular=self.xml.get_widget('entryCelular')
        
        #mantem o foco do combobox no primeiro item 
        self.comboEstadoCivil.set_active(0)
        self.comboUf.set_active(0)

       # Autoconnect Signals and Callbacks
        self.xml.signal_autoconnect(self)
        
        #self.buttonSalvar.connect('clicked',self.on_buttonSalvar_clicked)

        #self.buttonFechar.connect('clicked',self.on_buttonFechar_clicked)
        
        self.cadastro_vendedor.show_all() 
        self.criartabela()    
        gtk.main()
    
    
    def criartabela(self):
        
         if  not os.path.exists('agenciaBeta1.db'):
         
                    conexao = MySQLdb.connect(host="localhost", user="root",passwd="carros", db="agenciaBeta1")
                    cursor = conexao.cursor()
                    
                    sql = """create table v(
                            codigovendedor int(10) PRIMARY KEY AUTO_INCREMENT NOT NULL UNIQUE ,
                            setor varchar(30) not null,
                            nome  varchar(60) not null,
                            estadocivil varchar(20) not null,
                            endereco varchar(60) not null,
                            numero varchar(5) not null,
                            bairro varchar(40) not null,
                            cidade varchar(40) not null,
                            cep varchar(9) not null,
                            uf varchar (2) not null,
                            email varchar(40),
                            datanascimento varchar(10) not null,
                            cpf  varchar(11) not null,
                            rg   varchar(9) not null,
                            dddresidencial varchar(2) not null,
                            residencial varchar(8) not null,
                            dddcelular varchar(2) not null,
                            celular varchar(8)not null,
                            data varchar(15))"""

                    try:
                            cursor.execute(sql)
                            conexao.commit()
                            
                    except MySQLdb.Error, e:
                    
                       if e.args[0] == 1050:                     
                         print  'Tratando o erro'
                         
    def on_buttonSalvar_clicked (self,widget):
        print'buttonSalvar'
        if (self.entryNome.props.text == "" or self.entrySetor.props.text  == "" or self.entryEndereco.props.text == "" or self.entryNumero.props.text  == ""  or self.entryBairro.props.text == "" or self.entryCidade.props.text == "" or self.entryCpf.props.text == "" or self.entryRg.props.text == "" or self.entryResidencial.props.text == "" ):
        
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Por favor preencha todos os campos')
            resposta=msg.run()
            msg.destroy()
            
        else:
            
            #model = self.treev.get_model()
            setor = self.entrySetor.props.text
            nome = self.entryNome.props.text
            estadocivil=self.comboEstadoCivil.get_active_text()
            endereco= self.entryEndereco.props.text
            numero= self.entryNumero.props.text
            bairro= self.entryBairro.props.text
            cidade= self.entryCidade.props.text
            cep= self.entryCep.props.text
            uf=self.comboUf.get_active_text()
            email=self.entryEmail.props.text
            datanascimento= self.entryNascimento.props.text
            cpf= self.entryCpf.props.text
            rg=self.entryRg.props.text
            dddresidencial=self.entryDddResidencial.props.text
            residencial=self.entryResidencial.props.text
            dddcelular=self.entryDddCelular.props.text
            celular=self.entryCelular.props.text
            data1 = datetime.datetime.now().date().isoformat()
            data=  '/'.join(data1.split('-')[::-1])
            
            
            " Limpando os campos "
            self.entrySetor.props.text = ""
            self.entryNome.props.text = ""
            self.comboEstadoCivil.set_active(0)
            self.entryEndereco.props.text = ""
            self.entryNumero.props.text = ""
            self.entryBairro.props.text = ""
            self.entryCidade.props.text = ""
            self.entryCep.props.text = ""
            self.comboUf.set_active(0)
            self.entryEmail.props.text = ""
            self.entryNascimento.props.text = ""
            self.entryCpf.props.text = ""
            self.entryRg.props.text = ""
            self.entryDddResidencial.props.text = ""
            self.entryResidencial.props.text = ""
            self.entryDddCelular.props.text = ""
            self.entryCelular.props.text = ""
            
            #gravando dados no Banco
            sql = "insert into v(setor,nome,estadocivil, endereco, numero, bairro, cidade, cep,uf, email, datanascimento, cpf, rg, dddresidencial,residencial,dddcelular, celular,data) values('" + setor + "','" + nome + "', '" + estadocivil + "', '" + endereco  + "', '" + numero + "','" + bairro  + "', '" + cidade  + "', '" + cep + "', '" + uf + "','" + email + "','" + datanascimento + "', '" + cpf + "', '" + rg + "', '" + dddresidencial + "','" + residencial + "', '" + dddcelular + "','" + celular + "','" + data + "' )"
            self.conexao=MySQLdb.connect(self.host,self.user,self.passwd,self.database)
            self.cursor = self.conexao.cursor()
            self.cursor.execute(sql)
            self.conexao.commit()#Para enviar tudo para o Banco
            
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Cadastrado Com Sucesso')
            msg.run()
            msg.destroy()
            self.cadastro_vendedor.hide()
            cadasu=CadastroUsuario()
            
        #gtk.main()

    def on_buttonFechar_clicked (self,widget):
        print'buttonFechar'
        self.cadastro_vendedor.hide()
        gtk.main_quit()
        
    def on_cadastro_vendedor_destroy(self,widget):
        print 'k'
        gtk.main_quit()
        
      
if __name__ == '__main__':

     c= CadastrarVendedor()
