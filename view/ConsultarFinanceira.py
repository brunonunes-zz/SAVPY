# -*- coding: utf-8 -*-
'''
Created on 19/08/2009

@author: Gustavo
'''

import sys
try:

    import pygtk
    pygtk.require('2.0')
    import gtk
    import gtk.glade
    import MySQLdb
except:
    print ' Erro Ao Carregar um dos Import'
    sys.exit(1)

class ConsultarFinanceira(object):
    def __init__(self):
        self.host= "localhost"
        self.user= "root"
        self.passwd= "carros"
        self.database = "agenciaBeta1"
        #Setando a variavel com o arquivo glade
        self.arquivoglade = "Projects\consultar_financeira\consultar_financeira.glade"
        #Extraindo conteudo XML do arquivo
        self.xml = gtk.glade.XML(self.arquivoglade)        
        #Componentes da Janela ConsultarCliente
        self.consultar_financeira=self.xml.get_widget('consultar_financeira')
        self.buttonPesquisar= self.xml.get_widget('buttonPesquisar')
        self.entryFinanceira= self.xml.get_widget('entryFinanceira')
        self.buttonExcluir= self.xml.get_widget('buttonExcluir')
        self.buttonFechar=self.xml.get_widget('buttonFechar')
        self.buttonEditar=self.xml.get_widget('buttonEditar')
        self.treeviewConsultarFinanceira =self.xml.get_widget('treeviewConsultarFinanceira')
        
        #self.buttonPesquisar.connect('clicked',self.on_buttonPesquisar_clicked)
        #self.buttonExcluir.connect('clicked',self.on_buttonExcluir_clicked)
        #self.buttonFechar.connect('clicked',self.on_buttonFechar_clicked)
        #self.buttonEditar.connect('clicked',self.on_buttonEditar_clicked)
        #==========================================================
        # Comboxbox
        self.comboboxFinanceira = self.xml.get_widget('comboboxFinanceira')
        
        # Preparar a Caixa Comboxbox para selecao
        
        # Componente ListStore para armazenar as retas
        store = gtk.ListStore(str)
        store.append(["Todos"])
        store.append(["Nome"])

        # Celula texto para nossa Caixa de Selecao
        celula = gtk.CellRendererText()
        # Associa o ListStore a Caixa de Selecao
        self.comboboxFinanceira.set_model(store)
        # Associa a celula a caixa de selecao
        self.comboboxFinanceira.pack_start(celula, True)
        self.comboboxFinanceira.add_attribute(celula, 'text', 0)
        
        # Coloca o foco no -Selecionar-
        self.comboboxFinanceira.set_active(0)
