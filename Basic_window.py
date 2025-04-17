import customtkinter
import tkinter as tk
from playsound import playsound
import time


class App(customtkinter.CTk):

	def __init__(self):
		super().__init__()
		self.geometry('500x600')
		self.grid_columnconfigure((0, 7), weight = 1)

		self.casual_value = tk.IntVar()
		self.backyard_value = tk.IntVar()
		self.twitcher_value = tk.IntVar()
		self.lister_value = tk.IntVar()
		self.photo_value = tk.IntVar()
		self.sci_value = tk.IntVar()
		self.travel_value = tk.IntVar()
		self.sound_value = tk.IntVar()
		self.armchair_value = tk.IntVar()
		self.artistic_value = tk.IntVar()
		self.conservation_value = tk.IntVar()
		self.social_value = tk.IntVar()

		self.welcome = customtkinter.CTkButton(self, text = 'Welcome to BirdCode', width = 200, command = self.button_welcome)
		self.welcome.grid(row = 0, column = 0, padx = 20, pady = (20, 20), columnspan = 2)
		self.birders_types_audio_button = customtkinter.CTkButton(self, text = 'Listen', width = 200, command = self.birders_types_audio_playing)
		self.birders_types_audio_button.grid(row = 7, column = 0, padx = 20, pady = (20, 20), columnspan = 2) 
		
		self.casual_checkbox = customtkinter.CTkCheckBox(self, text = 'Casual Birdwatcher', variable = self.casual_value)
		self.casual_checkbox.grid(row = 1, column = 0, padx = 20, pady = (30, 20), sticky = 'w')
		self.backyard_checkbox = customtkinter.CTkCheckBox(self, text = 'Backyard Birder', variable = self.backyard_value)
		self.backyard_checkbox.grid(row = 1, column = 1, padx = 20, pady = (30,20), sticky = 'w')
		self.twitcher_chechbox = customtkinter.CTkCheckBox(self, text = 'Twitcher (or Chaser)', variable = self.twitcher_value)
		self.twitcher_chechbox.grid(row = 2, column = 0, padx = 20, pady = (30, 20), sticky = 'w')
		self.lister_checkbox = customtkinter.CTkCheckBox(self, text = 'Lister (or Ticker)', variable = self.lister_value)
		self.lister_checkbox.grid(row = 2, column = 1, padx = 20, pady = (30, 20), sticky = 'w')
		self.photographic_checkbox = customtkinter.CTkCheckBox(self, text = 'Photographic Birder', variable = self.photo_value)
		self.photographic_checkbox.grid(row = 3, column = 0, padx = 20, pady = (30, 20), sticky = 'w')
		self.scientific_checkbox = customtkinter.CTkCheckBox(self, text = 'Scientific Birder', variable = self.sci_value)
		self.scientific_checkbox.grid(row = 3, column = 1, padx = 20, pady = (30, 20), sticky = 'w')
		self.travel_checkbox = customtkinter.CTkCheckBox(self, text = 'Travel & Eco-Tour Birder', variable = self.travel_value)
		self.travel_checkbox.grid(row = 4, column = 0, padx = 20, pady = (30, 20), sticky = 'w')
		self.sound_checkbox = customtkinter.CTkCheckBox(self, text = 'Sound Birder (By-Ear Birder)', variable = self.sound_value)
		self.sound_checkbox.grid(row = 4, column = 1, padx = 20, pady = (30, 20), sticky = 'w')
		self.armchair_checkbox = customtkinter.CTkCheckBox(self, text = 'Armchair Birder', variable = self.armchair_value)
		self.armchair_checkbox.grid(row = 5, column = 0, padx = 20, pady = (30, 20), sticky = 'w')
		self.artistic_checkbox = customtkinter.CTkCheckBox(self, text = 'Artistic Birder', variable = self.artistic_value)
		self.artistic_checkbox.grid(row = 5, column = 1, padx = 20, pady = (30, 20), sticky = 'w')
		self.conservation_checkbox = customtkinter.CTkCheckBox(self, text = 'Conservation-Focused Birder', variable = self.conservation_value)
		self.conservation_checkbox.grid(row = 6, column = 0, padx = 20, pady = (30, 20), sticky = 'w')
		self.social_checkbox = customtkinter.CTkCheckBox(self, text = 'Social Birder', variable = self.social_value)
		self.social_checkbox.grid(row = 6, column = 1, padx = 20, pady = (30, 20), sticky = 'w')



	def button_welcome(self):

		print('Welcome to BirdCode')
		playsound('Audios/welcome_audio.mp3')
		time.sleep(2)
		playsound('Audios/welcome_audio_zh.mp3')
		time.sleep(2)
		playsound('Audios/welcome_audio_es.mp3')

	def birders_types_audio_playing(self):

		if self.casual_value.get() == 1:

			playsound('Audios/CasualBirder_audio.mp3')
			time.sleep(6)

		if self.backyard_value.get() == 1:

			playsound('Audios/BackyardBirder_audio.mp3')
			time.sleep(6)

		if self.twitcher_value.get() == 1:

			playsound('Audios/TwitcherBirder_audio.mp3')
			time.sleep(6)

		if self.lister_value.get() == 1:

			playsound('Audios/ListerBirder_audio.mp3')
			time.sleep(6)

		if self.photo_value.get() == 1:

			playsound('Audios/PhotographicBirder_audio.mp3')
			time.sleep(6)

		if self.sci_value.get() == 1:

			playsound('Audios/ScientificBirder_audio.mp3')
			time.sleep(6)

		if self.travel_value.get() == 1:

			playsound('Audios/Travel_EcoBirder_audio.mp3')
			time.sleep(6)

		if self.sound_value.get() == 1:

			playsound('Audios/SoundBirder_audio.mp3')
			time.sleep(6)

		if self.armchair_value.get() == 1:

			playsound('Audios/ArmchairBirder_audio.mp3')
			time.sleep(6)

		if self.artistic_value.get() == 1:

			playsound('Audios/ArtisticBirder_audio.mp3')
			time.sleep(6)

		if self.conservation_value.get() == 1:

			playsound('Audios/ConservationBirder_audio.mp3')
			time.sleep(6)

		if self.social_value.get() == 1:

			playsound('Audios/SocialBirder_audio.mp3')
			time.sleep(6)






app = App()
app.mainloop()