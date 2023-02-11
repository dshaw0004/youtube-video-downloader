# require modules
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showerror, showinfo

from pytube import YouTube


def download():  # this fuction handle all the logic
    path = askdirectory(title='Select Folder')
    videoLink = link.get()
    downloadType = fileType.get()
    resolution = res.get()
    video = YouTube(videoLink)

    try:
        if downloadType == "audio":
            file = video.streams.filter(only_audio=True).first()
        else:
            file = video.streams.filter(resolution=resolution).first()

        file.download(path)

    except:
        showerror("error", "Unable to download video at this time!")

    showinfo("download complete", f"{downloadType} downloaded!")


bgColor = "#aaddff"  # backgrond color of the app
# Initializing tkinter
root = Tk()
root.geometry("350x250")
root.resizable(0, 0)
root.configure(bg=bgColor)
# root.iconbitmap("./icon.ico") #this does not work properly
root.title("YTdownloader")

# Widget implementation
Label(root, text="Youtube Downloader",
      bg=bgColor, font="sarif 15 bold").pack(pady=7)


frame = Frame(root, padx=10, pady=20,
              bg=bgColor, height=150
              )
frame.pack(fill="both")

link = StringVar()  # link of the video will be saved here
Entry(frame, textvariable=link).place(
    in_=frame, anchor="c", relx=.5,
    rely=0.0, relheight=0.3, relwidth=0.9)


Label(text="filetype", bg=bgColor).place(
    in_=frame, anchor="c", relx=.25, rely=.325)

fileType = StringVar()  # type of download video or audio
fileType.set("video")  # setting the default type to video

OptionMenu(frame, fileType, *["video", "audio"]
           ).place(in_=frame, anchor="c", relx=.25, rely=.575)

Label(text="resolution", bg=bgColor).place(
    in_=frame, anchor="c", relx=.75, rely=.325)

res = StringVar()  # video quality of the video will stored here
resList = ["144p", "240p", "360p", "480p", "720p", "1080p"]
res.set(resList[2])  # setting the deafult video quality to 360p

OptionMenu(frame, res, *resList
           ).place(in_=frame, anchor="c", relx=.75, rely=.575)


Button(root, command=download, text="download").place(
    in_=frame, anchor="c", relx=.5, rely=.9, relheight=0.3)

root.mainloop()
