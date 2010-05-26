# -*- coding: utf-8 -*-
'''
Created on 23/09/2009

@author: Lu�s Gustavo
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


class ConsultarVendaTroca(object):
    '''
    Classe Referênte a consulta da Venda e Troca de um Ve�culo  Cadastrado no  Bando de Dados da Tabela da Ag�ncia
    '''


    def __init__(self):
        self.host= "localhost"
        self.user= "root"
        self.passwd= "carros"  #"aaasesaa"
        self.database = "agenciaBeta1" 
        #Setando a variavel com o arquivo glade
        self.arquivoglade = "Projects\consultar_venda_troca\consultar_venda_troca.glade"
        #Extraindo conteudo XML do arquivo
        self.xml = gtk.glade.XML(self.arquivoglade)        
       #Componentes da Janela ConsultarVeiculo
        self.consultar_venda_troca=self.xml.get_widget('consultar_venda_troca')
        #propriedde para colocar cor na janela 
        self.consultar_venda_troca.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#00FF00"))

        #instanciando os botoes 
        self.combovenda_troca=self.xml.get_widget('combovenda_troca')
        # Coloca o foco no -Selecionar-
        self.combovenda_troca.set_active(0)
        # Autoconnect Signals and Callbacks
        self.xml.signal_autoconnect(self)      
        #aparece tudo que esta na janela consultar veiculo
        self.consultar_venda_troca.show_all() 
        #Conectando no banco
        self.conexao = MySQLdb.connect(host="localhost", user="root",passwd="carros", db="agenciaBeta1")
        self.cursor = self.conexao.cursor()
        gtk.main()
        
    def addTreeViewVenda(self):
        #Instancia o treeview coloca os descreve as colunas e as propriedades 
        self.model = gtk.ListStore(str,str,str,str,str,str,str)
        self.treeviewConsultarVenda.set_model(self.model)
        #muda a cor da celula  e torna o campo editavel 
        renderer1 = gtk.CellRendererText()        
        renderer1.set_property("background", "gray") # Cor do foreground como propriedade
        renderer1.set_property("foreground", "black") # Cor do foreground como propriedade
        
        col0 = gtk.TreeViewColumn('Codigo Venda', renderer1, text=0)
        col1 = gtk.TreeViewColumn('Nome Cliente', gtk.CellRendererText() , text=1)
        col2 = gtk.TreeViewColumn('Placa Veículo', renderer1, text=2)
        col3 = gtk.TreeViewColumn('Forma Pagamento',gtk.CellRendererText() , text=3)
        col4 = gtk.TreeViewColumn('Financeira', renderer1, text=4)
        col5 = gtk.TreeViewColumn('Vendedor', gtk.CellRendererText() , text=5)
        col6 = gtk.TreeViewColumn('Data Venda', renderer1, text=6)
              
        self.treeviewConsultarVenda.append_column(col0)
        self.treeviewConsultarVenda.append_column(col1)
        self.treeviewConsultarVenda.append_column(col2)
        self.treeviewConsultarVenda.append_column(col3)
        self.treeviewConsultarVenda.append_column(col4)
        self.treeviewConsultarVenda.append_column(col5)
        self.treeviewConsultarVenda.append_column(col6)

        self.leBancoVenda()
        
        #gtk.main()
    
    def addTreeViewTroca(self):
        #Instancia o treeview coloca os descreve as colunas e as propriedades 
        self.model = gtk.ListStore(str,str,str,str,str,str,str,str,str,str,str)
        self.treeviewConsultarTroca.set_model(self.model)
        #muda a cor da celula  e torna o campo editavel 
        renderer1 = gtk.CellRendererText()        
        renderer1.set_property("background", "gray") # Cor do foreground como propriedade
        renderer1.set_property("foreground", "black") # Cor do foreground como propriedade
        
        col0 = gtk.TreeViewColumn('Codigo Troca', renderer1, text=0)
        col1 = gtk.TreeViewColumn('Nome Cliente ',gtk.CellRendererText(), text=1)
        col2 = gtk.TreeViewColumn('Placa Veículo Agência', renderer1, text=2)
        col3 = gtk.TreeViewColumn('Placa Veículo Cliente', gtk.CellRendererText(), text=3)
        col4 = gtk.TreeViewColumn('Modelo Veículo Cliente', renderer1, text=4)
        col5 = gtk.TreeViewColumn('Marca Veículo Cliente', gtk.CellRendererText(), text=5)
        col6 = gtk.TreeViewColumn('Ano Veículo Cliente', renderer1, text=6)
        col7 = gtk.TreeViewColumn('Proprietário Veículo Cliente', gtk.CellRendererText(), text=7)
        col8 = gtk.TreeViewColumn('Valor Veículo Cliente', renderer1, text=8)
        col9 = gtk.TreeViewColumn('Vendedor', gtk.CellRendererText(), text=9)
        col10 = gtk.TreeViewColumn(' Data Troca', renderer1, text=10)
    
        self.treeviewConsultarTroca.append_column(col0)
        self.treeviewConsultarTroca.append_column(col1)
        self.treeviewConsultarTroca.append_column(col2)
        self.treeviewConsultarTroca.append_column(col3)
        self.treeviewConsultarTroca.append_column(col4)
        self.treeviewConsultarTroca.append_column(col5)
        self.treeviewConsultarTroca.append_column(col6)
        self.treeviewConsultarTroca.append_column(col7)
        self.treeviewConsultarTroca.append_column(col8)
        self.treeviewConsultarTroca.append_column(col9)
        self.treeviewConsultarTroca.append_column(col10)
        self.leBancoTroca()
        #gtk.main()
        
    def on_combovenda_troca_changed(self,*args):
                
        combo = self.combovenda_troca.get_active_text()
        if combo == 'Troca':
            self.consultar_venda_troca.hide()
            #Setando a variavel com o arquivo glade
            self.arquivoglade = "Projects\consultar_troca\consultar_troca.glade"
            #Extraindo conteudo XML do arquivo
            self.xml = gtk.glade.XML(self.arquivoglade)        
           #Componentes da Janela ConsultarVeiculo
            self.consultar_troca=self.xml.get_widget('consultar_troca')
            #instanciando os botoes 
            self.buttonEditar= self.xml.get_widget('buttonEditarTroca')
            self.buttonExcluir=self.xml.get_widget('buttonExcluir')
            self.buttonFechar=self.xml.get_widget('buttonFechar')
            self.comboTroca=self.xml.get_widget('comboTroca')
            self.treeviewConsultarTroca=self.xml.get_widget('treeviewConsultarTroca')
            # Autoconnect Signals and Callbacks
            self.xml.signal_autoconnect(self)      
            #aparece tudo que esta na janela consultar veiculo
            self.consultar_troca.show_all() 

            self.addTreeViewTroca()
            #gtk.main()
        elif combo != 'Troca' or combo != 'Escolha uma Opcao':# se for igual a VENDA
            self.consultar_venda_troca.hide()
            print'venda'
            #Setando a variavel com o arquivo glade
            self.arquivoglade = "Projects\consultar_venda\consultar_venda.glade"
            #Extraindo conteudo XML do arquivo
            self.xml = gtk.glade.XML(self.arquivoglade)        
            #Componentes da Janela ConsultarVeiculo
            self.consultar_venda=self.xml.get_widget('consultar_venda')
            #instanciando os botoes 
            self.buttonEditarVenda= self.xml.get_widget('buttonEditarVenda')
            self.buttonExcluir=self.xml.get_widget('buttonExcluir')
            self.buttonFechar=self.xml.get_widget('buttonFechar')
            self.comboVenda=self.xml.get_widget('comboVenda')
            self.treeviewConsultarVenda=self.xml.get_widget('treeviewConsultarVenda')
            # Autoconnect Signals and Callbacks
            self.xml.signal_autoconnect(self)      
            #aparece tudo que esta na janela consultar veiculo
            self.consultar_venda.show_all() 
            self.addTreeViewVenda()
            #gtk.main()
            
    def leBancoVenda(self):
         sqlv = "select * from venven  "
         model = self.treeviewConsultarVenda.get_model()
         model.clear()
         self.cursor.execute(sqlv)
         resultado = self.cursor.fetchall()
         print resultado
         for linha in resultado:
             #esse linha adiciona no treewie e ordenei os numeros de acordo com o nome do campo e dados armazenado nele. 
             model.append([linha[0], linha[1], linha[2], linha[4], linha[5],linha[3],linha[6]])
         #gtk.main()
         
    def leBancoTroca(self):
         sqlt = "select * from trocae"
         
         model = self.treeviewConsultarTroca.get_model()
         model.clear()
         self.cursor.execute(sqlt)
         resultado = self.cursor.fetchall()
         print resultado
         for linha in resultado:
            model.append([linha[0], linha[1], linha[2], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[3], linha[10]])
         print 'hu'
         #gtk.main()
    def on_buttonEditarTroca_clicked (self,widget):
        print 'teste button editartroca'
        
        #gtk.main()
    def on_buttonExcluirTroca_clicked (self,widget):
        print 'teste button excluir'
        #gtk.main()
    def on_buttonFecharTroca_clicked (self,widget):
        print 'teste button fechar'
        self.consultar_troca.hide()
        gtk.main_quit()
    def on_buttonEditarVenda_clicked (self,widget):
        print 'teste button editartroca'
        
        #gtk.main()
    def on_buttonExcluirVenda_clicked (self,widget):
        print 'teste button excluir'
        #gtk.main()
    def on_buttonFecharVenda_clicked (self,widget):
        print 'teste button fechar'
        self.consultar_venda.hide()
        gtk.main_quit()
        
    def on_consultar_venda_troca_destroy (self,widget):
        gtk.main_quit()
    def on_consultar_venda_destroy (self,widget):
        gtk.main_quit()
    def on_consultar_troca_destroy (self,widget):
        gtk.main_quit()

if __name__ == '__main__':

    consvt = ConsultarVendaTroca()    

        