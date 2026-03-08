from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
Window.clearcolor=(0.1,0.1,0.18,1)
class BenimappApp(App):
    def build(self):
        self.title="BenimApp"
        root=BoxLayout(orientation="vertical",padding=20,spacing=12)
        root.add_widget(Label(text="🚀 BenimApp",font_size="24sp",size_hint=(1,None),height=60,color=(0.49,0.23,0.93,1)))
        self.entry=TextInput(hint_text="Bir şey yaz...",font_size="16sp",size_hint=(1,None),height=60,background_color=(0.15,0.15,0.25,1),foreground_color=(0.9,0.9,0.9,1))
        root.add_widget(self.entry)
        btn=Button(text="⚡ İşlem Yap",font_size="16sp",size_hint=(1,None),height=56,background_color=(0.49,0.23,0.93,1),background_normal="")
        btn.bind(on_press=self._go); root.add_widget(btn)
        self.res=Label(text="Sonuç burada görünecek...",font_size="14sp",color=(0.6,0.6,0.6,1),halign="center")
        root.add_widget(self.res)
        return root
    def _go(self,*a):
        t=self.entry.text.strip()
        self.res.text=f"✅ {t}" if t else "⚠️ Bir şey girin!"
if __name__=="__main__": BenimappApp().run()
