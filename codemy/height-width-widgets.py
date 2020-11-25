#!/usr/bin/python3

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    # initialize infinite keyword
    def __init__(self,**kwargs):
        ## Call grid layout constructor
        super(MyGridLayout,self).__init__(**kwargs)

        ## Set columns 
        self.cols = 1

        self.top_grid = GridLayout()
        self.top_grid.cols  = 2

        ## Add widgets 
        #Add Label
        self.top_grid.add_widget(Label(text="Name: ",size_hint_y=None,height=50,size_hint_x=None,width=200))
        ## Add Input Box 
        self.name = TextInput(multiline=True,size_hint_y=None,height=50,size_hint_x=None,width=200)
        self.top_grid.add_widget(self.name)


        self.top_grid.add_widget(Label(text="Favorite Pizza:",size_hint_y=None,height=50,size_hint_x=None,width=200))
        self.pizza = TextInput(multiline=False,size_hint_y=None,height=50,size_hint_x=None,width=200)
        self.top_grid.add_widget(self.pizza)

        self.top_grid.add_widget(Label(text="Favorite Color:",size_hint_y=None,height=50,size_hint_x=None,width=200))
        self.color = TextInput(multiline=False,size_hint_y=None,height=50,size_hint_x=None,width=200)
        self.top_grid.add_widget(self.color)

       
        self.add_widget(self.top_grid)
        self.submit = Button(text="Submit",font_size=32,size_hint_y=None,height=50,size_hint_x=None,width=200)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        #print(f'Hello your name is {name}, your favorite pizza is {pizza}, your favorite color is {color}')
        self.add_widget(Label(text=f'Hello your name is {name}, your favorite pizza is {pizza}, your favorite color is {color}'))
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""

class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    MyApp().run()
