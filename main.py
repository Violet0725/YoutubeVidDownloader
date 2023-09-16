import tkinter
import customtkinter
from pytube import YouTube

def vDownload():
    try:
        title.configure(text="Insert a youtube link")
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_prog)
        vid = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title)
        vid.download()
        finLabel.configure(text="Downloaded", text_color = "white")
    except:
        finLabel.configure(text="The link is invalid", text_color = "red")

def on_prog(stream, chunk, bytes_remaining):
    size = stream.filesize
    bytes_downloaded = size - bytes_remaining
    cur_perc = bytes_downloaded/size * 100
    per = str(int(cur_perc))
    perc.configure(text=per+'%')
    perc.update()
    bar.set(float(cur_perc/100))

customtkinter.FontManager.load_font("Users\Admin\Downloads\OnlineWebFonts_COM_a446384da0b9eba65b425c99fedfbcdb\Torus Notched SemiBold")
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")



app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Video Downloader")

title = customtkinter.CTkLabel(app, text="Insert a youtube link", font=("Arial", 22, "bold"))
title.pack(pady=10)

url = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width = 350, height = 40, textvariable=url)
link.pack()

finLabel = customtkinter.CTkLabel(app, text="")
finLabel.pack()

perc = customtkinter.CTkLabel(app, text="0%")
perc.pack()

bar = customtkinter.CTkProgressBar(app, width = 400)
bar.set(0)
bar.pack(pady=10)

download = customtkinter.CTkButton(app, text="Download", command=vDownload)
download.pack(pady=20)

app.mainloop()