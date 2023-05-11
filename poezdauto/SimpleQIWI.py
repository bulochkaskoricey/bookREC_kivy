class Session:
    pass


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







canvas:
        Color:
            rgb: 1, 1, 1
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