import cv2
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivymd.uix.fitimage import FitImage
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDTextButton
from kivymd.uix.label import MDLabel
from kivymd.uix.navigationdrawer import MDNavigationDrawer, MDNavigationDrawerItem
from kivymd.uix.button import MDIconButton
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.toolbar import MDTopAppBar
from kivy.metrics import dp
from kivy.graphics import Color, Rectangle
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.camera import Camera
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.properties import StringProperty
from kivy.app import App
import os
from datetime import datetime
from PIL import Image as PILImage
import pyrebase
import firebase_admin
from firebase_admin import credentials, db
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

KV = '''
ScreenManager:
    MainScreen:
    SignIn:
    RegisterForm:
    LogInForm:
    HomePage:
    CameraPage:

<ArrowButton@Button>:
    size_hint: None, None
    size: 50, 50
    background_normal: ''
    background_color: 0, 0, 0, 0
    canvas.before:
        Color:
            rgba: (0, 0, 0, 1)  # Border color
        Line:
            width: 1.5
            circle: (self.center_x, self.center_y, 25)
        Color:
            rgba: (0, 0, 0, 1)  # Arrow color and line
        Line:
            points: (self.center_x - 10, self.center_y, self.center_x + 10, self.center_y)
        Triangle:
            points: (self.center_x + 10, self.center_y + 5, self.center_x + 10, self.center_y - 5, self.center_x + 15, self.center_y)

<MainScreen>:
    name: 'main'
    canvas.before:
        Color:
            rgba: (240/255, 246/255, 237/255, 1)
        Rectangle:
            size: self.size
            pos: self.pos

    FitImage:
        source: "Shutter.png"
        size_hint: None, None
        size: 1000, 1000
        pos_hint: {"center_x": 0.5, "center_y": 0.5}

    ArrowButton:
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        on_release: app.on_arrow_click()

<SignIn>:
    name: 'sign'
    canvas.before:
        Color:
            rgba: (240/255, 246/255, 237/255, 1)
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        size_hint: None, None
        size: 800, 500 
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        orientation: 'vertical'
        padding: 40
        spacing: 20
        canvas.before:
            Color:
                rgba: (165/255, 165/255, 141/255, 1)  
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [20]

    MDRoundFlatButton:
        text: "Register"
        size_hint: 0.1, None
        height: dp (48)
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        halign: "center"
        font_size: 12
        font_style: "Caption"
        text_style: "GlacialIndifference-Regular.ttf"
        text_color: 0, 0, 0, 1
        md_bg_color: 0.867, 0.894, 0.882, 1
        line_color: 0, 0, 0, 1
        radius: [24, 24, 24, 24]
        on_release: app.root.current = 'register'

    MDRoundFlatButton:
        text: "Login"
        size_hint: 0.1, None
        height: dp (48)
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        halign: "center"
        font_size: 12
        font_style: "Caption"
        text_style: "GlacialIndifference-Regular.ttf"
        text_color: 0, 0, 0, 1
        md_bg_color: 0.867, 0.894, 0.882, 1
        line_color: 0, 0, 0, 1
        radius: [24, 24, 24, 24]
        on_release: app.root.current = 'login'

    FitImage:
        source: "Shutter.png"
        size_hint: None, None
        size: 1000, 1000
        pos_hint: {"center_x": 0.5, "center_y": 0.5}

<RegisterForm>:
    name: 'register'
    canvas.before:
        Color:
            rgba: (240/255, 246/255, 237/255, 1)
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        size_hint: None, None
        size: 1000, 800 
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        orientation: 'vertical'
        padding: 40
        spacing: 20
        canvas.before:
            Color:
                rgba: (165/255, 165/255, 141/255, 1)  
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [20]

    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
        size_hint: None, None
        size: dp(50), dp(50)
        pos_hint: {"x": 0.05, "top": 0.95}
        on_release: app.root.current = 'sign'

    MDTextField:
        id: full_name
        hint_text: "Full name:"
        mode: "rectangle"
        size_hint_x: None
        width: 400
        pos_hint: {"center_x": 0.5, "center_y": 0.55}
        font_size: "12sp"

        text_color: 0, 0, 0, 1
        line_color_normal: 0, 0, 0, 1
        line_color_focus: 0, 0, 0, 1
        hint_text_color: 0, 0, 0, 1
        helper_text_mode: "on_focus"

    MDTextField:
        id: username
        hint_text: "Username"
        mode: "rectangle"
        size_hint_x: None
        width: 400
        pos_hint: {"center_x": 0.5, "center_y": 0.45}
        font_size: "12sp"

        text_color: 0, 0, 0, 1
        line_color_normal: 0, 0, 0, 1
        line_color_focus: 0, 0, 0, 1
        hint_text_color: 0, 0, 0, 1
        helper_text_mode: "on_focus"

    MDTextField:
        id: password
        hint_text: "Password"
        mode: "rectangle"
        size_hint_x: None
        width: 400
        pos_hint: {"center_x": 0.5, "center_y": 0.35}
        font_size: "12sp"
        password: True
        text_color: 0, 0, 0, 1
        line_color_normal: 0, 0, 0, 1
        line_color_focus: 0, 0, 0, 1
        hint_text_color: 0, 0, 0, 1
        helper_text_mode: "on_focus"

        MDIconButton:
            id: toggle_icon
            icon: "eye-off"
            pos_hint: {"center_x": 0.95, "center_y": 0.5}
            size_hint: None, None
            size: dp(30), dp(30)
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
            on_release: app.toggle_password_visibility()

    MDTextField:
        id: confirm_password
        hint_text: "Confirm Password:"
        mode: "rectangle"
        size_hint_x: None
        width: 400
        pos_hint: {"center_x": 0.5, "center_y": 0.25}
        font_size: "12sp"

        text_color: 0, 0, 0, 1
        line_color_normal: 0, 0, 0, 1
        line_color_focus: 0, 0, 0, 1
        hint_text_color: 0, 0, 0, 1
        helper_text_mode: "on_focus"

    MDRoundFlatButton:
        text: "Register"
        size_hint: 0.1, None
        height: dp (48)
        pos_hint: {"center_x": 0.5, "center_y": 0.15}
        halign: "center"
        font_size: 12
        font_style: "Caption"
        text_style: "GlacialIndifference-Regular.ttf"
        text_color: 0, 0, 0, 1
        md_bg_color: 0.867, 0.894, 0.882, 1
        line_color: 0, 0, 0, 1
        radius: [24, 24, 24, 24]
        on_release: root.register_user()

    FitImage:
        source: "Shutter.png"
        size_hint: None, None
        size: 1000, 1000
        pos_hint: {"center_x": 0.5, "center_y": 0.65}

<LogInForm>:
    name: 'login'
    canvas.before:
        Color:
            rgba: (240/255, 246/255, 237/255, 1)
        Rectangle:
            size: self.size
            pos: self.pos

    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
        size_hint: None, None
        size: dp(50), dp(50)
        pos_hint: {"x": 0.05, "top": 0.95}
        on_release: app.root.current = 'sign'

    BoxLayout:
        size_hint: None, None
        size: 1000, 800 
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        orientation: 'vertical'
        padding: 40
        spacing: 20
        canvas.before:
            Color:
                rgba: (165/255, 165/255, 141/255, 1)  
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [20]

    MDTextField:
        id:  login_username
        hint_text: "Username"
        mode: "rectangle"
        size_hint_x: None
        width: 400
        pos_hint: {"center_x": 0.5, "center_y": 0.54}
        font_size: "12sp"

        text_color: 0, 0, 0, 1
        line_color_normal: 0, 0, 0, 1
        line_color_focus: 0, 0, 0, 1
        hint_text_color: 0, 0, 0, 1
        helper_text_mode: "on_focus"

    MDTextField:
        id: login_password
        hint_text: "Password"
        password: True
        mode: "rectangle"
        size_hint_x: None
        width: 400
        pos_hint: {"center_x": 0.5, "center_y": 0.44}
        font_size: "12sp"

        text_color: 0, 0, 0, 1
        line_color_normal: 0, 0, 0, 1
        line_color_focus: 0, 0, 0, 1
        hint_text_color: 0, 0, 0, 1
        helper_text_mode: "on_focus"

    MDTextButton:
        text: "Forgot Password?"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1  # Blue text (change color as needed)
        font_size: "14sp"
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        on_release: app.forgot_password()  # Calls a function when clicked

    MDRoundFlatButton:
        text: "Login"
        size_hint: 0.1, None
        height: dp (48)
        pos_hint: {"center_x": 0.5, "center_y": 0.34}
        halign: "center"
        font_size: 12
        font_style: "Caption"
        text_style: "GlacialIndifference-Regular.ttf"
        text_color: 0, 0, 0, 1
        md_bg_color: 0.867, 0.894, 0.882, 1
        line_color: 0, 0, 0, 1
        radius: [24, 24, 24, 24]
        on_release: root.check_login()

    FitImage:
        source: "Shutter.png"
        size_hint: None, None
        size: 1000, 1000
        pos_hint: {"center_x": 0.5, "center_y": 0.65}

<HomePage>:
    name: 'home'
    canvas.before:
        Color:
            rgba: (240/255, 246/255, 237/255, 1)
        Rectangle:
            size: self.size
            pos: self.pos

    FitImage:
        source: "Shutter.png"
        size_hint: None, None
        size: 1000, 1000
        pos_hint: {"center_x": 0.5, "center_y": 0.75}

    MDNavigationLayout:
        ScreenManager:
            Screen:
                MDBoxLayout:
                    orientation: 'vertical'

                    Widget:

                    MDFloatLayout:
                        size_hint_y: None
                        height: dp(56)
                        padding: dp(10)
                        pos_hint: {"top": 1, "right": 1}  
                        spacing: dp(10)
                        
                        MDIconButton:
                            icon: "menu"
                            theme_icon_color: "Custom"
                            icon_color: "black"
                            pos_hint: {"center_y": 13.20, "center_x": 0.95} 
                            on_release: nav_drawer.set_state("toggle")             

                ClickableImage:
                    source: "set1 (2).png"
                    size_hint: None, None
                    size: dp(300), dp(300)
                    pos_hint: {"center_y": 0.35, "x": 0.10}
                    on_release: app.root.current = 'camera'
                
                MDLabel:
                    text: "SET 1"
                    halign: "center"
                    pos_hint: {"center_x": 0.20, "center_y": 0.15}
                    text_style: "GlacialIndifference-Regular.ttf"
                         
                             
                ClickableImage:
                    source: "set2.png"
                    size_hint: None, None
                    size: dp(350), dp(350)
                    pos_hint: {"center_y": 0.38, "x": 0.25}
                    on_release: app.root.current = 'camera'
                
                MDLabel:
                    text: "SET 2"
                    halign: "center"
                    pos_hint: {"center_x": 0.36, "center_y": 0.15}
                    text_style: "GlacialIndifference-Regular.ttf"
                    
                ClickableImage:
                    source: "set3.png"
                    size_hint: None, None
                    size: dp(400), dp(400)
                    pos_hint: {"center_y": 0.42, "x": 0.40}
                    on_release: app.root.current = 'camera'
                    
                MDLabel:
                    text: "SET 3"
                    halign: "center"
                    pos_hint: {"center_x": 0.52, "center_y": 0.15}
                    text_style: "GlacialIndifference-Regular.ttf"

                ClickableImage:
                    source: "set4.png"
                    size_hint: None, None
                    size: dp(350), dp(350)
                    pos_hint: {"center_y": 0.33, "x": 0.62}
                    on_release: app.root.current = 'camera'
                
                MDLabel:
                    text: "SET 4"
                    halign: "center"
                    pos_hint: {"center_x": 0.73, "center_y": 0.15}
                    text_style: "GlacialIndifference-Regular.ttf"
                     
        MDNavigationDrawer:
            id: nav_drawer
            anchor: 'right'
            md_bg_color: 146/255, 170/255, 131/255, 1
        
            MDList:
                OneLineListItem:
                    text: "ACCOUNT"
                    theme_text_color: "Custom"
                    text_color: "black"
                    pos_hint: {"top": 15}
                    size_hint_y: None
                    on_release: app.root.current = 'account'    
                
                MDList:
                    OneLineListItem:
                        text: "ABOUT"
                        theme_text_color: "Custom"
                        text_color: "black"
                        pos_hint: {"top": 3}
                        size_hint_y: None
                        on_release: app.root.current = 'about'      
                    
                    MDList:
                        OneLineListItem:
                            text: "CONTACT"
                            theme_text_color: "Custom"
                            text_color: "black"
                            pos_hint: {"top": 3}
                            size_hint_y: None
                            on_release: app.root.current = 'contact'            
                                       

<CameraPage>:
    name: 'camera'
    canvas.before:
        Color:
            rgba: (240/255, 246/255, 237/255, 1)
        Rectangle:
            size: self.size
            pos: self.pos   
            
<AccountPage>:
    name: 'account'
    canvas.before:
        Color:
            rgba: (240/255, 246/255, 237/255, 1)  # Light green background
        Rectangle:
            size: self.size
            pos: self.pos
    
    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
        size_hint: None, None
        size: dp(50), dp(50)
        pos_hint: {"x": 0.95, "top": 0.98}
        on_release: app.root.current = 'home'
    
    BoxLayout:
        orientation: 'horizontal'
        size_hint_y: None
        height: 120
        padding: 20
        spacing: 15
        
        Image:
            source: 'Profile.png'
            size_hint: None, None
            size: 60, 60
            pos_hint: {"y": 11, "x": 3}
            
        FloatLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: 60
            
            Label:
                text: "FULL NAME"
                bold: True
                font_size: 18
                color: 0, 0, 0, 1
                height: 25
                pos_hint: {"center_x": 0.02, "center_y": 15.1}
            
            Label:
                text: "@USERNAME"
                font_size: 14
                color: 0, 0, 0.5, 1
                height: 20
                pos_hint: {"center_x": 0.02, "center_y": 14.8}
            
            Label:
                text: "PHOTOS"
                font_size: 14
                bold: True
                size_hint_y: None
                height: 30
                color: 0, 0, 0.5, 1
                pos_hint: {"center_x": 0.01, "center_y": 12.8}

<AboutPage>:
    name: 'about'
    canvas.before:
        Color:
            rgba: (240/255, 246/255, 237/255, 1)  # Light green background
        Rectangle:
            size: self.size
            pos: self.pos  
    
    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
        size_hint: None, None
        size: dp(50), dp(50)
        pos_hint: {"x": 0.95, "top": 0.98}
        on_release: app.root.current = 'home'
          
    BoxLayout:
        orientation: 'horizontal'
        size_hint_y: None
        height: 120
        padding: 20
        spacing: 15 
        
        Image:
            source: 'About.png'
            size_hint: None, None
            size: 60, 60
            pos_hint: {"y": 10.8, "x": 3}               
    
    FloatLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: 60
        
        Label:
            text: "ABOUT US"
            bold: True
            font_size: 25
            color: 0, 0, 0, 1
            size_hint_y: None
            height: 30       
            pos_hint: {"center_x": 0.08, "center_y": 15.2}
            
        Label:
            text: """ShutterBooth is dedicated to bringing people together through fun, creative, and high-quality photo booth experiences.Our app is designed to make capturing memories effortless and enjoyable, whether at events, gatherings, or just everyday moments. With customizable features, instant sharing options,and a user-friendly interface, we empower users to express themselves and preserve special occasions in a unique way. At ShutterBooth, we believe every snapshot tells a story—let’s create yours together! """
            bold: True
            font_size: 25
            color: 0, 0, 0, 1
            size_hint_y: None
            height: 30       
            pos_hint: {"center_x": 0.08, "center_y": 15.2}
                   
<ContactPage>:
    name: 'contact'
    canvas.before:
        Color:
            rgba: (240/255, 246/255, 237/255, 1)  # Light green background
        Rectangle:
            size: self.size
            pos: self.pos  
    
    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
        size_hint: None, None
        size: dp(50), dp(50)
        pos_hint: {"x": 0.95, "top": 0.98}
        on_release: app.root.current = 'home'
        
    BoxLayout:
        orientation: 'horizontal'
        size_hint_y: None
        height: 120
        padding: 20
        spacing: 15      
    
          
    FloatLayout:
        orientation: 'vertical' 
        size_hint_y: None
        height: 60
                  
        Label:
            text: "CONTACTS"
            bold: True
            font_size: 25
            color: 0, 0, 0, 1
            height: 40   
            pos_hint: {"center_x": 0.05, "center_y": 15.0}      
        
        Image:
            source: 'Email.png'
            size_hint: None, None
            size: 40, 40
            pos_hint: {"y": 14.0, "x": 0.02}
            
        Label:
            text: "shutterboothofficial@gmail.com"
            bold: True
            font_size: 15
            color: 0, 0, 0, 1
            height: 40   
            pos_hint: {"center_x": 0.10, "center_y": 14.3}   
            
        Image:
            source: 'Facebook.png'
            size_hint: None, None
            size: 40, 40
            pos_hint: {"y": 13.2, "x": 0.02}  
            
        Label:
            text: "Shutter Booth Official"
            bold: True
            font_size: 15
            color: 0, 0, 0, 1
            height: 40   
            pos_hint: {"center_x": 0.08, "center_y": 13.5}  
            
        Image:
            source: 'Contact.png'
            size_hint: None, None
            size: 40, 40
            pos_hint: {"y": 12.3, "x": 0.02}  
            
        Label:
            text: "(08)- 2025 -1709"
            bold: True
            font_size: 15
            color: 0, 0, 0, 1
            height: 40   
            pos_hint: {"center_x": 0.08, "center_y": 12.7}  

<CameraPage>:
    name: 'camera'
    canvas.before:
        Color:
            rgba: (240/255, 246/255, 237/255, 1)
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: 'horizontal'
        padding: dp(40)
        spacing: dp(30)

        BoxLayout:
            orientation: 'vertical'
            padding: [dp(60), dp(30), 0, 0]
            spacing: dp(10)

            Camera:
                id: cam
                resolution: (640, 480)
                play: True
                allow_stretch: True
                keep_ratio: True
                size_hint: (0.6, 0.6)

            MDRoundFlatButton:
                text: "Take a Photo"
                size_hint: 0.1, None
                height: dp(48)
                pos_hint: {"center_x": 0.5, "center_y": 0.15}
                halign: "center"
                font_size: 12
                font_style: "Caption"
                text_style: "GlacialIndifference-Regular.ttf"
                text_color: 0, 0, 0, 1
                md_bg_color: 0.867, 0.894, 0.882, 1
                line_color: 0, 0, 0, 1
                radius: [24, 24, 24, 24]
                on_release: root.capture()

        BoxLayout:
            orientation: 'horizontal'
            size_hint: None, None
            size: dp(240), dp(420)  
            pos: root.width - dp(240), dp(0)  

            BoxLayout:
                orientation: 'vertical'
                size_hint: None, None
                size: dp(180), dp(420)
                spacing: dp(10)
        
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Rectangle:
                        size: self.size
                        pos: self.pos

                BoxLayout:
                    size_hint: None, None
                    size: dp(160), dp(200)
                    padding: dp(5)
                    pos_hint: {'center_x': 0.5}

                    canvas.before:
                        Color: 
                            rgba: 1, 1, 1, 1
                        Rectangle:
                            size: self.size
                            pos: self.pos

                    Image:
                        id: photo1
                        source: root.photo1_source
                        allow_stretch: True
                        keep_ratio: False
                        size_hint: 1, 1

                BoxLayout:
                    size_hint: None, None
                    size: dp(160), dp(200)
                    padding: dp(5)
                    pos_hint: {'center_x': 0.5}

                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1
                        Rectangle:
                            size: self.size
                            pos: self.pos

                    Image:
                        id: photo2
                        source: root.photo2_source
                        allow_stretch: True
                        keep_ratio: False
                        size_hint: 1, 1

    MDRoundFlatButton:
        text: "Confirm"
        size_hint: 0.1, None
        height: dp(48)
        pos_hint: {"center_x": 0.5, "center_y": 0.15}
        halign: "center"
        font_size: 12
        font_style: "Caption"
        text_style: "GlacialIndifference-Regular.ttf"
        text_color: 0, 0, 0, 1
        md_bg_color: 0.867, 0.894, 0.882, 1
        line_color: 0, 0, 0, 1
        radius: [24, 24, 24, 24]
        on_release: root.confirm()
        
    MDIconButton:
        icon: "arrow-left"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
        size_hint: None, None
        size: dp(50), dp(50)
        pos_hint: {"x": 0.1, "top": 0.95}
        on_release: app.root.current = 'home'

'''
class ArrowButton(Button):
    pass


