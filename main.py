
import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
import random
kivy.require('1.9.0')

class MyRoot(BoxLayout):
    def __init__(self):
        super(MyRoot,self).__init__()
    
    def generate_number(self):
        self.random_label.text=str(random.randint(0,1000))

class MyMapViewApp(App):
    def build(self):
        #mapview = MapView(zoom=11, lat=50.6394, lon=3.057)
        return MyRoot()

MyMapViewApp().run()