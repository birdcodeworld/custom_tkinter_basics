import customtkinter
from playsound import playsound
import time


class App(customtkinter.CTk):

	def __init__(self):
		super().__init__()
		self.geometry('500x600')
		self.grid_columnconfigure((0, 1), weight = 1)

		self.welcome = customtkinter.CTkButton(self, text = 'Welcome to BirdCode', width = 200, command = self.button_welcome)
		self.welcome.grid(row = 0, column = 0, padx = 20, pady = 20, columnspan = 2)
		self.casual_checkbox = customtkinter.CTkCheckBox(self, text = 'Casual Birdwatcher')
		self.casual_checkbox.grid(row = 1, column = 0, padx = 20, pady = (30, 20), sticky = 'w')
		self.backyard_checkbox = customtkinter.CTkCheckBox(self, text = 'Backyard Birder')
		self.backyard_checkbox.grid(row = 1, column = 1, padx = 20, pady = (30,20), sticky = 'w')
		self.twitcher_chechbox = customtkinter.CTkCheckBox(self, text = 'Twitcher (or Chaser)')
		self.twitcher_chechbox.grid(row = 2, column = 0, padx = 20, pady = (30, 20), sticky = 'w')
		self.lister_checkbox = customtkinter.CTkCheckBox(self, text = 'Lister (or Ticker)')
		self.lister_checkbox.grid(row = 2, column = 1, padx = 20, pady = (30, 20), sticky = 'w')
		self.photographic_checkbox = customtkinter.CTkCheckBox(self, text = 'Photographic Birder')
		self.photographic_checkbox.grid(row = 3, column = 0, padx = 20, pady = (30, 20), sticky = 'w')
		self.scientific_checkbox = customtkinter.CTkCheckBox(self, text = 'Scientific Birder')
		self.scientific_checkbox.grid(row = 3, column = 1, padx = 20, pady = (30, 20), sticky = 'w')
		self.travel_checkbox = customtkinter.CTkCheckBox(self, text = 'Travel & Eco-Tour Birder')
		self.travel_checkbox.grid(row = 4, column = 0, padx = 20, pady = (30, 20), sticky = 'w')
		self.sound_checkbox = customtkinter.CTkCheckBox(self, text = 'Sound Birder (By-Ear Birder)')
		self.sound_checkbox.grid(row = 4, column = 1, padx = 20, pady = (30, 20), sticky = 'w')
		self.armchair_checkbox = customtkinter.CTkCheckBox(self, text = 'Armchair Birder')
		self.armchair_checkbox.grid(row = 5, column = 0, padx = 20, pady = (30, 20), sticky = 'w')
		self.artistic_checkbox = customtkinter.CTkCheckBox(self, text = 'Artistic Birder')
		self.artistic_checkbox.grid(row = 5, column = 1, padx = 20, pady = (30, 20), sticky = 'w')
		self.conservation_checkbox = customtkinter.CTkCheckBox(self, text = 'Conservation-Focused Birder')
		self.conservation_checkbox.grid(row = 6, column = 0, padx = 20, pady = (30, 20), sticky = 'w')
		self.social_checkbox = customtkinter.CTkCheckBox(self, text = 'Social Birder')
		self.social_checkbox.grid(row = 6, column = 1, padx = 20, pady = (30, 20), sticky = 'w')




	def button_welcome(self):

		print('Welcome to BirdCode')
		playsound('Audios/welcome_audio.mp3')
		time.sleep(2)
		playsound('Audios/welcome_audio_zh.mp3')
		time.sleep(2)
		playsound('Audios/welcome_audio_es.mp3')



app = App()
app.mainloop()