class MainScreen(Screen):
    pass


class SignIn(Screen):
    pass


class RegisterForm(Screen):
    dialog = None

    def register_user(self):
        full_name = self.ids.full_name.text
        username = self.ids.username.text
        password = self.ids.password.text
        confirm_password = self.ids.confirm_password.text

        if not full_name or not username or not password or not confirm_password:
            self.show_error_dialog("Please fill in all the fields!")
            return

        if password == confirm_password:
            ref = db.reference('users')
            ref.child(username).set({
                'full_name': full_name,
                'password': password
            })
            print("Registration successful!")
            self.manager.current = "login"
        else:
            print("Passwords do not match!")

    def show_error_dialog(self, message):
        if not self.dialog:
            self.dialog = MDDialog(
                type = "custom",
                content_cls = MDLabel(
                    text = "Registration Error",
                    halign = "center",
                    font_name = "GlacialIndifference-Regular.ttf",
                    font_size = "16sp",
                    theme_text_color = "Custom",
                    text_color = (0, 0, 0, 1),
                ),
                    size_hint = (0.2, None),
                    radius = [20, 20, 20, 20],
                    height = dp(150),
                    buttons = [
                        MDFlatButton(
                            text = "OK",
                            font_name = "GlacialIndifference-Regular.ttf",
                            text_color = (0, 0, 0, 1),
                            on_release = lambda x: self.dialog.dismiss()
                    ),
                ],
            )
        self.dialog.text = message
        self.dialog.open()

