import customtkinter
from playsound import playsound
import time


class App(customtkinter.CTk):

	def __init__(self):
		super().__init__()
		self.geometry('900x600')

		self.welcome = customtkinter.CTkButton(self, text = 'BirdCode', command = self.button_welcome)
		self.welcome.pack(padx = 20, pady = 20)

	def button_welcome(self):

		print('Welcome to BirdCode')
		playsound('welcome_audio.mp3')
		time.sleep(2)
		playsound('welcome_audio_zh.mp3')
		time.sleep(2)
		playsound('welcome_audio_es.mp3')



app = App()
app.mainloop()