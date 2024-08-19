
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout

import telebot



class TelegramSenderApp(App):
    def build(self):
        # Replace with your Telegram Bot API Token
        self.BOT_TOKEN = "6517080417:AAHQx2gxkQ5Sxs2GilTyCaOI4-jJZfIGaho"
        # Set App Title
        Window.clearcolor = (1, 1, 1, 1)  # Set background to white
        Window.title = "Telegram Message Sender"

        # Main Layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

         #Title Label
        title_label = Label(text="Send Telegram Messages", font_size=24, bold=True, color="black")
        layout.add_widget(title_label)

        # Image
        #telegram_image = Image(source='telegram.png')
#        layout.add_widget(telegram_image)

        # Input Field
        self.input_field = TextInput(multiline=False, hint_text="Enter your message", size_hint=(1, None))
        layout.add_widget(self.input_field)

        # Send Button
        send_button = Button(text="Send", size_hint=(1, None))
        send_button.bind(on_press=self.send_message)
        layout.add_widget(send_button)

        return layout

    def send_message(self, instance):
        message = self.input_field.text
        if message:
            try:
                # Create a Telegram Bot object
                bot = telebot.TeleBot(self.BOT_TOKEN)

                # Replace with your chat ID (get it from Telegram)
                chat_id = "1085837500" 
                bot.send_message(chat_id=chat_id, text=message)

                # Success Popup
                popup = Popup(title='Success', content=Label(text='Message sent successfully!'), size_hint=(None, None), size=(200, 150))
                popup.open()

            except Exception as e:
                # Error Popup
                popup = Popup(title='Error', content=Label(text=f'Error sending message: {e}'), size_hint=(None, None), size=(250, 150))
                popup.open()

            self.input_field.text = ''

if __name__ == '__main__':
    r = TelegramSenderApp()
    r.run()
