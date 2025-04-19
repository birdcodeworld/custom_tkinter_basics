import os
import customtkinter
import tkinter as tk
from tkintermapview import TkinterMapView
from playsound import playsound
import time
from PIL import Image, ImageTk


class myTabView(customtkinter.CTkTabview):

	def __init__(self, master, **kwargs):
		super().__init__(master, **kwargs)

		# Create tabs
		self.add('Login')
		self.add('Birdwatcher Types')
		self.add('Birding China')
		self.add('Map of provinces Locations')

		self.province_name = tk.StringVar()

		self.checkbox_frame = myCheckBoxFrame(master = self.tab('Birdwatcher Types'))
		self.checkbox_frame.grid(row = 1, column = 0, padx = 30, pady = (20, 20), sticky = 'nsw')

		self.birders_types_audio_button = customtkinter.CTkButton(master = self.tab('Birdwatcher Types'), text = 'Listen', 
			width = 200, command = self.checkbox_frame.get_audios)
		self.birders_types_audio_button.grid(row = 7, column = 0, padx = 20, pady = (20, 20))

		self.welcome = customtkinter.CTkButton(master = self.tab('Birdwatcher Types'), text = 'Welcome to BirdCode', width = 200, command = self.button_welcome)
		self.welcome.grid(row = 0, column = 2, padx = 20, pady = (10, 0), columnspan = 2)

		self.EagleImage = customtkinter.CTkImage(dark_image = Image.open('Images/Accipitriforme4.png'), size = (750, 500))
		self.EagleImage_Label = customtkinter.CTkLabel(master = self.tab('Birdwatcher Types'), image = self.EagleImage, text = '')
		self.EagleImage_Label.grid(row = 1, column = 2, padx = 20, pady = 20, rowspan = 8)

		#self.mark = customtkinter.CTkImage(dark_image = Image.open('Images/logo (3).png'))

		self.map_widget_china = TkinterMapView(master = self.tab('Birding China'), width = 800, height = 570)
		self.map_widget_china.grid(row = 0, column = 0, padx = 10, pady = 10, rowspan = 8)
		self.map_widget_china.set_position(36.220879, 104.787180)
		self.map_widget_china.set_zoom(4)
		
		self.map_title = customtkinter.CTkLabel(master = self.tab('Birding China'), text = 'PROVINCE NAME GUESSING GAME', font = ('Times New Roman', 20))
		self.map_title.grid(row = 0, column = 1, padx = 30, pady = 10, columnspan = 2)

		self.guess_province = customtkinter.CTkEntry(master = self.tab('Birding China'), textvariable = self.province_name, font = ('Kaiti', 30))
		self.guess_province.grid(row = 1, column = 1, padx = 30, pady = 10)
		self.guess_province.configure(width = 250)

		self.send_name_button = customtkinter.CTkButton(master = self.tab('Birding China'), text = 'Send', width = 20, font = ('Times New Roman', 20))
		self.send_name_button.grid(row = 1, column = 2, pady = 10)

		self.current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
		self.mark = ImageTk.PhotoImage(Image.open(os.path.join(self.current_path, "Images", "Marker_black.png")).resize((50, 65)))

		
		self.marker1 = self.map_widget_china.set_marker(30.499426, 102.853586, text = 'Sichuan', icon = self.mark, 
			text_color = 'black', command = self.define_province_zoom)


		self.map_widget_province = TkinterMapView(master = self.tab('Map of provinces Locations'), width = 950, height = 570)
		self.map_widget_province.grid(row = 0, column = 0, padx = 10, pady = 10)
		self.map_widget_province.set_position(30.499426, 102.853586)
		self.map_widget_province.set_zoom(4)
		self.map_widget_province.set_tile_server('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}')
		self.name2 = customtkinter.CTkLabel(master = self.tab('Map of provinces Locations'), text = '')
		self.name2.grid(row = 0, column = 1)


	def define_province_zoom(self, marker1):

		self.map_widget_province.set_zoom(6)
		self.marker2 = self.map_widget_province.set_marker(30.499426, 102.853586, icon = self.mark,
		text = 'Sichuan', text_color = 'white', font = ('Times New Roman', 20), command = self.name)

	def name(self, marker2):

		self.name2.configure(text = 'Done')




	def button_welcome(self):

		print('Welcome to BirdCode')
		playsound('Audios/welcome_audio.mp3')
		time.sleep(2)
		playsound('Audios/welcome_audio_zh.mp3')
		time.sleep(2)
		playsound('Audios/welcome_audio_es.mp3')


