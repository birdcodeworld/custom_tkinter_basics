import os
import customtkinter
import tkinter as tk
from tkintermapview import TkinterMapView
import psycopg2
import hashlib
from Markers import *
from Audios import *
#from db_connections import *
from hash import *
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

		self.username = tk.StringVar()

		self.Eagle_logo = customtkinter.CTkImage(dark_image = Image.open('Images/BirdCode_logo.png'), size = (600, 528))
		self.points_logo = customtkinter.CTkImage(dark_image = Image.open('Images/Points_logo.png'), size = (100, 120))
		self.coins_logo = customtkinter.CTkImage(dark_image = Image.open('Images/Coins_logo.png'), size = (100, 120))
		self.feathers_logo = customtkinter.CTkImage(dark_image = Image.open('Images/Feathers_logo.png'), size = (100, 120))
		self.Eagle_login = customtkinter.CTkButton(master = self.tab('Login'), image = self.Eagle_logo, text = '', command = self.login_user)
		self.Eagle_login.grid(row = 0, column = 0, padx = 20, pady = 20, rowspan = 7)

		self.sichuan_photo = customtkinter.CTkImage(dark_image = Image.open('Images/sichuanphoto.png'), size = (300, 200))
		
		self.Login_label = customtkinter.CTkLabel(master = self.tab('Login'), text = 'BIRDCODE LOGIN', font = ('Times New Roman', 30))
		self.Login_label.grid(row = 0, column = 1, padx = 150, pady = 40, columnspan = 3)

		self.username_label = customtkinter.CTkLabel(master = self.tab('Login'), text = 'Username', font = ('Times New Roman', 25))
		self.username_label.grid(row = 1, column = 1, padx = 80, pady = 10, sticky = 'w', columnspan = 3)

		self.username_entry = customtkinter.CTkEntry(master = self.tab('Login'), width = 370, font = ('Times New Roman', 20),
			textvariable = self.username)
		self.username_entry.grid(row = 2, column = 1, padx = 30, sticky = 'w', columnspan = 3)

		self.password_label = customtkinter.CTkLabel(master = self.tab('Login'), text = 'Password', font = ('Times New Roman', 25))
		self.password_label.grid(row = 3, column = 1, padx = 80, pady = 10, sticky = 'w', columnspan = 3)

		self.password_entry = customtkinter.CTkEntry(master = self.tab('Login'), width = 370, font = ('Times New Roman', 20))
		self.password_entry.grid(row = 4, column = 1, padx = 30, sticky = 'w', columnspan = 3)

		self.points_button = customtkinter.CTkButton(master = self.tab('Login'), image = self.points_logo, text = '')
		self.points_button.grid(row = 5, column = 1, padx = (30, 5), pady = (80, 20), sticky = 'w')
		self.coins_button = customtkinter.CTkButton(master = self.tab('Login'), image = self.coins_logo, text = '')
		self.coins_button.grid(row = 5, column = 2, padx = (0, 0), pady = (80, 20), sticky = 'w')
		self.feathers_button = customtkinter.CTkButton(master = self.tab('Login'), image = self.feathers_logo, text = '')
		self.feathers_button.grid(row = 5, column = 3, padx = (5, 20), pady = (80, 20), sticky = 'w')

		self.points_label = customtkinter.CTkLabel(master = self.tab('Login'), text = '1230', font = ('Times New Roman', 25))
		self.points_label.grid(row = 6, column = 1, padx = (50, 30), sticky = 'nwse')
		self.coins_label = customtkinter.CTkLabel(master = self.tab('Login'), text = '5444', font = ('Times New Roman', 25))
		self.coins_label.grid(row = 6, column = 2, padx = (0, 20), sticky = 'nwse')
		self.feathers_label = customtkinter.CTkLabel(master = self.tab('Login'), text = '3888', font = ('Times New Roman', 25))
		self.feathers_label.grid(row = 6, column = 3, padx = (50, 0), sticky = 'nw')
		

		self.login_zh = customtkinter.CTkLabel(master = self.tab('Login'), text = '欢\n迎\n来\n到\n鸟\n码\n中\n国', font = ('Kaiti', 40))
		self.login_zh.grid(row = 0, column = 3, rowspan = 5, padx = (70, 30), sticky = 'ne')


		self.birder_types_title = customtkinter.CTkLabel(master = self.tab('Birdwatcher Types'), text = 'BIRDWATCHER TYPES',
			font = ('Times New Roman', 20))
		self.birder_types_title.grid(row = 0, column = 0, padx = 10, pady = 10, columnspan = 2)

		self.checkbox_frame = myCheckBoxFrame(master = self.tab('Birdwatcher Types'))
		self.checkbox_frame.grid(row = 1, column = 0, padx = 30, pady = (0, 20), sticky = 'nsw', columnspan = 2)

		self.birders_types_audio_button = customtkinter.CTkButton(master = self.tab('Birdwatcher Types'), text = 'Listen', 
			width = 100, command = self.checkbox_frame.get_audios)
		self.birders_types_audio_button.grid(row = 7, column = 0, padx = 20, pady = (20, 20))

		self.upload_birder_types = customtkinter.CTkButton(master = self.tab('Birdwatcher Types'), text = 'Upload your hobbie')
		self.upload_birder_types.grid(row = 7, column = 1, padx = 10)

		self.welcome = customtkinter.CTkButton(master = self.tab('Birdwatcher Types'), text = 'Welcome to BirdCode China', 
			width = 200, command = self.button_welcome)
		self.welcome.grid(row = 0, column = 2, padx = 20, pady = (10, 0), columnspan = 2)

		self.EagleImage = customtkinter.CTkImage(dark_image = Image.open('Images/Accipitriforme4.png'), size = (750, 500))
		self.EagleImage_Label = customtkinter.CTkLabel(master = self.tab('Birdwatcher Types'), image = self.EagleImage, text = '')
		self.EagleImage_Label.grid(row = 1, column = 2, padx = 20, pady = 20, rowspan = 8)

		#self.mark = customtkinter.CTkImage(dark_image = Image.open('Images/logo (3).png'))

		self.map_widget_china = TkinterMapView(master = self.tab('Birding China'), width = 800, height = 570)
		self.map_widget_china.grid(row = 0, column = 0, padx = 10, pady = 10, rowspan = 6)
		self.map_widget_china.set_position(36.220879, 104.787180)
		self.map_widget_china.set_zoom(4)
		
		self.map_title = customtkinter.CTkLabel(master = self.tab('Birding China'), text = 'PROVINCE NAME GUESSING GAME', font = ('Times New Roman', 20))
		self.map_title.grid(row = 0, column = 1, padx = 30, columnspan = 2)

		self.answer_entry_zhname = myAnswerEntryFrame(master = self.tab('Birding China'))
		self.answer_entry_zhname.grid(row = 1, column = 1, columnspan = 2)

		self.hits = customtkinter.CTkLabel(master = self.tab('Birding China'), text = 'Hits', font = ('Times New Roman', 25))
		self.hits.grid(row = 2, column = 1, padx = 20)

		self.wrongs = customtkinter.CTkLabel(master = self.tab('Birding China'), text = 'Wrongs', font = ('Times New Roman', 25))
		self.wrongs.grid(row = 2, column = 2, padx = 20)

		self.hits_score = customtkinter.CTkLabel(master = self.tab('Birding China'), text = '350', font = ('Times New Roman', 50))
		self.hits_score.grid(row = 3, column = 1, padx = 10)

		self.wrongs_score = customtkinter.CTkLabel(master = self.tab('Birding China'), text = '780', font = ('Times New Roman', 50))
		self.wrongs_score.grid(row = 3, column = 2, padx = 10)

		self.sichuan_photo_button = customtkinter.CTkButton(master = self.tab('Birding China'), image = self.sichuan_photo, 
			text = '', command = self.photo_questions_01)
		self.sichuan_photo_button.grid(row = 4, column = 1, padx = 20, pady = 20, columnspan = 2)

		self.change_photo_button_frw = customtkinter.CTkButton(master = self.tab('Birding China'), text = 'forward')
		self.change_photo_button_frw.grid(row = 5, column = 1, padx = 20, sticky = 'w')



		self.current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
		self.mark_black = ImageTk.PhotoImage(Image.open(os.path.join(self.current_path, "Images", "Marker_black.png")).resize((45, 58)))
		self.mark_white = ImageTk.PhotoImage(Image.open(os.path.join(self.current_path, "Images", "Marker_white.png")).resize((45, 58)))
		self.mark_red = ImageTk.PhotoImage(Image.open(os.path.join(self.current_path, "Images", "Marker_red.png")).resize((45, 58)))

		
		self.marker1 = self.map_widget_china.set_marker(31.519240, 103.117257, text = '1', icon = self.mark_black, 
			text_color = 'black', command = self.define_province_zoom)
		self.marker2 = self.map_widget_china.set_marker(24.580697, 100.832101, text = '2', icon = self.mark_black,
			text_color = 'black', command = self.define_province_zoom)

		self.map_widget_province = TkinterMapView(master = self.tab('Map of provinces Locations'), width = 800, height = 570)
		self.map_widget_province.grid(row = 0, column = 0, padx = 10, pady = 10)
		self.map_widget_province.set_position(30.499426, 102.853586)
		self.map_widget_province.set_zoom(4)
		self.map_widget_province.set_tile_server('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}')
		self.name2 = customtkinter.CTkLabel(master = self.tab('Map of provinces Locations'), text = '')
		self.name2.grid(row = 0, column = 1)


	def login_user(self):

		self.username_db = ''
		self.login_check = False

		self.wdatos = bytes(self.password_entry.get(), 'utf-8')
		self.h = hashlib.new(algoritmo, self.wdatos)
		self.hash2 = HASH.generaHash(self.h)

		self.miConexion1 = psycopg2.connect(host = 'bctc8tdlqly4cpe3dj0b-postgresql.services.clever-cloud.com', port = 50013, 
		user = 'uylah5thtah6mgce6pcu', dbname = 'bctc8tdlqly4cpe3dj0b', password = 'W4IDeZIuZSOKKxRqzXhjFsiu1WFcYT')
		
		self.miCursor1 = self.miConexion1.cursor()

		self.sql1 = 'select * from users where username = (%s)'
		self.sql1_data = (self.username_entry.get(), )

		self.sql2 = 'insert into users(username, password, points, coins, feathers) values(%s,%s,%s,%s,%s)'
		self.sql2_data = (self.username_entry.get(), self.hash2, 0, 0, 0)

		self.miCursor1.execute(self.sql1, self.sql1_data)
		self.dlt1 = self.miCursor1.fetchall()

		if len(self.dlt1) == 0 and self.username_entry.get() != '' and self.password_entry.get() != '':

			self.miCursor1.execute(self.sql2, self.sql2_data)
			self.miCursor1.execute(self.sql1, self.sql1_data)
			self.dlt2 = self.miCursor1.fetchall()
			#hash256_passw_label.config(text = hash2)
			#username_db = dlt2[0][1]
			self.login_check = True
			#print(username_db)
			playsound('Audios/bambu_click.mp3')
			#playsound('NuevoUsuarioCreado.mp3')
			#playsound('NewUserCreated.mp3')
			time.sleep(2)
			#labelPlayerBCM.config(text = 'Welcome, {}'.format(username_dbc.get()))
			#labelPlayerBCM2.config(text = 'Welcome, {}'.format(username_dbc.get()))
			#labelPlayerBCM3.config(text = 'Welcome, {}'.format(username_dbc.get()))
			#labelPlayerBCM4.config(text = 'Welcome, {}'.format(username_dbc.get()))

		elif len(self.dlt1) > 0 and self.hash2 == self.dlt1[0][2]:

			#hash256_passw_label.config(text = dlt1[0][2])
			self.username_db = self.dlt1[0][1]
			self.login_check = True
			#print(username_db)
			playsound('Audios/bambu_click.mp3')
			#playsound('CorrectoLogin.mp3')
			#playsound('CorrectLogin.mp3')
			time.sleep(2)
			#playsound('UseMachine.mp3')
			#labelPlayerBCM.config(text = 'Welcome to BirdCipher, {}'.format(username_dbc.get()))
			#labelPlayerBCM2.config(text = 'Welcome to BirdCipher, {}'.format(username_dbc.get()))
			#labelPlayerBCM3.config(text = 'Welcome to BirdCipher, {}'.format(username_dbc.get()))
			#labelPlayerBCM4.config(text = 'Welcome to BirdCipher, {}'.format(username_dbc.get()))
			#labelPlayerLoginHashing.config(text = 'Welcome to BirdCipher, {}'.format(username_dbc.get()))

		# elif len(dlt1) > 0 and hash2 != dlt1[0][2]:

		# 	playsound('ContrasenaIncorrectaVI.mp3')

		# elif self.username_entry.get() == '' or self.password_entry.get() == '':

		# 	playsound('DebesIngresarCredenciales.mp3')

		self.miConexion1.commit()
		self.miConexion1.close()


	def define_province_zoom(self, marker):

		#print(marker1.text)
		playsound(audio_provinces[int(marker.text) - 1])
		self.map_widget_province.set_position(marker.position[0], marker.position[1])
		self.map_widget_province.set_zoom(7)
		marker.change_icon(self.mark_red)

		for i, value in enumerate(bird_china_markers[marker.text]):

			self.lat = value[2]
			self.long = value[3]
			self.name_marker = value[0]
			self.map_widget_province.set_marker(self.lat, self.long, text = self.name_marker, icon = self.mark_white, 
				text_color = 'white')


	def name(self, marker2):

		self.name2.configure(text = 'Done')


	def button_welcome(self):

		print('Welcome to BirdCode')
		playsound('Audios/welcome_audio.mp3')
		time.sleep(2)
		playsound('Audios/welcome_audio_zh.mp3')
		time.sleep(2)
		playsound('Audios/welcome_audio_es.mp3')

	def photo_questions_01(self):

		playsound('Audios/welcome_audio.mp3')


