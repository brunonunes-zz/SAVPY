# -*- coding: utf-8 -*-
'''
Created on 17/08/2009

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
    print ' Erro Ao Carregar um dos Import98'
    sys.exit(1)

class ConsultarVendedor(object):
    def __init__(self):
        self.host= "localhost"
        self.user= "root"
        self.passwd= "carros"
        self.database = "agenciaBeta1"
        #Setando a variavel com o arquivo glade
        self.arquivoglade = "Projects\consultar_vendedor\consultar_vendedor.glade"
        #Extraindo conteudo XML do arquivo
        self.xml = gtk.glade.XML(self.arquivoglade)        
        #Componentes da Janela ConsultarCliente
        self.consultar_vendedor=self.xml.get_widget('consultar_vendedor')
        self.buttonPesquisar= self.xml.get_widget('buttonPesquisar')
        self.entryPesquisarVendedor= self.xml.get_widget('entryPesquisarVendedor')

        self.buttonExcluir= self.xml.get_widget('buttonExcluir')
        self.buttonFechar=self.xml.get_widget('buttonFechar')
        self.buttonEditar=self.xml.get_widget('buttonEditar')

        self.treeviewConsultarVendedor =self.xml.get_widget('treeviewConsultarVendedor')

        
      
        #Tela Principal
       # self.cliente.connect('destroy', gtk.main_quit)
        #Tela Clente
        #self.buttonPesquisar.connect('clicked',self.on_buttonPesquisar_clicked)
        #self.buttonExcluir.connect('clicked',self.on_buttonExcluir_clicked)
        #self.buttonFechar.connect('clicked',self.on_buttonFechar_clicked)
        #self.buttonEditar.connect('clicked',self.on_buttonEditar_clicked)
        #==========================================================
        # Comboxbox
        self.comboboxVendedor = self.xml.get_widget('comboboxVendedor')
        
        # Preparar a Caixa Comboxbox para selecao
        
        # Componente ListStore para armazenar as retas
        store = gtk.ListStore(str)
        store.append(["Todos"])
        store.append(["Setor"])
        store.append(["Nome"])
        

    
         

        # Celula texto para nossa Caixa de Selecao
        celula = gtk.CellRendererText()
        # Associa o ListStore a Caixa de Selecao
        self.comboboxVendedor.set_model(store)
        # Associa a celula a caixa de selecao
        self.comboboxVendedor.pack_start(celula, True)
        self.comboboxVendedor.add_attribute(celula, 'text', 0)
        
        # Coloca o foco no -Selecionar-
        self.comboboxVendedor.set_active(0)
#=====================================================================
        #Conectando no banco
        self.conexao = MySQLdb.connect(host="localhost", user="root",passwd="carros", db="agenciaBeta1")
        self.cursor = self.conexao.cursor()
        self.addTreeView()
         # Autoconnect Signals and Callbacks

        self.xml.signal_autoconnect(self)
        #mostra tudo que esta dentro da consultar cliente
        #colocar depois
        self.consultar_vendedor.show_all() 
        gtk.main()   
        
        
    def addTreeView(self):
        
        #Instancia o treeview coloca os descreve as colunas e as propriedades 
        self.model = gtk.ListStore(str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str)
        self.treeviewConsultarVendedor.set_model(self.model)
        #muda a cor da celula  e torna o campo editavel 
        renderer1 = gtk.CellRendererText()        
        renderer1.set_property("background", "gray") # Cor do foreground como propriedade
        renderer1.set_property("foreground", "black") # Cor do foreground como propriedade
       

        
        col0 = gtk.TreeViewColumn('Codigo', renderer1, text=0)
        col1 = gtk.TreeViewColumn('Setor',gtk.CellRendererText(), text=1)
        col2 = gtk.TreeViewColumn('Nome', renderer1, text=2)
        col3 = gtk.TreeViewColumn('Estado Civil', gtk.CellRendererText(), text=3)
        col4 = gtk.TreeViewColumn('Endereco', renderer1, text=4)
        col5 = gtk.TreeViewColumn('Numero', gtk.CellRendererText(), text=5)
        col6 = gtk.TreeViewColumn('Bairro', renderer1, text=6)
        col7 = gtk.TreeViewColumn('Cidade', gtk.CellRendererText(), text=7)
        col8 = gtk.TreeViewColumn('Cep', renderer1, text=8)
        col9 = gtk.TreeViewColumn('UF', gtk.CellRendererText(), text=9)
        col10 = gtk.TreeViewColumn('Email',renderer1, text=10)
        col11 = gtk.TreeViewColumn('Data Nascimento', gtk.CellRendererText(), text=11)
        col12 = gtk.TreeViewColumn('CPF', renderer1, text=12)
        col13 = gtk.TreeViewColumn('RG', gtk.CellRendererText(), text=13)  
        col14 = gtk.TreeViewColumn('DDD_Residencial',renderer1, text=14)
        col15 = gtk.TreeViewColumn('Tel-Residencial', gtk.CellRendererText(), text=15)
        col16 = gtk.TreeViewColumn('DDD_Celular', renderer1, text=16)
        col17 = gtk.TreeViewColumn('Celular', gtk.CellRendererText(), text=17)
        col18 = gtk.TreeViewColumn('Data',renderer1, text=18)

        


        col0.set_min_width(30)
        col1.set_min_width(150)
        col2.set_min_width(124)
        col3.set_min_width(123)
        #col4.set_min_width(124)
        self.treeviewConsultarVendedor.append_column(col0)
        self.treeviewConsultarVendedor.append_column(col1)
        self.treeviewConsultarVendedor.append_column(col2)
        self.treeviewConsultarVendedor.append_column(col3)
        self.treeviewConsultarVendedor.append_column(col4)
        self.treeviewConsultarVendedor.append_column(col5)
        self.treeviewConsultarVendedor.append_column(col6)
        self.treeviewConsultarVendedor.append_column(col7)
        self.treeviewConsultarVendedor.append_column(col8)
        self.treeviewConsultarVendedor.append_column(col9)
        self.treeviewConsultarVendedor.append_column(col10)
        self.treeviewConsultarVendedor.append_column(col11)
        self.treeviewConsultarVendedor.append_column(col12)
        self.treeviewConsultarVendedor.append_column(col13)
        self.treeviewConsultarVendedor.append_column(col14)
        self.treeviewConsultarVendedor.append_column(col15)
        self.treeviewConsultarVendedor.append_column(col16)
        self.treeviewConsultarVendedor.append_column(col17)
        self.treeviewConsultarVendedor.append_column(col18)

        self.leBanco()
        # metodo que  ler o banco de dados e adiciona no trewview 
    def leBanco(self):
        sql = "select * from v "
        model = self.treeviewConsultarVendedor.get_model()
        model.clear()
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        for linha in resultado:
            model.append([linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[10], linha[11], linha[12], linha[13], linha[14], linha[15], linha[16], linha[17], linha[18]])
    
                    
    def on_buttonPesquisar_clicked (self,widget):
        print'buttonPesquisar'
        combo = self.comboboxVendedor.get_active_text()

        if combo=='Todos':
             #desabilitar a caixa de texto

            sql = "select * from v "
            model = self.treeviewConsultarVendedor.get_model()
            model.clear()
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            for linha in resultado:
                model.append([linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[10], linha[11], linha[12], linha[13], linha[14], linha[15], linha[16], linha[17], linha[18]])

        elif combo=='Setor':
                   
            setor = self.entryPesquisarVendedor.props.text
            sql = "select * from v where setor='%s' " %(setor)
            model = self.treeviewConsultarVendedor.get_model()
            model.clear()
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            for linha in resultado:
                model.append([linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[10], linha[11], linha[12], linha[13], linha[14], linha[15], linha[16], linha[17], linha[18]])
            

        elif combo=='Nome':
                   
            nome = self.entryPesquisarVendedor.props.text
            sql = "select * from v where nome='%s' " %(nome)
            model = self.treeviewConsultarVendedor.get_model()
            model.clear()
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            for linha in resultado:
                model.append([linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[10], linha[11], linha[12], linha[13], linha[14], linha[15], linha[16], linha[17], linha[18]])
            

        #gtk.main()
        
        
    def on_buttonEditar_clicked (self,widget):
        print'ButtonEditar'
        valor = self.treeviewConsultarVendedor.get_cursor()
        
        
        self.n1=valor[0] #guarda o valor do curso e eu pego esse valor no  metodo atualizar
        n = valor[0]
        print n
        if n == None:
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Nenhum registro selecionado para atualizacao')
            msg.set_position(gtk.WIN_POS_CENTER)
            msg.run()
            msg.destroy()
        else:
          
            #Setando a variavel com o arquivo glade
            self.arquivoglade = "Projects\update_cadastrar_vendedor\update_cadastrar_vendedor.glade"
            #Extraindo conteudo XML do arquivo
            self.xml = gtk.glade.XML(self.arquivoglade) 
           
            self.update_cadastrar_vendedor=self.xml.get_widget('update_cadastrar_vendedor')
    
            self.entryCodigo=self.xml.get_widget('entryCodigo')
            self.entrySetor=self.xml.get_widget('entrySetor')
            self.entryNome=self.xml.get_widget('entryNome')
            self.entryEndereco=self.xml.get_widget('entryEndereco')
            self.entryNumero=self.xml.get_widget('entryNumero')
            self.entryBairro=self.xml.get_widget('entryBairro')
            self.entryCidade=self.xml.get_widget('entryCidade')
            self.entryCep=self.xml.get_widget('entryCep')
            self.entryEmail=self.xml.get_widget('entryEmail')
            self.entryNascimento=self.xml.get_widget('entryNascimento')
            self.entryCpf=self.xml.get_widget('entryCpf')
            self.entryRg=self.xml.get_widget('entryRg')
            self.entryDddResidencial=self.xml.get_widget('entryDddResidencial')
            self.entryResidencial=self.xml.get_widget('entryResidencial')
            self.entryDddCelular=self.xml.get_widget('entryDddCelular')
            self.entryCelular=self.xml.get_widget('entryCelular')
            #deixa a caixa de texto do codigo desativado
            self.entryCodigo.set_editable(False)

            self.xml.signal_autoconnect(self)
            
             
            print'gu'
            
            self.valor = self.treeviewConsultarVendedor.get_selection()
            self.valor.set_mode(gtk.SELECTION_MULTIPLE)
            " Pegando a linha selecionada "
            modelo, caminhos = self.valor.get_selected_rows()
            print modelo 
            print caminhos
            for caminho in caminhos:
                    kiter = modelo.get_iter(caminho)
                    #coloquei o self para poer pegar esse valor em outro lugar
                    self.codigo = modelo.get_value(kiter, 0)
                    setor = modelo.get_value(kiter, 1)
                    nome = modelo.get_value(kiter, 2)
                    #deixei vago para pular o  valor do combobox e ntrar nos seus respectivos ugares
                    endereco = modelo.get_value(kiter, 4)
                    numero= modelo.get_value(kiter, 5)
                    bairro = modelo.get_value(kiter, 6)
                    cidade = modelo.get_value(kiter, 7)
                    cep = modelo.get_value(kiter, 8)
                    email = modelo.get_value(kiter, 10)
                    datanascimento = modelo.get_value(kiter, 11)
                    cpf = modelo.get_value(kiter, 12)
                    rg = modelo.get_value(kiter, 13)
                    dddresidencial = modelo.get_value(kiter, 14)
                    residencial = modelo.get_value(kiter, 15)
                    dddcelular = modelo.get_value(kiter, 16)
                    celular = modelo.get_value(kiter, 17)
                    
                    #coloca os dados referente a consulta dentro de seus respctivos lugares
                    self.entryCodigo.props.text= self.codigo
                    self.entrySetor.props.text= setor
                    self.entryNome.props.text= nome
                    self.entryEndereco.props.text= endereco
                    self.entryNumero.props.text= numero
                    self.entryBairro.props.text= bairro
                    self.entryCidade.props.text= cidade
                    self.entryCep.props.text= cep
                    self.entryEmail.props.text= email
                    self.entryNascimento.props.text= datanascimento
                    self.entryCpf.props.text= cpf
                    self.entryRg.props.text= rg
                    self.entryDddResidencial.props.text= dddresidencial
                    self.entryResidencial.props.text= residencial
                    self.entryDddCelular.props.text= dddcelular
                    self.entryCelular.props.text = celular

        #gtk.main()
        
    #correspondente a tela update cadastrar vendedor
    def on_buttonAtualizar_clicked (self,widget):
        print'Atualizar'
        # so cadastra se o nome da tela atualizar estiver preenchido
        if (self.entryNome.props.text == "" ):
        
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Por favor preencha todos os campos')
            resposta=msg.run()
            msg.destroy()
            
        else:
            codigo=self.entryCodigo.props.text
            setor = self.entrySetor.props.text
            nome = self.entryNome.props.text
            endereco= self.entryEndereco.props.text
            numero= self.entryNumero.props.text
            bairro= self.entryBairro.props.text
            cidade= self.entryCidade.props.text
            cep= self.entryCep.props.text
            email=self.entryEmail.props.text
            datanascimento= self.entryNascimento.props.text
            cpf= self.entryCpf.props.text
            rg=self.entryRg.props.text
            dddresidencial=self.entryDddResidencial.props.text
            residencial=self.entryResidencial.props.text
            dddcelular=self.entryDddCelular.props.text
            celular=self.entryCelular.props.text

    
        
            #entryPesquisarVendedor referente a caixa de texto da tela consultar vendedor
            if self.entryPesquisarVendedor.props.text=='':
                print 'testa nome'
                sql = "select * from v"
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
                            #sql3 = "insert into vv(1placav,renavamv,documento,motor,freio,cambio,funilaria,multas,outros,valorcompraveiculo,totalgastos,porcentagemlucro,valorsugeridovenda) values('" + placav + "','" + renavamv + "',%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f)"%(documento,motor,freio,cambio,funilaria,multas,outros,valorcompraveiculo,totalgastos,porcentagemlucro,valorsugeridovenda)
                            sql=('''update v set setor='%s',nome='%s',endereco='%s',numero='%s',bairro='%s',cidade='%s',cep='%s',email='%s',datanascimento='%s',cpf='%s',rg='%s',dddresidencial='%s',residencial='%s',dddcelular='%s',celular='%s' where codigovendedor=%i '''%(setor,nome,endereco,numero,bairro,cidade,cep,email,datanascimento,cpf,rg,dddresidencial,residencial,dddcelular,celular,linha[0]))
                            self.cursor.execute(sql)
                            self.conexao.commit()
                            self.leBanco()
                        i=i+1
                        #fecha a tela de update .
                self.update_cadastrar_vendedor.hide()
                msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Atualizado Com Sucesso')
                msg.run()
                msg.destroy()
            elif    self.entryPesquisarVendedor.props.text!='':
                print 'diferente'
                sql = "select * from v"
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
                            sql=('''update v set setor='%s',nome='%s',endereco='%s',numero='%s',bairro='%s',cidade='%s',cep='%s',email='%s',datanascimento='%s',cpf='%s',rg='%s',dddresidencial='%s',residencial='%s',dddcelular='%s',celular='%s' where codigovendedor=%i '''%(setor,nome,endereco,numero,bairro,cidade,cep,email,datanascimento,cpf,rg,dddresidencial,residencial,dddcelular,celular,linha[0]))
                            self.cursor.execute(sql)
                            self.conexao.commit()
                            self.leBanco()
                        #i=i+1
                        #fecha a tela de update .
                
                self.update_cadastrar_vendedor.hide()
                msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Atualizado Com Sucesso')
                msg.run()
                msg.destroy()
    
    
        gtk.main()
        
        

    def on_buttonExcluir_clicked (self,widget):
        print'buttonExcluir'
        
        valor = self.treeviewConsultarVendedor.get_cursor()
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
                if  self.entryPesquisarVendedor.props.text=='':
                    valor = self.treeviewConsultarVendedor.get_cursor()
                    n = valor[0]
                    sql = "select * from v"
                    self.cursor.execute(sql)
                    resultado = self.cursor.fetchall()
                    i = 0
                    t1 = range(1)
                    for linha in resultado:
                        t1[0] = i
                        t2 = n
                        if t1[0] == t2[0]:
                            sql = "DELETE FROM v WHERE codigovendedor = %i" % (linha[0])
                            self.cursor.execute(sql)
                            self.conexao.commit()
                        i = i+1
                    self.leBanco()
                    msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Deletado com Sucesso!')
                    msg.run()
                    msg.destroy()
                    
                elif self.entryPesquisarVendedor.props.text!='':
                
                        self.valor = self.treeviewConsultarVendedor.get_selection()
    
                        self.valor.set_mode(gtk.SELECTION_MULTIPLE)
                        " Pegando a linha selecionada "
                        modelo, caminhos = self.valor.get_selected_rows()
                        print modelo 
                        print caminhos
                        for caminho in caminhos:
                                kiter = modelo.get_iter(caminho)
                                #coloquei o self para poer pegar esse valor em outro lugar
                                self.codigovendedor = modelo.get_value(kiter, 0)
                                
                        print self.codigovendedor
                        sql = "select * from v"
                        self.cursor.execute(sql)
                        resultado = self.cursor.fetchall()
                                           
                        for linha in resultado:
                                
                            
                                t1 = int(self.codigovendedor)#transformei em inteiro para fazer a comparacao com o linha[0]que vinha em inteiro
                                print 'gugu'
                                print self.codigovendedor  
                                print linha[0]                                    
                                if t1 == linha[0]:
                                    sql = "DELETE FROM v WHERE codigovendedor = %i" % (linha[0])
                                    self.cursor.execute(sql)
                                    self.conexao.commit()
                                    self.leBanco()
                msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Deletado com Sucesso!')
                msg.run()
                msg.destroy()
        #gtk.main()
            
    def on_buttonFechar_clicked (self,widget):
        print'buttonFechar'
        self.consultar_vendedor.hide()
        gtk.main_quit()
    
    #correspondente a tela update cadastrar Vendedor
    def on_buttonSair_clicked (self,widget):
        print'buttonSair'
        self.update_cadastrar_vendedor.hide()
        #gtk.main_quit()
        
    def on_consultar_vendedor_destroy (self,widget):
        gtk.main_quit()
        
           
   
if __name__ == '__main__':

    consultav = ConsultarVendedor()
  
    
