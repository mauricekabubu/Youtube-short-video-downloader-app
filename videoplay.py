# import the necessary libraries
# tkinter for graphical user interface
from tkinter import *
from tkinter import messagebox
import yt_dlp
import  os
# Using classes to call all functions
# Creating the app widget
class Youtube:
    def __init__(self,win):
        self.win = win
        win.config(bg= 'light grey')
        win.geometry('600x400')
        win.title('Youtube Downloader App')
        # creating the widget
        label = Label(win,text='Youtube Downloader',bg='light grey',fg='blue',
                      font=('britannic bold',20))
        label.place(x=180,y=20)

        but = Button(win,text='Start',bg='light green',fg='black',font=('arial bold',15),
                     width=20,bd=0,command=self.main_window)
        but.place(x=180,y=140)

        but0 = Button(win, text='Exit', bg='red', fg='black', font=('arial bold', 15),
                     width=20, bd=0,command=exit)
        but0.place(x=180, y=200)

        win.mainloop()

    def main_window(self):
        self.delete_window()
        label0 = Label(win,text='Enter url: ',bg='light grey',fg='blue',
                       font=('britannic bold',15))
        label0.place(x=250,y=20)

        entry = Entry(win,bg='cyan',font=('britannic bold',15),width=30)
        entry.place(x=120,y=60)

        but1 = Button(win, text='Download', bg='blue', fg='black', font=('arial bold', 15),
                      width=20, bd=0, command=lambda :self.app_functionality(url=entry.get(),output_path='C:\\Users\\USER\\PycharmProjects\Youtube Downloader\downloads'))
        but1.place(x=180, y=100)

    def app_functionality(self,url,output_path='downloads'):
        try:
            if not os.path.exists(output_path):
                os.makedirs(output_path)

            ydl_opts = {
                'format': 'best',
                'outtmpl': f'{output_path}/%(title)s.%(ext)s',
                'noplaylist': True  # corrected key name
            }

            messagebox.showinfo("Youtube_downloader",f"Attending to download: {url}")
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            messagebox.showinfo("Youtube_downloader",f"Download complete! Video saved to {output_path}")

        except yt_dlp.utils.DownloadError as de:
            messagebox.showerror("Youtube_downloader",f"Download error! {str(de)}")
            messagebox.showerror("Youtube_downloader","\nListing available formats...")

            try:
                with yt_dlp.YoutubeDL({'listformats': True}) as ydl:
                    ydl.download([url])
            except Exception as e:
                messagebox.showerror("Youtube_downloader",f"Failed to list formats: {str(e)}")

    def delete_window(self):
        for item in win.winfo_children():
            item.destroy()

win = Tk()
object = Youtube(win)

win.mainloop()