class myCheckBoxFrame(customtkinter.CTkFrame):

	def __init__(self, master):
		super().__init__(master)

		self.casual_checkbox = customtkinter.CTkCheckBox(self, text = 'Casual Birdwatcher')
		self.casual_checkbox.grid(row = 0, column = 0, padx = 20, pady = (30, 20), sticky = 'w')
		self.backyard_checkbox = customtkinter.CTkCheckBox(self, text = 'Backyard Birder')
		self.backyard_checkbox.grid(row = 0, column = 1, padx = 20, pady = (30,20), sticky = 'w')
		self.twitcher_chechbox = customtkinter.CTkCheckBox(self, text = 'Twitcher (or Chaser)')
		self.twitcher_chechbox.grid(row = 1, column = 0, padx = 20, pady = (30, 20), sticky = 'w')
		self.lister_checkbox = customtkinter.CTkCheckBox(self, text = 'Lister (or Ticker)')
		self.lister_checkbox.grid(row = 1, column = 1, padx = 20, pady = (30, 20), sticky = 'w')
		self.photographic_checkbox = customtkinter.CTkCheckBox(self, text = 'Photographic Birder')
		self.photographic_checkbox.grid(row = 2, column = 0, padx = 20, pady = (30, 20), sticky = 'w')
		self.scientific_checkbox = customtkinter.CTkCheckBox(self, text = 'Scientific Birder')
		self.scientific_checkbox.grid(row = 2, column = 1, padx = 20, pady = (30, 20), sticky = 'w')
		self.travel_checkbox = customtkinter.CTkCheckBox(self, text = 'Travel Birder')
		self.travel_checkbox.grid(row = 3, column = 0, padx = 20, pady = (30, 20), sticky = 'w')
		self.sound_checkbox = customtkinter.CTkCheckBox(self, text = 'Sound Birder')
		self.sound_checkbox.grid(row = 3, column = 1, padx = 20, pady = (30, 20), sticky = 'w')
		self.armchair_checkbox = customtkinter.CTkCheckBox(self, text = 'Armchair Birder')
		self.armchair_checkbox.grid(row = 4, column = 0, padx = 20, pady = (30, 20), sticky = 'w')
		self.artistic_checkbox = customtkinter.CTkCheckBox(self, text = 'Artistic Birder')
		self.artistic_checkbox.grid(row = 4, column = 1, padx = 20, pady = (30, 20), sticky = 'w')
		self.conservation_checkbox = customtkinter.CTkCheckBox(self, text = 'Conservation Birder')
		self.conservation_checkbox.grid(row = 5, column = 0, padx = 20, pady = (30, 20), sticky = 'w')
		self.social_checkbox = customtkinter.CTkCheckBox(self, text = 'Social Birder')
		self.social_checkbox.grid(row = 5, column = 1, padx = 20, pady = (30, 20), sticky = 'w')


	def get_audios(self):

		self.re = [self.casual_checkbox, self.backyard_checkbox]
		self.au = ['Audios/CasualBirder_audio.mp3', 'Audios/BackyardBirder_audio.mp3']

		count = 0

		while count < len(self.re):

			if self.re[count].get() == 1:

				playsound(self.au[count])
				time.sleep(5)

			count = count + 1

		# if self.casual_checkbox.get() == 1:

		# 	playsound('Audios/CasualBirder_audio.mp3')
		# 	time.sleep(6)

		# if self.backyard_checkbox.get() == 1:

		# 	playsound('Audios/BackyardBirder_audio.mp3')
		# 	time.sleep(6)

		# if self.twitcher_chechbox.get() == 1:

		# 	playsound('Audios/TwitcherBirder_audio.mp3')
		# 	time.sleep(6)

		# if self.lister_checkbox.get() == 1:

		# 	playsound('Audios/ListerBirder_audio.mp3')
		# 	time.sleep(6)

		# if self.photographic_checkbox.get() == 1:

		# 	playsound('Audios/PhotographicBirder_audio.mp3')
		# 	time.sleep(6)

		# if self.scientific_checkbox.get() == 1:

		# 	playsound('Audios/ScientificBirder_audio.mp3')
		# 	time.sleep(6)

		# if self.travel_checkbox.get() == 1:

		# 	playsound('Audios/Travel_EcoBirder_audio.mp3')
		# 	time.sleep(6)

		# if self.sound_checkbox.get() == 1:

		# 	playsound('Audios/SoundBirder_audio.mp3')
		# 	time.sleep(6)

		# if self.armchair_checkbox.get() == 1:

		# 	playsound('Audios/ArmchairBirder_audio.mp3')
		# 	time.sleep(6)

		# if self.artistic_checkbox.get() == 1:

		# 	playsound('Audios/ArtisticBirder_audio.mp3')
		# 	time.sleep(6)

		# if self.conservation_checkbox.get() == 1:

		# 	playsound('Audios/ConservationBirder_audio.mp3')
		# 	time.sleep(6)

		# if self.social_checkbox.get() == 1:

		# 	playsound('Audios/SocialBirder_audio.mp3')
		# 	time.sleep(6)


class App(customtkinter.CTk):

	def __init__(self):
		super().__init__()
		self.geometry('1250x650')
		self.title('BirdCode World')
		self.grid_columnconfigure((0, 2), weight = 1)
		customtkinter.set_appearance_mode('dark')
		customtkinter.set_default_color_theme('green')
		
		self.tab_view = myTabView(master = self, width = 1200, height = 630)
		self.tab_view.grid(row = 0, column = 0, padx = 10, pady = 0)

		
	
app = App()
app.mainloop()