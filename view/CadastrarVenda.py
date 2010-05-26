# -*- coding: utf-8 -*-

'''
Created on 01/09/2009

@author: Gustavo
'''

import sys
try:

    import pygtk
    pygtk.require('2.0')
    import gtk
    import gtk.glade
    import MySQLdb
    import os.path
    import datetime
    from TrocarVeiculo import *
    from CadastrarVeiculo import *


except:
    print ' Erro Ao Carregar um dos Import54'
    sys.exit(1)


class CadastrarVenda(object):
    


    def __init__(self):
        self.host= "localhost"
        self.user= "root"
        self.passwd= "carros"
        self.database = "agenciaBeta1"
        #conexao com o banco de dados
        self.conexao = MySQLdb.connect(host="localhost", user="root",passwd="carros", db="agenciaBeta1")
        self.cursor = self.conexao.cursor()
        
        #Setando a variavel com o arquivo glade referente a tela da escolha entre venda e troca de  veiculo
        self.arquivoglade = "Projects\cadastrar_venda_troca\cadastrar_venda_troca.glade"
        #Extraindo conteudo XML do arquivo
        self.xml = gtk.glade.XML(self.arquivoglade)        
        #Componentes da Janela referente a tela de da escolha entre venda e troca
        self.cadastrar_venda_troca=self.xml.get_widget('cadastrar_venda_troca')
        self.combovenda_troca = self.xml.get_widget('combovenda_troca')
        #seta o foco para a primeira posicao do combobox
        self.combovenda_troca.set_active(0)     
        self.cadastrar_venda_troca.show_all()
        self.xml.signal_autoconnect(self)
        
        gtk.main()
        
    def addTreeViewCliente(self):
        #Instancia o treeview coloca os descreve as colunas e as propriedades 
        self.model = gtk.ListStore(str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str)
        self.treeviewCliente.set_model(self.model)
        #muda a cor da celula  e torna o campo editavel 
        renderer1 = gtk.CellRendererText()        
        renderer1.set_property("background", "pink") # Cor do foreground como propriedade
        renderer1.set_property("foreground", "blue") # Cor do foreground como propriedade
        
        renderer2 = gtk.CellRendererText()        
        renderer2.set_property("background", "green") # Cor do foreground como propriedade
        renderer2.set_property("foreground", "black") # Cor do foreground como propriedade
                
        col0 = gtk.TreeViewColumn('Codigo', renderer1, text=0)
        col1 = gtk.TreeViewColumn('Nome', gtk.CellRendererText(), text=1)
        col2 = gtk.TreeViewColumn('EstadoCivil', gtk.CellRendererText(), text=2)
        col3 = gtk.TreeViewColumn('Endereco', renderer2, text=3)
        col4 = gtk.TreeViewColumn('Numero', gtk.CellRendererText(), text=4)
        col5 = gtk.TreeViewColumn('Bairro', gtk.CellRendererText(), text=5)
        col6 = gtk.TreeViewColumn('Cidade', gtk.CellRendererText(), text=6)
        col7 = gtk.TreeViewColumn('Cep', gtk.CellRendererText(), text=7)
        col8 = gtk.TreeViewColumn('Uf', gtk.CellRendererText(), text=8)
        col9 = gtk.TreeViewColumn('Email', gtk.CellRendererText(), text=9)
        col10 = gtk.TreeViewColumn('CPF', gtk.CellRendererText(), text=10)
        col11= gtk.TreeViewColumn('RG', gtk.CellRendererText(), text=11)
        col12 = gtk.TreeViewColumn('Data Nascimento', gtk.CellRendererText(), text=12)
        col13 = gtk.TreeViewColumn('DDD_Residencial', gtk.CellRendererText(), text=13)
        col14 = gtk.TreeViewColumn('DDD_Comercial', gtk.CellRendererText(), text=14)
        col15 = gtk.TreeViewColumn('DDD_Celular', gtk.CellRendererText(), text=15)
        col16 = gtk.TreeViewColumn('Tel-Residencial', gtk.CellRendererText(), text=16)
        col17 = gtk.TreeViewColumn('Tel-Comercial', gtk.CellRendererText(), text=17)
        col18 = gtk.TreeViewColumn('Celular', gtk.CellRendererText(), text=18)
        col19 = gtk.TreeViewColumn('Ramal', gtk.CellRendererText(), text=19)
        col20 = gtk.TreeViewColumn('Ramal', gtk.CellRendererText(), text=20)
        col21 = gtk.TreeViewColumn('Banco', gtk.CellRendererText(), text=21)
        col22 = gtk.TreeViewColumn('Agencia', gtk.CellRendererText(), text=22)
        col23 = gtk.TreeViewColumn('Numero Conta', gtk.CellRendererText(), text=23)
        col24 = gtk.TreeViewColumn('TipoConta', gtk.CellRendererText(), text=24)
        col25= gtk.TreeViewColumn('Data', gtk.CellRendererText(), text=25)

        col0.set_min_width(30)
        col1.set_min_width(150)
        col2.set_min_width(124)
        col3.set_min_width(123)
    
        self.treeviewCliente.append_column(col0)
        self.treeviewCliente.append_column(col1)
        self.treeviewCliente.append_column(col2)
        self.treeviewCliente.append_column(col3)
        self.treeviewCliente.append_column(col4)
        self.treeviewCliente.append_column(col5)
        self.treeviewCliente.append_column(col6)
        self.treeviewCliente.append_column(col7)
        self.treeviewCliente.append_column(col8)
        self.treeviewCliente.append_column(col9)
        self.treeviewCliente.append_column(col10)
        self.treeviewCliente.append_column(col11)
        self.treeviewCliente.append_column(col12)
        self.treeviewCliente.append_column(col13)
        self.treeviewCliente.append_column(col14)
        self.treeviewCliente.append_column(col15)
        self.treeviewCliente.append_column(col16)
        self.treeviewCliente.append_column(col17)
        self.treeviewCliente.append_column(col18)
        self.treeviewCliente.append_column(col19)
        self.treeviewCliente.append_column(col20)
        self.treeviewCliente.append_column(col21)
        self.treeviewCliente.append_column(col22)
        self.treeviewCliente.append_column(col23)
        self.treeviewCliente.append_column(col24)
        self.treeviewCliente.append_column(col25)
       # self.treeviewVeiculo()# metodo que  ler o banco de dados e adiciona no trewview 
        self.treeViewVeiculo()

    def treeViewVeiculo(self):
        #adicionando no treeview
        self.model = gtk.ListStore(str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str)
        self.treeviewVeiculo.set_model(self.model)
        #muda a cor da celula  e torna o campo editavel 
        renderer1 = gtk.CellRendererText()        
        renderer1.set_property("background", "gray") # Cor do foreground como propriedade
        renderer1.set_property("foreground", "black") # Cor do foreground como propriedade
        renderer1.set_property('editable', True) # A primeira coluan e editavel
                
        col0 = gtk.TreeViewColumn('Codigo', renderer1, text=0)
        col1 = gtk.TreeViewColumn('Placa', gtk.CellRendererText(), text=1)
        col2 = gtk.TreeViewColumn('Renavam', renderer1, text=2)
        col3 = gtk.TreeViewColumn('Numero Chassi', gtk.CellRendererText(), text=3)
        col4 = gtk.TreeViewColumn('Fabricante', renderer1, text=4)
        col5 = gtk.TreeViewColumn('Modelo', gtk.CellRendererText(), text=5)
        col6 = gtk.TreeViewColumn('Marca', renderer1, text=6)
        col7 = gtk.TreeViewColumn('Ano', gtk.CellRendererText(), text=7)
        col8 = gtk.TreeViewColumn('Cidade',renderer1, text=8)
        col9 = gtk.TreeViewColumn('UF', gtk.CellRendererText(), text=9)
        col10 = gtk.TreeViewColumn('Combustivel', renderer1, text=10)
        col11 = gtk.TreeViewColumn('Km', gtk.CellRendererText(), text=11)
        col12 = gtk.TreeViewColumn('Cor', renderer1, text=12)
        col13 = gtk.TreeViewColumn('Numero  de Portas', gtk.CellRendererText(), text=13)
        col14 = gtk.TreeViewColumn('Pneu Dianteiro', gtk.CellRendererText(), text=14)
        col15 = gtk.TreeViewColumn('Pneu Traseiro', renderer1, text=15)
        col16 = gtk.TreeViewColumn('Estepe', gtk.CellRendererText(), text=16)
        col17 = gtk.TreeViewColumn('Rodas', gtk.CellRendererText(), text=17)
        col18 = gtk.TreeViewColumn('Colisao', gtk.CellRendererText(), text=18)
        col19 = gtk.TreeViewColumn('Suspensao', gtk.CellRendererText(), text=19)
        col20 = gtk.TreeViewColumn('Funilaria', gtk.CellRendererText(), text=20)
        col21 = gtk.TreeViewColumn('Pintura', gtk.CellRendererText(), text=21)
        col22 = gtk.TreeViewColumn('Estofados', gtk.CellRendererText(), text=22)
        col23 = gtk.TreeViewColumn('Motor', gtk.CellRendererText(), text=23)
        col24 = gtk.TreeViewColumn('Cambio', gtk.CellRendererText(), text=24)
        col25 = gtk.TreeViewColumn('Amortecedor Dianteiro', gtk.CellRendererText(), text=25)
        col26 = gtk.TreeViewColumn('Amortecedor Traseiro', gtk.CellRendererText(), text=26)
        col27 = gtk.TreeViewColumn('Anotacoes', gtk.CellRendererText(), text=27)
        col28 = gtk.TreeViewColumn('Disponibilidade Veiculo na Agencia', gtk.CellRendererText(), text=28)
        col29 = gtk.TreeViewColumn('Data Venda Veiculo', gtk.CellRendererText(), text=29)

        col0.set_min_width(30)
        col1.set_min_width(50)
        col2.set_min_width(50)
        col3.set_min_width(50)
        col4.set_min_width(50)
        col5.set_min_width(50)
        col6.set_min_width(50)
        col7.set_min_width(50)
        col8.set_min_width(50)
        col9.set_min_width(50)
        col10.set_min_width(50)
        col11.set_min_width(50)
        col12.set_min_width(50)

        self.treeviewVeiculo.append_column(col0)
        self.treeviewVeiculo.append_column(col1)
        self.treeviewVeiculo.append_column(col2)
        self.treeviewVeiculo.append_column(col3)
        self.treeviewVeiculo.append_column(col4)
        self.treeviewVeiculo.append_column(col5)
        self.treeviewVeiculo.append_column(col6)
        self.treeviewVeiculo.append_column(col7)
        self.treeviewVeiculo.append_column(col8)
        self.treeviewVeiculo.append_column(col9)
        self.treeviewVeiculo.append_column(col10)
        self.treeviewVeiculo.append_column(col11)
        self.treeviewVeiculo.append_column(col12)
        self.treeviewVeiculo.append_column(col13)
        self.treeviewVeiculo.append_column(col14)
        self.treeviewVeiculo.append_column(col15)
        self.treeviewVeiculo.append_column(col16)
        self.treeviewVeiculo.append_column(col17)
        self.treeviewVeiculo.append_column(col18)
        self.treeviewVeiculo.append_column(col19)
        self.treeviewVeiculo.append_column(col20)
        self.treeviewVeiculo.append_column(col21)
        self.treeviewVeiculo.append_column(col22)
        self.treeviewVeiculo.append_column(col23)
        self.treeviewVeiculo.append_column(col24)
        self.treeviewVeiculo.append_column(col25)
        self.treeviewVeiculo.append_column(col26)
        self.treeviewVeiculo.append_column(col27)
        self.treeviewVeiculo.append_column(col28)
        self.treeviewVeiculo.append_column(col29)
        self.treeViewValorVeiculo()

    def treeViewValorVeiculo(self):

        #Valor do Veiculo
        self.model = gtk.ListStore(str,str)
        self.treeviewValor.set_model(self.model)
        #muda a cor da celula  e torna o campo editavel 
        renderer1 = gtk.CellRendererText()        
        renderer1.set_property("background", "red") # Cor do foreground como propriedade
        renderer1.set_property("foreground", "black") # Cor do foreground como propriedade
        
        renderer2 = gtk.CellRendererText()   
        renderer2.set_property("background", "black") # Cor do foreground como propriedade
        renderer2.set_property("foreground", "white") # Cor do foreground como propriedade    
        
        col0 = gtk.TreeViewColumn('Valor Sugerido da Venda do Veiculo',renderer2 , text=0)
        col1 = gtk.TreeViewColumn('Porcentagem de Lucro da Agencia', gtk.CellRendererText() , text=1)
        
