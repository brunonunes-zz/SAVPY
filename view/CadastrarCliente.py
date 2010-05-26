# -*- coding: utf-8 -*-
'''
Created on 10/08/2009

@author: Luis Gustavo
'''

import sys
try:
    import datetime
    import pygtk
    pygtk.require('2.0')
    import gtk
    import gtk.glade
    import MySQLdb
    import os.path



except:
    print ' Erro Ao Carregar um dos Import76'
    sys.exit(1)

class CadastrarCliente(object):
    
    def __init__(self):
        """
        Metodo Construtor da classe
        """

        # setando as variaveis para acessar o banco de dados
        self.host= "localhost"
        self.user= "root"
        self.passwd= "carros"
        self.database ="agenciaBeta1"
        
        #Setando a variavel com o arquivo glade
        self.arquivoglade = "Projects\cadastro_cliente\cadastro_cliente.glade"
        #Carrega a interface a partir do arquivo glade
        self.xml = gtk.glade.XML(self.arquivoglade)        
        #Componentes da Janela CadastrarCliente
        self.cadastro_cliente=self.xml.get_widget('cadastro_cliente')
        self.entryCodigo=self.xml.get_widget('entryCodigo')
        self.entryNome=self.xml.get_widget('entryNome')
        self.comboEstadoCivil=self.xml.get_widget('comboEstadoCivil')
        self.entryEndereco=self.xml.get_widget('entryEndereco')
        self.entryNumero=self.xml.get_widget('entryNumero')
        self.entryBairro=self.xml.get_widget('entryBairro')
        self.entryCidade=self.xml.get_widget('entryCidade')
        self.entryCep=self.xml.get_widget('entryCep')
        self.comboUf=self.xml.get_widget('comboUf')
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
        self.entryBanco=self.xml.get_widget('entryBanco')
        self.entryAgencia=self.xml.get_widget('entryAgencia')
        self.entryTipoConta=self.xml.get_widget('entryTipoConta')
        self.entryNumeroConta=self.xml.get_widget('entryNumeroConta')
        self.buttonSalvar= self.xml.get_widget('buttonSalvar')
        self.buttonFechar=self.xml.get_widget('buttonFechar')       
        #mantem o foco do combobox no primeiro item 
        self.comboEstadoCivil.set_active(0)
        self.comboUf.set_active(0)
        
        self.xml.signal_autoconnect(self)
        
        #exibe todo os componentes  que estao dentro da janela cadastrar cliente 
        self.cadastro_cliente.show_all()
        #chama o metodo criar tabela 
        self.criarTabelaeBanco()   
        #inicia o loop principal  
        gtk.main()
        
    # cria um banco de dados e a tabela referente ao banco caso nao exista. 
    def criarTabelaeBanco(self):
        
        if not os.path.exists('agenciaBeta1.db'):
                    conexao = MySQLdb.connect(host="localhost", user="root",passwd="carros", db="agenciaBeta1")
                    cursor = conexao.cursor()
                    sql = """create table c(
                                codigo  int(10)PRIMARY KEY AUTO_INCREMENT NOT NULL UNIQUE ,
                                nome  varchar(50) not null,
                                estadocivil varchar(20) not null,
                                endereco  varchar(50) not null,
                                numero   varchar(9) not null,
                                bairro varchar(50) not null,
                                cidade varchar(50) not null,
                                cep varchar(9) not null,
                                uf varchar(2) not null,
                                email varchar (50) ,
                                cpf varchar(15) not null,
                                rg varchar(9) not null,
                                nascimento varchar(8) not null,
                                dddresidencial varchar(2) not null,
                                residencial varchar(9) not null,
                                ramalresidencial varchar(10),
                                dddcomercial varchar(2),
                                comercial varchar(9),
                                ramalcomercial varchar(10),
                                dddcelular varchar(2),
                                celular varchar(9),
                                banco varchar(25) not null,
                                agencia varchar(25)not null,
                                numeroconta varchar(25) not null,
                                tipoconta varchar(25) not null ,
                                data varchar(20))"""
        
               
                    try:
                            #executa o sql
                            cursor.execute(sql)
                            # 
                            conexao.commit()
                            print 'k'
                    except MySQLdb.Error, e:
                    
                       if e.args[0] == 1050:                     
                         print  'Tratando o erro'
                         
    def on_buttonSalvar_clicked (self,widget):
        print'buttonSalvar'
        
        
        #verifica se a caixa de texto esta vazia se sim aparece uma mensagem dizendo para preencher
        if (self.entryNome.props.text == "" or self.entryEndereco.props.text  == "" or self.entryNumero.props.text=="" or self.entryBairro.props.text == "" or self.entryCidade.props.text  == "" or self.entryCep.props.text == "" or self.entryCpf.props.text  == "" or self.entryRg.props.text  == "" or self.entryDataNascimento.props.text == "" or self.entryDddResidencial.props.text=="" or self.entryResidencial.props.text=="" ):
            #caixa de dialogo
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Por favor preencha os campos Marcado com *')
            resposta=msg.run()
            msg.destroy()
            
        else:
            #pegando o que foi digitado ou selecionado e armazenado nas variaveis
            nome = self.entryNome.props.text
            estadocivil=self.comboEstadoCivil.get_active_text()
            endereco= self.entryEndereco.props.text
            numero= self.entryNumero.props.text
            bairro= self.entryBairro.props.text
            cidade= self.entryCidade.props.text
            cep= self.entryCep.props.text
            uf=self.comboUf.get_active_text()
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
            banco=self.entryBanco.props.text
            agencia=self.entryAgencia.props.text
            numeroconta=self.entryNumeroConta.props.text
            tipoconta=self.entryTipoConta.props.text
            data1 = datetime.datetime.now().date().isoformat()
            data=  '/'.join(data1.split('-')[::-1])
        
            
            #" Limpando os campos "
            self.entryNome.props.text = ""
            self.comboEstadoCivil.set_active(0)
            self.entryEndereco.props.text = ""
            self.entryNumero.props.text = ""
            self.entryBairro.props.text = ""
            self.entryCidade.props.text = ""
            self.entryCep.props.text = ""
            self.comboUf.set_active(0)
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
            self.entryBanco.props.text = ""
            self.entryAgencia.props.text = ""
            self.entryNumeroConta.props.text = ""
            self.entryTipoConta.props.text = ""
            
            #gravando dados no Banco
            sql = "insert into c(nome,estadocivil, endereco, numero, bairro, cidade, cep,uf, email, cpf, rg, nascimento, dddresidencial, dddcomercial, dddcelular, residencial, comercial, celular, ramalresidencial, ramalcomercial,banco, agencia,numeroconta, tipoconta,data) values('" + nome + "','" + estadocivil + "', '" + endereco  + "', '" + numero + "','" + bairro  + "', '" + cidade  + "', '" + cep + "','" + uf + "','" + email + "', '" + cpf + "', '" + rg + "','" + nascimento + "', '" + dddresidencial + "', '" + dddcomercial+ "','" + dddcelular + "','" + residencial + "','" + comercial + "','" + celular + "','" + ramalresidencial + "','" + ramalcomercial + "','" + banco + "','" + agencia + "','" + numeroconta + "','" + tipoconta + "','" + data + "' )"
            #fazendo a conexao com o banco 
            self.conexao=MySQLdb.connect(self.host,self.user,self.passwd,self.database)
            self.cursor = self.conexao.cursor()
            self.cursor.execute(sql)
            self.conexao.commit()#Para enviar tudo para o Banco
            
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Cadastrado Com Sucesso')
            msg.run()
            msg.destroy()
        #gtk.main()
    def on_buttonFechar_clicked (self,widget):
        print'buttonFechar'
        #fecha a janela cadastro de cliente no clique do botao fechar
        self.cadastro_cliente.hide()
        gtk.main_quit()
        
    
    def on_cadastro_cliente_destroy(self,*args):
        print 'hueu'
        gtk.main_quit()

  
if __name__ == '__main__':

    cc = CadastrarCliente()
 
