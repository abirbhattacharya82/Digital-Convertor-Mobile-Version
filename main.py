from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


Builder.load_file("design.kv")
def dec_to_bin(n):  
    return bin(n).replace("0b", "")

def bin_to_dec(n):
    num = n; 
    dec_value = 0; 
    base = 1; 
    temp = num; 
    while(temp): 
        last_digit = temp % 10; 
        temp = int(temp / 10); 
          
        dec_value += last_digit * base; 
        base = base * 2; 
    return dec_value; 

class Sc(Screen):
    def convert(self,bina,dec):
        x=""+bina
        y=""+dec
        if x=="":
            a=int(y)
            x=str(dec_to_bin(int(a)))
            self.ids.bina.text=x
        elif y=="":
            a=int(x)
            y=str(bin_to_dec(a))
            self.ids.dec.text=y

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__=="__main__":
    MainApp().run()