#referente a configuracao da largura dos campos
        col0.set_min_width(30)
        col1.set_min_width(40)
               
        self.treeviewValor.append_column(col0)
        self.treeviewValor.append_column(col1)
        
    #=====================
    def on_combovenda_troca_changed(self,*args):
                
        combo_venda = self.combovenda_troca.get_active_text()
        print combo_venda
        
        if combo_venda != 'Troca':#se o combobox selecionado for diferente a troca ou seja se for igual a venda :
            #fechar a tela de escolha entre venda e troca
            self.cadastrar_venda_troca.hide()
            print '2'
            #Setando a variavel com o arquivo glade
            self.arquivoglade = "Projects\cadastrar_venda\cadastrar_venda.glade"
            #Extraindo conteudo XML do arquivo
            self.xml = gtk.glade.XML(self.arquivoglade)        
            #Componentes da Janela CadastrarCliente
            self.cadastrar_venda=self.xml.get_widget('cadastrar_venda')
            self.comboboxVendedor = self.xml.get_widget('comboboxVendedor')
            self.buttonSalvarVenda = self.xml.get_widget('buttonSalvarVenda')
            self.buttonFecharVenda = self.xml.get_widget('buttonFecharVenda')
            self.treeviewCliente =self.xml.get_widget('treeviewCliente')
            self.treeviewVeiculo=self.xml.get_widget('treeviewVeiculo')
            self.treeviewValor=self.xml.get_widget('treeviewValor')
            self.comboboxCliente = self.xml.get_widget('comboboxCliente')
            self.comboboxVeiculo = self.xml.get_widget('comboboxVeiculo')
            self.comboboxVendedor = self.xml.get_widget('comboboxVendedor')
            self.combobox1 = self.xml.get_widget('combobox1')
            
            self.comboboxFormaPagamento = self.xml.get_widget('comboboxFormaPagamento')
            self.comboboxFormaPagamento.set_active(0)     
            #coloca o foco no primeiro elemento
            self.combobox1.set_active(0)     

            #==================================================================
            #carrega o comboboxcliente com todos os clientes cadastrado no sistema 
            sql = "select nome from c "
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            #pega a consulta  e adiciona no combobox
            store = gtk.ListStore(str)
            
            for linha in resultado:
                print linha[0]
                store.append([linha[0]])
            
            # Celula texto para nossa Caixa de Selecao
            celula = gtk.CellRendererText()
            # Associa o ListStore a Caixa de Selecao
            self.comboboxCliente.set_model(store)
            
            # Associa a celula a caixa de selecao
            self.comboboxCliente.pack_start(celula, True)
            #chave primaria e mais a posicao que deseja colocar no combobox
            self.comboboxCliente.add_attribute(celula, 'text', 0)
            
    #=====================================================================        
            #carrega o comboboxvendedor com todos os vendedores cadastrados no sistema
            sql = "select nome from v "
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            #pega a consulta  e adiciona no combobox
            store = gtk.ListStore(str)
            
            for linha in resultado:
                print linha[0]
                store.append([linha[0]])

            # Celula texto para nossa Caixa de Selecao
            celula = gtk.CellRendererText()
            # Associa o ListStore a Caixa de Selecao
            self.comboboxVendedor.set_model(store)
            
            # Associa a celula a caixa de selecao
            self.comboboxVendedor.pack_start(celula, True)
            #chave primaria e mais a posicao que deseja colocar no combobox
            self.comboboxVendedor.add_attribute(celula, 'text', 0)
            
            #=====================================================================        
            #carrega o comboboxVeiculo com todos os veiculos cadastrado no sistema  fazendo aparecer 
            #somente as placas no combobox e aqueles que estiverem com disponibilidade igual a estoque
            sql = "select placa from desv where disponibilidade='Estoque'"
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            #pega a consulta  e adiciona no combobox
            store = gtk.ListStore(str)        
            for linha in resultado:
                print linha[0]
                store.append([linha[0]])

            # Celula texto para nossa Caixa de Selecao
            celula = gtk.CellRendererText()
            # Associa o ListStore a Caixa de Selecao
            self.comboboxVeiculo.set_model(store)
            
            # Associa a celula a caixa de selecao
            self.comboboxVeiculo.pack_start(celula, True)
            #chave primaria e mais a posicao que deseja colocar no combobox
            self.comboboxVeiculo.add_attribute(celula, 'text', 0)
                        
            self.cadastrar_venda.show_all()
            self.xml.signal_autoconnect(self)
            self.criartabela_venda()
            
        elif combo_venda=='Troca':
            #fechar a tela de decisao entre troca e venda
            self.cadastrar_venda_troca.hide()
            self.arquivoglade = "Projects\cadastrar_troca\cadastrar_troca.glade"
            print 'testando'
            #Extraindo conteudo XML do arquivo
            self.xml = gtk.glade.XML(self.arquivoglade)    
               
           #Componentes da Janela Cadastrar Troca de Veiculo
            self.cadastrar_troca=self.xml.get_widget('cadastrar_troca')
            self.treeviewCliente =self.xml.get_widget('treeviewCliente')
            self.treeviewVeiculo=self.xml.get_widget('treeviewVeiculo')
            self.treeviewValor=self.xml.get_widget('treeviewValor')
            self.comboboxCliente = self.xml.get_widget('comboboxCliente')
            self.comboboxVeiculo = self.xml.get_widget('comboboxVeiculo')
            self.comboboxVendedor = self.xml.get_widget('comboboxVendedor')
            self.entryPlaca=self.xml.get_widget('entryPlaca')
            self.entryModelo=self.xml.get_widget('entryModelo')
            self.entryMarca=self.xml.get_widget('entryMarca')
            self.entryAno=self.xml.get_widget('entryAno')
            self.entryProprietario=self.xml.get_widget('entryProprietario')
            self.entryValor=self.xml.get_widget('entryValor')
        
            #==================================================================
            #carrega o comboboxcliente com todos os clientes cadastrado no sistema
            
            sql = "select nome from c "
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            #pega a consulta  e adiciona no combobox
            store = gtk.ListStore(str)
            
            for linha in resultado:
                print linha[0]
                store.append([linha[0]])            
            
            # Celula texto para nossa Caixa de Selecao
            celula = gtk.CellRendererText()
            # Associa o ListStore a Caixa de Selecao
            self.comboboxCliente.set_model(store)
            
            # Associa a celula a caixa de selecao
            self.comboboxCliente.pack_start(celula, True)
            #chave primaria e mais a posicao que deseja colocar no combobox
            self.comboboxCliente.add_attribute(celula, 'text', 0)           
    
    #=====================================================================       
            #carrega o comboboxvendedor com todos os vendedores cadastrado no sistema 
            sql = "select nome from v "
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            #pega a consulta  e adiciona no combobox
            store = gtk.ListStore(str)
            
            for linha in resultado:
                print linha[0]
                store.append([linha[0]])            
            # Celula texto para nossa Caixa de Selecao
            celula = gtk.CellRendererText()
            # Associa o ListStore a Caixa de Selecao
            self.comboboxVendedor.set_model(store)
            
            # Associa a celula a caixa de selecao
            self.comboboxVendedor.pack_start(celula, True)
            #chave primaria e mais a posicao que deseja colocar no combobox
            self.comboboxVendedor.add_attribute(celula, 'text', 0)
            
            #=====================================================================       
             #carrega o comboboxVeiculo com todos os veiculos cadastrado no sistema  fazendo aparecer 
            #somente as placas no combobox e aqueles que estiverem com disponibilidade igual a estoque

            sql = "select placa from desv where disponibilidade='Estoque'"
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            #pega a consulta  e adiciona no combobox
            store = gtk.ListStore(str)        
            for linha in resultado:
                print linha[0]
                store.append([linha[0]])
    
            # Celula texto para nossa Caixa de Selecao
            celula = gtk.CellRendererText()
            # Associa o ListStore a Caixa de Selecao
            self.comboboxVeiculo.set_model(store)
            
            # Associa a celula a caixa de selecao
            self.comboboxVeiculo.pack_start(celula, True)
            #chave primaria e mais a posicao que deseja colocar no combobox
            self.comboboxVeiculo.add_attribute(celula, 'text', 0)
            
            self.xml.signal_autoconnect(self)
            self.criartabela_troca()
            #gtk.main()
            
    def criartabela_troca(self):
        if not os.path.exists('agenciaBeta1.db'):
                    print 'Banco de Dados existente troca'
            
                    conexao = MySQLdb.connect(self.host,self.user,self.passwd,self.database )
                    print 'Banco de Dados ja instalado troca'
          #trocar aqui na linha de baixo o db
                    conexao = MySQLdb.connect(host="localhost", user="root",passwd="carros", db="agenciaBeta1")
                    cursor = conexao.cursor()
                    
                    sqlt = """create table trocae(
                              codigotroca int(10) PRIMARY kEY Auto_increment NOT NULL UNIQUE,
                              codigocliente  varchar(60)       NOT NULL  ,
                              codigoveiculo  varchar(10)       NOT NULL  ,
                              codigovendedor varchar(60)       NOT NULL  , 
                              placa varchar(10)       NOT NULL  ,         
                              modelo varchar(60)       NOT NULL  ,
                              marca varchar(60)       NOT NULL  ,
                              ano varchar(60)       NOT NULL  ,
                              proprietario varchar(60)       NOT NULL  ,
                              valor float(10) ,
                              data varchar(20))"""
                    try:
                    #verifica se o database nomeado acima ja foi criado 
                            print '    uuuu    troca'      
                        
                            cursor.execute(sqlt)
                            conexao.commit()
                            print 'trocado'
                    except MySQLdb.Error, e:
                    
                       if e.args[0] == 1150:                     
                         print  'Tratando o erro'
                    self.addTreeViewCliente() 
    #cria a tabela da venda
    def criartabela_venda(self):       
        
        if  not os.path.exists('agenciaBeta1.db'):
                    print 'Banco de Dados existente'
            
                    conexao = MySQLdb.connect(self.host,self.user,self.passwd,self.database )
                    print 'Banco de Dados ja instalado'
                    conexao = MySQLdb.connect(host="localhost", user="root",passwd="carros", db="agenciaBeta1")
                    cursor = conexao.cursor()
                    
                    sql = """create table venven(
                             codigovenda int(10) PRIMARY kEY Auto_increment NOT NULL UNIQUE,
                             codigo  varchar(60)       NOT NULL  ,
                             codigoveiculo  varchar(10)  NOT NULL  ,
                             codigovendedor varchar(60) NOT NULL  ,
                             formadepagamento varchar(50) not null,
                             financeira varchar(50)not null,
                             data varchar(20))"""
                    
                    print'l'
                    try:
                     
                            print ' testando 1'      
                            cursor.execute(sql)
                            conexao.commit()
                            
                            print 'testando 2'
                    except MySQLdb.Error, e:
                    
                       if e.args[0] == 1050:                     
                         print  'Tratando o erro'
                    self.addTreeViewCliente() 
                    
    #carrega o  combo vendedor com os vendedores cadastrados
    def on_comboboxVendedor_changed(self,*args):
        combov = self.comboboxVendedor.get_active_text()
        sql = "select * from v "
        self.cursor.execute(sql)
        self.cursor.fetchall()
        
        #referente a seleção da forma de pagamento, se a seleção for financiamento o combobox1
        #ao lado será preenchido com o nome das financeiras cadastrada no sistema.
    def on_comboboxFormaPagamento_changed(self,*args):
        combov = self.comboboxFormaPagamento.get_active_text()
        if combov=="Financiamento":
            print 'testando1'
            sql = "select nome from cf "
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            #pega a consulta  e adiciona no combobox
            store = gtk.ListStore(str)
            
            for linha in resultado:
                print linha[0]
                store.append([linha[0]])            
            # Celula texto para nossa Caixa de Selecaoe
            celula = gtk.CellRendererText()
            # Associa o ListStore a Caixa de Selecao
            self.combobox1.set_model(store)
            
            # Associa a celula a caixa de selecao
            self.combobox1.pack_start(celula, True)
            #chave primaria e mais a posicao que deseja colocar no combobox
            self.combobox1.add_attribute(celula, 'text', 0) 
        
        #gtk.main()
        
     #este def tem a funcao de pegar o dados que foi selecionado no combobox o combobox do veiculo com apenas os veiculo cadastrado disponivel no estoque e os valores dos mesmos 
    def on_comboboxVeiculo_changed(self,*args):
        print 'teste1'
        #combov e responsavel por guardar o valor que foi selecionado no combobox 
        combov = self.comboboxVeiculo.get_active_text() 
        print combov
        #faz uma consulta na tabela desv onde a placa selecionada no combobox for igual a da tabela e adiciona na treewiev
        sql = "select * from desv where placa='%s' and disponibilidade='Estoque' "%(combov)
        model = self.treeviewVeiculo.get_model()
        model.clear()
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        for linha in resultado:
            model.append([linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[10], linha[11], linha[12], linha[13], linha[14], linha[15], linha[16], linha[17], linha[18], linha[19], linha[20], linha[21], linha[22], linha[23], linha[24], linha[25], linha[26], linha[27], linha[28], linha[29]])
         #faz uma consulta na tabela de valores disponibilizando apenas os campos porcentagem e valorcompraeiculo e adiciona na treewiev
        sql3 = "select porcentagemlucro,valorcompraveiculo from vv "
        
        model = self.treeviewValor.get_model()
        print model
        model.clear()
        self.cursor.execute(sql3)
        resultado = self.cursor.fetchall()
        for linha in resultado:
            model.append([linha[0],linha[1]])
                
    
        #gtk.main()
        # carrega todos os veiculos cadastrado no sistema.
    def on_comboboxCliente_changed(self,*args):
        print 'teste2'
        comboc = self.comboboxCliente.get_active_text()
        print comboc
        sql = "select * from c where nome='%s'"% (comboc)
        model = self.treeviewCliente.get_model()
        model.clear()
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        for linha in resultado:
            model.append([linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[10], linha[11], linha[12], linha[13], linha[14], linha[15], linha[16], linha[17], linha[18], linha[19], linha[20], linha[21], linha[22], linha[23], linha[24],linha[25]])       

        #gtk.main()
    
    # referente ao salvar da tela venda
    def on_buttonSalvarVenda_clicked (self,widget):
        print'buttonSalvar'
        #verifica se o combobox nao esta vazio
        print self.comboboxCliente.get_active_text()
        if ((self.comboboxCliente.get_active_text() == None) or (self.comboboxVeiculo.get_active_text()== None) or (self.comboboxVendedor.get_active_text()== None)or (self.combobox1.get_active_text()== None)):
        
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Por favor preencha todos os campos')
            resposta=msg.run()
            msg.destroy()
            
        else:
            
            #model = self.treev.get_model()
            cliente = self.comboboxCliente.get_active_text()
            print cliente
            veiculo = self.comboboxVeiculo.get_active_text()
            print veiculo
            vendedor = self.comboboxVendedor.get_active_text()
            print vendedor
            formadepagamento=self.comboboxFormaPagamento.get_active_text()
            print formadepagamento
            financeira=self.combobox1.get_active_text()
            data1 = datetime.datetime.now().date().isoformat()
            data=  '/'.join(data1.split('-')[::-1])
            
            sql = "insert into venven(codigo,codigoveiculo,codigovendedor,formadepagamento,financeira,data) values('" + cliente + "','" + veiculo + "','" + vendedor + "', '" + formadepagamento  + "','" + financeira + "','" + data + "' )"
            self.conexao=MySQLdb.connect(self.host,self.user,self.passwd,self.database)
            self.cursor = self.conexao.cursor()
            self.cursor.execute(sql)
            self.conexao.commit()
            # faz a atualizacao no estoque do veiculo que foi comprado. 
            sql2=('''update desv set disponibilidade='Vendido' where placa='%s' ''')%(veiculo) 
            self.cursor.execute(sql2)
            self.conexao.commit()   
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Cadastrado Com Sucesso')
            msg.run()
            msg.destroy()
            self.cadastrar_venda.hide()
        #gtk.main()
        
    # referente ao salvar da tela venda
    def on_buttonSalvarTroca_clicked (self,widget):
        print'buttonSalvar'
        #verifica se o combobox nao esta vazio caso esteja informa uma mensagem na caixa de dialogo
        print self.comboboxCliente.get_active_text()
        if ((self.comboboxCliente.get_active_text() == None) or (self.comboboxVeiculo.get_active_text()== None) or (self.comboboxVendedor.get_active_text()== None)):
        
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Por favor preencha todos os campos')
            resposta=msg.run()
            msg.destroy()
            
        else:
            
            # pega os dados selecionados e guarda na variavel para inserir no banco
            cliente = self.comboboxCliente.get_active_text()
            print cliente
            veiculo = self.comboboxVeiculo.get_active_text()
            print veiculo
            vendedor = self.comboboxVendedor.get_active_text()
            print vendedor
            placa=self.entryPlaca.props.text
            modelo=self.entryModelo.props.text
            marca=self.entryMarca.props.text
            ano=self.entryAno.props.text
            proprietario=self.entryProprietario.props.text
            valor=self.entryValor.props.text

            data1 = datetime.datetime.now().date().isoformat()
            data=  '/'.join(data1.split('-')[::-1])
            #referente aos campos que foram criado na tabela troca  e o value e referente as variavel que  guardam os valores.
            sql = "insert into trocae(codigocliente,codigoveiculo,codigovendedor,placa,modelo,marca,ano,proprietario,valor,data) values('" + cliente + "','" + veiculo + "','" + vendedor + "', '" + placa  + "', '" + modelo  + "', '" + marca  + "', '" + ano  + "', '" + proprietario  + "', '" + valor + "','" + data + "' )"
            #conecta o banco com o mysql
            self.conexao=MySQLdb.connect(self.host,self.user,self.passwd,self.database)
            
            self.cursor = self.conexao.cursor()
            
            self.cursor.execute(sql)
            
            self.conexao.commit()
            
            # faz a atualizacao no estoque do veiculo que foi comprado. 
            sql2=('''update desv set disponibilidade='Trocado' where placa='%s' ''')%(veiculo) 
            self.cursor.execute(sql2)
            self.conexao.commit()   
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Cadastrado Com Sucesso')
            msg.run()
            msg.destroy()
            #fecha a tela depois do cadastro da troca.
            self.cadastrar_troca.hide()
            #abre a classe cadastrar Veículo
            cadasv=CadastrarVeiculo()
        
        #gtk.main()
        
    def on_buttonFecharTroca_clicked (self,widget):
        print 'buttonFechar1'
        self.cadastrar_troca.hide()
        gtk.main_quit()
        
    def on_cadastrar_venda_troca_destroy (self,widget):
        print'ol'
        gtk.main_quit()
        
    def on_buttonFecharVenda_clicked (self,widget):
        print 'buttonFechar2'
        self.cadastrar_venda.hide()
        gtk.main_quit()
        
    def on_cadastrar_venda_destroy(self,widget):
        gtk.main_quit()
        
if __name__ == '__main__':

    cv = CadastrarVenda()


        