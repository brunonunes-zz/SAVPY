'''
Created on 23/07/2009

@author: Gustavo,Bruno,Eduardo
'''

import sys
try:
    #faz ligacao cm o model por causa do mvc exemplo quando termos 
    #que editar os dados que estao no model vao para o view
    #sys.path.append("C:\\Documents and Settings\\Administrador\\workspace\\agencia\\src\\model")
    import gtk,pygtk
    import gtk.glade
    import datetime
    import gobject
    import pygtk
    import pango
    #import pango
    pygtk.require('2.0')
    import gtk
    import gtk.glade
    from CadastrarCliente import *
    from ConsultarCliente import *
    from CadastrarVeiculo import *
    from ConsultarVeiculo import *
    from CadastrarVendedor import *
    from ConsultarVendedor import* 
    from ValidacaoUsuario import *
    from CadastroUsuario import *
    from Sobre import *
    from CadastrarFinanceira import *
    from ConsultarFinanceira import *
    from HistoricoVeiculo import *


    
    #import datetime
    #import MySQLdb
    #conn = MySQLdb.connect(host='localhost', user='root', 
    #passwd='carros', db='estudo')
        

except :#MySQLdb.Error, e:
    #print "Falha na conexao. Erro %d: %s" % (e.args[0], e.args[1])
    print ' Erro Ao Carregar um dos Import2'
    sys.exit(1)

class TelaPrincipal(object):
    '''
    classdocs
    '''

    
    def __init__(self):
        '''
        Constructor
        '''
        
        #O arquivo glade
        self.arquivoglade="C:\Documents and Settings\Bruno\Projects\principal\principal.glade"
        #Rereentacao do arquivo xml
        self.xml = gtk.glade.XML(self.arquivoglade)
       #Componentes da Janela TelaPrincipal
        self.principal = self.xml.get_widget('principal')
        #self.telaprincipal.set_title('Testando Titulo')
        #botao sair#
        self.sair=self.xml.get_widget('sair')
        self.image1=self.xml.get_widget('image1')
    
      # A barra de status que reber a data
        self.data = self.xml.get_widget('statusbar1')
        
        # O label que recebera a hora
        self.labelHora = self.xml.get_widget("labelHora")
        
        # Um temporizador para manter a hora atualiada
        self.timer = gobject.timeout_add(1000,self.on_timer)

        # Muda a fonte do rotulo
        self.labelHora.modify_font(pango.FontDescription('verdana 12'))

        
        self.sair.connect('activate', self.on_sair_activate)
        #conectando aos metodos callback
        self.xml.signal_autoconnect(self)
       # print self.data        #testando com o comando print
        #inseri a imagem na tela
        self.image1.set_from_file('Civic.jpg')
        #inserir i icone no canto direito do pc
        self.statusIcon = gtk.StatusIcon()
        self.statusIcon.set_from_file( "Civic.jpg")
        self.statusIcon.set_visible(True)
        self.principal.show_all()
        gtk.main()
    
        
        
        
    def on_timer(self):
        
        # Pega a hora do sistema
        hora = datetime.datetime.now().time().isoformat().split('.')[0]

        # Muda o texto do Label
        self.labelHora.set_text(hora)
        # Pega a data do sistema em formato ISO
        data = datetime.datetime.now().date().isoformat()
        data = 'Data: ' + '/'.join(data.split('-')[::-1])
        
        # Coloca a data na barra de status
        self.data.push(0, data)
        # Faz o temporiador rodar de novo
        return True
    def on_sair_activate (self,widget):
        print 'botao Sair'      
        self.principal.hide()
        gtk.main()  
    def on_cadastrar_cliente_activate(self,widget):
        cadasc=CadastrarCliente()
        gtk.main()
    def on_consultar_cliente_activate(self,widget):
        consulc=ConsultarCliente()
        gtk.main()
    def on_cadastrar_veiculo_activate(self,widget):
        cadasv=CadastrarVeiculo()
        gtk.main() 
    def on_consultar_veiculo_activate(self,widget):
        consulv=ConsultarVeiculo()
        gtk.main()
    def on_historico_veiculo_activate(self,widget):
        hv=HistoricoVeiculo()
        gtk.main()
    def on_cadastrar_usuario_activate(self,widget):
        cu=CadastroUsuario()
        gtk.main()  
    def on_permissao_usuario_activate(self,widget):
        P=PermissaoUsuario()    
        gtk.main()
    def on_cadastrar_vendedor_activate(self,widget):
        cadasvend=CadastrarVendedor()
        gtk.main() 
    def on_consultar_vendedor_activate(self,widget):
        consulvend=ConsultarVendedor()
        gtk.main()
    def on_sobre_activate(self,widget):
        s=Sobre()
        gtk.main()
    def on_cadastrar_financeira_activate(self,widget):
        cf=CadastrarFinanceira()
        gtk.main()
    def on_consultar_financeira_activate(self,widget):
        cof=ConsultarFinanceira()        
        gtk.main()
    #tirei a instancia pq no controller eu faco a mesma .
#if __name__ == '__main__':

if __name__ == '__main__':

    t= TelaPrincipal()
    
           
        