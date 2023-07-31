from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.clock import Clock
import webbrowser
import keyboard as k



class Adm (ScreenManager):
    pass

class Principal (Screen):



    def add1 (self):
     # estabelecendo caminho para a id "carrinho" dispensando o "self"
        carrinho = self.manager.get_screen('carrinho')


        if carrinho.ids.pedido1.text =="" :
            carrinho.ids.pedido1.text = "Super bacon (1)"
            self.ids.label1.text = "Adicionado ao carrinho"
            ####### temporizando a label1 com a função reset_label_text no clock schedule ############
            Clock.schedule_once(self.reset_label_text, 2)

        elif carrinho.ids.pedido2.text =="":
            carrinho.ids.pedido2.text = "Super bacon (1)"
            self.ids.label1.text = "Adicionado ao carrinho"
            Clock.schedule_once(self.reset_label_text, 2)
        elif carrinho.ids.pedido3.text =="":
            carrinho.ids.pedido3.text = "Super bacon (1)"
            self.ids.label1.text = "Adicionado ao carrinho"
            Clock.schedule_once(self.reset_label_text, 2)
        elif carrinho.ids.pedido4.text =="":
            carrinho.ids.pedido4.text = "Super bacon (1)"
            self.ids.label1.text = "Adicionado ao carrinho"
            Clock.schedule_once(self.reset_label_text, 2)
        elif carrinho.ids.pedido5.text =="":
            carrinho.ids.pedido5.text = "Super bacon (1)"
            self.ids.label1.text = "Adicionado ao carrinho"
            Clock.schedule_once(self.reset_label_text, 2)

    def add2 (self):

        carrinho = self.manager.get_screen('carrinho')

        if carrinho.ids.pedido1.text =="" :
            carrinho.ids.pedido1.text = "X-TUDO (1)"
            self.ids.label1.text = "Adicionado ao carrinho"
            ####### temporizando a label1 com a função reset_label_text no clock schedule ############
            Clock.schedule_once(self.reset_label_text, 2)

        elif carrinho.ids.pedido2.text =="":
            carrinho.ids.pedido2.text = "X-TUDO (1)"
            self.ids.label1.text = "Adicionado ao carrinho"
            Clock.schedule_once(self.reset_label_text, 2)
        elif carrinho.ids.pedido3.text =="":
            carrinho.ids.pedido3.text = "X-TUDO (1)"
            self.ids.label1.text = "Adicionado ao carrinho"
            Clock.schedule_once(self.reset_label_text, 2)
        elif carrinho.ids.pedido4.text =="":
            carrinho.ids.pedido4.text = "X-TUDO (1)"
            self.ids.label1.text = "Adicionado ao carrinho"
            Clock.schedule_once(self.reset_label_text, 2)
        elif carrinho.ids.pedido5.text =="":
            carrinho.ids.pedido5.text = "X-TUDO (1)"
            self.ids.label1.text = "Adicionado ao carrinho"
            Clock.schedule_once(self.reset_label_text, 2)

    def add3 (self):

        carrinho = self.manager.get_screen('carrinho')

        if carrinho.ids.pedido1.text =="" :
            carrinho.ids.pedido1.text = "X-EGG (1)"
            self.ids.label1.text = "Adicionado ao carrinho"
            ####### temporizando a label1 com a função reset_label_text no clock schedule ############
            Clock.schedule_once(self.reset_label_text, 2)

        elif carrinho.ids.pedido2.text =="":
            carrinho.ids.pedido2.text = "X-EGG (1)"
            self.ids.label1.text = "Adicionado ao carrinho"
            Clock.schedule_once(self.reset_label_text, 2)
        elif carrinho.ids.pedido3.text =="":
            carrinho.ids.pedido3.text = "X-EGG (1)"
            self.ids.label1.text = "Adicionado ao carrinho"
            Clock.schedule_once(self.reset_label_text, 2)
        elif carrinho.ids.pedido4.text =="":
            carrinho.ids.pedido4.text = "X-EGG (1)"
            self.ids.label1.text = "Adicionado ao carrinho"
            Clock.schedule_once(self.reset_label_text, 2)
        elif carrinho.ids.pedido5.text =="":
            carrinho.ids.pedido5.text = "X-EGG (1)"
            self.ids.label1.text = "Adicionado ao carrinho"
            Clock.schedule_once(self.reset_label_text, 2)

    def add4 (self):

        carrinho = self.manager.get_screen('carrinho')

        if carrinho.ids.pedido1.text =="" :
            carrinho.ids.pedido1.text = "HOT-DOG (1)"
            self.ids.label1.text = "Adicionado ao carrinho"
            ####### temporizando a label1 com a função reset_label_text no clock schedule ############
            Clock.schedule_once(self.reset_label_text, 2)

        elif carrinho.ids.pedido2.text =="":
            carrinho.ids.pedido2.text = "HOT-DOG (1)"
            self.ids.label1.text = "Adicionado ao carrinho"
            Clock.schedule_once(self.reset_label_text, 2)
        elif carrinho.ids.pedido3.text =="":
            carrinho.ids.pedido3.text = "HOT-DOG (1)"
            self.ids.label1.text = "Adicionado ao carrinho"
            Clock.schedule_once(self.reset_label_text, 2)
        elif carrinho.ids.pedido4.text =="":
            carrinho.ids.pedido4.text = "HOT-DOG (1)"
            self.ids.label1.text = "Adicionado ao carrinho"
            Clock.schedule_once(self.reset_label_text, 2)
        elif carrinho.ids.pedido5.text =="":
            carrinho.ids.pedido5.text = "HOT-DOG (1)"
            self.ids.label1.text = "Adicionado ao carrinho"
            Clock.schedule_once(self.reset_label_text, 2)


    def add5 (self):

        carrinho = self.manager.get_screen('carrinho')

        if carrinho.ids.pedido1.text =="" :
            carrinho.ids.pedido1.text = "Batata frita (1)"
            self.ids.label1.text = "Adicionado ao carrinho"
            ####### temporizando a label1 com a função reset_label_text no clock schedule ############
            Clock.schedule_once(self.reset_label_text, 2)

        elif carrinho.ids.pedido2.text =="":
            carrinho.ids.pedido2.text = "Batata frita (1)"
            self.ids.label1.text = "Adicionado ao carrinho"
            Clock.schedule_once(self.reset_label_text, 2)
        elif carrinho.ids.pedido3.text =="":
            carrinho.ids.pedido3.text = "Batata frita (1)"
            self.ids.label1.text = "Adicionado ao carrinho"
            Clock.schedule_once(self.reset_label_text, 2)
        elif carrinho.ids.pedido4.text =="":
            carrinho.ids.pedido4.text = "Batata frita (1)"
            self.ids.label1.text = "Adicionado ao carrinho"
            Clock.schedule_once(self.reset_label_text, 2)
        elif carrinho.ids.pedido5.text =="":
            carrinho.ids.pedido5.text = "Batata frita (1)"
            self.ids.label1.text = "Adicionado ao carrinho"
            Clock.schedule_once(self.reset_label_text, 2)


    def add6 (self):

        carrinho = self.manager.get_screen('carrinho')

        if carrinho.ids.pedido1.text =="" :
            carrinho.ids.pedido1.text = "Coca-cola lata (1)"
            self.ids.label1.text = "Adicionado ao carrinho"
            ####### temporizando a label1 com a função reset_label_text no clock schedule ############
            Clock.schedule_once(self.reset_label_text, 2)

        elif carrinho.ids.pedido2.text =="":
            carrinho.ids.pedido2.text = "Coca-cola lata (1)"
            self.ids.label1.text = "Adicionado ao carrinho"
            Clock.schedule_once(self.reset_label_text, 2)
        elif carrinho.ids.pedido3.text =="":
            carrinho.ids.pedido3.text = "Coca-cola lata (1)"
            self.ids.label1.text = "Adicionado ao carrinho"
            Clock.schedule_once(self.reset_label_text, 2)
        elif carrinho.ids.pedido4.text =="":
            carrinho.ids.pedido4.text = "Coca-cola lata (1)"
            self.ids.label1.text = "Adicionado ao carrinho"
            Clock.schedule_once(self.reset_label_text, 2)
        elif carrinho.ids.pedido5.text =="":
            carrinho.ids.pedido5.text = "Coca-cola lata (1)"
            self.ids.label1.text = "Adicionado ao carrinho"
            Clock.schedule_once(self.reset_label_text, 2)



    def reset_label_text(self, dt):
        self.ids.label1.text = ""






