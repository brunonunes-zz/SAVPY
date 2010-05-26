
'''
Created on 22/07/2009

@author: Gustavo
'''

import sys
import gtk
import pygtk
import MySQLdb
sys.path.append("C:\\Documents and Settings\\Administrador\\workspace\\agencia\\src\\controller")
#importando a classe ControllerPrincipal do pacote controller
from ControllerTelaPrincipal import *

class ConexaoMysql(object):
    def __init__(self):
 
       
# Abre a conexao com com o MySQL 
        self.host= "localhost"
        self.user= "root"
        self.passwd= "carros"
        self.database = "tete"
        #chama o metodo a ser executado executa somente um metodo.
        #self.consulta()
        self.criatabelaedatabase()
       
         
            
    def criatabelaedatabase(self):  
      
        try:
            #verifica se o data base nomeado acima ja foi criado 
            
            self.conexao = MySQLdb.connect(self.host,self.user,self.passwd,self.database)
            print ' Banco de Dados ja instalado'
            
          
        except MySQLdb.Error, e:
            #caso nao foi criado cria o database e a tabela referete a ele
            
            if e.args[0] == 1049:
                msg1 = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Esse software depende do Mysql instalado em sua maquina!')
                msg1.run()
                msg1.destroy()
                msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_QUESTION, gtk.BUTTONS_YES_NO, 'Base de dados inexistente. Deseja criar? ?')
                resposta = msg.run()
                if resposta == gtk.RESPONSE_YES:
                    
                    self.conexao = MySQLdb.connect(self.host,self.user,self.passwd)
                    self.cursor = self.conexao.cursor()
                    
                    self.cursor.execute('create database %s' %self.database)
                    
                 
                    self.cursor.close()
                    msg.destroy() 
        # criando a tabela t
            
                    self.conexao = MySQLdb.connect(host="localhost", user="root",passwd="carros", db="tete")
                    self.cursor = self.conexao.cursor()
                    sql = """create table exe (
                              nome  varchar(20) not null,
                              sobrenome  varchar(20),
                             ano int,  
                             sexo char(1))"""
                    self.cursor.execute(sql)
                    self.conexao.commit()
        #chamo o metodo consultar            
        self.consulta()
        gtk.main()
        #######################################################
        
        #codigo abaixo referente a consulta
        ######################################################## 
       # Executa uma consulta   
    def consulta(self):
        self.conexao = MySQLdb.connect(self.host,self.user,self.passwd)
# Pega o cursor para execucao de query   
        self.cursor = self.conexao.cursor()   
# Seleciona o banco de dados   
        self.conexao.select_db(self.database)
           
        self.cursor.execute("select * from exe ")

# Faz fetch do resultado   
        self.resultado = self.cursor.fetchall()   
        
        for self.linha in self.resultado:        
             print self.linha[0], self.linha[1],self.linha[2] 
        self.conexao.close()
        #gtk.main()           
        gtk.main()
          
            
if __name__ == '__main__':
 c=ConexaoMysql()
 