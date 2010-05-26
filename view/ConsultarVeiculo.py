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
    

except:
    print ' Erro Ao Carregar um dos Import65'
    sys.exit(1)

class ConsultarVeiculo(object):
    def __init__(self):
        self.host= "localhost"
        self.user= "root"
        self.passwd= "carros"  #"aaasesaa"
        self.database = "agenciaBeta1" 
        #Setando a variavel com o arquivo glade
        self.arquivoglade = "Projects\consultar_veiculo2\consultar_veiculo2.glade"
        #Extraindo conteudo XML do arquivo
        self.xml = gtk.glade.XML(self.arquivoglade)        
       #Componentes da Janela ConsultarVeiculo
        self.consultar_veiculo=self.xml.get_widget('consultar_veiculo')
        #instanciando os botoes 
        self.buttonPesquisar= self.xml.get_widget('buttonPesquisar')
        self.buttonEditarDescricao=self.xml.get_widget('buttonEditarDescricao')
        self.buttonEditarDocumentacao=self.xml.get_widget('buttonEditarDocumentacao')
        self.buttonEditarValor=self.xml.get_widget('buttonEditarValor')
        self.buttonExcluir=self.xml.get_widget('buttonExcluir')
        self.buttonFechar=self.xml.get_widget('buttonFechar')
        self.buttonSairDocumentacao=self.xml.get_widget('buttonSairDocumentacao')
        self.buttonSairDescricao=self.xml.get_widget('buttonSairDescricao')
        self.buttonSairValor=self.xml.get_widget('buttonSairValor')

        
        #instanciando os treeview
        self.treeviewDescricao=self.xml.get_widget('treeviewDescricao')
        self.treeviewDocumentacao=self.xml.get_widget('treeviewDocumentacao')
        self.treeviewValor=self.xml.get_widget('treeviewValor')
        #instanciando as caixa de texto
        self.entryPesquisar=self.xml.get_widget('entryPesquisar')
        # Comboxbox
        self.comboboxDescricao = self.xml.get_widget('comboboxDescricao')
        # Coloca o foco no -Selecionar-
        self.comboboxDescricao.set_active(0)
        # rferente a ligacao do clique do botao com o metodo
        #self.buttonPesquisar.connect('clicked',self.on_buttonPesquisar_clicked)
        #self.buttonExcluir.connect('clicked',self.on_buttonExcluir_clicked)
        #self.buttonFechar.connect('clicked',self.on_buttonFechar_clicked)
        #self.buttonEditarValor.connect('clicked',self.on_buttonEditarValor_clicked)
        #self.buttonSairValor.connect('clicked',self.on_buttonSairValor_clicked)
        #self.buttonEditarDocumentacao.connect('clicked',self.on_buttonEditarDocumentacao_clicked)
        #self.buttonSairDocumentacao.connect('clicked',self.on_buttonSairDocumentacao_clicked)
        #self.buttonEditarDescricao.connect('clicked',self.on_buttonEditarDescricao_clicked)
        
        #Conectando no banco
        self.conexao = MySQLdb.connect(host="localhost", user="root",passwd="carros", db="agenciaBeta1")
        self.cursor = self.conexao.cursor()
        self.adicionartreeView()
              
       # Autoconnect Signals and Callbacks
        self.xml.signal_autoconnect(self)      
        #aparece tudo que esta na janela consultar veiculo
        self.consultar_veiculo.show_all() 
        gtk.main()
            
    #adiciona os campos nas treeviews da aba descricao,documentacao,valor 
    def adicionartreeView(self):
        #Descricao do Veiculo
        #Instancia o treeview coloca os descreve as colunas e as propriedades 
         #================================================================
        #Combobox    #
        
        #adicionando no treeview
        self.model = gtk.ListStore(str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str)
        self.treeviewDescricao.set_model(self.model)
        #muda a cor da celula  e torna o campo editavel 
        renderer1 = gtk.CellRendererText()        
        renderer1.set_property("background", "gray") # Cor do foreground como propriedade
        renderer1.set_property("foreground", "black") # Cor do foreground como propriedade
        renderer1.set_property('editable', True) # A primeira coluan e editavel
        
        #renderer2 = gtk.CellRendererText()        
        #renderer2.set_property("background", "green") # Cor do foreground como propriedade
        #renderer2.set_property("foreground", "black") # Cor do foreground como propriedade
        #renderer2.set_property('editable', True) # A primeira coluan e editavel

        
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
        col14 = gtk.TreeViewColumn('Pneu Dianteiro', renderer1, text=14)
        col15 = gtk.TreeViewColumn('Pneu Traseiro',gtk.CellRendererText(), text=15)
        col16 = gtk.TreeViewColumn('Estepe', renderer1, text=16)
        col17 = gtk.TreeViewColumn('Rodas', gtk.CellRendererText(), text=17)
        col18 = gtk.TreeViewColumn('Colisao', renderer1, text=18)
        col19 = gtk.TreeViewColumn('Suspensao', gtk.CellRendererText(), text=19)
        col20 = gtk.TreeViewColumn('Funilaria',renderer1, text=20)
        col21 = gtk.TreeViewColumn('Pintura', gtk.CellRendererText(), text=21)
        col22 = gtk.TreeViewColumn('Estofados', renderer1, text=22)
        col23 = gtk.TreeViewColumn('Motor', gtk.CellRendererText(), text=23)
        col24 = gtk.TreeViewColumn('Cambio',renderer1, text=24)
        col25 = gtk.TreeViewColumn('Amortecedor Dianteiro', gtk.CellRendererText(), text=25)
        col26 = gtk.TreeViewColumn('Amortecedor Traseiro', renderer1, text=26)
        col27 = gtk.TreeViewColumn('Anotacoes', gtk.CellRendererText(), text=27)
        col28 = gtk.TreeViewColumn('Disponibilidade Veiculo na Agencia',renderer1, text=28)
        col29 = gtk.TreeViewColumn('Data do Cadastro', gtk.CellRendererText(), text=29)

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
        #col4.set_min_width(124)
        
        self.treeviewDescricao.append_column(col0)
        self.treeviewDescricao.append_column(col1)
        self.treeviewDescricao.append_column(col2)
        self.treeviewDescricao.append_column(col3)
        self.treeviewDescricao.append_column(col4)
        self.treeviewDescricao.append_column(col5)
        self.treeviewDescricao.append_column(col6)
        self.treeviewDescricao.append_column(col7)
        self.treeviewDescricao.append_column(col8)
        self.treeviewDescricao.append_column(col9)
        self.treeviewDescricao.append_column(col10)
        self.treeviewDescricao.append_column(col11)
        self.treeviewDescricao.append_column(col12)
        self.treeviewDescricao.append_column(col13)
        self.treeviewDescricao.append_column(col14)
        self.treeviewDescricao.append_column(col15)
        self.treeviewDescricao.append_column(col16)
        self.treeviewDescricao.append_column(col17)
        self.treeviewDescricao.append_column(col18)
        self.treeviewDescricao.append_column(col19)
        self.treeviewDescricao.append_column(col20)
        self.treeviewDescricao.append_column(col21)
        self.treeviewDescricao.append_column(col22)
        self.treeviewDescricao.append_column(col23)
        self.treeviewDescricao.append_column(col24)
        self.treeviewDescricao.append_column(col25)
        self.treeviewDescricao.append_column(col26)
        self.treeviewDescricao.append_column(col27)
        self.treeviewDescricao.append_column(col28)
        self.treeviewDescricao.append_column(col29)


        #============================================================#
        #Documentacao do Veiculo

        self.model = gtk.ListStore(str,str,str,str,str,str,str,str,str,str,str)
        self.treeviewDocumentacao.set_model(self.model)
        #muda a cor da celula  e torna o campo editavel 
        renderer1 = gtk.CellRendererText()        
        renderer1.set_property("background", "gray") # Cor do foreground como propriedade
        renderer1.set_property("foreground", "black") # Cor do foreground como propriedade
       
        col0 = gtk.TreeViewColumn('Codigo', renderer1, text=0)
        col1 = gtk.TreeViewColumn('Placa', gtk.CellRendererText(), text=1)
        col2 = gtk.TreeViewColumn('Renavam', renderer1, text=2)
        col3 = gtk.TreeViewColumn('Ipva', gtk.CellRendererText(), text=3)
        col4 = gtk.TreeViewColumn('Chassi', renderer1, text=4)
        col5 = gtk.TreeViewColumn('Proprietario', gtk.CellRendererText(), text=5)
        col6 = gtk.TreeViewColumn('UF', renderer1, text=6)
        col7 = gtk.TreeViewColumn('Endereco', gtk.CellRendererText(), text=7)
        col8 = gtk.TreeViewColumn('CPF', renderer1, text=8)
        col9 = gtk.TreeViewColumn('Bairro', gtk.CellRendererText(), text=9)
        col10 = gtk.TreeViewColumn('Data', renderer1, text=10)

        
        


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
        #col4.set_min_width(124)
        self.treeviewDocumentacao.append_column(col0)
        self.treeviewDocumentacao.append_column(col1)
        self.treeviewDocumentacao.append_column(col2)
        self.treeviewDocumentacao.append_column(col3)
        self.treeviewDocumentacao.append_column(col4)
        self.treeviewDocumentacao.append_column(col5)
        self.treeviewDocumentacao.append_column(col6)
        self.treeviewDocumentacao.append_column(col7)
        self.treeviewDocumentacao.append_column(col8)
        self.treeviewDocumentacao.append_column(col9)
        self.treeviewDocumentacao.append_column(col10)
        
        #===========================================================#
        #Valor do Veiculo

        self.model = gtk.ListStore(str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str)
        self.treeviewValor.set_model(self.model)
        #muda a cor da celula  e torna o campo editavel 
        renderer1 = gtk.CellRendererText()        
        renderer1.set_property("background", "gray") # Cor do foreground como propriedade
        renderer1.set_property("foreground", "black") # Cor do foreground como propriedade
       
        col0 = gtk.TreeViewColumn('Codigo',renderer1 , text=0)
        col1 = gtk.TreeViewColumn('Placa', gtk.CellRendererText() , text=1)
        col2 = gtk.TreeViewColumn('Renavam',renderer1, text=2)
        col3 = gtk.TreeViewColumn('Documento', gtk.CellRendererText(), text=3)
        col4 = gtk.TreeViewColumn('Motor',renderer1, text=4)
        col5 = gtk.TreeViewColumn('Freio', gtk.CellRendererText(), text=5)
        col6 = gtk.TreeViewColumn('Cambio',renderer1, text=6)
        col7 = gtk.TreeViewColumn('Funilaria', gtk.CellRendererText(), text=7)
        col8 = gtk.TreeViewColumn('Multas',renderer1, text=8)
        col9 = gtk.TreeViewColumn('Outros', gtk.CellRendererText(), text=9)
        col10 = gtk.TreeViewColumn('Valor  da Compra Veiculo',renderer1, text=10)
        col11 = gtk.TreeViewColumn('Total Gasto no Veiculo', gtk.CellRendererText(), text=11)
        col12 = gtk.TreeViewColumn('Porcentagem de Lucro da Agencia',renderer1, text=12)
        col13 = gtk.TreeViewColumn('Valor Sugerido da Venda do Veiculo',gtk.CellRendererText(), text=13)
        col14 = gtk.TreeViewColumn('Lucro da Agencia',renderer1, text=14)
        #col15 = gtk.TreeViewColumn('Data',renderer1, text=15)
