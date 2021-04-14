# main.py filename needed for deployment
# pip install kivy
# main.py for logic
# design.kv for GUI
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('design.kv')

class LoginScreen(Screen):
    # comes after screenmanager
    pass

class RootWidget(ScreenManager):
    # comes after app
    pass

class MainApp(App):
    # highest hierarchy
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()