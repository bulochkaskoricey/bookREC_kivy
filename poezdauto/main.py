from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import mainthread
import threading
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
import webbrowser
from kivy.factory import Factory

Window.clearcolor = (255 / 255, 198 / 255, 123 / 255, 222)
Window.title = "PoezdRu"

Builder.load_string("""




<MenuScreen>:

    labelone: Label
    
    BoxLayout:
        
	    orientation: "vertical"
        spacing: 20
	    
	    
        

        


	    MDLabel:
	        id: Label
		    font_size: "15sp"
		    multiline: True
		    text_size: self.width*0.98, None
		    size_hint_x: 1.0
		    size_hint_y: 1.0
		    height: self.texture_size[1] + 15
            text: "   ".format(app.theme_cls.theme_style)
		    markup: True
		    on_ref_press: root.linki()	
            halign: 'center'
            color: 'black'
		



	    MDRaisedButton:
		    text: "Книга Рецептов"
		    bold: True
		    
		    background_color:'#3A79FF'
		    size_hint: ( . 0.7, 0.5)
		    on_press: root.manager.current = 'pay'
		    color:'#E6F1FF'
		    padding_y: (9)
            pos_hint: {"center_x": 0.5, "center_y":0.5}
            size_hint: (0.4, 0.4)
            icon: "1234.png"
            shadow_radius: 6
            shadow_offset: 0, 2
            
        MDRaisedButton
            text: "Новости"
		    bold: True
		    background_color:'#476BD6'
		    size_hint: (0.7, 0.5)
		    on_press: root.manager.current = 'news'
		    color:'#E6F1FF'
            halign: 'center'
            pos_hint: {"center_x": 0.5, "center_y":0.5}
            size_hint: (0.4, 0.4)
            icon: "12345.png"
		    shadow_radius: 6
            shadow_offset: 0, 2
        
	    MDRaisedButton
		    text: "Сообщить об ошибке"
		    bold: True
		    background_color:'#476BD6'
		    size_hint: (0.7, 0.5)
		    on_press: root.callback3()
		    color:'#E6F1FF'
            halign: 'center'
            pos_hint: {"center_x": 0.5, "center_y":0.5}
            size_hint: (0.4, 0.4)
            icon: "12345.png"
		    shadow_radius: 6
            shadow_offset: 0, 2


	    MDRaisedButton:
	        id: Button_4
		    text: "О работе"
		    bold: True
		    background_color:'#476BD6'
		    size_hint: (0.7, 0.5)
		    color:'#E6F1FF'
		    on_press: root.callback4()
            halign: 'center'
            pos_hint: {"center_x": 0.5, "center_y":0.5}
            size_hint: (0.4, 0.4)
            icon: "123456.png"
            shadow_radius: 6
            shadow_offset: 0, 2

        
            
        MDBottomNavigation:
            #panel_color: "#eeeaea"
            selected_color_background: "orange"
            text_color_active: "lightgrey"

            MDBottomNavigationItem:
                name: 'screen 1'
                text: 'Mail'
                icon: 'gmail'
                badge_icon: "numeric-10"
                

                MDLabel:
                    text: 'Mail'
                    halign: 'center'
                    color: 'black'
                    


            MDBottomNavigationItem:
                name: 'screen 2'
                text: 'Twitter'
                icon: 'twitter'
                badge_icon: "numeric-5"

                MDLabel:
                    text: 'Twitter'
                    halign: 'center'
                    color: 'black'

            MDBottomNavigationItem:
                name: 'screen 3'
                text: 'LinkedIN'
                icon: 'linkedin'

                MDLabel:
                    text: 'LinkedIN'
                    halign: 'center'
                    color: 'black'
                    
<SettingsScreen>:
    txt: txt
    inf:Inf
    
    BoxLayout:
        orientation: "vertical"
	    
	    
	    spacing:20
	    
	    MDLabel:
	        id: Inf
	        text: "Укажите город в котором хотите узнать погоду:"
	        font_size: "15sp"
		    multiline: True
		    text_size: self.width*0.98, None
		    size_hint_x: 1.0
		    size_hint_y: 1.0
		    height: self.texture_size[1] + 15
		    markup: True
		    on_ref_press: root.linki()	
            halign: 'center'
            color: 'black'
	    
	    
	    MDTextField:
            hint_text: "Город"
            mode: "fill"
	        id: txt
		    multiline: False
		    size_hint: (0.4, 0.3)
            pos_hint: {"center_x": 0.5, "center_y":0.5}
		    on_text: 
		    

	    
        MDRaisedButton:
            text: 'Узнать'
            on_press: root.printTxt(txt.text)
            on_release:root.pogoda()
            background_color:'#476BD6'
            size_hint: (0.4, 0.3)
            pos_hint: {"center_x": 0.5, "center_y":0.5}
		    
        MDRaisedButton:
            text: 'Вернуться назад'
            on_press: root.manager.current = 'menu'
            background_color:'#476BD6'
		    size_hint: (0.4, 0.3)
            pos_hint: {"center_x": 0.5, "center_y":0.5}
        
        MDBottomNavigation:
            #panel_color: "#eeeaea"
            selected_color_background: "orange"
            text_color_active: "lightgrey"

            MDBottomNavigationItem:
                name: 'screen 1'
                text: 'Mail'
                icon: 'gmail'
                badge_icon: "numeric-10"

                MDLabel:
                    text: 'Mail'
                    halign: 'center'
                    color: 'black'

            MDBottomNavigationItem:
                name: 'screen 2'
                text: 'Twitter'
                icon: 'twitter'
                badge_icon: "numeric-5"

                MDLabel:
                    text: 'Twitter'
                    halign: 'center'
                    color: 'black'

            MDBottomNavigationItem:
                name: 'screen 3'
                text: 'LinkedIN'
                icon: 'linkedin'

                MDLabel:
                    text: 'LinkedIN'
                    halign: 'center'
                    color: 'black'

        


<PayScreen>:
    canvas:
        Rectangle:
            size: self.size
            pos: self.pos

    ScrollView:
        size: self.size
        
        BoxLayout:
            cols: 1
            size_hint_y: None
            height: self.minimum_height
            orientation: 'vertical'
            spacing:20
	    
	    
	    
	   
	    
        
            
            MDLabel:
    	        id: Inf
    	        text: " "
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                color: 'black'


            MDLabel:
    	        id: Inf
    	        text: " "
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                color: 'black'


            MDLabel:
    	        id: Inf
    	        text: " "
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                color: 'black'

            MDLabel:
    	        id: Inf
    	        text: " "
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                color: 'black'


            MDLabel:
    	        id: Inf
    	        text: " "
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                color: 'black'



            MDLabel:
    	        id: Inf
    	        text: " "
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                color: 'black'

            MDLabel:
    	        id: Inf
    	        text: " "
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                color: 'black'
    
    

            MDRaisedButton:
                text: 'Суп Харчо'
                on_press: root.manager.current = 'recone'
                background_color:'#476BD6'
    		    size_hint: (0.3, 0.2)
                pos_hint: {"center_x": 0.5, "center_y":0.1}

            MDRaisedButton:
                text: 'Суп Куриный'
                on_press: root.manager.current = 'rectwo'
                background_color:'#476BD6'
    		    size_hint: (0.3, 0.2)
                pos_hint: {"center_x": 0.5, "center_y":0.1}

            MDRaisedButton:
                text: 'Суп Белый'
                on_press: root.manager.current = 'rectwo'
                background_color:'#476BD6'
    		    size_hint: (0.3, 0.2)
                pos_hint: {"center_x": 0.5, "center_y":0.1}

            MDRaisedButton:
                text: 'Соус Тар-Тар'
                on_press: root.manager.current = 'rectwo'
                background_color:'#476BD6'
    		    size_hint: (0.3, 0.2)
                pos_hint: {"center_x": 0.5, "center_y":0.1}    

            MDRaisedButton:
                text: 'Окрошка'
                on_press: root.manager.current = 'rectwo'
                background_color:'#476BD6'
    		    size_hint: (0.3, 0.2)
                pos_hint: {"center_x": 0.5, "center_y":0.1}

            


            

            MDRaisedButton:
                text: 'Квас'
                on_press: root.manager.current = 'rectwo'
                background_color:'#476BD6'
    		    size_hint: (0.3, 0.2)
                pos_hint: {"center_x": 0.5, "center_y":0.1}

            MDRaisedButton:
                text: 'Плов'
                on_press: root.manager.current = 'rectwo'
                background_color:'#476BD6'
    		    size_hint: (0.3, 0.2)
                pos_hint: {"center_x": 0.5, "center_y":0.1}    

                
            MDRaisedButton:
                text: 'Щи'
                on_press: root.manager.current = 'rectwo'
                background_color:'#476BD6'
    		    size_hint: (0.3, 0.2)
                pos_hint: {"center_x": 0.5, "center_y":0.1}

            MDRaisedButton:
                text: 'Бургер'
                on_press: root.manager.current = 'rectwo'
                background_color:'#476BD6'
    		    size_hint: (0.3, 0.2)
                pos_hint: {"center_x": 0.5, "center_y":0.1}   

            MDRaisedButton:
                text: 'Шашлык'
                on_press: root.manager.current = 'recthree'
                background_color:'#476BD6'
    		    size_hint: (0.3, 0.2)
                pos_hint: {"center_x": 0.5, "center_y":0.1}

            MDRaisedButton:
                text: 'Люля'
                on_press: root.manager.current = 'recfhore'
                background_color:'#476BD6'
    		    size_hint: (0.3, 0.2)
                pos_hint: {"center_x": 0.5, "center_y":0.1}


            MDRaisedButton:
                text: 'Шаурма'
                on_press: root.manager.current = 'recfive'
                background_color:'#476BD6'
    		    size_hint: (0.3, 0.2)
                pos_hint: {"center_x": 0.5, "center_y":0.1}


            MDRaisedButton:
                text: 'Вернуться назад'
                on_press: root.manager.current = 'menu'
                background_color:'#476BD6'
    		    size_hint: (0.4, 0.3)
                pos_hint: {"center_x": 0.5, "center_y":0.5}

            MDBottomNavigation:
                #panel_color: "#eeeaea"
                selected_color_background: "orange"
                text_color_active: "lightgrey"

                MDBottomNavigationItem:
                    name: 'screen 1'
                    text: 'Mail'
                    icon: 'gmail'
                    badge_icon: "numeric-10"


                    MDLabel:
                        text: 'Mail'
                        halign: 'center'
                        color: 'black'



                MDBottomNavigationItem:
                    name: 'screen 2'
                    text: 'Twitter'
                    icon: 'twitter'
                    badge_icon: "numeric-5"

                    MDLabel:
                        text: 'Twitter'
                        halign: 'center'
                        color: 'black'

                MDBottomNavigationItem:
                    name: 'screen 3'
                    text: 'LinkedIN'
                    icon: 'linkedin'

                    MDLabel:
                        text: 'LinkedIN'
                        halign: 'center'
                        color: 'black'


<NewsScreen>:
    canvas:
        Rectangle:
            size: self.size
            pos: self.pos

    ScrollView:
        size: self.size
        
        BoxLayout:
            cols: 1
            size_hint_y: None
            height: self.minimum_height
            orientation: 'vertical'
            spacing:20


            MDLabel:
    	        id: Inf
    	        text: " "
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                color: 'black'


            MDLabel:
    	        id: Inf
    	        text: " "
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                color: 'black'


            MDLabel:
    	        id: Inf
    	        text: " "
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                color: 'black'

            MDLabel:
    	        id: Inf
    	        text: " "
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                color: 'black'


            MDLabel:
    	        id: Inf
    	        text: " "
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                color: 'black'



            MDLabel:
    	        id: Inf
    	        text: " "
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                color: 'black'


            MDLabel:
    	        id: Inf
    	        text: " "
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                color: 'black'


            MDLabel:
    	        id: Inf
    	        text: " "
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                color: 'black'

            MDLabel:
    	        id: Inf
    	        text: " "
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                color: 'black'

            MDLabel:
    	        id: Inf
    	        text: " "
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                color: 'black'

            MDLabel:
    	        id: Inf
    	        text: " "
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                color: 'black'

            MDLabel:
    	        id: Inf
    	        text: " "
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                color: 'black'

            MDLabel:
    	        id: Inf
    	        text: " "
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                color: 'black'

            MDLabel:
    	        id: Inf
    	        text: " "
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                color: 'black'

            MDLabel:
    	        id: Inf
    	        text: " "
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                color: 'black'

            MDLabel:
    	        id: Inf
    	        text: " "
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                color: 'black'

            MDLabel:
    	        id: Inf
    	        text: " "
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                color: 'black'

            MDLabel:
    	        id: Inf
    	        text: " "
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                color: 'black'

            MDLabel:
    	        id: Inf
    	        text: " "
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                color: 'black'

            MDLabel:
    	        id: Inf
    	        text: " "
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                color: 'black'

            MDLabel:
    	        id: Inf
    	        text: " "
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                color: 'black'

            MDLabel:
    	        id: Inf
    	        text: " "
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                color: 'black'

            MDLabel:
    	        id: Inf
    	        text: " "
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                color: 'black'

            MDLabel:
    	        id: Inf
    	        text: " "
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                color: 'black'


            MDLabel:
    	        id: Inf
    	        text: " "
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                color: 'black'

            MDLabel:
    	        id: Inf
    	        text: " "
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                color: 'black'

            MDLabel:
    	        id: Inf
    	        text: " "
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                color: 'black'

            MDLabel:
    	        id: Inf
    	        text: "МОСКВА, 2 мая — РИА Новости. На перегоне Унеча — Рассуха в Брянской области, где из-за взрыва сошли с рельсов вагоны, восстановили движение поездов, сообщили РЖД в своем Telegram-канале. В 4:53 мск РЖД открыли движение поездов на перегоне Унеча — Рассуха, нарушенное 1 мая из-за схода подвижного состава в результате незаконного вмешательства в работу железной дороги, — говорится в сообщении."
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
                
            MDLabel:
    	        id: Inf
    	        text: "МОСКВА, 2 мая — РИА Новости. На перегоне Унеча — Рассуха в Брянской области, где из-за взрыва сошли с рельсов вагоны, восстановили движение поездов, сообщили РЖД в своем Telegram-канале. В 4:53 мск РЖД открыли движение поездов на перегоне Унеча — Рассуха, нарушенное 1 мая из-за схода подвижного состава в результате незаконного вмешательства в работу железной дороги, — говорится в сообщении."
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'
            
            MDLabel:
    	        id: Inf
    	        text: "МОСКВА, 2 мая — РИА Новости. На перегоне Унеча — Рассуха в Брянской области, где из-за взрыва сошли с рельсов вагоны, восстановили движение поездов, сообщили РЖД в своем Telegram-канале. В 4:53 мск РЖД открыли движение поездов на перегоне Унеча — Рассуха, нарушенное 1 мая из-за схода подвижного состава в результате незаконного вмешательства в работу железной дороги, — говорится в сообщении."
    	        font_size: "15sp"
    		    multiline: True
    		    text_size: self.width*0.98, None
    		    size_hint_x: 1.0
    		    size_hint_y: 1.0
    		    height: self.texture_size[1] + 15
    		    markup: True
    		    on_ref_press: root.linki()	
                halign: 'center'


            

            MDRaisedButton:
                text: 'Вернуться назад'
                on_press: root.manager.current = 'menu'
                background_color:'#476BD6'
    		    size_hint: (0.4, 0.3)
                pos_hint: {"center_x": 0.5, "center_y":0.5}
                
            
        
        
<ReconeScreen>:
    lab: gtr
    BoxLayout:
        id: grid_id
        orientation: "vertical"
        spacing: 20

        Label:
	        id: gtr
	        text: "Блюда из курицы занимают прочное место в нашем меню, пользуясь равным успехом и в будни, и в праздники."
	        font_size: "14sp"
		    multiline: True
		    size_hint_x: 1.0
		    size_hint_y: 0.3
		    height: self.texture_size[1] + 15
		    markup: True
		    on_ref_press: root.linki()	
            halign: 'center'
            color: 'black'
            size_hint: (0.8, 0.3)
            pos_hint: {"center_x": 0.5, "center_y":0.2}
            
        

        
        MDTextField:
            multiline: True
            hint_text: "Введите новый рецепт"
            id: text_1

        MDRaisedButton:
            text: 'Внести изменения'
            on_press: root.text_input_1(text_1.text)
            on_release: root.vizer()
            background_color:'#476BD6'
		    size_hint: (0.3, 0.1)
            pos_hint: {"center_x": 0.5, "center_y":0.5}
            
        MDRaisedButton:
            text: 'Вернуться назад'
            on_press: root.manager.current = 'pay'
            background_color:'#476BD6'
		    size_hint: (0.3, 0.1)
            pos_hint: {"center_x": 0.5, "center_y":0.5}
        
        

<RectwoScreen>:
    lab: gtr
    BoxLayout:
        id: try
        orientation: "vertical"
        spacing: 20

        MDLabel:
	        id: gtr
	        text: "Блюда из курицы занимают прочное место в нашем меню, пользуясь равным успехом и в будни, и в праздники.С приготовления блюд из курицы зачастую начинается знакомство с кулинарным искусством: нужно очень постараться, чтобы приготовить курицу невкусно.Сегодня в продаже есть целые тушки курицы, свежие, охлаждённые или замороженные. Курицу можно приготовить целиком или разделив на 8 частей: две грудки, два бедра, две голени и два крылышка. Останется также хребет вместе с шеей – отличное сырьё для бульона. Можно купить те же самые части курицы, но отдельно.Покупайте курицу для использования по любому рецепту из расчёта 350 г на порцию.Какое бы блюдо из курицы вы не готовили, неплохо знать внутреннюю температуру, при которой птица полностью готова. Эта температура разная в  разных частях птицы и составляет: - для целой курицы с начинкой: термометр, вставленный в начинку, должен показывать 74 С;  - для целой курицы без начинки: термометр, вставленный в толстую часть мяса, не касаясь костей, должен показывать 82 С;  - грудки: 82 С;  - бёдрышки: 76 С."
	        font_size: "14sp"
		    multiline: True
		    size_hint_x: 1.0
		    size_hint_y: 0.3
		    height: self.texture_size[1] + 15
		    markup: True
		    on_ref_press: root.linki()	
            halign: 'center'
            color: 'black'
            size_hint: (0.8, 0.3)
            pos_hint: {"center_x": 0.5, "center_y":0.2}
            
        Image:
            source: 'rty.jpeg'
            size: self.texture_size
            anim_delay: 7
	        size_hint: (0.4, 0.4)
            pos_hint: {"center_x": 0.5, "center_y":0.5}
        
        MDTextField:
            multiline: True
            hint_text: "Введите новый рецепт"
            id: text_1    

        MDRaisedButton:
            text: 'Внести изменения'
            on_press: root.text_input_1(text_1.text)
            on_release: root.vizer()
            background_color:'#476BD6'
		    size_hint: (0.3, 0.1)
            pos_hint: {"center_x": 0.5, "center_y":0.5}

        MDRaisedButton:
            text: 'Вернуться назад'
            on_press: root.manager.current = 'pay'
            background_color:'#476BD6'
		    size_hint: (0.3, 0.1)
            pos_hint: {"center_x": 0.5, "center_y":0.5}
        
<RecthreeScreen>:
    lab: gtr
    BoxLayout:
        id: try
        orientation: "vertical"
        spacing: 20

        MDLabel:
	        id: gtr
	        text: "Тем, кто ищет легкий рецепт шашлыка, стоит обратить внимание на шашлык из курицы или индейки. Готовить шашлыки из мяса птицы удобно и просто, правда, если не знать некоторых секретов, он может получиться суховатым.Резать мясо лучше поперек волокон, тогда оно будет лучше жеваться. Чтобы мясо стало мягче, его можно замариновать. Самый простой способ — положить в емкость с кусками мяса нарезанный репчатый лук, соль, специи, пряные травы, хорошо перемешать, накрыть крышкой и поставить в холодильник. Через пару часов мясо можно жарить. А дальше ваш полет фантазии по выбору идеального маринада ничем не ограничивается. Мята и розмарин используются в маринаде для шашлыка из баранины, базилик, орегано и тимьян — из курятины. Кориандр особенно хорош с мясом птицы. Можно положить в маринад чеснок и измельченный корень имбиря. Уксусом и лимонным соком увлекаться не стоит, потому что кислота не размягчает мясо, а наоборот, делает его более жестким. "
	        font_size: "14sp"
		    multiline: True
		    size_hint_x: 1.0
		    size_hint_y: 0.3
		    height: self.texture_size[1] + 15
		    markup: True
		    on_ref_press: root.linki()	
            halign: 'center'
            color: 'black'
            size_hint: (0.8, 0.3)
            pos_hint: {"center_x": 0.5, "center_y":0.2}
            
        Image:
            source: 'fff.jpeg'
            size: self.texture_size
            anim_delay: 7
	        size_hint: (0.4, 0.4)
            pos_hint: {"center_x": 0.5, "center_y":0.5}
        
        MDTextField:
            multiline: True
            hint_text: "Введите новый рецепт"
            id: text_1    

        MDRaisedButton:
            text: 'Внести изменения'
            on_press: root.text_input_1(text_1.text)
            on_release: root.vizer()
            background_color:'#476BD6'
		    size_hint: (0.3, 0.1)
            pos_hint: {"center_x": 0.5, "center_y":0.5}    
        
        MDRaisedButton:
            text: 'Вернуться назад'
            on_press: root.manager.current = 'pay'
            background_color:'#476BD6'
		    size_hint: (0.3, 0.1)
            pos_hint: {"center_x": 0.5, "center_y":0.5}


<RecfhoreScreen>:
    lab: gtr
    BoxLayout:
        id: try
        orientation: "vertical"
        spacing: 20

        MDLabel:
	        id: gtr
	        text: "Люля-кебаб – мясное блюдо, популярное на Ближнем Востоке и в Центральной Азии. Точно определить его родину сложно, все потому, что оно имеет множество разновидностей. С персидского языка, кебаб переводится как «жареное мясо». А способ приготовления этого жареного мяса у разных народов свой. Люля-кебабом называют мясной фарш или рубленое мясо, нанизанное на шампур и обжаренное на углях. Своеобразная мясная котлета, но без добавления яиц, муки или хлеба. Фарш замешивается достаточно долго, чтобы сформировать однородную плотную массу. За счет этого готовое изделие не распадается при термической обработке. Правильно приготовленный люля-кебаб – это поджаренная золотистая корочка и сочное мясо внутри. Добавьте к нему горячую домашнюю лепешку, свежие овощи, зелень и различные соусы – невозможно устоять! В моём случае люля- кебаб приготовлен в домашних условиях в электропечи. Аромат, вкусовые качества при этом не пострадали."
	        font_size: "14sp"
		    multiline: True
		    size_hint_x: 1.0
		    size_hint_y: 0.3
		    height: self.texture_size[1] + 15
		    markup: True
		    on_ref_press: root.linki()	
            halign: 'center'
            color: 'black'
            size_hint: (0.8, 0.3)
            pos_hint: {"center_x": 0.5, "center_y":0.2}
            
        Image:
            source: 'kebab.jpg'
            size: self.texture_size
            anim_delay: 7
	        size_hint: (0.4, 0.4)
            pos_hint: {"center_x": 0.5, "center_y":0.5}
        MDTextField:
            multiline: True
            hint_text: "Введите новый рецепт"
            id: text_1  
        MDRaisedButton:
            text: 'Внести изменения'
            on_press: root.text_input_1(text_1.text)
            on_release: root.vizer()
            background_color:'#476BD6'
		    size_hint: (0.3, 0.1)
            pos_hint: {"center_x": 0.5, "center_y":0.5}       

        MDRaisedButton:
            text: 'Вернуться назад'
            on_press: root.manager.current = 'pay'
            background_color:'#476BD6'
		    size_hint: (0.3, 0.1)
            pos_hint: {"center_x": 0.5, "center_y":0.5}

            

<RecfiveScreen>:
    labe: gtr
    BoxLayout:
        id: try
        orientation: "vertical"
        spacing: 20

        MDLabel:
	        id: gtr
	        text: "Шаурма, или шаверма, — это ближневосточное (левантийское) мясное блюдо, завернутое в питу или лаваш. Начинка может быть из курицы, индейки, говядины, телятины или из смешанных сортов мяса, которое готовится на вертикальном гриле. Мясо нанизывается на вертикальный шампур и вращается внутри нагревательных элементов. По мере готовности верхнего слоя его срезают, остальное мясо продолжает вращаться на вертеле. Затем мясо мелко нарезают и кладут в начинку вместе с разными овощами с добавлением соусов. Шаурму можно подавать на тарелке (как правило, с овощами) и в виде сэндвича или врапа. Шаурму обычно едят с помидорами, капустой, огурцами и салатом. Начинки могут включать в себя тахини, хумус, маринованную репу. Пошаговый рецепт приготовления с фотографиями — идеальное пособие для тех, кто хочет приготовить шаурму в домашних "
	        font_size: "14sp"
		    multiline: True
		    size_hint_x: 1.0
		    size_hint_y: 0.3
		    height: self.texture_size[1] + 15
		    markup: True
		    on_ref_press: root.linki()	
            halign: 'center'
            color: 'black'
            size_hint: (0.8, 0.3)
            pos_hint: {"center_x": 0.5, "center_y":0.2}
            
        Image:
            source: 'rtt.jpeg'
            size: self.texture_size
            anim_delay: 7
	        size_hint: (0.4, 0.4)
            pos_hint: {"center_x": 0.5, "center_y":0.5}
        MDTextField:
            multiline: True
            hint_text: "Введите новый рецепт"
            id: text_1  
        MDRaisedButton:
            text: 'Внести изменения'
            on_press: root.text_input_1(text_1.text)
            on_release: root.vizer()
            background_color:'#476BD6'
		    size_hint: (0.3, 0.1)
            pos_hint: {"center_x": 0.5, "center_y":0.5}    
        MDRaisedButton:
            text: 'Вернуться назад'
            on_press: root.manager.current = 'pay'
            background_color:'#476BD6'
		    size_hint: (0.3, 0.1)
            pos_hint: {"center_x": 0.5, "center_y":0.5}

<Taper>:
    
    BoxLayout:
        orientation: "vertical"
	    size_hint: (0.95, 0.95)
	    pos_hint: {"center_x": 0.65, "center_y":0.5}
	    spacing:30
	    
	    Label:
	        text: "Ваш билет:"
	        font_size: "15sp"
		    multiline: True
		    text_size: self.width*0.98, None
		    size_hint_x: 11.0
		    size_hint_y: 1.0
		    height: self.texture_size[1] + 15
		    markup: True
		    on_ref_press: root.linki()	    
		    
		    
		Image:
            source: 'bil.jpg'
            size: self.texture_size
            anim_delay: 7
	        size_hint: (0.7, 1)
	        
	    MDRectangleFlatButton:
            text: 'Вернуться назад'
            on_press: root.manager.current = 'menu'
            background_color:'#476BD6'
		    size_hint: (0.7, 0.2)

""")



