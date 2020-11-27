#!/usr/bin/python3

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('hau.kv')

class MyGridLayout(Widget):
   
   
    s421 = ObjectProperty(None)
    s401 = ObjectProperty(None)
    s433 = ObjectProperty(None)
    s416 = ObjectProperty(None)
    s406 = ObjectProperty(None)
    s434 = ObjectProperty(None)
    s445 = ObjectProperty(None)
    b401 = ObjectProperty(None)

    def start_load(self):
        s421 = self.s421.active
        if s421 is True:
            print('s421')
    
    def stop_load(self):
        pass

    def start_test(self):
        pass

    def stop_test(self):
        pass




class HauApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    HauApp().run()