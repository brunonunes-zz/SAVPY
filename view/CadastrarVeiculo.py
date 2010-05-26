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
    import datetime
    import MySQLdb
    import os.path
except:
    print ' Erro Ao Carregar um dos Importfm'
    sys.exit(1)

class CadastrarVeiculo(object):
    def __init__(self):
        self.host= "localhost"
        self.user= "root"
        self.passwd= "carros"  
        self.database = "agenciaBeta1" 
        
        #Setando a variavel com o arquivo glade
        self.arquivoglade = "Projects\cadastro_veiculo\cadastro_veiculo.glade"
        #Extraindo conteudo XML do arquivo
        self.xml = gtk.glade.XML(self.arquivoglade)        
        #Componentes da Janela CadastrarVeiculo
        self.cadastro_veiculo=self.xml.get_widget('cadastro_veiculo')
        self.buttonSalvar= self.xml.get_widget('buttonSalvar')
        self.buttonSair=self.xml.get_widget('buttonSair')
        
        #instancia todos os componentes da tela Descricao do Veiculo
        self.entryPlaca=self.xml.get_widget('entryPlaca')
        self.entryRenavam=self.xml.get_widget('entryRenavam')
        self.entryChassi=self.xml.get_widget('entryChassi')
        self.entryFabricante=self.xml.get_widget('entryFabricante')
        self.entryModelo=self.xml.get_widget('entryModelo')
        self.entryMarca=self.xml.get_widget('entryMarca')
        self.entryAno=self.xml.get_widget('entryAno')
        self.entryCidade=self.xml.get_widget('entryCidade')
        self.comboUfDescricao=self.xml.get_widget('comboUfDescricao')
        self.entryCombustivel=self.xml.get_widget('entryCombustivel')
        self.entryKm=self.xml.get_widget('entryKm')
        self.entryCor=self.xml.get_widget('entryCor')
        self.entryPortas=self.xml.get_widget('entryPortas')
        self.comboPdianteiro=self.xml.get_widget('comboPdianteiro')
        self.comboPtraseiro=self.xml.get_widget('comboPtraseiro')
        self.comboEstepe=self.xml.get_widget('comboEstepe')
        self.comboRodas=self.xml.get_widget('comboRodas')
        self.comboColisao=self.xml.get_widget('comboColisao')
        self.comboSuspensao=self.xml.get_widget('comboSuspensao')
        self.comboFunilaria=self.xml.get_widget('comboFunilaria')
        self.comboPintura=self.xml.get_widget('comboPintura')
        self.comboEstofado=self.xml.get_widget('comboEstofado')
        self.comboMotor=self.xml.get_widget('comboMotor')
        self.comboCambio=self.xml.get_widget('comboCambio')
        self.comboAdianteiro=self.xml.get_widget('comboAdianteiro')
        self.comboAtraseiro=self.xml.get_widget('comboAtraseiro')
        self.anotacoes=self.xml.get_widget('anotacoes')
        
        #coloca o foco no primeiro item do combobox
        self.comboUfDescricao.set_active(0)
        self.comboPdianteiro.set_active(0)
        self.comboPtraseiro.set_active(0)
        self.comboEstepe.set_active(0)
        self.comboRodas.set_active(0)
        self.comboColisao.set_active(0)
        self.comboSuspensao.set_active(0)
        self.comboFunilaria.set_active(0)
        self.comboPintura.set_active(0)
        self.comboEstofado.set_active(0)
        self.comboMotor.set_active(0)
        self.comboCambio.set_active(0)
        self.comboAdianteiro.set_active(0)
        self.comboAtraseiro.set_active(0)
        #==========================================================
        #instancia todos os componentes da tela Documentacao do Veiculo
        self.entryPlacad=self.xml.get_widget('entryPlacad')
        self.entryRenavamd=self.xml.get_widget('entryRenavamd')
        self.entryIpvad=self.xml.get_widget('entryIpvad')
        self.entryChassid=self.xml.get_widget('entryChassid')
        self.entryProprietariod=self.xml.get_widget('entryProprietariod')
        self.comboUfd=self.xml.get_widget('comboUfd')
        self.entryEnderecod=self.xml.get_widget('entryEnderecod')
        self.entryCpfd=self.xml.get_widget('entryCpfd')
        self.entryBairrod=self.xml.get_widget('entryBairrod')
        
        #foco no primeiro item do combobox
        self.comboUfd.set_active(0)
        #============================================================
        #instancia todos os componentes da tela Valor do Veiculo
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
        self.entryPorcentagem=self.xml.get_widget('entryPorcentagem')
        #=====================================================================        
        # Autoconnect Signals and Callbacks
        self.xml.signal_autoconnect(self)
        self.cadastro_veiculo.show_all()
        self.criartabela()
        gtk.main()
         
    def criartabela(self):
        
        if  not os.path.exists('agenciaBeta.db'):
                    conexao = MySQLdb.connect(host="localhost", user="root",passwd="carros", db="agenciaBeta1")
                    cursor = conexao.cursor()
                    #executei 3 comando de sql porque minha tela sera dentro de um componente notebook
                    #sql referente a primeira aba descricao do veiculo
                    sql1 = """create table desv(
                        codigoveiculo  int(10)PRIMARY KEY AUTO_INCREMENT NOT NULL UNIQUE ,
                        placa varchar(7) not null,
                        renavam varchar(9) not null,
                        chassi varchar(17) not null,
                        fabricante varchar (30),
                        modelo varchar(35) not null,
                        marca varchar(40) not null,
                        anofabricacao varchar(4) not null,
                        cidade varchar(50) not null,
                        uf varchar (2) not null,
                        combustivel varchar(20) not null,
                        km varchar(10) not null,
                        cor varchar(20)not null,
                        numerosportas varchar(4) not null,
                        pneuDianteiro varchar(7) not null,
                        pneuTrazeiro varchar(7)not null,
                        pneuEstepe varchar(7)not null,
                        pneuRoda varchar(7)not null,
                        colisao varchar(20)not null,
                        suspensao varchar(7)not null,
                        funilaria varchar(7)not null, 
                        pintura varchar(7)not null,
                        estofado varchar(7)not null,
                        motor varchar(7)not null,
                        cambio varchar(7)not null,
                        amortecedordianteiro varchar(7)not null,
                        amortecedortrazeiro varchar(7)not null,
                        anotacoes varchar(300),
                        disponibilidade varchar (20) not null,
                        data varchar(20))"""
                    #sql referente a segunda aba documentacao veiculo   
                    sql2="""create table docv(
                        codigodocumentacao  int(10)PRIMARY KEY AUTO_INCREMENT NOT NULL UNIQUE ,
                        placad varchar(7),
                        renavamd varchar(20),
                        ipvad varchar(20) not null,
                        chassid varchar(30) not null,
                        proprietariod varchar(60) not null,
                        ufd varchar(2) not null,
                        enderecod varchar(60) not null,
                        cpfd varchar(11) not null,
                        bairrod varchar(50) not null,
                        datad varchar(20))"""
                        #sql referente a terceira aba valor veiculo
                    sql3="""create table vv(
                        codigovalor  int(10)PRIMARY KEY AUTO_INCREMENT NOT NULL UNIQUE ,
                        placav varchar(7),
                        renavamv varchar(15),
                        documento float(10),
                        motor float(10),
                        freio float(10),
                        cambio float(10),
                        funilaria float(10),
                        multas float(10),
                        outros float(10),
                        valorcompraveiculo float(10) ,
                        totalgastos float(10),
                        porcentagemlucro float(10),
                        valorsugeridovenda float(10),
                        lucroagencia float(10),
                        datav varchar(20))"""

                    try:     
                            cursor.execute(sql1)
                            cursor.execute(sql2)
                            cursor.execute(sql3)
                            conexao.commit()
                            
                    except MySQLdb.Error, e:
                    
                       if e.args[0] == 1050:                     
                         print  'Tratando o erro'
                             
    def on_buttonSalvar_clicked (self,widget):
        print'buttoSalvar'

                       
        if (self.entryPlaca.props.text == "" or self.entryRenavam.props.text=="" or self.entryDocumento.props.text == "" or self.entryMotor.props.text == "" or self.entryFreio.props.text == "" or self.entryCambio.props.text == "" or self.entryFunilaria.props.text == "" or self.entryMultas.props.text == "" ):
        
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Por favor preencha os campos Marcado com *')
            resposta=msg.run()
            msg.destroy()
            
        else:
            
            #DESCRICAO DO VEICULO
            placa = self.entryPlaca.props.text
            renavam= self.entryRenavam.props.text
            chassi= self.entryChassi.props.text
            fabricante= self.entryFabricante.props.text
            modelo= self.entryModelo.props.text
            marca= self.entryMarca.props.text
            anofabricacao=self.entryAno.props.text
            cidade= self.entryCidade.props.text
            uf=self.comboUfDescricao.get_active_text()
            combustivel= self.entryCombustivel.props.text
            km=self.entryKm.props.text
            cor=self.entryCor.props.text
 #          portas=self.entryPortas.props.text
            numerosportas=self.entryPortas.props.text
            pdianteiro=self.comboPdianteiro.get_active_text()
            ptraseiro=self.comboPtraseiro.get_active_text()
            estepe=self.comboEstepe.get_active_text()
            rodas=self.comboRodas.get_active_text()
            colisao=self.comboColisao.get_active_text()
            suspensao=self.comboSuspensao.get_active_text()
            funilaria=self.comboFunilaria.get_active_text()
            pintura=self.comboPintura.get_active_text()
            estofado=self.comboEstofado.get_active_text()
            motor=self.comboMotor.get_active_text()
            cambio=self.comboCambio.get_active_text()
            adianteiro=self.comboAdianteiro.get_active_text()
            atraseiro=self.comboAtraseiro.get_active_text()
            disponibilidade='Estoque'
            data1 = datetime.datetime.now().date().isoformat()
            data=  '/'.join(data1.split('-')[::-1])
            


            #DOCUMENTACAO VEICULO
            placad=self.entryPlaca.props.text#para facilicar na consuta eu peguei o valor da placa da descricao do veiculo e joguei na documentacao e valor do veiculo
            renavamd=self.entryRenavam.props.text
            ipvad=self.entryIpvad.props.text
            chassid=self.entryChassid.props.text
            proprietariod=self.entryProprietariod.props.text
            ufd=self.comboUfd.get_active_text()
            enderecod=self.entryEnderecod.props.text
            cpfd=self.entryCpfd.props.text
            bairrod=self.entryBairrod.props.text
            datad=data
            
            #VALOR VEICULO
            placav=self.entryPlaca.props.text
            renavamv=self.entryRenavam.props.text#self.entryRenavamv.props.text
            documentov=float(self.entryDocumento.props.text)
            motorv=float(self.entryMotor.props.text)
            freiov=float(self.entryFreio.props.text)
            cambiov=float(self.entryCambio.props.text)
            funilariav=float(self.entryFunilaria.props.text)
            multasv=float(self.entryMultas.props.text) 
            outrosv=float(self.entryOutros.props.text)
            valorcompraveiculov=float(self.entryValorCompra.props.text)
            totalgastosv=documentov+motorv+freiov+cambiov+funilariav+multasv+outrosv    
            porcentagemlucrov=float(self.entryPorcentagem.props.text)
            lucroagenciav= ((valorcompraveiculov+(totalgastosv))*(porcentagemlucrov/100))
            valorsugeridovendav=((valorcompraveiculov+totalgastosv)+(lucroagenciav))#*(porcentagemlucrov/100))+((valorcompraveiculov+totalgastosv))
            datav=data
            #vendo qual tipo e essa variavel            
 
            " Limpando os campos "
            #Descricao do Veiculo
           # if(self.entryRenavam.props.text == self.entryRenavamd.props.text == self.entryRenavamv.props.text and self.entryPlacad.props.text == self.entryPlacav.props.text == self.entryPlaca.props.text):

            self.entryPlaca.props.text = ""
            self.entryRenavam.props.text = ""
            self.entryChassi.props.text = ""
            self.entryFabricante.props.text = ""
            self.entryModelo.props.text = ""
            self.entryMarca.props.text = ""
            self.entryAno.props.text = ""
            self.entryCidade.props.text = ""
            self.comboUfDescricao.set_active(0)
            self.entryCombustivel.props.text = ""
            self.entryKm.props.text = ""
            self.entryCor.props.text = ""
            self.entryPortas.props.text = ""
            self.comboPdianteiro.set_active
            self.comboPtraseiro.set_active(0)
            self.comboEstepe.set_active(0)
            self.comboRodas.set_active(0)
            self.comboColisao.set_active(0)
            self.comboSuspensao.set_active(0)
            self.comboFunilaria.set_active(0)
            self.comboPintura.set_active(0)
            self.comboEstofado.set_active(0)
            self.comboMotor.set_active(0)
            self.comboCambio.set_active(0)
            self.comboAdianteiro.set_active(0)
            self.comboAtraseiro.set_active(0)

            #Documentacao do Veiculo
            
            self.entryIpvad.props.text = ""
            self.entryChassid.props.text = ""
            self.entryProprietariod.props.text = ""
            self.comboUfd.set_active(0)
            self.entryEnderecod.props.text = ""
            self.entryCpfd.props.text = ""
            self.entryBairrod.props.text = ""
              
                #Valor do Veiculo            
            
            self.entryDocumento.props.text = .00
            self.entryMotor.props.text = .00
            self.entryFreio.props.text = 0.0
            self.entryCambio.props.text =0.0
            self.entryFunilaria.props.text = 0.0
            self.entryMultas.props.text = 0.0
            self.entryOutros.props.text = 0.0
            self.entryValorCompra.props.text = 0.0
            self.entryPorcentagem.props.text=1.0
            #self.entryTotal.props.text = 0.0
            #self.entryCalculado.props.text = 0.0
              
            #===========================================================
                #gravando dados no Banco
                # mesmo nome igual ao banco de dados
            sql1 = "insert into desv(placa,renavam,chassi,fabricante,modelo,marca,anofabricacao,cidade,uf,combustivel,km,cor,numerosportas,pneuDianteiro,pneuTrazeiro,pneuEstepe,pneuRoda,colisao,suspensao,funilaria,pintura,estofado,motor,cambio,amortecedordianteiro,amortecedortrazeiro,disponibilidade,data) values('" + placa + "', '" + renavam  + "', '" + chassi + "','" + fabricante  + "', '" + modelo  + "', '" + marca + "','" + anofabricacao + "', '" + cidade + "', '" + uf + "', '" + combustivel + "','" + km + "', '" + cor + "', '" + numerosportas + "','" + pdianteiro + "','" + ptraseiro+ "','" + estepe + "','" + rodas + "','" + colisao + "','" + suspensao + "','" + funilaria + "','" + pintura + "','" + estofado + "','" + motor + "','" + cambio + "','" + adianteiro + "','" + atraseiro + "','" + disponibilidade + "','" + data + "' )"
            sql2 = "insert into docv(placad,renavamd,ipvad,chassid,proprietariod,ufd,enderecod,cpfd,bairrod,datad) values('" + placad + "', '" + renavamd  + "', '" + ipvad + "', '" + chassid + "','" + proprietariod  + "', '" + ufd + "', '" + enderecod + "','" + cpfd  + "', '" + bairrod + "', '" + datad + "')"
                #pedi pra recber float mais na verdade tudo que digitamos vem em formato instring temos que transformar string em float
                #('" + documento + "', '" + motor  + "', '" + freio + "','" + cambio  + "', '" + funilaria  + "', '" + multas + "','" + outros + "', '" + valorcompraveiculo + "', '" + totalgastos + "','" + porcentagemlucro + "', '" + valorsugeridovenda + "')"
            sql3 = "insert into vv(placav,renavamv,documento,motor,freio,cambio,funilaria,multas,outros,valorcompraveiculo,totalgastos,porcentagemlucro,valorsugeridovenda,lucroagencia) values('" + placav + "','" + renavamv + "',%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f)"%(documentov,motorv,freiov,cambiov,funilariav,multasv,outrosv,valorcompraveiculov,totalgastosv,porcentagemlucrov,valorsugeridovendav,lucroagenciav)
    
            self.conexao=MySQLdb.connect(self.host,self.user,self.passwd,self.database)
            self.cursor = self.conexao.cursor()
            self.cursor.execute(sql1)
            self.cursor.execute(sql2)
            self.cursor.execute(sql3)
        
            self.conexao.commit()#Para enviar tudo para o Banco
                
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Cadastrado Com Sucesso')
            msg.run()
            msg.destroy()
           # else:
            #    msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Placas e Renavam deve ser iguais em todas as Abas  ')
             #   msg.run()
              #  msg.destroy()
        #gtk.main()
        

    def on_buttonSair_clicked (self,widget):
        print'buttonSair'
        self.cadastro_veiculo.hide()
        gtk.main_quit()
                   
    def on_cadastro_veiculo_destroy(self,*args):
        print'ii'
        gtk.main_quit()

if __name__ == '__main__':

    cv = CadastrarVeiculo()
    #gtk.main()
  