class Carrinho (Screen):
    def apaga1 (self):
        self.ids.pedido1.text =""

    def apaga2 (self):
        self.ids.pedido2.text =""

    def apaga3 (self):
        self.ids.pedido3.text =""

    def apaga4 (self):
        self.ids.pedido4.text =""

    def apaga5 (self):
        self.ids.pedido5.text =""



class Pagamento (Screen):

    def pagamento1 (self):
        self.ids.label2.text = "Pagamento: PIX"

    def pagamento2 (self):
        self.ids.label2.text = "Pagamento: Cartão"

    def pagamento3 (self):
        self.ids.label2.text = "Pagamento: Dinheiro"

    def pegar1 (self):
        self.ids.label3.text = "Retirada: Retirar no local"

    def pegar2 (self):
        self.ids.label3.text = "Retirada: Solicito entrega"



    def envia (self):
        carrinho = self.manager.get_screen('carrinho')

        pedido1 = carrinho.ids.pedido1.text
        pedido2 = carrinho.ids.pedido2.text
        pedido3 = carrinho.ids.pedido3.text
        pedido4 = carrinho.ids.pedido4.text
        pedido5 = carrinho.ids.pedido5.text
        pagamento = self.ids.label2.text
        retirada = self.ids.label3.text

        pedido_final = "- "+pedido1+"\n\n" + "- "+pedido2+"\n\n" + "- "+pedido3+"\n\n" + "- "+pedido4+"\n\n" + "- "+pedido5+"\n\n\n" + "- "+pagamento+"\n\n" + "- "+retirada+"\n"


        number = "+5581996746778"
        message = pedido_final
        whatsapp_link = f"https://api.whatsapp.com/send?phone={number}&text={message}"
        webbrowser.open(whatsapp_link)
        k.press_and_release('enter')





class MainApp (MDApp):
    def fechar(self):
        self.stop()

    def build (self):

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"
        return Adm()




MainApp().run()
