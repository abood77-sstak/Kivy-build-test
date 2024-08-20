from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.network.urlrequest import UrlRequest

class NetworkApp(App):
       def build(self):
           layout = BoxLayout(orientation='vertical')

           def on_success(request, result):
               # Handle the response data here
               response_label.text = "the messgae send"
               
           def on_error(request, error):
               # Handle errors if the request fails
               response_label.text = f"Error: {error}"

           request = UrlRequest("https://api.telegram.org/bot6684570996:AAFzhusCTo7muBNGfo0MUdHaNVY5YVAA9pU/sendmessage?text=hi&chat_id=1085837500", on_success=on_success, on_error=on_error)
   
           response_label = Label(text="Waiting for response...")
           layout.add_widget(response_label)

           return layout

if __name__ == '__main__':
       NetworkApp().run()
   
