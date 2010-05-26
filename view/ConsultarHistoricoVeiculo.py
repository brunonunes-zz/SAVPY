# -*- coding: utf-8 -*-
'''
Created on 06/09/2009

@author: Administrador
'''

import sys
try:

    import pygtk
    pygtk.require('2.0')
    import gtk
    import gtk.glade
    import MySQLdb


except:
    print ' Erro Ao Carregar um dos Import54'
    sys.exit(1)


class ConsultarHistoricoVeiculo(object):
    


    def __init__(self):
        #é
        self.host= "localhost"
        self.user= "root"
        self.passwd= "carros"  #"aaasesaa"
        self.database = "agenciaBeta1" 
        
        #Setando a variavel com o arquivo glade
        self.arquivoglade = "Projects\consultar_historico_veiculo\consultar_historico_veiculo.glade"
        #Extraindo conteudo XML do arquivo
        self.xml = gtk.glade.XML(self.arquivoglade)        
        #Componentes da Janela CadastrarCliente
        self.consultar_historico_veiculo=self.xml.get_widget('consultar_historico_veiculo')
        
        self.buttonFechar=self.xml.get_widget('buttonFechar')
        self.treeviewConsultarHistorico=self.xml.get_widget('treeviewConsultarHistorico')
           #==========================================================
        #self.buttonFechar.connect('clicked',self.on_buttonFechar_clicked)
        
        self.comboHistorico=self.xml.get_widget('comboHistorico')
        # Comboxbox
        # Coloca o foco no -Selecionar-
        self.comboHistorico.set_active(0)
#====================================================================

#Conectando no banco
        self.conexao = MySQLdb.connect(host="localhost", user="root",passwd="carros", db="agenciaBeta1")
        self.cursor = self.conexao.cursor()
        self.adicionartreeView()
        # Autoconnect Signals and Callbacks
        self.xml.signal_autoconnect(self)    
        self.consultar_historico_veiculo.show_all()
        
        gtk.main()
        
    def on_comboHistorico_changed(self,*args):
       

        combo = self.comboHistorico.get_active_text()
        print combo
        if combo=="Estoque":
            
            self.leBancoEstoque()
        elif combo=="Vendido":
            self.leBancoVendido()
        elif combo=="Trocado":
            self.leBancoTrocado()
        #gtk.main()
            
            
            
    
    def adicionartreeView(self):
        #Descricao do Veiculo
        #Instancia o treeview coloca os descreve as colunas e as propriedades 
         #================================================================
        #Combobox    #
        
        #adicionando no treeview
        self.model = gtk.ListStore(str,str,str,str,str,str,str,str)
        self.treeviewConsultarHistorico.set_model(self.model)
        #muda a cor da celula  e torna o campo editavel 
        renderer1 = gtk.CellRendererText()        
        renderer1.set_property("background", "gray") # Cor do foreground como propriedade
        renderer1.set_property("foreground", "black") # Cor do foreground como propriedade
        
        
        col0 = gtk.TreeViewColumn('Codigo', renderer1, text=0)
        col1 = gtk.TreeViewColumn('Placa', gtk.CellRendererText(), text=1)
        col2 = gtk.TreeViewColumn('Renavam', renderer1, text=2)
        col3 = gtk.TreeViewColumn('Numero Chassi', gtk.CellRendererText(), text=3)
        col4 = gtk.TreeViewColumn('Fabricante', renderer1, text=4)
        col5 = gtk.TreeViewColumn('Marca', renderer1, text=5)
        col6 = gtk.TreeViewColumn('Modelo', gtk.CellRendererText(), text=6)
        col7 = gtk.TreeViewColumn('Ano', renderer1, text=7)
        

        self.treeviewConsultarHistorico.append_column(col0)
        self.treeviewConsultarHistorico.append_column(col1)
        self.treeviewConsultarHistorico.append_column(col2)
        self.treeviewConsultarHistorico.append_column(col3)
        self.treeviewConsultarHistorico.append_column(col4)
        self.treeviewConsultarHistorico.append_column(col5)
        self.treeviewConsultarHistorico.append_column(col6)
        self.treeviewConsultarHistorico.append_column(col7)

        self.leBancoEstoque()
        
    def leBancoEstoque(self):
        sql = "select * from desv  where disponibilidade='Estoque'"
        model = self.treeviewConsultarHistorico.get_model()
        model.clear()
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        for linha in resultado:
            
            model.append([linha[0],linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7]])

    def leBancoVendido(self):
        sql = "select * from desv  where disponibilidade='Vendido'"
        model = self.treeviewConsultarHistorico.get_model()
        model.clear()
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        for linha in resultado:
            
            model.append([linha[0],linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7]])
   
    def leBancoTrocado(self):
        sql = "select * from desv  where disponibilidade='Trocado'"
        model = self.treeviewConsultarHistorico.get_model()
        model.clear()
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        for linha in resultado:
            
            model.append([linha[0],linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7]])


    def on_buttonFechar_clicked (self,widget):
        print'buttonFechar'
        self.consultar_historico_veiculo.hide()
        gtk.main_quit()
        
    def on_consultar_historico_veiculo_destroy (self,widget):
        gtk.main_quit()


    
if __name__ == '__main__':

    chv = ConsultarHistoricoVeiculo()


        