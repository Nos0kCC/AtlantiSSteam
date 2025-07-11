import tkinter
import customtkinter as ctk
from PIL import Image
import requests
import webbrowser

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("AtlantiSSteam")
app.geometry("800x600")
app.resizable(True, True)

def options():
	def tema():
		if tema_opt.get():
			ctk.set_appearance_mode("light")
			ctk.set_default_color_theme("green")
		else:
			ctk.set_appearance_mode("dark")
			ctk.set_default_color_theme("green")
			
	opt = ctk.CTkToplevel(app)
	opt.title("настройки..")
	opt.geometry("800x600")
	opt.resizable(True, True)
	
	tema_opt = ctk.CTkSwitch(
	master=opt, 
	text="смена темы светлая/тёмная", 
	command=tema)
	tema_opt.place(x=10, y=10)
	
option_button = ctk.CTkButton(
master=app, 
text="настройки", 
width=200, 
height=50, 
corner_radius=20, 
command=options
)
option_button.place(x=10, y=10)

def project_list():
	pro = ctk.CTkToplevel(app)
	pro.title("проекты...")
	pro.geometry("800x600")
	pro.resizable(True, True)
	
	def CRS_installer():
		crs = ctk.CTkToplevel(pro)
		crs.title("CRD car simulator")
		crs.geometry("800x600")
		crs.resizable(True, True)
		
		bunner_crs = ctk.CTkImage(
		light_image=Image.open("CRS_bunner.png"), 
		dark_image=Image.open("CRS_bunner.png"), 
		size=(700, 400))
		
		crs_fon = ctk.CTkLabel(
		master=crs, 
		text=None, 
		image=bunner_crs, 
		)
		crs_fon.place(x=50, y=30)
		
		url_crs = "https://objects.githubusercontent.com/github-production-release-asset-2e65be/1006231607/7ee68019-fa67-49de-9baa-b4eb515a3a06?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=releaseassetproduction%2F20250709%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250709T130644Z&X-Amz-Expires=1800&X-Amz-Signature=97abd99866806432392977db7a32ca16e29621070e53960b7159e4cc15c74d5a&X-Amz-SignedHeaders=host&response-content-disposition=attachment%3B%20filename%3DCRS.0.2.5.-.BETA.zip&response-content-type=application%2Foctet-stream"
		
		def download_crs():
			response = requests.get(url_crs, stream=True)
			
			with open("CRS.0.2.5.-.BETA.zip", "wb") as file:
				for chunk in response.iter_content(1024):
					file.write(chunk)
		
		download_crs = ctk.CTkButton(
		master=crs, 
		text="скачать", 
		corner_radius=20, 
		width=770, 
		height=70, 
		command=download_crs
		)
		download_crs.place(x=10, y=510)
	
	CRS_list = ctk.CTkButton(
	master=pro, 
	text="CRS", 
	width=770, 
	height=70, 
	corner_radius=20, 
	command=CRS_installer
	)
	CRS_list.place(x=10, y=10)
	
	ico_CRS_img = ctk.CTkImage(
	light_image=Image.open("CRS_ico.png"), 
	dark_image=Image.open("CRS_ico.png"), 
	size=(50, 50))
	
	ico_CRS = ctk.CTkLabel(
	master=CRS_list, 
	image=ico_CRS_img, 
	text=None
	)
	ico_CRS.place(x=10, y=10)

project_button = ctk.CTkButton(
master=app, 
text="проекты", 
width=200, 
height=50, 
corner_radius=20, 
command=project_list
)
project_button.place(x=10, y=70)

def seti():
	seti = ctk.CTkToplevel(app)
	seti.title("соц.. сети")
	seti.geometry("800x600")
	seti.resizable(True, True)
	
	telegram = ctk.CTkImage(
	light_image=Image.open("telegram.png"), 
	dark_image=Image.open("telegram.png"), 
	size=(300, 300))
	
	telegram_ico = ctk.CTkLabel(
	master=seti, 
	image=telegram, 
	text=None
	)
	telegram_ico.place(x=250, y=100)
	
	url_tg = "https://t.me/atlantis_studio_chat"
	
	tg_silka = ctk.CTkButton(
	master=seti, 
	text="перейти...", 
	corner_radius=20, 
	width=500, 
	height=70, 
	command=lambda: webbrowser.open(url_tg)
	)
	tg_silka.place(x=140, y=500)

seti_button = ctk.CTkButton(
master=app, 
text="соц.. сети", 
width=200, 
height=50, 
corner_radius=20, 
command=seti
)
seti_button.place(x=10, y=130)

info_okno = ctk.CTkButton(
master=app, 
text=None, 
width=200, 
height=330, 
corner_radius=20
)
info_okno.place(x=10, y=190)

info_text = ctk.CTkLabel(
master=info_okno, 
text="AtlantiSSteam \nBeta 1.0 by Atlantis \n studio... Nos0k", 
font=ctk.CTkFont(size=20, weight="bold"))
info_text.place(x=10, y=10)

text_fon = ctk.CTkLabel(
master=app, 
text="Добро пожааловать! в AtlantiSSteam!")
text_fon.place(x=400, y=10)

hotbar = ctk.CTkButton(
master=app, 
text=None, 
corner_radius=20, 
width=780, 
height=60
)
hotbar.place(x=10, y=530)



if __name__ == "__main__":
	app.mainloop()