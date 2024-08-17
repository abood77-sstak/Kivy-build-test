import kivy
kivy.require('2.0.0')  # Replace with your Kivy version

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

import telebot

# Replace with your Telegram Bot API Token
BOT_TOKEN = "6517080417:AAHQx2gxkQ5Sxs2GilTyCaOI4-jJZfIGaho" 

class TelegramSenderApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Label for the input field
        self.label = Label(text='Enter your message:')
        layout.add_widget(self.label)
        
        # Input field for the message
        self.input_field = TextInput(multiline=False)  
        layout.add_widget(self.input_field)
        self.error_label = Label()
        layout.add_widget(self.error_label)
        # Send button
        send_button = Button(text='Send to Telegram')
        send_button.bind(on_press=self.send_message)
        layout.add_widget(send_button)
        layout.add_widget(Label())
        return layout

    def send_message(self, instance):
        message = self.input_field.text
        if message:
            # Create a new Telegram Bot object
            bot = telebot.TeleBot(BOT_TOKEN) 
            
            try:
                # Send the message to your desired chat ID
                # Replace with your actual chat ID 
                bot.send_message(chat_id=1085837500, text=message) 
                self.error_label.text = 'Message sent successfully!'
                self.input_field.text = ''  # Clear the input field
            except Exception as e:
                self.error_label.text = 'sending message invalid'

if __name__ == '__main__':
    TelegramSenderApp().run()
