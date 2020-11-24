#!/usr/bin/python3

from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.scatter import Scatter
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class HelloWorldApp(App):
    def build(self):
        l1 = Label(text='s421')
        #b1 = Button(size_hint=(0.7,1),width=50,background_color=(0,0,1,1))
        c1 = CheckBox(size_hint_x=None,width=50)
        l2 = Label(text='s401')
        c2 = CheckBox(size_hint_x=None,width=50)
        g = GridLayout(cols=2)
        g.add_widget(l1)
        g.add_widget(c1)
        g.add_widget(l2)
        g.add_widget(c2)
        return g


if __name__ == "__main__":

    HelloWorldApp().run()