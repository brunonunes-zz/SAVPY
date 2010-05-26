'''
Created on 10/08/2009

@author: Luis Gustavo
'''

import sys
try:

    import pygtk
    pygtk.require('2.0')
    import gtk
    import gtk.glade
    import MySQLdb
    from ConsultarCliente import *
    sys.path.append("C:\\Documents and Settings\\Administrador\\workspace\\agencia\\src\\model")
    sys.path.append("C:\\Documents and Settings\\Administrador\\workspace\\agencia\\src\\controller")



except:
    print ' Erro Ao Carregar um dos Import'
    sys.exit(1)

class CadastrarCliente(object):
    def __init__(self):
        self.host= "localhost"
        self.user= "root"
        self.passwd= "carros"
        self.database = "qqll" 
        #Setando a variavel com o arquivo glade
        self.arquivoglade = "C:\Documents and Settings\Administrador\Projects\cadastro_cliente\cadastro_cliente.glade"
        #Extraindo conteudo XML do arquivo
        self.xml = gtk.glade.XML(self.arquivoglade)        
        #Componentes da Janela CadastrarCliente
        self.cadastro_cliente=self.xml.get_widget('cadastro_cliente')
        self.entryCodigo=self.xml.get_widget('entryCodigo')
        self.entryNome=self.xml.get_widget('entryNome')
        self.entryEndereco=self.xml.get_widget('entryEndereco')
        self.entryNumero=self.xml.get_widget('entryNumero')
        self.entryBairro=self.xml.get_widget('entryBairro')
        self.entryCidade=self.xml.get_widget('entryCidade')
        self.entryCep=self.xml.get_widget('entryCep')
        self.entryEmail=self.xml.get_widget('entryEmail')
        self.entryCpf=self.xml.get_widget('entryCpf')
        self.entryRg=self.xml.get_widget('entryRg')
        self.entryDataNascimento=self.xml.get_widget('entryDataNascimento')
        self.entryResidencial=self.xml.get_widget('entryResidencial')
        self.entryComercial=self.xml.get_widget('entryComercial')
        self.entryCelular=self.xml.get_widget('entryCelular')
        self.entryRamalResidencial=self.xml.get_widget('entryRamalResidencial')
        self.entryRamalComercial=self.xml.get_widget('entryRamalComercial')
        self.entryDddResidencial=self.xml.get_widget('entryDddResidencial')
        self.entryDddComercial=self.xml.get_widget('entryDddComercial')
        self.entryDddCelular=self.xml.get_widget('entryDddCelular')
        self.entryAgencia=self.xml.get_widget('entryAgencia')
        self.entryContaCorrente=self.xml.get_widget('entryContaCorrente')
        
        self.buttonSalvar= self.xml.get_widget('buttonSalvar')
        self.buttonFechar=self.xml.get_widget('buttonFechar') 
        self.buttonEditar=self.xml.get_widget('buttonEditar')       
        # liga o clique do botao ao metodo
        self.buttonSalvar.connect('clicked',self.on_buttonSalvar_clicked)
        self.buttonFechar.connect('clicked',self.on_buttonFechar_clicked)
        self.buttonEditar.connect('clicked',self.on_buttonEditar_clicked)

        # Autoconnect Signals and Callbacks
        #faz a conexao com o banco de dados
        self.conexao = MySQLdb.connect(host="localhost", user="root",passwd="carros", db="g")
        self.cursor = self.conexao.cursor()
        self.xml.signal_autoconnect(self)
        #mostra todo os componentes  que estao dentro da janela cadastrar cliente 
        self.cadastro_cliente.show_all()
        #chama o metodo criar tabela 
        self.criarTabelaeBanco()    
        gtk.main()
    # cria um banco de dados e a tabela referente ao banco caso nao exista. 
    def criarTabelaeBanco(self):
        
        try:
                    #verifica se o database nomeado acima ja foi criado 
                    
            conexao = MySQLdb.connect(self.host,self.user,self.passwd,self.database)
            print ' Banco de Dados ja instalado'
                    
                  
        except MySQLdb.Error, e:
                    #caso nao foi criado cria o database e a tabela referete a ele
                    
            if e.args[0] == 1049:
                msg1 = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Esse software depende do Mysql instalado em sua maquina!')
                msg1.run()
                msg1.destroy()
                msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_QUESTION, gtk.BUTTONS_YES_NO, 'Base de dados inexistente. Deseja criar? ?')
                resposta = msg.run()
                #cria a tabela referente ao database
                if resposta == gtk.RESPONSE_YES:
                    conexao = MySQLdb.connect(host,user,passwd)
                    cursor = conexao.cursor()
                    cursor.execute('create database %s' %database)     
                    cursor.close()
                    msg.destroy() 
                    
                    
                    cursor = conexao.cursor()
                   # parte da tabela c unsigned not null auto_increment
                    sql = """create table c(
                                codigo  int(10)PRIMARY KEY AUTO_INCREMENT NOT NULL UNIQUE ,
                                nome  varchar(40) not null,
                                endereco  varchar(50),
                                numero   varchar(9),
                                bairro varchar(50) ,
                                cidade varchar(50),
                                cep varchar(9),
                                email varchar (50),
                                cpf varchar(15),
                                rg varchar(12),
                                nascimento varchar(10),
                                dddresidencial varchar(2),
                                dddcomercial varchar(2),
                                dddcelular varchar(2),
                                residencial varchar(10),
                                comercial varchar(10),
                                celular varchar(10),
                                ramalresidencial varchar(10),
                                ramalcomercial varchar(10),
                                contacorrente varchar(10),
                                agencia varchar(10))"""
        
                    cursor.execute(sql)
                    conexao.commit()
                else:
                    msg.destroy()
                    msg1 = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Voce depende da Criacao do Banco de Dados!')
                    msg1.run()
                    msg1.destroy()
    def on_buttonSalvar_clicked (self,widget):
        print'buttonSalvar'
        #verifica se a caixa de texto esta vazia se sim aparece uma mensagem dizendo para reencher
        if (self.entryNome.props.text == "" or self.entryEndereco.props.text  == ""  or self.entryBairro.props.text == "" or self.entryCidade.props.text  == "" or self.entryCep.props.text == ""or self.entryEmail.props.text  == "" or self.entryCpf.props.text  == "" or self.entryRg.props.text  == "" or self.entryDataNascimento.props.text == ""):
        
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Por favor preencha todos os campos')
            resposta=msg.run()
            msg.destroy()
            
        else:
            #pegando o que foi digitado e armazenado nas variaveis
            nome = self.entryNome.props.text
            endereco= self.entryEndereco.props.text
            numero= self.entryNumero.props.text
            bairro= self.entryBairro.props.text
            cidade= self.entryCidade.props.text
            cep= self.entryCep.props.text
            email=self.entryEmail.props.text
            cpf= self.entryCpf.props.text
            rg=self.entryRg.props.text
            nascimento= self.entryDataNascimento.props.text
            dddresidencial=self.entryDddResidencial.props.text
            dddcomercial=self.entryDddComercial.props.text
            dddcelular=self.entryDddCelular.props.text
            residencial=self.entryResidencial.props.text
            comercial=self.entryComercial.props.text
            celular=self.entryCelular.props.text
            ramalresidencial=self.entryRamalResidencial.props.text
            ramalcomercial=self.entryRamalComercial.props.text
            agencia=self.entryAgencia.props.text
            contacorrente=self.entryContaCorrente.props.text
            
            
            
            #" Limpando os campos "
            self.entryNome.props.text = ""
            self.entryEndereco.props.text = ""
            self.entryNumero.props.text = ""
            self.entryBairro.props.text = ""
            self.entryCidade.props.text = ""
            self.entryCep.props.text = ""
            self.entryEmail.props.text = ""
            self.entryCpf.props.text = ""
            self.entryRg.props.text = ""
            self.entryDataNascimento.props.text = ""
            self.entryDddResidencial.props.text = ""
            self.entryDddComercial.props.text = ""
            self.entryDddCelular.props.text = ""
            self.entryResidencial.props.text = ""
            self.entryComercial.props.text = ""
            self.entryCelular.props.text = ""
            self.entryRamalResidencial.props.text = ""
            self.entryRamalComercial.props.text = ""
            self.entryAgencia.props.text = ""
            self.entryContaCorrente.props.text = ""
            #gravando dados no Banco
            sql = "insert into c(nome, endereco, numero, bairro, cidade, cep, email, cpf, rg, nascimento, dddresidencial, dddcomercial, dddcelular, residencial, comercial, celular, ramalresidencial, ramalcomercial, agencia, contacorrente) values('" + nome + "', '" + endereco  + "', '" + numero + "','" + bairro  + "', '" + cidade  + "', '" + cep + "','" + email + "', '" + cpf + "', '" + rg + "','" + nascimento + "', '" + dddresidencial + "', '" + dddcomercial+ "','" + dddcelular + "','" + residencial + "','" + comercial + "','" + celular + "','" + ramalresidencial + "','" + ramalcomercial + "','" + agencia + "','" + contacorrente + "' )"
            self.conexao=MySQLdb.connect(self.host,self.user,self.passwd,self.database)
            self.cursor = self.conexao.cursor()
            self.cursor.execute(sql)
            self.conexao.commit()#Para enviar tudo para o Banco
            
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Cadastrado Com Sucesso')
            msg.run()
            msg.destroy()
        gtk.main()
    def on_buttonFechar_clicked (self,widget):
        print'buttonFechar'
        #fecha a janela cadastro de cliente no clique do botao fechar
        self.cadastro_cliente.hide()
        gtk.main()
    def on_buttonEditar_clicked (self,widget):
        print 'buttonEditar'
        self.cadastro_cliente.hide()
        c=ConsultarCliente()
        gtk.main()
           
'''   
if __name__ == '__main__':

    cc = CadastrarCliente()
'''  
