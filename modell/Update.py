'''
Created on 30/07/2009

@author: Administrador
'''
import sys

import pygtk
pygtk.require('2.0')
import gtk
import gtk.glade   
import MySQLdb

class Update(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        host= "localhost"
        user= "root"
        passwd= "carros"
        database = "locadora"
  # Abre a conexao com com o MySQL  
        titulo=str(raw_input("Digite o novo titulo que deseja atualizar:" ))
       # ano=int(raw_input("Digite o ano do aniversario:" ))
        diretor=str(raw_input("Digite o novo nome do diretor a ser modificado :" ))
        ano=int(raw_input("Digite o ano que voce deseja modificar os dados:" ))

        sql=('''update filmes set titulo='%s',diretor='%s' where ano=%i'''%(titulo,diretor,ano))
#sql=('''insert into filmes(id, titulo,ano,diretor) VALUES(%i,%s,%i,%s)'''%(id,titulo ,ano,diretor ))


 
        conexao=MySQLdb.connect(host, user, passwd)
                         # Pega o cursor para execucao de query   
        cursor = conexao.cursor()   
# Seleciona o banco de dados   
        conexao.select_db(database)   
# inserindo na tabela
# Dados para inclusao

# Executa o SQL para inclusao    
        cursor.execute(sql)
# Necessario para comandos de INSERT, UPDATE e DELETE   
# connection.commit()   
        conexao.commit()  
        cursor.close()
        print ' Atualizado Com sucesso'
        gtk.main()
if __name__ =='__main__':
    I=Update()
