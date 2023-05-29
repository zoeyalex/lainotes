#!/usr/bin/env python
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class MyGridLayout(GridLayout):

    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        # set number of columns
        self.cols = 1
        # add text box and initialize it
        self.text = TextInput(text=self.load())
        self.add_widget(self.text)
        # add button and initialize it
        self.submit = Button(text="Save")
        self.submit.bind(on_press=self.save)
        self.add_widget(self.submit)

    def save(self, instance):
        with open("notes", "w") as f:
            f.write(self.text.text)

    def load(self):
        with open("notes") as f:
            return f.read()


class MainApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MainApp().run()
