import customtkinter
import tkinter as tk
from playsound import playsound
import time


class App(customtkinter.CTk):

	def __init__(self):
		super().__init__()
		self.geometry('500x650')
		self.title('BirdCode World')
		self.grid_columnconfigure((0, 7), weight = 1)
		customtkinter.set_appearance_mode('dark')
		customtkinter.set_default_color_theme('green')

		
		self.welcome = customtkinter.CTkButton(self, text = 'Welcome to BirdCode', width = 200, command = self.button_welcome)
		self.welcome.grid(row = 0, column = 0, padx = 20, pady = (20, 20), columnspan = 2)
		self.birders_types_audio_button = customtkinter.CTkButton(self, text = 'Listen', width = 200, command = self.birders_types_audio_playing)
		self.birders_types_audio_button.grid(row = 7, column = 0, padx = 20, pady = (20, 20))


		self.checkbox_frame = customtkinter.CTkFrame(self)
		self.checkbox_frame.grid(row = 1, column = 0, padx = 20, pady = (20, 20), sticky = 'nsw')
		self.casual_checkbox = customtkinter.CTkCheckBox(self.checkbox_frame, text = 'Casual Birdwatcher')
		self.casual_checkbox.grid(row = 0, column = 0, padx = 20, pady = (30, 20), sticky = 'w')
		self.backyard_checkbox = customtkinter.CTkCheckBox(self.checkbox_frame, text = 'Backyard Birder')
		self.backyard_checkbox.grid(row = 0, column = 1, padx = 20, pady = (30,20), sticky = 'w')
		self.twitcher_chechbox = customtkinter.CTkCheckBox(self.checkbox_frame, text = 'Twitcher (or Chaser)')
		self.twitcher_chechbox.grid(row = 1, column = 0, padx = 20, pady = (30, 20), sticky = 'w')
		self.lister_checkbox = customtkinter.CTkCheckBox(self.checkbox_frame, text = 'Lister (or Ticker)')
		self.lister_checkbox.grid(row = 1, column = 1, padx = 20, pady = (30, 20), sticky = 'w')
		self.photographic_checkbox = customtkinter.CTkCheckBox(self.checkbox_frame, text = 'Photographic Birder')
		self.photographic_checkbox.grid(row = 2, column = 0, padx = 20, pady = (30, 20), sticky = 'w')
		self.scientific_checkbox = customtkinter.CTkCheckBox(self.checkbox_frame, text = 'Scientific Birder')
		self.scientific_checkbox.grid(row = 2, column = 1, padx = 20, pady = (30, 20), sticky = 'w')
		self.travel_checkbox = customtkinter.CTkCheckBox(self.checkbox_frame, text = 'Travel & Eco-Tour Birder')
		self.travel_checkbox.grid(row = 3, column = 0, padx = 20, pady = (30, 20), sticky = 'w')
		self.sound_checkbox = customtkinter.CTkCheckBox(self.checkbox_frame, text = 'Sound Birder (By-Ear Birder)')
		self.sound_checkbox.grid(row = 3, column = 1, padx = 20, pady = (30, 20), sticky = 'w')
		self.armchair_checkbox = customtkinter.CTkCheckBox(self.checkbox_frame, text = 'Armchair Birder')
		self.armchair_checkbox.grid(row = 4, column = 0, padx = 20, pady = (30, 20), sticky = 'w')
		self.artistic_checkbox = customtkinter.CTkCheckBox(self.checkbox_frame, text = 'Artistic Birder')
		self.artistic_checkbox.grid(row = 4, column = 1, padx = 20, pady = (30, 20), sticky = 'w')
		self.conservation_checkbox = customtkinter.CTkCheckBox(self.checkbox_frame, text = 'Conservation-Focused Birder')
		self.conservation_checkbox.grid(row = 5, column = 0, padx = 20, pady = (30, 20), sticky = 'w')
		self.social_checkbox = customtkinter.CTkCheckBox(self.checkbox_frame, text = 'Social Birder')
		self.social_checkbox.grid(row = 5, column = 1, padx = 20, pady = (30, 20), sticky = 'w')



	def button_welcome(self):

		print('Welcome to BirdCode')
		playsound('Audios/welcome_audio.mp3')
		time.sleep(2)
		playsound('Audios/welcome_audio_zh.mp3')
		time.sleep(2)
		playsound('Audios/welcome_audio_es.mp3')

	def birders_types_audio_playing(self):

		if self.casual_checkbox.get() == 1:

			playsound('Audios/CasualBirder_audio.mp3')
			time.sleep(6)

		if self.backyard_checkbox.get() == 1:

			playsound('Audios/BackyardBirder_audio.mp3')
			time.sleep(6)

		if self.twitcher_chechbox.get() == 1:

			playsound('Audios/TwitcherBirder_audio.mp3')
			time.sleep(6)

		if self.lister_checkbox.get() == 1:

			playsound('Audios/ListerBirder_audio.mp3')
			time.sleep(6)

		if self.photographic_checkbox.get() == 1:

			playsound('Audios/PhotographicBirder_audio.mp3')
			time.sleep(6)

		if self.scientific_checkbox.get() == 1:

			playsound('Audios/ScientificBirder_audio.mp3')
			time.sleep(6)

		if self.travel_checkbox.get() == 1:

			playsound('Audios/Travel_EcoBirder_audio.mp3')
			time.sleep(6)

		if self.sound_checkbox.get() == 1:

			playsound('Audios/SoundBirder_audio.mp3')
			time.sleep(6)

		if self.armchair_checkbox.get() == 1:

			playsound('Audios/ArmchairBirder_audio.mp3')
			time.sleep(6)

		if self.artistic_checkbox.get() == 1:

			playsound('Audios/ArtisticBirder_audio.mp3')
			time.sleep(6)

		if self.conservation_checkbox.get() == 1:

			playsound('Audios/ConservationBirder_audio.mp3')
			time.sleep(6)

		if self.social_checkbox.get() == 1:

			playsound('Audios/SocialBirder_audio.mp3')
			time.sleep(6)


app = App()
app.mainloop()