'''
Created on 04/08/2009

@author: Administrador
'''
#! /usr/bin/env python
# -.- coding: utf-8 -.-

import sys
import gobject
import pygtk
pygtk.require('2.0')
import gtk
import gtk.glade   
import MySQLdb
import os.path

#verifica se o banco de dados existe se nao o cria
'''
if not os.path.exists('banco.db'):
    conexao = sqlite.connect('banco.db')
    cursor = conexao.cursor()
    sql = """
CREATE TABLE usuarios (
  codigo   integer PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
  usuario  char(20) NOT NULL,
  senha    char(20) NOT NULL,
  server   char(20) NOT NULL
)"""
    cursor.execute(sql)
    conexao.commit()
'''



#Pegando o arquivo glade
class Ola:
    def __init__(self):

        self.arquivoglade="C:\Documents and Settings\Administrador\Projects\interface\interface.glade"
        #Rereentacao do arquivo xml
        self.xml = gtk.glade.XML(self.arquivoglade)
       #Componentes da Janela TelaPrincipal
        self.interface = self.xml.get_widget('interface')
        self.entryTitulo = self.xml.get_widget('entryTitulo')
        self.entryAno = self.xml.get_widget('entryAno')
        self.entryDiretor = self.xml.get_widget('entryDiretor')
        self.buttonGravar = self.xml.get_widget('buttonGravar')
        self.buttonDelete=self.xml.get_widget('buttonDelete')
        self.buttonEditar=self.xml.get_widget('buttonEditar')

        self.combo=self.xml.get_widget('combo')
        #desabilita a caixa de texto
        #self.entryDiretor.set_editable(False)
        #self.entryAno.set_invisible_char(True)
        #faz o que foi digitado virar *
        self.entryAno.set_visibility(False)
    # Comboxbox
        
        
        # Preparar a Caixa Comboxbox para selecao
        
        # Componente ListStore para armazenar as retas
        
        store = gtk.ListStore(str)
        for i in range(1985,2020):
           store.append([i])
         
        
        # Celula texto para nossa Caixa de Selecao
        celula = gtk.CellRendererText()
        # Associa o ListStore a Caixa de Selecao
        self.combo.set_model(store)
        
        # Associa a celula a caixa de selecao
        self.combo.pack_start(celula, True)
        self.combo.add_attribute(celula, 'text', 0)
        
        # Coloca o foco no -Selecionar-
        self.combo.set_active(0)
        # acaba o combobox acima
        
        
        self.treev =self.xml.get_widget('treeview')


        # Referente a chamada do metodo e ao click do botao
        self.treev.connect('row-activated',self.on_treeview_row_activated) 
        self.buttonDelete.connect('clicked',self.on_buttonDelete_clicked)
        self.buttonGravar.connect('clicked',self.on_gravar_clicked)
        self.buttonEditar.connect('clicked',self.on_buttonEditar_clicked)  
        #este e seu treeview
        #aqui uma consulta SQL para pegar os dados e depois jogar no treeview
        self.model = gtk.ListStore(str, str, str,str)
        self.treev.set_model(self.model)
        #muda a cor da celula  e torna o campo editavel 
        renderer1 = gtk.CellRendererText()        
        renderer1.set_property("background", "black") # Cor do foreground como propriedade
        renderer1.set_property("foreground", "white") # Cor do foreground como propriedade
        renderer1.set_property('editable', True) # A primeira coluan e editavel

        renderer2 = gtk.CellRendererText()        
        renderer2.set_property("background", "black") # Cor do foreground como propriedade
        renderer2.set_property("foreground", "white") # Cor do foreground como propriedade
        renderer2.set_property('editable', True) # A primeira coluan e editavel
        
        renderer3 = gtk.CellRendererText()        
        renderer3.set_property("background", "black") # Cor do foreground como propriedade
        renderer3.set_property("foreground", "white") # Cor do foreground como propriedade
        renderer3.set_property('editable', True)
        
        col0 = gtk.TreeViewColumn('id',gtk.CellRendererText(), text=0)
        col1 = gtk.TreeViewColumn('Titulo',renderer1 , text=1)
        col2 = gtk.TreeViewColumn('Ano',renderer2 , text=2)
        col3 = gtk.TreeViewColumn('Diretor', renderer3, text=3)
        col0.set_min_width(50)
        col1.set_min_width(123)
        col2.set_min_width(124)
        col3.set_min_width(123)
        self.treev.append_column(col0)
        self.treev.append_column(col1)
        self.treev.append_column(col2)
        self.treev.append_column(col3)

        #Conectando no banco
        self.conexao = MySQLdb.connect(host="localhost", user="root",passwd="carros", db="locadora")
        self.cursor = self.conexao.cursor()
        self.leBanco()
        self.xml.signal_autoconnect(self) 
        self.interface.show_all()
        gtk.main()
        
        
    ###Evento click do botao Gravar###
    
    def on_gravar_clicked(self, widget):
        if (self.entryTitulo.props.text == "" or self.entryAno.props.text  == "" or self.entryDiretor.props.text == ""):
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Por favor preencha todos os campos')
            resposta=msg.run()
            msg.destroy()
            
        else:
            model = self.treev.get_model()
            self.titulo = self.entryTitulo.props.text
            #entryAno
            
            ano = self.entryAno.props.text
            diretor = self.entryDiretor.props.text
            " Limpando os campos "
            self.entryTitulo.props.text = ""
            self.entryAno.props.text = ""
            self.entryDiretor.props.text = ""
            #gravando dados no Banco
            sql = "insert into filmes(titulo, ano, diretor) values('"+ titulo + "', '" + ano + "', '" + diretor + "')"
            
            self.cursor.execute(sql)
            self.conexao.commit()#Para enviar tudo para o Banco
            
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Cadastrado Com Sucesso')
            msg.run()
            msg.destroy()
            
            #chama o metodo para que  os dados sejam exibido no treview
            
            self.leBanco()
        gtk.main()
            
     #exibe o resultado no metodo       
    def leBanco(self):
        sql = "select * from filmes "
        model = self.treev.get_model()
        model.clear()     
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        for linha in resultado:
            model.append([linha[0], linha[1], linha[2],linha[3]])
            #self.entryTitulo.props.text=(linha[0])
    #duplo clique na treview        
    def on_treeview_row_activated(self,widget, path, column):
        print'gu'
        
    def on_buttonEditar_clicked(self, widget):
        
        print 'ButtonEditar'
        
        valor = self.treev.get_cursor()
        n = valor[0]
        if n == None:
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Selecione um registro a ser alterado')
            msg.set_position(gtk.WIN_POS_CENTER)
            msg.run()
        
        else:
            valor = self.treev.get_selection()
            valor.set_mode(gtk.SELECTION_MULTIPLE)
            " Pegando a linha selecionada "
            modelo, caminhos = valor.get_selected_rows()
            for caminho in caminhos:
                    kiter = modelo.get_iter(caminho)
                    cod = modelo.get_value(kiter, 1)
                    cod1 = modelo.get_value(kiter, 2)
                    cod2 = modelo.get_value(kiter, 3)

                    self.entryTitulo.props.text=cod
                    self.entryAno.props.text=cod1
                    self.entryDiretor.props.text=cod2
    #        sql = "select * from filmes"
     #       self.cursor.execute(sql)
      #      resultado = self.cursor.fetchall()
                # verificar no site o tal do fetchall
       #     for linha in resultado:
                    
            
                   
            
            
     ### Verifica se algum item do treeview foi selecionado
     #testar em algum ja testei em editar
        def pegaSelecaoTreev(self):
                valor = self.treev.get_cursor()
                n = valor[0]
                if n == None:
                        self.mensagem('info', 'Nenhum registro selecionado para Baixa')
                        return None
                else:
                        registro = self.treev.get_selection()
                        registro.set_mode(gtk.SELECTION_MULTIPLE)
                        " Pegando a linha selecionada "
                        modelo, caminhos = registro.get_selected_rows()
                        for caminho in caminhos:
                                kiter = modelo.get_iter(caminho)
                                cod = modelo.get_value(kiter, 7)
                        return cod
        ##########

    def on_buttonDelete_clicked(self, widget):
        valor = self.treev.get_cursor()
        n = valor[0]
        titulo = self.entryTitulo.props.text
        diretor = self.entryDiretor.props.text

        if n == None:
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Nenhum registro selecionado para exclusao')
            msg.set_position(gtk.WIN_POS_CENTER)
            msg.run()
            msg.destroy()
            #gtk.main()
        else:
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_QUESTION, gtk.BUTTONS_YES_NO, 'Deseja excluir o registro ?')
            resposta = msg.run()
            if resposta == gtk.RESPONSE_YES:
                valor = self.treev.get_cursor()
                n = valor[0]
                sql = "select * from filmes"
                self.cursor.execute(sql)
                resultado = self.cursor.fetchall()
                i = 0
                t1 = range(1)
                for linha in resultado:
                    t1[0] = i
                    t2 = n
                    print'esse'
                    print  t2
                
                    if t1[0] == t2[0]:
                        print t1
                        print t2
                        print '=============='
                        print linha[0]
                        print '==============='
                        #sql = "DELETE FROM filmes WHERE id = %i" % (linha[0])
                        sql=('''update filmes set titulo='%s' where id=%i '''%(titulo,linha[0]))
                        
                        self.cursor.execute(sql)
                        
                        self.conexao.commit()
                        
                    i = i+1
                self.leBanco()
                
            msg.destroy()
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Deletado com Sucesso!')
            msg.run()
            msg.destroy()
        gtk.main()
            


if __name__ == '__main__':
   O=Ola()
   #gtk.main()
   
