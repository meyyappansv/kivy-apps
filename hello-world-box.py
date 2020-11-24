#!/usr/bin/python3

from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class HelloWorldApp(App):
    def build(self):
        b = BoxLayout(orientation='vertical')
        f = FloatLayout()
        s = Scatter()
        l = Label(text="default",font_size=150)
        t = TextInput(font_size=150,size_hint_y=None,height=200,text='default')
        t.bind(text=l.setter('text'))
        f.add_widget(s)
        s.add_widget(l)
        b.add_widget(f)
        b.add_widget(t) 
        return b


if __name__ == "__main__":

    HelloWorldApp().run()