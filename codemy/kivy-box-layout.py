#!/usr/bin/python3

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('box-layout.kv')

class MyBoxLayout(Widget):
   
   pass

class MyAwesomeApp(App):
    def build(self):
        return MyBoxLayout()


if __name__ == "__main__":
    MyAwesomeApp().run()
