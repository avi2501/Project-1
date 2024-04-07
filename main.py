
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class myapp(MDApp):
    def build(self):
        a= MDLabel(text='welcme ji', halign='center')
        return a
    
if __name__ =='__main__':
    myapp().run()