class LogInForm(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dialog = None

    def show_error_dialog(self, message):
        if not self.dialog:
            self.dialog = MDDialog(
                type="custom",
                content_cls=MDLabel(
                    text="Login Error",  # Set the message properly
                    halign="center",
                    font_name="GlacialIndifference-Regular.ttf",
                    font_size="16sp",
                    theme_text_color="Custom",
                    text_color=(0, 0, 0, 1),
                ),
                size_hint=(0.2, None),
                radius=[20, 20, 20, 20],
                height=dp(150),
                buttons=[
                    MDFlatButton(
                        text="OK",
                        font_name="GlacialIndifference-Regular.ttf",
                        text_color=(0, 0, 0, 1),
                        on_release=lambda x: self.dialog.dismiss()
                    ),
                ],
            )
        self.dialog.open()

    def check_login(self):
        username = self.ids.login_username.text  # <<< NO self.root
        password = self.ids.login_password.text  # <<< NO self.root

        if not username or not password:
            self.show_error_dialog("Login Error: Please fill in the username and password fields.")  # <<< NO self.root
        else:
            self.login_user(username, password)

    def login_user(self, username, password):
        ref = db.reference('users')
        user_data = ref.child(username).get()

        if user_data:
            if user_data['password'] == password:
                print("Login successful!")
                self.manager.current = "home"
            else:
                self.show_error_dialog("Incorrect password. Please try again.")  # <<< NO self.root
        else:
            self.show_error_dialog("Username not found. Please check your username.")  # <<< NO self.root

class HomePage(Screen):
    pass

class AccountPage(Screen):
    pass

class AboutPage(Screen):
    pass

class ContactPage(Screen):
    pass

class CameraPage(Screen):
    photo1_source = StringProperty('')
    photo2_source = StringProperty('')
    captured_photos = []

    def crop_image_to_box(self, filename, target_width=160, target_height=200):
        img = PILImage.open(filename)
        img_width, img_height = img.size
        target_ratio = target_width / target_height
        current_ratio = img_width / img_height

        if current_ratio > target_ratio:
            new_width = int(img_height * target_ratio)
            left = (img_width - new_width) // 2
            box = (left, 0, left + new_width, img_height)
        else:
            new_height = int(img_width / target_ratio)
            top = (img_height - new_height) // 2
            box = (0, top, img_width, top + new_height)

        cropped = img.crop(box)
        cropped = cropped.resize((target_width, target_height), PILImage.LANCZOS)
        cropped.save(filename)

    def capture(self):
        camera = self.ids.cam
        if camera.texture:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"photo_{timestamp}.png"
            camera.export_to_png(filename)

            self.captured_photos.append(filename)
            if len(self.captured_photos) > 2:
                self.captured_photos.pop(0)

            if len(self.captured_photos) >= 1:
                self.photo1_source = self.captured_photos[0]
            if len(self.captured_photos) == 2:
                self.photo2_source = self.captured_photos[1]

    def crop_image_to_box(self, filename, target_width=160, target_height=200):
        img = PILImage.open(filename)
        img_width, img_height = img.size
        target_ratio = target_width / target_height
        current_ratio = img_width / img_height

        if current_ratio > target_ratio:
            new_width = int(img_height * target_ratio)
            left = (img_width - new_width) // 2
            box = (left, 0, left + new_width, img_height)
        else:
            new_height = int(img_width / target_ratio)
            top = (img_height - new_height) // 2
            box = (0, top, img_width, top + new_height)

        cropped = img.crop(box)
        cropped.save(filename)

    def update_photostrip(self):
        strip = self.ids.photo_strip
        strip.clear_widgets()

        for path in reversed(self.latest_photos):  # newest on top
            img = Image(source=path, size_hint_y=None, height=dp(120))
            img.reload()
            strip.add_widget(img)

class ClickableImage(ButtonBehavior, Image):
    def on_press(self):
        print("Image Clicked!")

class CameraWidget(Image):
    def __init__(self, **kwargs):
        super(CameraWidget, self).__init__(**kwargs)
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0 / 30.0)

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            frame = cv2.flip(frame, 0)
            buf = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB).tobytes()
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='rgb')
            texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')
            self.texture = texture

class Photobooth(MDApp):
    def build(self):
        Window.size = (1024, 768)
        return Builder.load_string(KV)

    def on_arrow_click(self):
        self.root.current = 'sign'

    def on_login_click(self):
        print("Login button clicked!")

    def on_register_click(self):
        print("Register button clicked!")

    def toggle_password_visibility(self):
        field = self.root.ids.password_field
        icon = self.root.ids.toggle_icon

        if field.password:
            field.password = False
            field.right_icon = "eye"
        else:
            field.password = True
            field.right_icon = "eye-off"

    def forgot_password(self):
        print("Forgot Password clicked!")

    def on_image_click(selfself, image_name):
        print(f"Clicked on: {image_name}")

    def show_account_screen(self):
        print("ACCOUNT clicked!")

cred = credentials.Certificate("C:/Users/lauronrochelle22/Downloads/shutterbooth-e72ed-firebase-adminsdk-fbsvc-005a141dfd.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://shutterbooth-e72ed-default-rtdb.asia-southeast1.firebasedatabase.app/users'
})


if __name__ == "__main__":
    Photobooth().run()