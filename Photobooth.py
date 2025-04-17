import mysql.connector
import cv2
from mysql.connector import Error
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


class ArrowButton(Button):
    pass


class MainScreen(Screen):
    pass


class SignIn(Screen):
    pass


class RegisterForm(Screen):
    pass


class LogInForm(Screen):
    pass


class HomePage(Screen):
    pass


class CameraPage(Screen):
    pass


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
        hint_text: "Username:"
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
        id: password_field
        hint_text: "Create Password:"
        mode: "rectangle"
        size_hint_x: None
        width: 400
        pos_hint: {"center_x": 0.5, "center_y": 0.35}
        font_size: "12sp"
        pasword: True
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
        on_release: app.root.current = 'login'

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
        hint_text: "Username:"
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
        hint_text: "Password:"
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
        on_release: app.root.current = 'home'

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

                    MDBoxLayout:
                        size_hint_y: None
                        height: dp(56)
                        padding: dp(10)
                        pos_hint: {"top": 1, "right": 1}  
                        spacing: dp(10) 

                        MDIconButton:
                            icon: "menu"
                            theme_icon_color: "Custom"
                            icon_color: "black"
                            on_release: nav_drawer.set_state("toggle")  

                ClickableImage:
                    source: "set1 (2).png"
                    size_hint: None, None
                    size: dp(300), dp(300)
                    pos_hint: {"center_y": 0.35, "x": 0.10}
                    on_release: app.root.current = 'camera'

                ClickableImage:
                    source: "set2.png"
                    size_hint: None, None
                    size: dp(350), dp(350)
                    pos_hint: {"center_y": 0.38, "x": 0.25}
                    on_release: app.root.current = 'camera'

                ClickableImage:
                    source: "set3.png"
                    size_hint: None, None
                    size: dp(400), dp(400)
                    pos_hint: {"center_y": 0.42, "x": 0.40}
                    on_release: app.root.current = 'camera'

                ClickableImage:
                    source: "set4.png"
                    size_hint: None, None
                    size: dp(350), dp(350)
                    pos_hint: {"center_y": 0.33, "x": 0.63}
                    on_release: app.root.current = 'camera'
                    

        MDNavigationDrawer:
            id: nav_drawer
            anchor: 'right'
            md_bg_color: 146/255, 170/255, 131/255, 1

            BoxLayout:
                orientation: 'vertical'
                spacing: dp(10)
                padding: dp(20) 
                
                Widget:
                    size_hint_y: None
                    height: dp(100)
                
                MDLabel:
                    text: "ACCOUNT"
                    theme_text_color: "Hint"
                    text_color: "black"
                    font_style: "H6"
                    halign: "right"
                    size_hint_y: None
                    height: self.texture_size[1]
                    on_touch_down: app.show_account_screen() if self.collide_point(*args[1].pos) else None
                
                Widget:
                    size_hint_y: None
                    height: dp(10)
                
                MDLabel: 
                    text: "ABOUT US"
                    theme_text_color: "Hint"
                    text_color: "black"
                    font_style: "H6"
                    halign: "right"
                    size_hint_y: None
                    height: self.texture_size[1]
                    on_touch_down: app.show_about_screen() if self.collide_point(*args[1].pos) else None
                
                Widget:
                    size_hint_y: None
                    height: dp(10)
                
                MDLabel:
                    text: "CONTACTS"
                    theme_text_color: "Hint"
                    text_color: "black"
                    font_style: "H6"
                    halign: "right"
                    size_hint_y: None
                    height: self.texture_size[1]
                    on_touch_down: app.show_contacts_screen() if self.collide_point(*args[1].pos) else None
            
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
            orientation: 'horizontal'
            spacing: dp(10)
            size_hint: (0.7, 1)
            
            Camera:
                id: cam
                resolution: (640, 480)
                play: True
                allow_stretch: True
                keep_ratio: True
                
            MDRaisedButton:
                text: "Take a Photo"
                size_hint: None, None
                size: dp(150), dp(50)
                pos_hint: {"center_x": 0.5}
                on_release: app.capture()
                
        BoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            size_hint: (0.3, 1)
            
            Label:
                text: "DISPLAY PHOTO 1"
                size_hint_y: None
                height: dp(200)
                color: (0, 0, 0, 1)
                halign: 'center'
                valign: 'middle'
                text_size: self.size
                
            Image: 
                id: photo1
                source: ''
                size_hint_y: None
                height: dp(200)
                allow_stretch: True
                keep_ratio: True
                
            Label: 
                text: "DISPLAY PHOTO 2"
                size_hint_y: None
                height: dp(200)
                color: (0, 0, 0, 1)
                halign: 'center'
                valign: 'middle'
                text_size: self.size
                
            Image: 
                id: photo2
                source: ''
                size_hint_y: None
                height: dp(200)
                allow_stretch: True
                keep_ratio: True
                
            MDRaisedButton:
                text: "Confirm"
                size_hint: None, None
                size: dp(120), dp(40)
                pos_hint: {"center_x": 0.5}
                on_release: app.confirm()
'''

try:
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "testdb"
    )
    if connection.is_connected():
        print("Connected to localhost MySQL server!")
except Error as e:
    print("Failed to connect:", e)
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Connection closed.")

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

    def connect_and_insert(self):
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "testdb"
        )

        cursor = mydb.cursor()

        sql = "INSERT INTO users (name, username, password) VALUES (%s, %s)"
        val = ("John Angelo Evangelista, John Doe", "qwerty1234")
        cursor.execute(sql, val)

        mydb.commit()
        print(cursor.rowcount, "record inserted.")

        cursor.executed("SELECT * FROM users")
        for row in cursor.fetchall():
            print(row)

        cursor.close()
        mydb.close()

class ClickableImage(ButtonBehavior, Image):
    def on_press(self):
        print("Image Clicked!")

class CameraWidget(Image):
    def __init__(self, **kwargs):
        super(CameraWidget, self).__init__(**kwargs)
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0/30.0)

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            frame = cv2.flip(frame, 0)
            buf = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB).tobytes()
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt = 'rgb')
            texture.blit_buffer(buf, colorfmt = 'rgb', bufferfmt = 'ubyte')
            self.texture = texture


if __name__ == "__main__":
    Photobooth().run()