class MenuScreen(Screen):

    def callback3(self):
        self.labelone.text = "Если вы нашли ошибку, то \nсоветуем написать нам по \nданной ссылке:@mavrikbot"

    def callback4(self):
        self.labelone.text = "NATRY inc. \nВерсия 0.5 (Betta)"
    
    def add_buttons(self):
        new_btn = MDRectangleFlatButton(text = "Да")
        new_btn.bind(on_press=self.on_press_button)
        new_btn.bind(on_press=self.oner)

        self.ids.grid_id.add_widget(new_btn)

        return MDRectangleFlatButton
    def on_press_button(self, instancce):
        self.manager.current = 'top'

    def oner(self, instancce):
        webbrowser.open('https://my.qiwi.com/Mykhayl-LQRB1GqfiH', new=2)

class SettingsScreen(Screen):
    pass

    def printTxt(instance, text):
        OWM_Mark = text


        from pyowm import OWM
        global watter
        owm = OWM('825cef665073edbb21d9f7d82d226b4d')

        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(OWM_Mark)
        w = observation.weather

        # температура
        t = w.temperature("celsius")
        t1 = t['temp']
        t2 = t['feels_like']
        t3 = t['temp_max']
        t4 = t['temp_min']
        # скорость ветра
        wi = w.wind()['speed']
        # Влажность
        humi = w.humidity
        # облачность
        cl = w.clouds
        # время
        ti = w.reference_time('iso')

        watter = (f"В городе {OWM_Mark} \nтемпература {t1}, \nощущается как {t2}, \nмаксимальная темпа {t3}, \nминимальная темпа {t4}")

    def pogoda(self):
        self.inf.text = watter