class myAnswerEntryFrame(customtkinter.CTkFrame):

	def __init__(self, master):
		super().__init__(master)

		self.province_name = tk.StringVar()

		self.guess_province = customtkinter.CTkEntry(self, textvariable = self.province_name, font = ('Kaiti', 30))
		self.guess_province.grid(row = 0, column = 0, padx = 20)
		self.guess_province.configure(width = 250)

		self.send_name_button = customtkinter.CTkButton(self, text = 'Send', width = 20, font = ('Times New Roman', 20))
		self.send_name_button.grid(row = 0, column = 1, pady = 10, sticky = 'w')




		





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

		self.birder_types = [self.casual_checkbox, self.backyard_checkbox, self.twitcher_chechbox, self.lister_checkbox,
		self.photographic_checkbox, self.scientific_checkbox, self.travel_checkbox, self.sound_checkbox, self.armchair_checkbox,
		self.artistic_checkbox, self.conservation_checkbox, self.social_checkbox]
		
		count = 0

		while count < len(self.birder_types):

			if self.birder_types[count].get() == 1:

				playsound(birder_types_audios[count])
				print(self.birder_types[count]._text)
				time.sleep(5)

			count = count + 1

		
class App(customtkinter.CTk):

	def __init__(self):
		super().__init__()
		self.geometry('1250x650')
		self.title('BirdCode World')
		#self.grid_columnconfigure((0, 2), weight = 1)
		customtkinter.set_appearance_mode('dark')
		customtkinter.set_default_color_theme('green')
		
		self.tab_view = myTabView(master = self, width = 1200, height = 630)
		self.tab_view.grid(row = 0, column = 0, padx = 10, pady = 0)

		
	
app = App()
app.mainloop()