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
    import datetime
    from CadastrarCliente import *
    

except:
    print ' Erro Ao Carregar um dos Import'
    sys.exit(1)

class ConsultarCliente(object):
    def __init__(self):
        self.host= "localhost"
        self.user= "root"
        self.passwd= "carros"
        self.database = "agenciaBeta1"
        #Setando a variavel com o arquivo glade
        self.arquivoglade = "Projects\consultar_cliente\consultar_cliente.glade"
        #Extraindo conteudo XML do arquivo
        self.xml = gtk.glade.XML(self.arquivoglade)        
        #Componentes da Janela ConsultarCliente
        self.consultar_cliente=self.xml.get_widget('consultar_cliente')
        self.buttonPesquisar= self.xml.get_widget('buttonPesquisar')
        self.buttonExcluir= self.xml.get_widget('buttonExcluir')
        self.buttonFechar=self.xml.get_widget('buttonFechar')
        self.buttonEditar=self.xml.get_widget('buttonEditar')
        self.entryPesquisarCliente= self.xml.get_widget('entryPesquisarCliente')
        self.treeviewConsultarCliente =self.xml.get_widget('treeviewConsultarCliente')

        
      
        #Tela Principal
       # self.cliente.connect('destroy', gtk.main_quit)
        #Tela Clente
        #self.buttonPesquisar.connect('clicked',self.on_buttonPesquisar_clicked)
        #self.buttonExcluir.connect('clicked',self.on_buttonExcluir_clicked)
        #self.buttonFechar.connect('clicked',self.on_buttonFechar_clicked)
        #self.buttonEditar.connect('clicked',self.on_buttonEditar_clicked)
