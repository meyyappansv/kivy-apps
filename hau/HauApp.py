#!/usr/bin/python3

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('hau.kv')

class MyGridLayout(Widget):
   
   
    def press(self):
        

        print('Hello your name is ')
        


class HauApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    HauApp().run()