#referente a configuracao da largura dos campos
        col0.set_min_width(30)
        col1.set_min_width(40)
        col2.set_min_width(40)
        col3.set_min_width(40)
        col4.set_min_width(40)
        col5.set_min_width(40)
        col6.set_min_width(40)
        col7.set_min_width(40)
        col8.set_min_width(40)
        col9.set_min_width(40)
        col10.set_min_width(40)
        col11.set_min_width(40)
        col12.set_min_width(40)
        #col4.set_min_width(124)
        self.treeviewValor.append_column(col0)
        self.treeviewValor.append_column(col1)
        self.treeviewValor.append_column(col2)
        self.treeviewValor.append_column(col3)
        self.treeviewValor.append_column(col4)
        self.treeviewValor.append_column(col5)
        self.treeviewValor.append_column(col6)
        self.treeviewValor.append_column(col7)
        self.treeviewValor.append_column(col8)
        self.treeviewValor.append_column(col9)
        self.treeviewValor.append_column(col10)
        self.treeviewValor.append_column(col11)
        self.treeviewValor.append_column(col12)
        self.treeviewValor.append_column(col13)
        self.treeviewValor.append_column(col14)
        #self.treeviewValor.append_column(col15)
        #chama o metodo para adicionar na treeview descricao
        #por sua vez dentro desse metodo chamado existe outro metodo a ser4
        # invocado .
        self.leBancoDesv()
    
        # metodo que  ler o banco de dados e adiciona no trewview 
    def leBancoDesv(self):
        sql = "select * from desv "
        model = self.treeviewDescricao.get_model()
        model.clear()
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        for linha in resultado:
            model.append([linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[10], linha[11], linha[12], linha[13], linha[14], linha[15], linha[16], linha[17], linha[18], linha[19], linha[20], linha[21], linha[22], linha[23], linha[24], linha[25], linha[26], linha[27], linha[28], linha[29]])
        self.leBancoDoc()
    def leBancoDoc(self):
        sql1 = "select * from docv "
        model = self.treeviewDocumentacao.get_model()
        model.clear()
        self.cursor.execute(sql1)
        resultado = self.cursor.fetchall()
        for linha in resultado:
            model.append([linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7],linha[8],linha[9],linha[10]])
        self.leBancoVv()
    def leBancoVv(self):
        sql3 = "select * from vv "
        model = self.treeviewValor.get_model()
        model.clear()
        self.cursor.execute(sql3)
        resultado = self.cursor.fetchall()
        for linha in resultado:
            model.append([linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[10], linha[11], linha[12], linha[13], linha[14], linha[15]])
            
    # Esse metodo verifica se o combobox esta marcado e de acordo com 
    #a escolha e no que for digitado nele aparecera a consulta realizada
   #De todas as abas simutaneamente
    def on_buttonPesquisar_clicked (self,widget):
        print'buttonPesquisar'
        #pega o que esta no combobox
        comboo = self.comboboxDescricao.get_active_text()
        
        if comboo=="Todos":
            sql1 = "select * from desv "
            

            model1 = self.treeviewDescricao.get_model()
            #model2 = self.treeviewDocumentacao.get_model()
            #model3 = self.treeviewValor.get_model()
            model1.clear()
            self.cursor.execute(sql1)
            resultado = self.cursor.fetchall()
            for linha in resultado:
                model1.append([linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[10], linha[11], linha[12], linha[13], linha[14], linha[15], linha[16], linha[17], linha[18], linha[19], linha[20], linha[21], linha[22], linha[23], linha[24], linha[25], linha[26], linha[27], linha[28], linha[29]])
            #==========================================
            sql2 = "select * from docv "

            model2 = self.treeviewDocumentacao.get_model()
            
            #model3 = self.treeviewValor.get_model()
            model2.clear()
            self.cursor.execute(sql2)
            
            resultado = self.cursor.fetchall()
            for linha in resultado:
                model2.append([linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7],linha[8],linha[9],linha[10]])
                
            #=====================================================
            sql3 = "select * from vv "
           
            model3 = self.treeviewValor.get_model()
            model3.clear()
            self.cursor.execute(sql3)
            
            resultado = self.cursor.fetchall()
            for linha in resultado:
                model3.append([linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[10],linha[11],linha[12],linha[13], linha[14], linha[15]])


        
        elif comboo=="Placa":
            placa = self.entryPesquisar.props.text
            sql1 = "select * from desv where placa='%s' " %(placa)
            model1 = self.treeviewDescricao.get_model()
            #model2 = self.treeviewDocumentacao.get_model()
            #model3 = self.treeviewValor.get_model()
            model1.clear()
            self.cursor.execute(sql1)
            resultado = self.cursor.fetchall()
            for linha in resultado:
                model1.append([linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[10], linha[11], linha[12], linha[13], linha[14], linha[15], linha[16], linha[17], linha[18], linha[19], linha[20], linha[21], linha[22], linha[23], linha[24], linha[25], linha[26], linha[27], linha[28], linha[29]])
            #==========================================
            sql2 = "select * from docv where placad='%s' " %(placa)

            model2 = self.treeviewDocumentacao.get_model()
            
            #model3 = self.treeviewValor.get_model()
            model2.clear()
            self.cursor.execute(sql2)
            
            resultado = self.cursor.fetchall()
            for linha in resultado:
                model2.append([linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7],linha[8],linha[9],linha[10]])
                
            #=====================================================
            sql3 = "select * from vv where placav='%s' " %(placa)
           
            model3 = self.treeviewValor.get_model()
            model3.clear()
            self.cursor.execute(sql3)
            
            resultado = self.cursor.fetchall()
            for linha in resultado:
                model3.append([linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[10],linha[11],linha[12],linha[13], linha[14], linha[15]])
        #============================================================
        elif comboo=="Renavam":
            renavam = self.entryPesquisar.props.text
            sql1 = "select * from desv where renavam='%s' " %(renavam)
            model1 = self.treeviewDescricao.get_model()
            #model2 = self.treeviewDocumentacao.get_model()
            #model3 = self.treeviewValor.get_model()
            model1.clear()
            self.cursor.execute(sql1)
            resultado = self.cursor.fetchall()
            for linha in resultado:
                model1.append([linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[10], linha[11], linha[12], linha[13], linha[14], linha[15], linha[16], linha[17], linha[18], linha[19], linha[20], linha[21], linha[22], linha[23], linha[24], linha[25], linha[26], linha[27], linha[28], linha[29]])
            #==========================================
            sql2 = "select * from docv where renavamd='%s' " %(renavam)

            model2 = self.treeviewDocumentacao.get_model()
            
            #model3 = self.treeviewValor.get_model()
            model2.clear()
            self.cursor.execute(sql2)
            
            resultado = self.cursor.fetchall()
            for linha in resultado:
                model2.append([linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7],linha[8],linha[9],linha[10]])
            #=====================================================
            sql3 = "select * from vv where renavamv='%s' " %(renavam)
           
            model3 = self.treeviewValor.get_model()
            model3.clear()
            self.cursor.execute(sql3)
            
            resultado = self.cursor.fetchall()
            for linha in resultado:
                model3.append([linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[10],linha[11],linha[12],linha[13], linha[14], linha[15]])
            
    # esse metodo instancia a tela de editar descricao do  veiculo 
    #e joga os dados em seus  respectivos lugares.
    

    def on_buttonEditarDescricao_clicked (self,widget):
        print'buttonAtualizar'  
        valor = self.treeviewDescricao.get_cursor()
        n = valor[0]
               
        self.ndescricao=valor[0] #guarda o valor do curso e eu pego esse valor no  metodo atualizar
        print '=========='
        print n
        print '=========='
       
        if n == None :
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Nenhum registro selecionado para atualizacao')
            msg.set_position(gtk.WIN_POS_CENTER)
            msg.run()
            msg.destroy()
            
        else:
            print 'descricao'
            #mostra a janela update cadastrar Financeira
            #Setando a variavel com o arquivo glade
            self.arquivoglade = "Projects\update_cadastrardescricao_veiculo\update_cadastrardescricao_veiculo.glade"
            #Extraindo conteudo XML do arquivo
            self.xml = gtk.glade.XML(self.arquivoglade) 
            #instanciano as caixas de texto
            self.update_cadastrardescricao_veiculo=self.xml.get_widget('update_cadastrardescricao_veiculo')
            #Referente a aba Descricao do Veiculo
            self.entryCodigoVeiculo=self.xml.get_widget('entryCodigo')
            self.entryPlaca=self.xml.get_widget('entryPlaca')
            self.entryRenavam=self.xml.get_widget('entryRenavam')
            self.entryChassi=self.xml.get_widget('entryChassi')
            self.entryFabricante=self.xml.get_widget('entryFabricante')
            self.entryModelo=self.xml.get_widget('entryModelo')
            self.entryMarca=self.xml.get_widget('entryMarca')
            self.entryAno=self.xml.get_widget('entryAno')
            self.entryCidade=self.xml.get_widget('entryCidade')
            self.entryCombustivel=self.xml.get_widget('entryCombustivel')
            self.entryKm=self.xml.get_widget('entryKm')
            self.entryCor=self.xml.get_widget('entryCor')
            self.entryPortas=self.xml.get_widget('entryPortas')
            self.buttonSairDescricao=self.xml.get_widget('buttonSairDescricao')
            #self.buttonSairDescricao.connect('clicked',self.on_buttonSair_clicked)

            #deixa a caixa de texto do codigo desativado
            self.entryCodigoVeiculo.set_editable(False)
            

            
            
            self.valor = self.treeviewDescricao.get_selection()
    
            self.valor.set_mode(gtk.SELECTION_MULTIPLE)
            " Pegando a linha selecionada "
            modelo, caminhos = self.valor.get_selected_rows()
            print modelo 
            print caminhos
            for caminho in caminhos:
                    kiter = modelo.get_iter(caminho)
                    #coloquei o self para poer pegar esse valor em outro lugar
                    self.codigodescricao = modelo.get_value(kiter, 0)
                    placa = modelo.get_value(kiter, 1)
                    renavam= modelo.get_value(kiter, 2)
                    chassi= modelo.get_value(kiter, 3)
                    fabricante= modelo.get_value(kiter, 4)
                    modeloo= modelo.get_value(kiter, 5)
                    marca= modelo.get_value(kiter, 6)
                    anofabricacao = modelo.get_value(kiter, 7)
                    cidade = modelo.get_value(kiter, 8)
                    # uf=modelo.get_value(kiter, 9)
                    combustivel = modelo.get_value(kiter, 10)
                    km = modelo.get_value(kiter, 11)
                    cor = modelo.get_value(kiter, 12)
                    numeroportas= modelo.get_value(kiter, 13)
                    
                    #coloca os dados referente a consulta dentro de seus respctivos lugares
                    self.entryCodigoVeiculo.props.text= self.codigodescricao
                    self.entryPlaca.props.text = placa
                    self.entryRenavam.props.text = renavam
                    self.entryChassi.props.text = chassi
                    self.entryFabricante.props.text = fabricante
                    self.entryModelo.props.text = modeloo
                    self.entryMarca.props.text = marca
                    self.entryAno.props.text = anofabricacao
                    self.entryCidade.props.text = cidade
                    self.entryCombustivel.props.text = combustivel
                    self.entryKm.props.text = km
                    self.entryCor.props.text = cor
                    self.entryPortas.props.text = numeroportas

            #deixa a caixa de texto do codigo desativado
            self.entryCodigoVeiculo.set_editable(False)           
            self.xml.signal_autoconnect(self)
            #self.consultar_veiculo.hide()

        #gtk.main()  
        
    #============================================
    #correspondente a atualizacao da descicao do veiculo
    def on_buttonAtualizardescricao_clicked (self,widget):
        print'Atualizar'
        # so cadastra se o nome da tela atualizar estiver preenchido
        if (self.entryPlaca.props.text == "" or self.entryRenavam.props.text == ""):
        
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Por favor preencha todos os campos')
            resposta=msg.run()
            msg.destroy()
            
        else:
            codigo=self.entryCodigoVeiculo.props.text
            placa = self.entryPlaca.props.text
            renavam= self.entryRenavam.props.text
            chassi= self.entryChassi.props.text
            fabricante= self.entryFabricante.props.text
            modelo= self.entryModelo.props.text
            marca= self.entryMarca.props.text
            anofabricacao=self.entryAno.props.text
            cidade= self.entryCidade.props.text
            combustivel= self.entryCombustivel.props.text
            km=self.entryKm.props.text
            cor=self.entryCor.props.text
            numerosportas=self.entryPortas.props.text
            #placa e renavam da tabela docv e vv para a atualizacao em massa
            placad = self.entryPlaca.props.text
            renavamd= self.entryRenavam.props.text
            placav = self.entryPlaca.props.text
            renavamv= self.entryRenavam.props.text
            #=====================================================
            #entryPesquisarVendedor referente a caixa de texto da tela consultar vendedor
            if self.entryPesquisar.props.text=='':
                print 'testa nome'
                sql = "select * from desv"
                self.cursor.execute(sql)
                resultado = self.cursor.fetchall()
                i = 0
                t1 = range(1)
                for linha in resultado:
                    
                        t1[0] = i# -1  0 1 2
                        t2 = self.ndescricao #Esse self.n1 tem armazenado ovalor do cursor quando eu clico no registo que quero editar editar.
                        print'================'
                        print linha[0]#1 2
                                          
                        if t1[0] == t2[0]:
                            print 'otaio'
                            
                            #gravando dados no Banco
                            #sql3 = "insert into vv(1placav,renavamv,documento,motor,freio,cambio,funilaria,multas,outros,valorcompraveiculo,totalgastos,porcentagemlucro,valorsugeridovenda) values('" + placav + "','" + renavamv + "',%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f)"%(documento,motor,freio,cambio,funilaria,multas,outros,valorcompraveiculo,totalgastos,porcentagemlucro,valorsugeridovenda)
                            sql=('''update desv set placa='%s',renavam='%s',chassi='%s',fabricante='%s',modelo='%s',marca='%s',anofabricacao='%s',cidade='%s',combustivel='%s',km='%s',cor='%s',numerosportas='%s' where codigoveiculo=%i '''%(placa,renavam,chassi,fabricante,modelo,marca,anofabricacao,cidade,combustivel,km,cor,numerosportas,linha[0]))
                            #sql1=('''update docv set placad='%s',renavamd='%s' where codigodocumentacao=%i '''%(placad,renavamd,linha[0]))

                            self.cursor.execute(sql)
                            #self.cursor.execute(sql1)
                            self.conexao.commit()
                            self.leBancoDesv()
                            
                            
                        i=i+1
               #============================referente a atualizacao da placa e renavam da documentacao
                #faz a atualizacao da placa e renavam da aba documentacao caso elas forem mudadas.
                sql1 = "select * from docv"
                self.cursor.execute(sql1)
                resultado1 = self.cursor.fetchall()
                i = 0
                t1 = range(1)
                for linha in resultado1:
                    
                        t1[0] = i
                        #armazena o codigo da aba descricao do veiculo ,se acontecer a atualizacao da placaou renavam ele seguir aquele mesmo codigo e fazer a gravacao .
                        t2 = self.ndescricao #Esse self.ndescricao tem armazenado ovalor do cursor quando eu clico no registo que quero editar.
                        print'================'
                        print linha[0]#1 2
                                          
                        if t1[0] == t2[0]:
                            print 'otaio'
                            
                            #gravando dados no Banco
                            #sql3 = "insert into vv(1placav,renavamv,documento,motor,freio,cambio,funilaria,multas,outros,valorcompraveiculo,totalgastos,porcentagemlucro,valorsugeridovenda) values('" + placav + "','" + renavamv + "',%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f)"%(documento,motor,freio,cambio,funilaria,multas,outros,valorcompraveiculo,totalgastos,porcentagemlucro,valorsugeridovenda)
                            sql1=('''update docv set placad='%s',renavamd='%s' where codigodocumentacao=%i '''%(placad,renavamd,linha[0]))
                            #sql1=('''update docv set placad='%s',renavamd='%s' where codigodocumentacao=%i '''%(placad,renavamd,linha[0]))

                            self.cursor.execute(sql1)
                            #self.cursor.execute(sql1)
                            self.conexao.commit()
                            self.leBancoDoc()
                        i=i+1
                #=========================================================================
                #faz a atualizacao da placa e renavam da aba valor caso elas forem mudadas.
                sql2 = "select * from vv"
                self.cursor.execute(sql2)
                resultado1 = self.cursor.fetchall()
                i = 0
                t1 = range(1)
                for linha in resultado1:
                    
                        t1[0] = i
                        #armazena o codigo da aba descricao do veiculo ,se acontecer a atualizacao da placaou renavam ele seguir aquele mesmo codigo e fazer a gravacao .
                        t2 = self.ndescricao #Esse self.ndescricao tem armazenado ovalor do cursor quando eu clico no registo que quero editar.
                        print'================'
                        print linha[0]#1 2
                                          
                        if t1[0] == t2[0]:
                            print 'otaio'
                            
                            #gravando dados no Banco
                            #sql3 = "insert into vv(1placav,renavamv,documento,motor,freio,cambio,funilaria,multas,outros,valorcompraveiculo,totalgastos,porcentagemlucro,valorsugeridovenda) values('" + placav + "','" + renavamv + "',%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f)"%(documento,motor,freio,cambio,funilaria,multas,outros,valorcompraveiculo,totalgastos,porcentagemlucro,valorsugeridovenda)
                            sql2=('''update vv set placav='%s',renavamv='%s' where codigovalor=%i '''%(placav,renavamv,linha[0]))
                            #sql1=('''update docv set placad='%s',renavamd='%s' where codigodocumentacao=%i '''%(placad,renavamd,linha[0]))

                            self.cursor.execute(sql2)
                            #self.cursor.execute(sql1)
                            self.conexao.commit()
                            self.leBancoVv()

                        i=i+1
                #====================================================================
                self.update_cadastrardescricao_veiculo.hide()
                msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Atualizado Com Sucesso')
                msg.run()
                msg.destroy()
            elif    self.entryPesquisar.props.text!='':
                print 'diferente'
                sql = "select * from desv"
                self.cursor.execute(sql)
                resultado = self.cursor.fetchall()
                i =1
                t1 = range(1)
                               
                for linha in resultado:
                        
                        
                        t1[0] = i# -1  0 1 2
                        # esse self.codigo vem do 
                        t2 = int(self.codigodescricao) #peguei o valor que  vinha em string do codigo  e transformei em inteiro
                        print t2
                                                                  
                        if t2 ==linha[0]:
                            
                            print 'otaio'
                            #gravando dados no Banco
                            #sql3 = "insert into vv(1placav,renavamv,documento,motor,freio,cambio,funilaria,multas,outros,valorcompraveiculo,totalgastos,porcentagemlucro,valorsugeridovenda) values('" + placav + "','" + renavamv + "',%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f)"%(documento,motor,freio,cambio,funilaria,multas,outros,valorcompraveiculo,totalgastos,porcentagemlucro,valorsugeridovenda)
                            sql=('''update desv set placa='%s',renavam='%s',chassi='%s',fabricante='%s',modelo='%s',marca='%s',anofabricacao='%s',cidade='%s',combustivel='%s',km='%s',cor='%s',numerosportas='%s' where codigoveiculo=%i '''%(placa,renavam,chassi,fabricante,modelo,marca,anofabricacao,cidade,combustivel,km,cor,numerosportas,linha[0]))
                            self.cursor.execute(sql)
                            self.conexao.commit()
                            self.leBancoDesv()
                        #i=i+1
                        
                        #fecha a tela de update .
                 #faz a atualizacao da placa e renavam da aba documentacao caso elas forem mudadas.
                sql1 = "select * from docv"
                self.cursor.execute(sql1)
                resultado1 = self.cursor.fetchall()
                i = 0
                t1 = range(1)
                for linha in resultado1:
                    
                        t1[0] = i
                        #armazena o codigo da aba descricao do veiculo ,se acontecer a atualizacao da placaou renavam ele seguir aquele mesmo codigo e fazer a gravacao .
                        t2 =  int(self.codigodescricao) #Esse self.ndescricao tem armazenado ovalor do cursor quando eu clico no registo que quero editar.
                        print'================'
                        print linha[0]#1 2
                                          
                        if t2 ==linha[0]:
                            print 'otaio'
                            
                            #gravando dados no Banco
                            #sql3 = "insert into vv(1placav,renavamv,documento,motor,freio,cambio,funilaria,multas,outros,valorcompraveiculo,totalgastos,porcentagemlucro,valorsugeridovenda) values('" + placav + "','" + renavamv + "',%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f)"%(documento,motor,freio,cambio,funilaria,multas,outros,valorcompraveiculo,totalgastos,porcentagemlucro,valorsugeridovenda)
                            sql1=('''update docv set placad='%s',renavamd='%s' where codigodocumentacao=%i '''%(placad,renavamd,linha[0]))
                            #sql1=('''update docv set placad='%s',renavamd='%s' where codigodocumentacao=%i '''%(placad,renavamd,linha[0]))

                            self.cursor.execute(sql1)
                            #self.cursor.execute(sql1)
                            self.conexao.commit()
                            self.leBancoDoc()
                #self.update_cadastrardescricao_veiculo.hide()
                #==========================================================
                #faz a atualizacao da placa e renavam da aba valor caso elas forem mudadas.
                sql2 = "select * from vv"
                self.cursor.execute(sql2)
                resultado1 = self.cursor.fetchall()
                i = 0
                t1 = range(1)
                for linha in resultado1:
                    
                        t1[0] = i
                        #armazena o codigo da aba descricao do veiculo ,se acontecer a atualizacao da placaou renavam ele seguir aquele mesmo codigo e fazer a gravacao .
                        t2 = int(self.codigodescricao) #Esse self.ndescricao tem armazenado ovalor do cursor quando eu clico no registo que quero editar.
                        print'================'
                        print linha[0]#1 2
                                          
                        if t2 ==linha[0]:
                            print 'otaio'
                            
                            #gravando dados no Banco
                            #sql3 = "insert into vv(1placav,renavamv,documento,motor,freio,cambio,funilaria,multas,outros,valorcompraveiculo,totalgastos,porcentagemlucro,valorsugeridovenda) values('" + placav + "','" + renavamv + "',%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f)"%(documento,motor,freio,cambio,funilaria,multas,outros,valorcompraveiculo,totalgastos,porcentagemlucro,valorsugeridovenda)
                            sql2=('''update vv set placav='%s',renavamv='%s' where codigovalor=%i '''%(placav,renavamv,linha[0]))
                            #sql1=('''update docv set placad='%s',renavamd='%s' where codigodocumentacao=%i '''%(placad,renavamd,linha[0]))

                            self.cursor.execute(sql2)
                            #self.cursor.execute(sql1)
                            self.conexao.commit()
                            self.leBancoVv()
                            
                self.update_cadastrardescricao_veiculo.hide()
                msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Atualizado Com Sucesso')
                msg.run()
                msg.destroy()
    
    
        #gtk.main()
        
    # esse metodo instancia a tela de editar da aba documentacao do  veiculo 
    #e joga os dados em seus  respectivos lugares.
        
    def on_buttonEditarDocumentacao_clicked (self,widget):

        valor1=self.treeviewDocumentacao.get_cursor()
        ndoc = valor1[0]
        self.ndocu=valor1[0]
        if ndoc == None :
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Nenhum registro selecionado para atualizacao')
            msg.set_position(gtk.WIN_POS_CENTER)
            msg.run()
            msg.destroy()
        else:
        
        
        
            self.arquivoglade = "Projects\update_cadastrardocumentacao_veiculo\update_cadastrardocumentacao_veiculo.glade"
            #Extraindo conteudo XML do arquivo
            self.xml = gtk.glade.XML(self.arquivoglade) 
            #instanciano as caixas de texto
            self.update_cadastrardocumentacao_veiculo=self.xml.get_widget('update_cadastrardocumentacao_veiculo')
            self.entryCodigo=self.xml.get_widget('entryCodigo')
            self.entryPlacad=self.xml.get_widget('entryPlacad')
            self.entryRenavamd=self.xml.get_widget('entryRenavamd')
            self.entryIpvad=self.xml.get_widget('entryIpvad')
            self.entryChassid=self.xml.get_widget('entryChassid')
            self.entryProprietariod=self.xml.get_widget('entryProprietariod')
            self.entryUfd=self.xml.get_widget('entryUfd')
            self.entryEnderecod=self.xml.get_widget('entryEnderecod')
            self.entryCpfd=self.xml.get_widget('entryCpfd')
            self.entryBairrod=self.xml.get_widget('entryBairrod')
            #self.buttonSairDocumentacao.connect('clicked',self.on_buttonSairDocumentacao_clicked)
            #self.buttonSairDocumentacao=self.xml.get_widget('buttonSairDocumentacao')
            #deixa a caixa de texto do codigo desativado
            self.entryCodigo.set_editable(False)
            self.entryPlacad.set_editable(False)
            self.entryRenavamd.set_editable(False)


            
            self.valor = self.treeviewDocumentacao.get_selection()
            self.valor.set_mode(gtk.SELECTION_MULTIPLE)
            " Pegando a linha selecionada "
            modelo, caminhos = self.valor.get_selected_rows()
            print modelo 
            print caminhos
            for caminho in caminhos:
                    kiter = modelo.get_iter(caminho)
                    #coloquei o self para  pegar esse valor em outro lugar
                    self.codigodocumentacao = modelo.get_value(kiter, 0)
                    placad = modelo.get_value(kiter, 1)
                    renavamd= modelo.get_value(kiter, 2)
                    ipvad= modelo.get_value(kiter, 3)
                    chassid= modelo.get_value(kiter, 4)
                    proprietariod= modelo.get_value(kiter, 5)
                    #ufd= modelo.get_value(kiter, 6)
                    enderecod= modelo.get_value(kiter, 7)
                    cpfd= modelo.get_value(kiter, 8)
                    bairrod = modelo.get_value(kiter, 9)
                    
                    #coloca os dados referente a consulta dentro de seus respctivos lugares
                    self.entryCodigo.props.text= self.codigodocumentacao
                    self.entryPlacad.props.text = placad
                    self.entryRenavamd.props.text = renavamd
                    self.entryIpvad.props.text = ipvad
                    self.entryChassid.props.text = chassid
                    self.entryProprietariod.props.text = proprietariod
                    self.entryEnderecod.props.text = enderecod
                    self.entryCpfd.props.text = cpfd
                    self.entryBairrod.props.text = bairrod

                    self.xml.signal_autoconnect(self)
            #gtk.main()
    

    #=================================================
    #Referente a atualizacao na documentacao do veiculo
    #=================================================
    def on_buttonAtualizardocumentacao_clicked (self,widget):
        print'Atualizar'
        # so cadastra se o nome da tela atualizar estiver preenchido
        if (self.entryPlacad.props.text == "" ):
        
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Por favor preencha todos os campos')
            resposta=msg.run()
            msg.destroy()
            
        else:
            placad=self.entryPlacad.props.text
            renavamd=self.entryRenavamd.props.text
            ipvad=self.entryIpvad.props.text
            chassid=self.entryChassid.props.text
            proprietariod=self.entryProprietariod.props.text
            #ufd=self.entryUfd.props.text
            enderecod=self.entryEnderecod.props.text
            cpfd=self.entryCpfd.props.text
            bairrod=self.entryBairrod.props.text

                    

                   #entryPesquisarVendedor referente a caixa de texto da tela consultar vendedor
            if self.entryPesquisar.props.text=='':
                print 'testa nome'
                sql = "select * from docv"
                self.cursor.execute(sql)
                resultado = self.cursor.fetchall()
                i = 0
                t1 = range(1)
                for linha in resultado:
                    
                        t1[0] = i# -1  0 1 2
                        t2 = self.ndocu #Esse self.ndocu tem armazenado ovalor do cursor quando eu clico no registo que quero editar.
                        print'================'
                        print linha[0]#1 2
                                          
                        if t1[0] == t2[0]:
                            print 'otaio'
                            #gravando dados no Banco
                            #sql3 = "insert into vv(1placav,renavamv,documento,motor,freio,cambio,funilaria,multas,outros,valorcompraveiculo,totalgastos,porcentagemlucro,valorsugeridovenda) values('" + placav + "','" + renavamv + "',%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f)"%(documento,motor,freio,cambio,funilaria,multas,outros,valorcompraveiculo,totalgastos,porcentagemlucro,valorsugeridovenda)
                            sql=('''update docv set placad='%s',renavamd='%s',ipvad='%s',chassid='%s',proprietariod='%s',enderecod='%s',cpfd='%s',bairrod='%s' where codigodocumentacao=%i '''%(placad,renavamd,ipvad,chassid,proprietariod,enderecod,cpfd,bairrod,linha[0]))
                            self.cursor.execute(sql)
                            self.conexao.commit()
                            self.leBancoDoc()
                        i=i+1
                        #fecha a tela de update .
                #fecha a tela  de update do cadastro
                self.update_cadastrardocumentacao_veiculo.hide()
                msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Atualizado Com Sucesso')
                msg.run()
                msg.destroy()
            elif    self.entryPesquisar.props.text!='':
                print 'diferente'
                sql = "select * from docv"
                self.cursor.execute(sql)
                resultado = self.cursor.fetchall()
                i =1
                t1 = range(1)
                for linha in resultado:
                                            
                        t1[0] = i# -1  0 1 2
                        # esse self.codigo vem do 
                        t2 = int(self.codigodocumentacao) #peguei o valor que  vinha em sring do codigo  e transformei em inteiro
                        print t2
                                                                  
                        if t2 ==linha[0]:
                            
                            print 'otaio'
                            #gravando dados no Banco
                            #sql3 = "insert into vv(1placav,renavamv,documento,motor,freio,cambio,funilaria,multas,outros,valorcompraveiculo,totalgastos,porcentagemlucro,valorsugeridovenda) values('" + placav + "','" + renavamv + "',%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f)"%(documento,motor,freio,cambio,funilaria,multas,outros,valorcompraveiculo,totalgastos,porcentagemlucro,valorsugeridovenda)
                            sql=('''update docv set placad='%s',renavamd='%s',ipvad='%s',chassid='%s',proprietariod='%s',ufd='%s',enderecod='%s',cpfd='%s',bairrod='%s' where codigodocumentacao=%i '''%(placad,renavamd,ipvad,chassid,proprietariod,ufd,enderecod,cpfd,bairrod,linha[0]))
                            self.cursor.execute(sql)
                            self.conexao.commit()
                            self.leBancoDoc()
                        #i=i+1
                        #fecha a tela de update .    
                #fecha a tela  de update do cadastro
                #self.update_cadastrardocumentacao_veiculo.hide()
                print 'docu'
                self.update_cadastrardocumentacao_veiculo.hide()
                msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Atualizado Com Sucesso')
                msg.run()
                msg.destroy()
    
    
        #gtk.main()#=================================================
    
    # esse metodo instancia a tela de editar valor veiculo e joga os dados em seus 
    #respectivos lugares.
    def on_buttonEditarValor_clicked (self,widget):

        valor2=self.treeviewValor.get_cursor()
        nvalor = valor2[0]
        self.nvalor=nvalor
        if nvalor == None :
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Nenhum registro selecionado para atualizacao')
            msg.set_position(gtk.WIN_POS_CENTER)
            msg.run()
            msg.destroy()
        else:
        
        
        
            self.arquivoglade = "Projects\update_cadastrarvalor_veiculo\update_cadastrarvalor_veiculo.glade"
            #Extraindo conteudo XML do arquivo
            self.xml = gtk.glade.XML(self.arquivoglade) 
            #instanciano as caixas de texto
            self.update_cadastrarvalor_veiculo=self.xml.get_widget('update_cadastrarvalor_veiculo')
            
            self.entryCodigovalor=self.xml.get_widget('entryCodigovalor')
            self.entryDocumento=self.xml.get_widget('entryDocumento')
            self.entryPlacav=self.xml.get_widget('entryPlacav')
            self.entryRenavamv=self.xml.get_widget('entryRenavamv')
            self.entryMotor=self.xml.get_widget('entryMotor')
            self.entryFreio=self.xml.get_widget('entryFreio')
            self.entryCambio=self.xml.get_widget('entryCambio')
            self.entryFunilaria=self.xml.get_widget('entryFunilaria')
            self.entryMultas=self.xml.get_widget('entryMultas')
            self.entryOutros=self.xml.get_widget('entryOutros')
            self.entryValorCompra=self.xml.get_widget('entryValorCompra')
           ## self.entryTotal=self.xml.get_widget('entryTotal')
            self.entryPorcentagem=self.xml.get_widget('entryPorcentagem')
            
            #self.buttonAtualizarvalor.connect('clicked',self.on_buttonAtualizarvalor_clicked)
            self.buttonSairValor=self.xml.get_widget('buttonSairValor')

            #deixa a caixa de texto do codigo desativado
            self.entryCodigovalor.set_editable(False)
            self.entryPlacav.set_editable(False)
            self.entryRenavamv.set_editable(False)

            
            
            
            self.valor = self.treeviewValor.get_selection()
            self.valor.set_mode(gtk.SELECTION_MULTIPLE)
            " Pegando a linha selecionada "
            modelo, caminhos = self.valor.get_selected_rows()
            print modelo 
            print caminhos
            for caminho in caminhos:
                    kiter = modelo.get_iter(caminho)
                    #coloquei o self para poer pegar esse valor em outro lugar
                    self.codigovalor = modelo.get_value(kiter, 0)
                    placav = modelo.get_value(kiter, 1)
                    renavamv= modelo.get_value(kiter, 2)
                    documento= modelo.get_value(kiter, 3)
                    motor= modelo.get_value(kiter, 4)
                    freio= modelo.get_value(kiter, 5)
                    cambio= modelo.get_value(kiter, 6)
                    funilaria= modelo.get_value(kiter, 7)
                    multas = modelo.get_value(kiter, 8)
                    outros= modelo.get_value(kiter, 9)
                    valorcompra= modelo.get_value(kiter, 10)
                   # total= modelo.get_value(kiter, 11)
                    porcentagem= modelo.get_value(kiter, 12)
                    calculado= modelo.get_value(kiter, 13)
                    
                    
                    #coloca os dados referente a consulta dentro de seus respctivos lugares
                    self.entryCodigovalor.props.text= self.codigovalor
                    self.entryPlacav.props.text = placav
                    self.entryRenavamv.props.text = renavamv
                    self.entryDocumento.props.text = float(documento)
                    self.entryMotor.props.text = float(motor)
                    self.entryFreio.props.text = float(freio)
                    self.entryCambio.props.text = float(cambio)
                    self.entryFunilaria.props.text = float(funilaria)
                    self.entryMultas.props.text = float(multas)
                    self.entryOutros.props.text = float(outros)
                    self.entryValorCompra.props.text = float(valorcompra)
                    #self.entryTotal.props.text = float(total)    
                    self.entryPorcentagem.props.text = float(porcentagem)
                    
            
                    self.xml.signal_autoconnect(self)
                    
        #gtk.main()    
        
    

    #=================================================
    #Referente a  atualizacao de dados da aba valor do veiculo
    #=================================================
    def on_buttonAtualizarValor_clicked (self,widget):
        print'Atualizar'
        # so cadastra se o nome da tela atualizar estiver preenchido
        if(self.entryRenavamv.props.text=='' or self.entryPlacav.props.text == ''):    
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Por favor preencha os campos RENAVAM E PLACA')
            resposta=msg.run()
            msg.destroy()
            
        else:
            placav=self.entryPlacav.props.text
            renavamv=self.entryRenavamv.props.text
            documento=float(self.entryDocumento.props.text)
            motor=float(self.entryMotor.props.text)
            freio=float(self.entryFreio.props.text)
            cambio=float(self.entryCambio.props.text)
            funilaria=float(self.entryFunilaria.props.text)
            multas=float(self.entryMultas.props.text) 
            outros=float(self.entryOutros.props.text)
            valorcompra=float(self.entryValorCompra.props.text)
            total=documento+motor+freio+cambio+funilaria+multas+outros    
            porcentagem=float(self.entryPorcentagem.props.text)
            lucroagencia= ((valorcompra+(total))*(porcentagem/100))
            valorsugeridovenda=((valorcompra+total)+(lucroagencia))
                    
                   #entryPesquisarVendedor referente a caixa de texto da tela consultar vendedor
            if self.entryPesquisar.props.text=='':
                print 'testa nome'
                sql = "select * from vv"
                self.cursor.execute(sql)
                resultado = self.cursor.fetchall()
                i = 0
                t1 = range(1)
                for linha in resultado:
                    
                        t1[0] = i# -1  0 1 2
                        t2 = self.nvalor#Esse self.n1 tem armazenado ovalor do cursor quando eu clico no registo que quero editar editar.
                        print'================'
                        print linha[0]#1 2
                                          
                        if t1[0] == t2[0]:
                            print 'otaio'
                            #gravando dados no Banco
                                    #Dados Referente ao Banco de Dados variaveis digitadas igual ao banco                                                                                                                                                        #referente as variaveis que digitei acima onde recebeu as caixas de textos
                            sql=('''update vv set placav='%s',renavamv='%s',documento='%s',motor='%s',freio='%s',cambio='%s',funilaria='%s',multas='%s',outros='%s',valorcompraveiculo='%s',totalgastos='%s',porcentagemlucro='%s',lucroagencia='%s',valorsugeridovenda='%s' where codigovalor=%i '''%(placav,renavamv,documento,motor,freio,cambio,funilaria,multas,outros,valorcompra,total,porcentagem,lucroagencia,valorsugeridovenda,linha[0]))
                            self.cursor.execute(sql)
                            self.conexao.commit()
                            self.leBancoVv()
                        i=i+1
                        #fecha a tela de update .
                self.update_cadastrarvalor_veiculo.hide()
                msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Atualizado Com Sucesso')
                msg.run()
                msg.destroy()
            elif    self.entryPesquisar.props.text!='':
                print 'diferente'
                sql = "select * from vv"
                self.cursor.execute(sql)
                resultado = self.cursor.fetchall()
                i =1
                t1 = range(1)
            
            
            
                    
            
                for linha in resultado:
                        
                        
                        t1[0] = i# -1  0 1 2
                        # esse self.codigo vem do 
                        t2 = int(self.codigovalor) #peguei o valor que  vinha em sring do codigo  e transformei em inteiro
                        print t2
                                                                  
                        if t2 ==linha[0]:
                            
                            print 'otaio'
                            #gravando dados no Banco
                            sql=('''update vv set placav='%s',renavamv='%s',documento='%s',motor='%s',freio='%s',cambio='%s',funilaria='%s',multas='%s',outros='%s',valorcompraveiculo='%s',totalgastos='%s',porcentagemlucro='%s',lucroagencia='%s',valorsugeridovenda='%s' where codigovalor=%i '''%(placav,renavamv,documento,motor,freio,cambio,funilaria,multas,outros,valorcompra,total,porcentagem,lucroagencia,valorsugeridovenda,linha[0]))
                            self.cursor.execute(sql)
                            self.conexao.commit()
                            self.leBancoVv()
                        #i=i+1
                        #fecha a tela de update .
                
                self.update_cadastrarvalor_veiculo.hide()
                msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Atualizado Com Sucesso')
                msg.run()
                msg.destroy()
    
    
        #gtk.main()
        
    
        
    def on_buttonExcluir_clicked (self,widget):
        print'buttonExcluir'  
        valor = self.treeviewDescricao.get_cursor()
        valor1 = self.treeviewDocumentacao.get_cursor()
        valor2 = self.treeviewValor.get_cursor()
        n = valor[0]
        n1 = valor1[0]
        n2 = valor2[0]
        if n == None:
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Selecione o Codigo da aba Descricao do Veiculo')
            msg.set_position(gtk.WIN_POS_CENTER)
            msg.run()
            msg.destroy()
            #gtk.main()
        else:
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_QUESTION, gtk.BUTTONS_YES_NO, 'Deseja excluir o registro ?')
            resposta = msg.run()
            msg.destroy()

            if resposta == gtk.RESPONSE_YES:
                 if self.entryPesquisar.props.text=='':
                
                        valor = self.treeviewDescricao.get_cursor()
                        valor1 = self.treeviewDocumentacao.get_cursor()
                        valor2 = self.treeviewValor.get_cursor()
                        n = valor[0]
                        n1 = valor[0]
                        n2 = valor[0]
                        sql = "select * from desv"
                        sqldocv = "select * from docv"
                        sqlvv = "select * from vv"
                        self.cursor.execute(sql)
                        self.cursor.execute(sqldocv)
                        self.cursor.execute(sqlvv)
                        resultado = self.cursor.fetchall()
                        i = 0
                        t1 = range(1)
                        for linha in resultado:
                            t1[0] = i
                            t2 = n
                            t3=n1
                            t4=n2
                            if t1[0] == t2[0] or t1[0] == t3[0] or t1[0] == t4[0]:
                                sql = "DELETE FROM desv WHERE codigoveiculo = %i" % (linha[0])
                                sqldocv = "DELETE FROM docv WHERE codigodocumentacao = %i" % (linha[0])
                                sqlvv = "DELETE FROM vv WHERE codigovalor = %i" % (linha[0])
            
                                self.cursor.execute(sql)
                                self.cursor.execute(sqldocv)
                                self.cursor.execute(sqlvv)
                                self.conexao.commit()
                            i = i+1
                        self.leBancoDesv()
                        self.leBancoDoc()
                        self.leBancoVv()
                        
                        msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Deletado com Sucesso!')
                        msg.run()
                        msg.destroy()
                 elif  self.entryPesquisar.props.text!='':
                     
                        self.valor = self.treeviewDescricao.get_selection()
    
                        self.valor.set_mode(gtk.SELECTION_MULTIPLE)
                        " Pegando a linha selecionada "
                        modelo, caminhos = self.valor.get_selected_rows()
                        print modelo 
                        print caminhos
                        for caminho in caminhos:
                                kiter = modelo.get_iter(caminho)
                                #coloquei o self para poer pegar esse valor em outro lugar
                                self.codigodescricao = modelo.get_value(kiter, 0)
                                
                        print self.codigodescricao
                        sql = "select * from desv"
                        self.cursor.execute(sql)
                        resultado = self.cursor.fetchall()
                                           
                        for linha in resultado:
                                
                            
                                t1 = int(self.codigodescricao)#transformei em inteiro para fazer a comparacao com o linha[0]que vinha em inteiro
                                print 'gugu'
                                print self.codigodescricao    
                                print linha[0]                                    
                                if t1 == linha[0]:
                                    
                                    print 'otaio'
                                    #gravando dados no Banco
                                    
                                    sql = "DELETE FROM desv WHERE codigoveiculo = %i" % (linha[0])
                                    sqldocv = "DELETE FROM docv WHERE codigodocumentacao = %i" % (linha[0])
                                    sqlvv = "DELETE FROM vv WHERE codigovalor = %i" % (linha[0])
            
                                    self.cursor.execute(sql)
                                    self.cursor.execute(sqldocv)
                                    self.cursor.execute(sqlvv)
                                    self.conexao.commit()
                                    self.leBancoDesv()
                                    self.leBancoDoc()
                                    self.leBancoVv()
            
                        msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Deletado com Sucesso!')
                        msg.run()
                        msg.destroy()
            
        #gtk.main()
        
    def on_buttonSairDescricao_clicked (self,widget):
        print 'plk'
        self.update_cadastrardescricao_veiculo.hide()
        #gtk.main()
        
    def on_buttonSairDocumentacao_clicked (self,widget):
        print 'oiu'
    
        self.update_cadastrardocumentacao_veiculo.hide()
        #gtk.main_quit()
        
    def on_buttonSairValor_clicked (self,widget):
        print 'gugu'
        self.update_cadastrarvalor_veiculo.hide()
        #gtk.main_quit()
        
    def on_buttonFechar_clicked (self,widget):
        print'buttonFechar'
        self.consultar_veiculo.hide()
        gtk.main_quit()
        
    def on_consultar_veiculo_destroy (self,widget):
        gtk.main_quit()
        
    
      
if __name__ == '__main__':

    consultarv = ConsultarVeiculo()    