#==========================================================
        # Comboxbox
        self.cbxSistema = self.xml.get_widget('combobox1')
        
        # Preparar a Caixa Comboxbox para selecao
        
        # Componente ListStore para armazenar as retas
        store = gtk.ListStore(str)
        store.append(["Todos"])
        store.append(["Nome"])
        store.append(["CPF"])
        store.append(["RG"])
         

        # Celula texto para nossa Caixa de Selecao
        celula = gtk.CellRendererText()
        # Associa o ListStore a Caixa de Selecao
        self.cbxSistema.set_model(store)
        # Associa a celula a caixa de selecao
        self.cbxSistema.pack_start(celula, True)
        self.cbxSistema.add_attribute(celula, 'text', 0)
        
        # Coloca o foco no -Selecionar-
        self.cbxSistema.set_active(0)
        #============================================================================
        #Conectando no banco
        self.conexao = MySQLdb.connect(host="localhost", user="root",passwd="carros", db="agenciaBeta1")
        self.cursor = self.conexao.cursor()
        self.addTreeView()
         # Autoconnect Signals and Callbacks
        self.xml.signal_autoconnect(self)
        #desabilita a caixa de texto caso a selecao do combobox for 'Todos'.
        #if self.cbxSistema.get_active_text()=='Todos':
              #self.entryPesquisar.set_editable(False)
        self.consultar_cliente.show_all() 
        
        gtk.main()   
    def combo(self):
        
        gtk.main()
    def addTreeView(self):
        #Instancia o treeview coloca os descreve as colunas e as propriedades 
        self.model = gtk.ListStore(str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str)
        self.treeviewConsultarCliente.set_model(self.model)
        #muda a cor da celula  e torna o campo editavel 
        renderer1 = gtk.CellRendererText()        
        renderer1.set_property("background", "gray") # Cor do foreground como propriedade
        renderer1.set_property("foreground", "black") # Cor do foreground como propriedade
        
        col0 = gtk.TreeViewColumn('Codigo', renderer1, text=0)
        col1 = gtk.TreeViewColumn('Nome', gtk.CellRendererText(), text=1)
        col2 = gtk.TreeViewColumn('EstadoCivil',renderer1, text=2)
        col3 = gtk.TreeViewColumn('Endereco',gtk.CellRendererText() , text=3)
        col4 = gtk.TreeViewColumn('Numero', renderer1, text=4)
        col5 = gtk.TreeViewColumn('Bairro', gtk.CellRendererText(), text=5)
        col6 = gtk.TreeViewColumn('Cidade', renderer1, text=6)
        col7 = gtk.TreeViewColumn('Cep', gtk.CellRendererText(), text=7)
        col8 = gtk.TreeViewColumn('Uf', renderer1, text=8)
        col9 = gtk.TreeViewColumn('Email', gtk.CellRendererText(), text=9)
        col10 = gtk.TreeViewColumn('CPF',renderer1, text=10)
        col11= gtk.TreeViewColumn('RG', gtk.CellRendererText(), text=11)
        col12 = gtk.TreeViewColumn('Data Nascimento',renderer1, text=12)
        col13 = gtk.TreeViewColumn('DDD_Residencial', gtk.CellRendererText(), text=13)
        col14 = gtk.TreeViewColumn('DDD_Comercial', renderer1, text=14)
        col15 = gtk.TreeViewColumn('DDD_Celular', gtk.CellRendererText(), text=15)
        col16 = gtk.TreeViewColumn('Tel-Residencial', renderer1, text=16)
        col17 = gtk.TreeViewColumn('Tel-Comercial', gtk.CellRendererText(), text=17)
        col18 = gtk.TreeViewColumn('Celular', renderer1, text=18)
        col19 = gtk.TreeViewColumn('Ramal', gtk.CellRendererText(), text=19)
        col20 = gtk.TreeViewColumn('Ramal', renderer1, text=20)
        col21 = gtk.TreeViewColumn('Banco', gtk.CellRendererText(), text=21)
        col22 = gtk.TreeViewColumn('Agencia', renderer1, text=22)
        col23 = gtk.TreeViewColumn('Numero Conta', gtk.CellRendererText(), text=23)
        col24 = gtk.TreeViewColumn('TipoConta', renderer1, text=24)
        col25= gtk.TreeViewColumn('Data', gtk.CellRendererText(), text=25)



        col0.set_min_width(30)
        col1.set_min_width(150)
        col2.set_min_width(124)
        col3.set_min_width(123)
        #col4.set_min_width(124)
        self.treeviewConsultarCliente.append_column(col0)
        self.treeviewConsultarCliente.append_column(col1)
        self.treeviewConsultarCliente.append_column(col2)
        self.treeviewConsultarCliente.append_column(col3)
        self.treeviewConsultarCliente.append_column(col4)
        self.treeviewConsultarCliente.append_column(col5)
        self.treeviewConsultarCliente.append_column(col6)
        self.treeviewConsultarCliente.append_column(col7)
        self.treeviewConsultarCliente.append_column(col8)
        self.treeviewConsultarCliente.append_column(col9)
        self.treeviewConsultarCliente.append_column(col10)
        self.treeviewConsultarCliente.append_column(col11)
        self.treeviewConsultarCliente.append_column(col12)
        self.treeviewConsultarCliente.append_column(col13)
        self.treeviewConsultarCliente.append_column(col14)
        self.treeviewConsultarCliente.append_column(col15)
        self.treeviewConsultarCliente.append_column(col16)
        self.treeviewConsultarCliente.append_column(col17)
        self.treeviewConsultarCliente.append_column(col18)
        self.treeviewConsultarCliente.append_column(col19)
        self.treeviewConsultarCliente.append_column(col20)
        self.treeviewConsultarCliente.append_column(col21)
        self.treeviewConsultarCliente.append_column(col22)
        self.treeviewConsultarCliente.append_column(col23)
        self.treeviewConsultarCliente.append_column(col24)
        self.treeviewConsultarCliente.append_column(col25)
        self.leBanco()
        # metodo que  ler o banco de dados e adiciona no trewview 
    def leBanco(self):
        sql = "select * from c "
        model = self.treeviewConsultarCliente.get_model()
        model.clear()
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        for linha in resultado:
            model.append([linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[10], linha[11], linha[12], linha[13], linha[14], linha[15], linha[16], linha[17], linha[18], linha[19], linha[20], linha[21], linha[22], linha[23], linha[24],linha[25]])
    
    #testando outra maneira de pegar selecao treev
    def pegaSelecaoTreev(self):
                valor = self.treeviewConsultarCliente.get_cursor()
                n = valor[0]
                if n == None:
                        msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Nenhum registro selecionado para Baixa')
                        msg.run()
                        msg.destroy()
                        return None
                else:
                        registro = self.treeviewConsultarCliente.get_selection()
                        registro.set_mode(gtk.SELECTION_MULTIPLE)
                        #" Pegando a linha selecionada "
                        modelo, caminhos = registro.get_selected_rows()
                        for caminho in caminhos:
                                kiter = modelo.get_iter(caminho)
                                codigo = modelo.get_value(kiter, 7)
                        return codigo   
            
    #metodo responsavel de fazer a pesquisa 
    def on_buttonPesquisar_clicked (self,widget):
        print'buttonPesquisar'
        
    
        #pega o que esta no combobox
        comboo = self.cbxSistema.get_active_text()
        if comboo=="Todos":
            
            sql = "select * from c "
            model = self.treeviewConsultarCliente.get_model()
            model.clear()
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            for linha in resultado:
                model.append([linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[10], linha[11], linha[12], linha[13], linha[14], linha[15], linha[16], linha[17], linha[18], linha[19], linha[20], linha[21], linha[22], linha[23], linha[24],linha[25]])
            #self.entryPesquisarCliente.props.text = ""
        
        elif comboo=="Nome":
            nome = self.entryPesquisarCliente.props.text
            sql = "select * from c where nome='%s'" %(nome) 
            model = self.treeviewConsultarCliente.get_model()
            model.clear()
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            for linha in resultado:
                model.append([linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[10], linha[11], linha[12], linha[13], linha[14], linha[15], linha[16], linha[17], linha[18], linha[19], linha[20], linha[21], linha[22], linha[23], linha[24],linha[25]])
            #self.entryPesquisarCliente.props.text = ""

        elif comboo=='CPF':
            cpf = self.entryPesquisarCliente.props.text
            sql = "select * from c where cpf='%s' " %(cpf)
            model = self.treeviewConsultarCliente.get_model()
            model.clear()
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            for linha in resultado:
                model.append([linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[10], linha[11], linha[12], linha[13], linha[14], linha[15], linha[16], linha[17], linha[18], linha[19], linha[20], linha[21], linha[22], linha[23], linha[24],linha[25]])
            #self.entryPesquisarCliente.props.text = ""

        elif comboo=='RG':
            rg = self.entryPesquisarCliente.props.text
            sql = "select * from c where rg='%s' " %(rg)
            model = self.treeviewConsultarCliente.get_model()
            model.clear()
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            for linha in resultado:
                model.append([linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[10], linha[11], linha[12], linha[13], linha[14], linha[15], linha[16], linha[17], linha[18], linha[19], linha[20],linha[21],linha[22],linha[23],linha[24],linha[25]])
            #self.entryPesquisarCliente.props.text = ""

        #gtk.main()

    
    def on_buttonEditar_clicked (self,widget):
        print'ButtonEditar'
        valor = self.treeviewConsultarCliente.get_cursor()
        
        
        self.n1=valor[0] #guarda o valor do curso e eu pego esse valor no  metodo atualizar
        n = valor[0]
        print n
        if n == None:
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Nenhum registro selecionado para atualizacao')
            msg.set_position(gtk.WIN_POS_CENTER)
            msg.run()
            msg.destroy()
        else:
            #mostra a janela update cadastrar Financeira
            #Setando a variavel com o arquivo glade
            self.arquivoglade = "Projects\update_cadastrar_cliente\update_cadastrar_cliente.glade"
            #Extraindo conteudo XML do arquivo
            self.xml = gtk.glade.XML(self.arquivoglade) 
            #instanciano as caixas de texto
            self.update_cadastrar_cliente=self.xml.get_widget('update_cadastrar_cliente')
    
            self.entryCodigo=self.xml.get_widget('entryCodigo')
            self.entryNome=self.xml.get_widget('entryNome')
          #  self.comboEstadoCivil=self.xml.get_widget('comboEstadoCivil')
            self.entryEndereco=self.xml.get_widget('entryEndereco')
            self.entryNumero=self.xml.get_widget('entryNumero')
            self.entryBairro=self.xml.get_widget('entryBairro')
            self.entryCidade=self.xml.get_widget('entryCidade')
            self.entryCep=self.xml.get_widget('entryCep')
           # self.comboUf=self.xml.get_widget('comboUf')
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
                #deixa a caixa de texto do codigo desativado
            self.entryCodigo.set_editable(False)

            self.xml.signal_autoconnect(self)
            
             
            print'gu'
            
            self.valor = self.treeviewConsultarCliente.get_selection()
            self.valor.set_mode(gtk.SELECTION_MULTIPLE)
            " Pegando a linha selecionada "
            modelo, caminhos = self.valor.get_selected_rows()
            print modelo 
            print caminhos
            for caminho in caminhos:
                    kiter = modelo.get_iter(caminho)
                    #coloquei o self para poer pegar esse valor em outro lugar
                    
                    self.codigo = modelo.get_value(kiter, 0)
                    nome = modelo.get_value(kiter, 1)
                    estadocivil = modelo.get_value(kiter, 2)
                    endereco = modelo.get_value(kiter, 3)
                    numero = modelo.get_value(kiter, 4)
                    bairro= modelo.get_value(kiter, 5)
                    cidade = modelo.get_value(kiter, 6)
                    cep = modelo.get_value(kiter, 7)
                   # uf = modelo.get_value(kiter, 8)
                    email= modelo.get_value(kiter, 9)
                    cpf = modelo.get_value(kiter, 10)
                    rg = modelo.get_value(kiter, 11)
                    nascimento = modelo.get_value(kiter, 12)
                    dddresidencial= modelo.get_value(kiter, 13)
                    dddcomercial = modelo.get_value(kiter, 14)
                    dddcelular = modelo.get_value(kiter, 15)
                    residencial = modelo.get_value(kiter, 16)
                    comercial= modelo.get_value(kiter, 17)
                    celular= modelo.get_value(kiter, 18)
                    ramalresidencial= modelo.get_value(kiter, 19)
                    ramalcomercial= modelo.get_value(kiter, 20)
                    banco = modelo.get_value(kiter, 21)
                    agencia= modelo.get_value(kiter, 22)
                    tipoconta = modelo.get_value(kiter, 23)
                    numeroconta = modelo.get_value(kiter, 24)

                    #contacorrente= modelo.get_value(kiter, 20)
                    
                    #coloca os dados referente a consulta dentro de seus respctivos lugares
                    self.entryCodigo.props.text=self.codigo
                    self.entryNome.props.text = nome
                    #estadocivil=self.comboEstadoCivil.get_model
                    self.entryEndereco.props.text = endereco
                    self.entryNumero.props.text = numero
                    self.entryBairro.props.text = bairro
                    self.entryCidade.props.text = cidade
                    self.entryCep.props.text = cep
                
                    self.entryEmail.props.text = email
                    self.entryCpf.props.text = cpf
                    self.entryRg.props.text= rg
                    self.entryDataNascimento.props.text = nascimento
                    self.entryDddResidencial.props.text = dddresidencial
                    self.entryDddComercial.props.text = dddcomercial
                    self.entryDddCelular.props.text = dddcelular
                    self.entryResidencial.props.text = residencial
                    self.entryComercial.props.text = comercial
                    self.entryCelular.props.text = celular
                    self.entryRamalResidencial.props.text = ramalresidencial
                    self.entryRamalComercial.props.text = ramalcomercial
                    self.entryBanco.props.text = banco
                    self.entryAgencia.props.text = agencia
                    self.entryNumeroConta.props.text = numeroconta
                    self.entryTipoConta.props.text = tipoconta
                    
                   # self.consultar_cliente.hide()

        #gtk.main()
        
    #correspondente a tela update cadastrar cliente
    def on_buttonAtualizar_clicked (self,widget):
        print'Atualizar'
        # so cadastra se o nome da tela atualizar estiver preenchido
        if (self.entryNome.props.text == "" ):
        
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Por favor preencha todos os campos')
            resposta=msg.run()
            msg.destroy()
            
        else:
            
            codigo=self.entryCodigo.props.text
            nome = self.entryNome.props.text
            #estadocivil=self.comboEstadoCivil.get_model
            endereco= self.entryEndereco.props.text
            numero= self.entryNumero.props.text
            bairro= self.entryBairro.props.text
            cidade= self.entryCidade.props.text
            cep= self.entryCep.props.text
            #uf=self.comboUf.get_active_text()
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
              
        
                   #entryPesquisarVendedor referente a caixa de texto da tela consultar vendedor
            if self.entryPesquisarCliente.props.text=='':
                print 'testa nome'
                sql = "select * from c"
                self.cursor.execute(sql)
                resultado = self.cursor.fetchall()
                i = 0
                t1 = range(1)
                for linha in resultado:
                    
                        t1[0] = i# -1  0 1 2
                        t2 = self.n1 #Esse self.n1 tem armazenado ovalor do cursor quando eu clico no registo que quero editar editar.
                        print'================'
                        print linha[0]#1 2
                                          
                        if t1[0] == t2[0]:
                            print 'otaio'
                            #gravando dados no Banco
                            sql=('''update c set nome='%s', endereco='%s', numero='%s', bairro='%s', cidade='%s', cep='%s', email='%s', cpf='%s', rg='%s', nascimento='%s', dddresidencial='%s', dddcomercial='%s', dddcelular='%s', residencial='%s', comercial='%s', celular='%s', ramalresidencial='%s', ramalcomercial='%s',banco='%s', agencia='%s',numeroconta='%s', tipoconta='%s' where codigo=%i '''%(nome, endereco, numero, bairro, cidade, cep, email, cpf, rg, nascimento, dddresidencial, dddcomercial, dddcelular, residencial, comercial, celular, ramalresidencial, ramalcomercial, banco, agencia,tipoconta,numeroconta,linha[0]))
                            self.cursor.execute(sql)
                            self.conexao.commit()
                        i=i+1
                        #fecha a tela de update .
                self.update_cadastrar_cliente.hide()
                msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Atualizado Com Sucesso')
                msg.run()
                msg.destroy()
            elif    self.entryPesquisarCliente.props.text!='':
                print 'diferente'
                sql = "select * from c"
                self.cursor.execute(sql)
                resultado = self.cursor.fetchall()
                i =1
                t1 = range(1)
            
            
            
                    
            
                for linha in resultado:
                        
                        
                        t1[0] = i# -1  0 1 2
                        t2 = int(self.codigo) #peguei o valor que  vinha em sring do codigo  e transformei em inteiro
                        print t2
                                                                  
                        if t2 ==linha[0]:
                            
                            print 'otaio'
                            #gravando dados no Banco
                            #sql3 = "insert into vv(1placav,renavamv,documento,motor,freio,cambio,funilaria,multas,outros,valorcompraveiculo,totalgastos,porcentagemlucro,valorsugeridovenda) values('" + placav + "','" + renavamv + "',%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f)"%(documento,motor,freio,cambio,funilaria,multas,outros,valorcompraveiculo,totalgastos,porcentagemlucro,valorsugeridovenda)
                            sql=('''update c set nome='%s', endereco='%s', numero='%s', bairro='%s', cidade='%s', cep='%s', email='%s', cpf='%s', rg='%s', nascimento='%s', dddresidencial='%s', dddcomercial='%s', dddcelular='%s', residencial='%s', comercial='%s', celular='%s', ramalresidencial='%s', ramalcomercial='%s',banco='%s', agencia='%s',numeroconta='%s', tipoconta='%s' where codigo=%i '''%(nome, endereco, numero, bairro, cidade, cep, email, cpf, rg, nascimento, dddresidencial, dddcomercial, dddcelular, residencial, comercial, celular, ramalresidencial, ramalcomercial, banco, agencia,tipoconta,numeroconta,linha[0]))
                            self.cursor.execute(sql)
                            self.conexao.commit()
                            self.leBanco()
                        #i=i+1
                        #fecha a tela de update .
                self.update_cadastrar_cliente.hide()
                msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Atualizado Com Sucesso')
                msg.run()
                msg.destroy()
    
    
        #gtk.main()
        
        

    def on_buttonExcluir_clicked (self,widget):
        print'buttonExcluir'
        #self.consultar_cliente.hide()
        #cadasc=CadastrarCliente()
        valor = self.treeviewConsultarCliente.get_cursor()
        n = valor[0]
        if n == None:
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Nenhum registro selecionado para exclusao')
            msg.set_position(gtk.WIN_POS_CENTER)
            msg.run()
            msg.destroy()
            #gtk.main()
        else:
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_QUESTION, gtk.BUTTONS_YES_NO, 'Deseja excluir o registro ?')
            resposta = msg.run()
            msg.destroy()

            if resposta == gtk.RESPONSE_YES:
                if self.entryPesquisarCliente.props.text=='':
                        valor = self.treeviewConsultarCliente.get_cursor()
                        n = valor[0]
                        sql = "select * from c"
                        self.cursor.execute(sql)
                        resultado = self.cursor.fetchall()
                        i = 0
                        t1 = range(1)
                        for linha in resultado:
                            t1[0] = i
                            t2 = n
                            if t1[0] == t2[0]:
                                sql = "DELETE FROM c WHERE codigo = %i" % (linha[0])
                                self.cursor.execute(sql)
                                self.conexao.commit()
                            i = i+1
                        self.leBanco()
                        msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Deletado com Sucesso!')
                        msg.run()
                        msg.destroy()
                elif self.entryPesquisarCliente.props.text!='':
                
                        self.valor = self.treeviewConsultarCliente.get_selection()
    
                        self.valor.set_mode(gtk.SELECTION_MULTIPLE)
                        " Pegando a linha selecionada "
                        modelo, caminhos = self.valor.get_selected_rows()
                        print modelo 
                        print caminhos
                        for caminho in caminhos:
                                kiter = modelo.get_iter(caminho)
                                #coloquei o self para poer pegar esse valor em outro lugar
                                self.codigo = modelo.get_value(kiter, 0)
                                
                        print self.codigo
                        sql = "select * from c"
                        self.cursor.execute(sql)
                        resultado = self.cursor.fetchall()
                                           
                        for linha in resultado:
                                
                            
                                t1 = int(self.codigo)#transformei em inteiro para fazer a comparacao com o linha[0]que vinha em inteiro
                                print 'gugu'
                                print self.codigo  
                                print linha[0]                                    
                                if t1 == linha[0]:
                                    sql = "DELETE FROM c WHERE codigo = %i" % (linha[0])
                                    self.cursor.execute(sql)
                                    self.conexao.commit()
                                    self.leBanco()
                msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Deletado com Sucesso!')
                msg.run()
                msg.destroy()
        #gtk.main()
            
    def on_buttonFechar_clicked (self,widget):
        print'button2Fechar'
        self.consultar_cliente.hide()
        gtk.main_quit()
        
    #correspondente a tela update cadastrar Vendedor
    def on_buttonSair_clicked (self,widget):
        print'button1Sair'
        self.update_cadastrar_cliente.hide()
        #gtk.main()
    def on_consultar_cliente_destroy(self,widget):
        print 'k'
        gtk.main_quit()
        
    #def on_update_cadastrar_cliente_destroy (self,widget):
     #   gtk.main_quit()
       
           
   
if __name__ == '__main__':

    consultac = ConsultarCliente()
  
    