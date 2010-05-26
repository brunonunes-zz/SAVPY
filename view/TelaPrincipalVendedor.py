# -*- coding: utf-8 -*-
'''
Created on 01/09/2009

@author: Administrador
'''
import sys
try:
   
    import gtk,pygtk
    import gtk.glade
    import datetime
    import gobject
    import pygtk
    import pango
    pygtk.require('2.0')
    import gtk
    import gtk.glade
    from CadastrarCliente import *
    from ConsultarCliente import *
    from CadastrarVeiculo import *
    from ConsultarVeiculo import *
    from Sobre import *
    from CadastrarVenda import *
    from PermissaoUsuario import *
    from ConsultarHistoricoVeiculo import *
    from ConsultarVendaTroca import  *
    from TelaPrincipalGerente import *#verificar
    from TelaPrincipalVendedor import *# verificar

except :
    print ' Erro Ao Carregar um dos Import3'
    sys.exit(1)

class TelaPrincipalVendedor(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        #O arquivo glade
        self.arquivoglade="Projects\principal_vendedor\principal_vendedor.glade"
        #Carrega a interface a partir do arquivo glade
        self.xml = gtk.glade.XML(self.arquivoglade)
       #Componentes da Janela TelaPrincipal
        self.principal_vendedor = self.xml.get_widget('principal_vendedor')
        self.image1=self.xml.get_widget('image1')
      # A barra de status que reber a data
        self.data = self.xml.get_widget('statusbar1')
        # O label que recebera a hora
        self.labelHora = self.xml.get_widget("labelHora")
        # Um temporizador para manter a hora atualizada
        self.timer = gobject.timeout_add(1000,self.on_timer)
        # Muda a fonte do rotulo
        self.labelHora.modify_font(pango.FontDescription('verdana 16'))
        # conecta sinais aos callbacks
        self.xml.signal_autoconnect(self)
        # inserir a imagem na tela
        self.image1.set_from_file('Civic.jpg')
        # inserir o icone no canto direito do pc
        self.statusIcon = gtk.StatusIcon()
        self.statusIcon.set_from_file( "Civic.jpg")
        self.statusIcon.set_visible(True)
        # Exibe toda a interface grafica
        self.principal_vendedor.show_all()
        # Inicia o loop principal de eventos (GTK MainLoop)
        gtk.main()
    
    #Callbacks
    
    def on_timer(self):
        
        # Pega a hora do sistema
        hora = datetime.datetime.now().time().isoformat().split('.')[0]

        # Muda o texto do Label
        self.labelHora.set_text(hora)
        # Pega a data do sistema em formato ISO
        data = datetime.datetime.now().date().isoformat()
        data = '                                                                                                                                                                                                                                              ' +'/'.join(data.split('-')[::-1])
        
        # Coloca a data na barra de status
        self.data.push(0, data)
        # Faz o temporiador rodar de novo
        return True
    def on_sair_activate (self,widget):
        print 'botao Sair'      
        self.principal_vendedor.hide()
        gtk.main_quit()
        
    def on_cadastrar_cliente_activate(self,widget):
        cadasc=CadastrarCliente()
        #gtk.main()
    def on_consultar_cliente_activate(self,widget):
        consulc=ConsultarCliente()
        #gtk.main()
    def on_cadastrar_veiculo_activate(self,widget):
        cadasv=CadastrarVeiculo()
        #gtk.main() 
    def on_consultar_veiculo_activate(self,widget):
        consulv=ConsultarVeiculo()
        #gtk.main()
    
    def on_sobre_activate(self,widget):
        s=Sobre()
        gtk.main_quit()
        
    def on_cadastrar_venda_activate(self,widget):
        cvr=CadastrarVenda()
        #gtk.main()
        
    def on_consultar_historico_veiculo_activate(self,widget):
        csg=ConsultarHistoricoVeiculo()
        #gtk.main()
        
    def on_consultar_venda_activate(self,widget):
        cvt=ConsultarVendaTroca()
        #gtk.main()    
    
    def on_principal_vendedor_destroy(self,*args):
        print 'hueu'
        #Sai do loop principal de eventos, finalizando o programa
        gtk.main_quit()
        
#Inicia a aplicacao
if __name__ == '__main__':

    t= TelaPrincipalVendedor()
    