import customtkinter
from playsound import playsound
import time


class App(customtkinter.CTk):

	def __init__(self):
		super().__init__()
		self.geometry('900x600')
		self.grid_columnconfigure((0, 1), weight = 1)

		self.welcome = customtkinter.CTkButton(self, text = 'BirdCode', width = 200, command = self.button_welcome)
		self.welcome.grid(row = 0, column = 0, padx = 20, pady = 20, columnspan = 2)
		self.casual_checkbox = customtkinter.CTkCheckBox(self, text = 'Casual birdwatcher')
		self.casual_checkbox.grid(row = 1, column = 0, padx = 20, pady = (30, 20), sticky = 'w')
		self.backyard_checkbox = customtkinter.CTkCheckBox(self, text = 'Backyard birder')
		self.backyard_checkbox.grid(row = 1, column = 1, padx = 20, pady = (30,20), sticky = 'w')

	def button_welcome(self):

		print('Welcome to BirdCode')
		playsound('Audios/welcome_audio.mp3')
		time.sleep(2)
		playsound('Audios/welcome_audio_zh.mp3')
		time.sleep(2)
		playsound('Audios/welcome_audio_es.mp3')



app = App()
app.mainloop()