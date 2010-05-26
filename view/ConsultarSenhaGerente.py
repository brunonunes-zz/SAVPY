# -*- coding: utf-8 -*-
'''
Created on 05/09/2009

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
    print ' Erro Ao Carregar um dos Import4'
    sys.exit(1)

class ConsultarSenhaGerente(object):
    def __init__(self):
        self.host= "localhost"
        self.user= "root"
        self.passwd= "carros"
        self.database = "agenciaBeta1"
        #Setando a variavel com o arquivo glade
        self.arquivoglade = "Projects\consultar_senha_gerente\consultar_senha_gerente.glade"
        #Extraindo conteudo XML do arquivo
        self.xml = gtk.glade.XML(self.arquivoglade)        
        #Componentes da Janela ConsultarCliente
        self.consultar_senha_gerente=self.xml.get_widget('consultar_senha_gerente')
        

        self.buttonExcluir= self.xml.get_widget('buttonExcluir')
        self.buttonFechar=self.xml.get_widget('buttonFechar')
        self.buttonEditar=self.xml.get_widget('buttonEditar')

        self.treeviewConsultar =self.xml.get_widget('treeviewConsultar')
        
        #self.buttonExcluir.connect('clicked',self.on_buttonExcluir_clicked)
        #self.buttonFechar.connect('clicked',self.on_buttonFechar_clicked)
        #self.buttonEditar.connect('clicked',self.on_buttonEditar_clicked)
    
        #==========================================================
        # Comboxbox
        self.combobox = self.xml.get_widget('combobox')
        
        # Preparar a Caixa Comboxbox para selecao
        
        # Componente ListStore para armazenar as retas
        store = gtk.ListStore(str)
        store.append(["Gerente"])
        store.append(["Vendedor"])

        # Celula texto para nossa Caixa de Selecao
        celula = gtk.CellRendererText()
        # Associa o ListStore a Caixa de Selecao
        self.combobox.set_model(store)
        # Associa a celula a caixa de selecao
        self.combobox.pack_start(celula, True)
        self.combobox.add_attribute(celula, 'text', 0)
        
        # Coloca o foco no -Selecionar-
        self.combobox.set_active(0)
#=====================================================================
        #Conectando no banco
        self.conexao = MySQLdb.connect(host="localhost", user="root",passwd="carros", db="agenciaBeta1")
        self.cursor = self.conexao.cursor()
        self.addTreeView()
         # Autoconnect Signals and Callbacks

        self.xml.signal_autoconnect(self)
        #mostra tudo que esta dentro da consultar cliente
        #colocar depois
        self.consultar_senha_gerente.show_all() 
        gtk.main()   
        
    def on_combobox_changed(self,*args):

        combo = self.combobox.get_active_text()
            
        if combo == "Gerente":  
            sql = "select * from gere "
            model = self.treeviewConsultar.get_model()
            model.clear()
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            for linha in resultado:
                model.append([linha[0], linha[1], linha[2], linha[3]])  
        
        elif combo == "Vendedor":
           
            sql = "select * from cs "
            model = self.treeviewConsultar.get_model()
            model.clear()
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            for linha in resultado:
                model.append([linha[0], linha[1], linha[2], linha[3]])  
        
        
    def addTreeView(self):
        
        #Instancia o treeview coloca os descreve as colunas e as propriedades 
        self.model = gtk.ListStore(str,str,str,str)
        self.treeviewConsultar.set_model(self.model)
        #muda a cor da celula  e torna o campo editavel 
        renderer1 = gtk.CellRendererText()        
        renderer1.set_property("background", "gray") # Cor do foreground como propriedade
        renderer1.set_property("foreground", "black") # Cor do foreground como propriedade

        
        col0 = gtk.TreeViewColumn('Codigo', renderer1, text=0)
        col1 = gtk.TreeViewColumn('Nome', gtk.CellRendererText(), text=1)
        col2 = gtk.TreeViewColumn('Senha', renderer1, text=2)
        col3 = gtk.TreeViewColumn('Confirmar Senha', gtk.CellRendererText(), text=3)
        
        


        col0.set_min_width(30)
        col1.set_min_width(150)
        col2.set_min_width(124)
        col3.set_min_width(123)
        #col4.set_min_width(124)
        self.treeviewConsultar.append_column(col0)
        self.treeviewConsultar.append_column(col1)
        self.treeviewConsultar.append_column(col2)
        self.treeviewConsultar.append_column(col3)
        
        
        self.leBancoGerente()
        # metodo que  ler o banco de dados e adiciona no trewview 
    def leBancoGerente(self):
        sql = "select * from gere "
        model = self.treeviewConsultar.get_model()
        model.clear()
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        for linha in resultado:
            model.append([linha[0], linha[1], linha[2], linha[3]])
    
    
    def leBancoVendedor(self):
        sql = "select * from cs "
        model = self.treeviewConsultar.get_model()
        model.clear()
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        for linha in resultado:
            model.append([linha[0], linha[1], linha[2], linha[3]])
    
                
   
        
    def on_buttonEditar_clicked (self,widget):
        print'ButtonEditar'
        valor = self.treeviewConsultar.get_cursor()       
        
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
            self.arquivoglade = "Projects\update_cadastrar_senha_gerente\update_cadastrar_senha_gerente.glade"
            #Extraindo conteudo XML do arquivo
            self.xml = gtk.glade.XML(self.arquivoglade) 
            #instanciano as caixas de texto
            self.update_cadastrar_senha_gerente=self.xml.get_widget('update_cadastrar_senha_gerente')
    
            self.entryCodigo=self.xml.get_widget('entryCodigo')
            self.entryNome=self.xml.get_widget('entryNome')
            self.entrySenha=self.xml.get_widget('entrySenha')
            self.entryConfirmar=self.xml.get_widget('entryConfirmar')
    
            #deixa a caixa de texto do codigo desativado
            self.entryCodigo.set_editable(False)

            self.xml.signal_autoconnect(self)
            
             
            print'gu'
            
            self.valor = self.treeviewConsultar.get_selection()
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
                    senha = modelo.get_value(kiter, 2)
                    confirmar = modelo.get_value(kiter, 3)
                   
                    
                    #coloca os dados referente a consulta dentro de seus respctivos lugares
                    self.entryCodigo.props.text= self.codigo
                    self.entryNome.props.text= nome
                    self.entrySenha.props.text= senha
                    self.entryConfirmar.props.text= confirmar
                    

                    #fecha a tela consultar financeira 
                   # self.consultar_senha_gerente.hide()

        #gtk.main()
        
    #correspondente a tela update cadastrar vendedor
    def on_buttonAtualizar_clicked (self,widget):
        print'Atualizar'
        # so cadastra se o nome da tela atualizar estiver preenchido
        if (self.entryNome.props.text == "" or self.entrySenha.props.text=="" or self.entryConfirmar.props.text =="" ):
        
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Por favor preencha todos os campos')
            msg.set_position(gtk.WIN_POS_CENTER)
            msg.run()
            msg.destroy()
            
        else:
            codigo=self.entryCodigo.props.text
            nome = self.entryNome.props.text
            senha = self.entrySenha.props.text
            confirmar= self.entryConfirmar.props.text
            

        combo = self.combobox.get_active_text()
        if combo=="Gerente":
            if self.entrySenha.props.text == self.entryConfirmar.props.text:
                print 'testa nome'
                sql = "select * from gere"
                self.cursor.execute(sql)
                self.resultado = self.cursor.fetchall()
                i = 0
                t1 = range(1)
                for linha in self.resultado:
                    
                        t1[0] = i# -1  0 1 2
                        t2 = self.n1 #Esse self.n1 tem armazenado ovalor do cursor quando eu clico no registo que quero editar editar.
                        print'================'
                        print linha[0]#1 2
                                          
                        if t1[0] == t2[0]:
                            print 'otaio'
                            #gravando dados no Banco
                            #sql3 = "insert into vv(1placav,renavamv,documento,motor,freio,cambio,funilaria,multas,outros,valorcompraveiculo,totalgastos,porcentagemlucro,valorsugeridovenda) values('" + placav + "','" + renavamv + "',%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f)"%(documento,motor,freio,cambio,funilaria,multas,outros,valorcompraveiculo,totalgastos,porcentagemlucro,valorsugeridovenda)
                            sql=('''update gere set nome='%s',senha='%s',confirmar='%s' where codigogerente=%i '''%(nome,senha,confirmar,linha[0]))
                            self.cursor.execute(sql)
                            self.conexao.commit()
                        i=i+1
                        #fecha a tela de update .
                self.update_cadastrar_senha_gerente.hide()
                self.leBancoGerente()
                msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Atualizado Com Sucesso')
                msg.set_position(gtk.WIN_POS_CENTER)
                msg.run()
                msg.destroy()
                

            else:
                msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Senha Diferente da Confirmacao Senha')
                msg.set_position(gtk.WIN_POS_CENTER)
                msg.run()
                msg.destroy()
                
        elif combo=="Vendedor" :
                        
            if self.entrySenha.props.text == self.entryConfirmar.props.text:
                print 'testa nome'
                sql = "select * from cs"
                self.cursor.execute(sql)
                self.resultado = self.cursor.fetchall()
                i = 0
                t1 = range(1)
                for linha in self.resultado:
                    
                        t1[0] = i# -1  0 1 2
                        t2 = self.n1 #Esse self.n1 tem armazenado ovalor do cursor quando eu clico no registo que quero editar editar.
                        print'================'
                        print linha[0]#1 2
                                          
                        if t1[0] == t2[0]:
                            print 'otaio'
                            #gravando dados no Banco
                            #sql3 = "insert into vv(1placav,renavamv,documento,motor,freio,cambio,funilaria,multas,outros,valorcompraveiculo,totalgastos,porcentagemlucro,valorsugeridovenda) values('" + placav + "','" + renavamv + "',%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f)"%(documento,motor,freio,cambio,funilaria,multas,outros,valorcompraveiculo,totalgastos,porcentagemlucro,valorsugeridovenda)
                            sql=('''update cs set nome='%s',senha='%s',confirmar='%s' where codigo=%i '''%(nome,senha,confirmar,linha[0]))
                            self.cursor.execute(sql)
                            self.conexao.commit()
                        i=i+1
                self.update_cadastrar_senha_gerente.hide()
                self.leBancoVendedor()
                msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Atualizado Com Sucesso')
                msg.set_position(gtk.WIN_POS_CENTER)
                msg.run()
                msg.destroy()
                    
            else:
                msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Senha Diferente da Confirmacao Senha')
                msg.set_position(gtk.WIN_POS_CENTER)
                msg.run()
                msg.destroy()        
        #gtk.main()
        
        

    def on_buttonExcluir_clicked (self,widget):
        print'buttonExcluir'
        
        valor = self.treeviewConsultar.get_cursor()
        n = valor[0]
        if n == None:
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Nenhum registro selecionado para exclusao')
            msg.set_position(gtk.WIN_POS_CENTER)
            msg.run()
            msg.destroy()
            #gtk.main()
        else:
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_QUESTION, gtk.BUTTONS_YES_NO, 'Deseja excluir o registro ?')
            msg.set_position(gtk.WIN_POS_CENTER)
            resposta = msg.run()
            msg.destroy()
            
            if resposta == gtk.RESPONSE_YES:
                    print 'huy'
                    combo = self.combobox.get_active_text()
                    if combo == "Gerente":
                
                        sql = "select * from gere"
                        self.cursor.execute(sql)
                        resultado = self.cursor.fetchall()
                        i = 0
                        t1 = range(1)
                        print 'iuj'
                        for linha in resultado:
                            t1[0] = i
                            t2 = n
                            if t1[0] == t2[0]:
                                print 'gugu'
                                sql = "DELETE FROM gere WHERE codigogerente = %i" % (linha[0])
                                self.cursor.execute(sql)
                                self.conexao.commit()
                            i = i+1
                        self.leBancoGerente()
                        msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Deletado com Sucesso!')
                        msg.set_position(gtk.WIN_POS_CENTER)
                        msg.run()
                        msg.destroy()
            
                    elif combo == "Vendedor":
                        sql = "select * from cs"
                        self.cursor.execute(sql)
                        resultado = self.cursor.fetchall()
                        i = 0
                        t1 = range(1)
                        for linha in resultado:
                            t1[0] = i
                            t2 = n
                            if t1[0] == t2[0]:
                                sql = "DELETE FROM cs WHERE codigo = %i" % (linha[0])
                                self.cursor.execute(sql)
                                self.conexao.commit()
                            i = i+1
                        self.leBancoVendedor()
                        msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Deletado com Sucesso!')
                        msg.set_position(gtk.WIN_POS_CENTER)
                        msg.run()
                        msg.destroy()
            
        #gtk.main()
            
    def on_buttonFechar_clicked (self,widget):
        print'buttonFechar'
        self.consultar_senha_gerente.hide()
        gtk.main_quit()
    
    #correspondente a tela update cadastrar Vendedor
    def on_buttonSair_clicked (self,widget):
        print'buttonSair'
        self.update_cadastrar_senha_gerente.hide()
        #gtk.main()
        
    def on_consultar_senha_gerente_destroy (self,widget):
        gtk.main_quit()
        
    #def on_update_cadastrar_senha_gerente_destroy (self,widget):
     #   gtk.main_quit()
    
        
           
   
if __name__ == '__main__':

    conssg = ConsultarSenhaGerente()
  
    