class PayScreen(Screen):
    pass

    


class Taper(Screen):
    pass


class ReconeScreen(Screen):
    pass

    def text_input_1(instance, text):
        global text_1
        text_1 = text
        
        
        
    
    def vizer(self):
        self.lab.text = text_1

    

class RectwoScreen(Screen):
    pass

    def add_buttons(self):
        new_btn = MDRectangleFlatButton(text = "Да" ,size_hint = (0.7, 0.2),pos = (20,100))
        new_btn.bind(on_press=self.on_press_button)
        new_btn.bind(on_press=self.oner)

        self.ids.grid_id.add_widget(new_btn)

        return MDRectangleFlatButton
    def on_press_button(self, instancce):
        self.manager.current = 'top'

    def text_input_1(instance, text):
        global text_1
        text_1 = text
        
        
        
    
    def vizer(self):
        self.lab.text = text_1


class RecthreeScreen(Screen):
    pass

    def text_input_1(instance, text):
        global text_1
        text_1 = text
        
        
        
    
    def vizer(self):
        self.lab.text = text_1

class RecfhoreScreen(Screen):
    pass

    def text_input_1(instance, text):
        global text_1
        text_1 = text
        
        
        
    
    def vizer(self):
        self.lab.text = text_1
class RecfiveScreen(Screen):
    pass
    def text_input_1(instance, text):
        global text_1
        text_1 = text
        
        
        
    
    def vizer(self):
        self.lab.text = text_1

class NewsScreen(Screen):
    pass

class MyApp(MDApp):
    running = True

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(PayScreen(name='pay'))
        sm.add_widget(ReconeScreen(name='recone'))
        sm.add_widget(RectwoScreen(name='rectwo'))
        sm.add_widget(RecthreeScreen(name='recthree'))
        sm.add_widget(RecfhoreScreen(name='recfhore'))
        sm.add_widget(RecfiveScreen(name='recfive'))
        sm.add_widget(NewsScreen(name='news'))
        sm.add_widget(Taper(name='top'))
        return sm

    

    def process(self):
        text = self.root.ids.Inp.text


    def on_stop(self):
        self.running = False


if __name__ == '__main__':
    MyApp().run()
