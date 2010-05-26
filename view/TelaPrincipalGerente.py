# -*- coding: utf-8 -*-
'''
Created on 23/07/2009

@author: Gustavo,Bruno,Eduardo
'''

import sys
try:
    
    import gtk.glade
    import datetime
    import pygtk
    import gtk
    from CadastrarCliente import *
    from ConsultarCliente import *
    from CadastrarVeiculo import *
    from ConsultarVeiculo import *
    from CadastrarVendedor import *
    from ConsultarVendedor import* 
    from CadastroUsuario import *
    from Sobre import *
    from CadastrarFinanceira import *
    from ConsultarFinanceira import *
    from CadastrarVenda import *
    from PermissaoUsuario import *
    from LoggofUsuario import *
    from ConsultarSenhaGerente import *
    from ConsultarHistoricoVeiculo import *
    from ConsultarVendaTroca import *
   

except :
    print ' Erro Ao Carregar um dos Import0'
    sys.exit(1)

class TelaPrincipalGerente(object):
    '''
    classdocs
    '''

    
    def __init__(self):
        '''
        Constructor
        '''

        #O arquivo glade
        self.arquivoglade="Projects\principal_gerente\principal_gerente.glade"
        #Rereentacao do arquivo xml
        self.xml = gtk.glade.XML(self.arquivoglade)
        #Componentes da Janela TelaPrincipal
        self.principal_gerente = self.xml.get_widget('principal_gerente')
        #self.telaprincipal.set_title('Testando Titulo')
        #botao sair#
        
        self.image1=self.xml.get_widget('image1')
        # A barra de status que reber a data
        self.data = self.xml.get_widget('statusbar')
        # O label que recebera a hora
        self.labelHora = self.xml.get_widget("labelHora")
        # Um temporizador para manter a hora atualiada
        self.timer = gobject.timeout_add(1000,self.on_timer)
        # Muda a fonte do rotulo
        self.labelHora.modify_font(pango.FontDescription('verdana 15'))
        #conectando aos metodos callback
        self.xml.signal_autoconnect(self)
       # print self.data        #testando com o comando print
        #inseri a imagem na tela
        self.image1.set_from_file('Civic.jpg')
        #inserir i icone no canto direito do pc
        self.statusIcon = gtk.StatusIcon()
        self.statusIcon.set_from_file( "sav.jpg")
        self.statusIcon.set_visible(True)
        self.principal_gerente.show_all()
        
        gtk.main()
    
        
        
    
    def on_timer(self):
        
        # Pega a hora do sistema
        hora = datetime.datetime.now().time().isoformat().split('.')[0]

        # Muda o texto do Label
        self.labelHora.set_text(hora)
        # Pega a data do sistema em formato ISO
        data = datetime.datetime.now().date().isoformat()
        data = '                                                                                                                                                                                                                                           ' + '/'.join(data.split('-')[::-1])
        
        # Coloca a data na barra de status
        self.data.push(0, data)
        # Faz o temporiador rodar de novo
        
        return True
    def on_sair_activate (self,widget):
        print 'botao Sair'      
        self.principal_gerente.hide()
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
    def on_cadastrar_usuario_activate(self,widget):
        cu=CadastroUsuario()
        #gtk.main()  
    def on_permissao_usuario_activate(self,widget):
        msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_QUESTION, gtk.BUTTONS_YES_NO, 'Deseja Fazer a Troca de Usuario ?')
        msg.set_position(gtk.WIN_POS_CENTER)
        resposta = msg.run()
        if resposta == gtk.RESPONSE_YES:
                self.principal_gerente.destroy()
                
                msg.destroy()
                print'gerente2'
                #P=LoggofUsuario()
                
    def on_trocar_usuario_activate(self,widget):
        msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_QUESTION, gtk.BUTTONS_YES_NO, 'Deseja Fazer a Troca de Usuario ?')
        msg.set_position(gtk.WIN_POS_CENTER)
        resposta = msg.run()
        if resposta == gtk.RESPONSE_YES:
                self.principal_gerente.destroy()
                msg.destroy()
                print'gerente1'
                t=LoggofUsuario()
        msg.destroy()
    def on_cadastrar_vendedor_activate(self,widget):
        cadasvend=CadastrarVendedor()
        #gtk.main() 
    def on_consultar_vendedor_activate(self,widget):
        consulvend=ConsultarVendedor()
        #gtk.main()
    def on_sobre_activate(self,widget):
        s=Sobre()
        #gtk.main()
    def on_cadastrar_financeira_activate(self,widget):
        cf=CadastrarFinanceira()
        #gtk.main()
    def on_consultar_financeira_activate(self,widget):
        cof=ConsultarFinanceira()        
        #gtk.main()
    def on_cadastrar_venda_activate(self,widget):
        cvr=CadastrarVenda()
        #gtk.main()
    def on_consultar_senha_gerente_activate(self,widget):
        csg=ConsultarSenhaGerente()
        #gtk.main()
    def on_consultar_historico_veiculo_activate(self,widget):
        csg=ConsultarHistoricoVeiculo()
        #gtk.main()
    def on_consultar_venda_activate(self,widget):
        cvt=ConsultarVendaTroca()
        #gtk.main()
        
    def on_principal_gerente_destroy(self,*args):
        print 'hueu'
        gtk.main_quit()
        

if __name__ == '__main__':

    t= TelaPrincipalGerente()
    
           
        