#=====================================================================
        #Conectando no banco
        self.conexao = MySQLdb.connect(host="localhost", user="root",passwd="carros", db="agenciaBeta1")
        self.cursor = self.conexao.cursor()
        self.addTreeView()
         # Autoconnect Signals and Callbacks
        self.xml.signal_autoconnect(self)
        #mostra tudo que esta dentro da consultar cliente
        self.consultar_financeira.show_all() 
        gtk.main()   
        
        
    def addTreeView(self):
        #Instancia o treeview coloca os descreve as colunas e as propriedades 
        self.model = gtk.ListStore(str,str,str,str,str,str,str,str,str,str,str)
        self.treeviewConsultarFinanceira.set_model(self.model)
        #muda a cor da celula  e torna o campo editavel 
        renderer1 = gtk.CellRendererText()        
        renderer1.set_property("background", "gray") # Cor do foreground como propriedade
        renderer1.set_property("foreground", "black") # Cor do foreground como propriedade
                
        col0 = gtk.TreeViewColumn('Codigo', renderer1, text=0)
        col1 = gtk.TreeViewColumn('Nome',gtk.CellRendererText() , text=1)
        col2 = gtk.TreeViewColumn('Local',renderer1, text=2)
        col3 = gtk.TreeViewColumn('Cidade',gtk.CellRendererText(), text=3)
        col4 = gtk.TreeViewColumn('CEP', renderer1, text=4)
        col5 = gtk.TreeViewColumn('CNPJ',gtk.CellRendererText(), text=5)
        col6 = gtk.TreeViewColumn('Telefone', renderer1, text=6)
        col7 = gtk.TreeViewColumn('Telefone',gtk.CellRendererText() , text=7)
        col8 = gtk.TreeViewColumn('Celular', renderer1, text=8)
        col9 = gtk.TreeViewColumn('Email', gtk.CellRendererText(), text=9)
        col10 = gtk.TreeViewColumn('Data', renderer1, text=10)  
  
        
        #referente a configuracao de cores da treeviewe
        col0.set_min_width(30)
        col1.set_min_width(150)
        col2.set_min_width(124)
        col3.set_min_width(123)
        #col4.set_min_width(124)
        self.treeviewConsultarFinanceira.append_column(col0)
        self.treeviewConsultarFinanceira.append_column(col1)
        self.treeviewConsultarFinanceira.append_column(col2)
        self.treeviewConsultarFinanceira.append_column(col3)
        self.treeviewConsultarFinanceira.append_column(col4)
        self.treeviewConsultarFinanceira.append_column(col5)
        self.treeviewConsultarFinanceira.append_column(col6)
        self.treeviewConsultarFinanceira.append_column(col7)
        self.treeviewConsultarFinanceira.append_column(col8)
        self.treeviewConsultarFinanceira.append_column(col9)
        self.treeviewConsultarFinanceira.append_column(col10)
        
        self.leBanco()
        
        # metodo que  ler o banco de dados e adiciona no trewview 
    def leBanco(self):
        sql = "select * from cf "
        model = self.treeviewConsultarFinanceira.get_model()
        model.clear()
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        for linha in resultado:
            model.append([linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9],linha[10]])
    
    
    #funcao para pegar a selecao do cursor para a exclusao
    def pegaSelecaoTreev(self):
                valor = self.treeviewConsultarFinanceira.get_cursor()
                n = valor[0]
                if n == None:
                        msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Nenhum registro selecionado para Baixa')
                        msg.run()
                        msg.destroy()
                        return None
                else:
                        registro = self.treeviewConsultarFinanceira.get_selection()
                        registro.set_mode(gtk.SELECTION_MULTIPLE)
                        #" Pegando a linha selecionada "
                        modelo, caminhos = registro.get_selected_rows()
                        for caminho in caminhos:
                                kiter = modelo.get_iter(caminho)
                                codigo = modelo.get_value(kiter, 7)
                        return codigo           
                    
                    
    def on_buttonPesquisar_clicked (self,widget):
        print'buttonPesquisar'
        self.combo = self.comboboxFinanceira.get_active_text()

        if self.combo=='Todos':
             #desabilitar a caixa de texto
            sql = "select * from cf "
            model = self.treeviewConsultarFinanceira.get_model()
            model.clear()
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            for linha in resultado:
                model.append([linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9],linha[10]])
        
        elif self.combo=='Nome':
                   
            nome = self.entryFinanceira.props.text
            sql = "select * from cf where nome='%s' " %(nome)
            model = self.treeviewConsultarFinanceira.get_model()
            model.clear()
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            for linha in resultado:
                model.append([linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9],linha[10]])
        
        #gtk.main()
        
        
    def on_buttonEditar_clicked (self,widget):
        print'ButtonEditar'
        #fechar a tela consultar financeira 
        
        valor = self.treeviewConsultarFinanceira.get_cursor()
        
        
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
            self.arquivoglade = "Projects\update_cadastrar_financeira\update_cadastrar_financeira.glade"
            #Extraindo conteudo XML do arquivo
            self.xml = gtk.glade.XML(self.arquivoglade) 
            #instanciano as caixas de texto
            self.update_cadastrar_financeira=self.xml.get_widget('update_cadastrar_financeira')
    
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
            #deixa a caixa de texto desativado
            self.entryCodigo.set_editable(False)

            self.xml.signal_autoconnect(self)
            
            #self.update_cadastrar_financeira.show_all() 
            print'gu'
            
            self.valor = self.treeviewConsultarFinanceira.get_selection()
            self.valor.set_mode(gtk.SELECTION_MULTIPLE)
            " Pegando a linha selecionada "
            modelo, caminhos = self.valor.get_selected_rows()
            print modelo 
            print caminhos
            for caminho in caminhos:
                    kiter = modelo.get_iter(caminho)
                    self.co= modelo.get_value(kiter, 0)
                    n = modelo.get_value(kiter, 1)
                    l = modelo.get_value(kiter, 2)
                    ci = modelo.get_value(kiter, 3)
                    ce = modelo.get_value(kiter, 4)
                    cn = modelo.get_value(kiter, 5)
                    t1 = modelo.get_value(kiter, 6)
                    t2 = modelo.get_value(kiter, 7)
                    cel = modelo.get_value(kiter, 8)
                    e= modelo.get_value(kiter, 9)
                    
                    
                    self.entryCodigo.props.text=self.co
                    self.entryNome.props.text=n
                    self.entryLocal.props.text=l
                    self.entryCidade.props.text=ci
                    self.entryCep.props.text=ce
                    self.entryCnpj.props.text=cn
                    self.entryTelefone1.props.text=t1
                    self.entryTelefone2.props.text=t2
                    self.entryCelular.props.text=cel
                    self.entryEmail.props.text=e
                    #fecha a tela consultar financeira 
                    #self.consultar_financeira.hide()

        #gtk.main()
        
    #correspondente a tela update cadastrar financeira
    def on_buttonAtualizar_clicked (self,widget):
        print'Atualizar'
        if (self.entryNome.props.text == "" ):
        
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Por favor preencha todos os campos')
            resposta=msg.run()
            msg.destroy()
            
        else:
            codigo=self.entryCodigo.props.text
            #codigo=self.entryCodigo.props.text
            nome = self.entryNome.props.text
            local= self.entryLocal.props.text
            cidade= self.entryCidade.props.text
            cep= self.entryCep.props.text
            cnpj=self.entryCnpj.props.text
            telefone1=self.entryTelefone1.props.text
            telefone2=self.entryTelefone2.props.text
            celular=self.entryCelular.props.text
            email=self.entryEmail.props.text
    
        
                #entryFinanceira referente a caixa de texto da tela consultar vendedor
            if self.entryFinanceira.props.text=='':
                print 'testa nome'
                sql = "select * from cf"
                self.cursor.execute(sql)
                resultado = self.cursor.fetchall()
                i = 0
                t1 = range(1)
                for linha in resultado:
                    
                        t1[0] = i# -1  0 1 2
                        t2 = self.n1 #Esse self.n1 contem ovalor do cursor quando eu clico na linha para editar.
                        print'================'
                        print linha[0]#1 2
                                          
                        if t1[0] == t2[0]:
                            print 'otaio'
                            #gravando dados no Banco
                            #sql3 = "insert into vv(1placav,renavamv,documento,motor,freio,cambio,funilaria,multas,outros,valorcompraveiculo,totalgastos,porcentagemlucro,valorsugeridovenda) values('" + placav + "','" + renavamv + "',%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f)"%(documento,motor,freio,cambio,funilaria,multas,outros,valorcompraveiculo,totalgastos,porcentagemlucro,valorsugeridovenda)
                            sql=('''update cf set nome='%s',local='%s',cidade='%s',cep='%s',cnpj='%s',telefone1='%s',telefone2='%s',celular='%s',email='%s' where codigofinanceira=%i '''%(nome,local,cidade,cep,cnpj,telefone1,telefone2,celular,email,linha[0]))
                            self.cursor.execute(sql)
                            self.conexao.commit()
                            self.leBanco()
                        i=i+1
                        #fecha a tela de update .
                self.update_cadastrar_financeira.hide()
                msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Atualizado Com Sucesso')
                msg.run()
                msg.destroy()
                #entryFinanceira referente a caixa de texto da tela consultar vendedor
            elif    self.entryFinanceira.props.text!='':
                print 'diferente'
                sql = "select * from cf"
                self.cursor.execute(sql)
                resultado = self.cursor.fetchall()
                i =1
                t1 = range(1)
            
            
            
                    
            
                for linha in resultado:
                        
                        
                        t1[0] = i# -1  0 1 2
                        t2 = int(self.co) #o valor vinha em sring e transformei em inteiro
                        print t2
                                                                  
                        if t2 ==linha[0]:
                            
                            print 'otaio'
                            #gravando dados no Banco
                            #sql3 = "insert into vv(1placav,renavamv,documento,motor,freio,cambio,funilaria,multas,outros,valorcompraveiculo,totalgastos,porcentagemlucro,valorsugeridovenda) values('" + placav + "','" + renavamv + "',%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f)"%(documento,motor,freio,cambio,funilaria,multas,outros,valorcompraveiculo,totalgastos,porcentagemlucro,valorsugeridovenda)
                            sql=('''update cf set nome='%s',local='%s',cidade='%s',cep='%s',cnpj='%s',telefone1='%s',telefone2='%s',celular='%s',email='%s' where codigofinanceira=%i '''%(nome,local,cidade,cep,cnpj,telefone1,telefone2,celular,email,linha[0]))
                            self.cursor.execute(sql)
                            self.conexao.commit()
                            self.leBanco()
                        #i=i+1
                        #fecha a tela de update .
                self.update_cadastrar_financeira.hide()
                msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Atualizado Com Sucesso')
                msg.run()
                msg.destroy()
    
    
        #gtk.main()
        
        
    def on_buttonExcluir_clicked (self,widget):
        print'buttonExcluir'
        #self.consultar_cliente.hide()
        #cadasc=CadastrarCliente()
        valor = self.treeviewConsultarFinanceira.get_cursor()
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
                if  self.entryFinanceira.props.text=='':
                    valor = self.treeviewConsultarFinanceira.get_cursor()
                    n = valor[0]
                    sql = "select * from cf"
                    self.cursor.execute(sql)
                    resultado = self.cursor.fetchall()
                    i = 0
                    t1 = range(1)
                    for linha in resultado:
                        t1[0] = i
                        t2 = n
                        if t1[0] == t2[0]:
                            sql = "DELETE FROM cf WHERE codigofinanceira = %i" % (linha[0])
                            self.cursor.execute(sql)
                            self.conexao.commit()
                        i = i+1
                    self.leBanco()
                    msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Deletado com Sucesso!')
                    msg.run()
                    msg.destroy()
                    
                elif self.entryFinanceira.props.text!='':
                
                        self.valor = self.treeviewConsultarFinanceira.get_selection()
    
                        self.valor.set_mode(gtk.SELECTION_MULTIPLE)
                        " Pegando a linha selecionada "
                        modelo, caminhos = self.valor.get_selected_rows()
                        print modelo 
                        print caminhos
                        for caminho in caminhos:
                                kiter = modelo.get_iter(caminho)
                                #coloquei o self para poer pegar esse valor em outro lugar
                                self.codigofinanceira = modelo.get_value(kiter, 0)
                                
                        print self.codigofinanceira
                        sql = "select * from cf"
                        self.cursor.execute(sql)
                        resultado = self.cursor.fetchall()
                                           
                        for linha in resultado:
                                
                            
                                t1 = int(self.codigofinanceira)#transformei em inteiro para fazer a comparacao com o linha[0]que vinha em inteiro
                                print 'gugu'
                                print self.codigofinanceira  
                                print linha[0]                                    
                                if t1 == linha[0]:
                                    sql = "DELETE FROM cf WHERE codigofinanceira = %i" % (linha[0])
                                    self.cursor.execute(sql)
                                    self.conexao.commit()
                                    self.leBanco()
                msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Deletado com Sucesso!')
                msg.run()
                msg.destroy()
        #gtk.main()
        
        #correspondente  a tela consultar financeira
    def on_buttonFechar_clicked (self,widget):
        print'buttonFechar'
        self.consultar_financeira.hide()
        gtk.main_quit()
        
    #correspondente a tela update cadastrar financeira
    def on_buttonSair_clicked (self,widget):
        print'buttonSair'
        self.update_cadastrar_financeira.hide()
    
    def on_consultar_financeira_destroy(self,widget):
        print 'k'
        gtk.main_quit()
        
    #def on_update_cadastrar_financeira_destroy (self,widget):
     #   gtk.main_quit()
    
    
        
           
   
if __name__ == '__main__':

    consultaf = ConsultarFinanceira()

    
