from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivymd.uix.fitimage import FitImage
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDTextButton
from kivymd.uix.label import MDLabel
from kivymd.uix.navigationdrawer import MDNavigationDrawer


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


KV = '''
ScreenManager:
    MainScreen:
    SignIn:
    RegisterForm:
    LogInForm:
    HomePage:

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
        source: "set1 (2).png"
        size_hint: None, None
        size: 200, 200
        pos_hint: {"center_x": 0.20, "center_y": 0.35}

    FitImage:
        source: "set2.png"
        size_hint: None, None
        size: 200, 300
        pos_hint: {"center_x": 0.35, "center_y": 0.40}

    FitImage:
        source: "set3.png"
        size_hint: None, None
        size: 200, 400
        pos_hint: {"center_x": 0.52, "center_y": 0.454}
        
    FitImage:
        source: "set4.png"
        size_hint: None, None
        size: 300, 300
        pos_hint: {"center_x": 0.73, "center_y": 0.353}

'''


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


if __name__ == "__main__":
    Photobooth().run()