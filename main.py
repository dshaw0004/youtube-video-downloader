from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showerror, showinfo

from pytube import YouTube


def YoutubeDownload(video_url, path, format, res):
    video = YouTube(video_url)

    try:
        if format == "audio":
            file = video.streams.filter(only_audio=True).first()
        else:
            file = video.streams.filter(resolution=res).first()

        file.download(path)

    except:
        showerror("error", "Unable to download video at this time!")

    return (["download complete", f"{format} downloaded!"])


bgColor = "#aaddff"


def processData():
    path = askdirectory(title='Select Folder')
    videoLink = link.get()
    downloadType = fileType.get()
    resolution = res.get()
    returnedData = YoutubeDownload(
        videoLink, fr"{path}", downloadType, resolution)
    showinfo(returnedData[0], returnedData[1])


root = Tk()
root.geometry("350x250")
root.resizable(0, 0)
root.configure(bg=bgColor)
root.iconbitmap("./icon.ico")
root.title("YTdownloader")


Label(root, text="Youtube Downloader",
      bg=bgColor, font="sarif 15 bold").pack(pady=7)


frame = Frame(root, padx=10, pady=20,
              bg=bgColor, height=150
              )
frame.pack(fill="both")
frame.columnconfigure(0, weight=2)
frame.columnconfigure(1, weight=2)


link = StringVar()
Entry(frame, textvariable=link).place(
    in_=frame, anchor="c", relx=.5, rely=0.0, relheight=0.3, relwidth=0.9)

Label(text="filetype", bg=bgColor).place(
    in_=frame, anchor="c", relx=.25, rely=.375)
fileType = StringVar()
fileType.set("video")
OptionMenu(frame, fileType, *["video", "audio"]
           ).place(in_=frame, anchor="c", relx=.25, rely=.65)

Label(text="resolution", bg=bgColor).place(
    in_=frame, anchor="c", relx=.75, rely=.375)

res = StringVar()
resList = ["144p", "240p", "360p", "480p", "720p", "1080p"]
res.set(resList[2])
OptionMenu(frame, res, *resList
           ).place(in_=frame, anchor="c", relx=.75, rely=.65)


Button(root, command=processData, text="download").pack(pady=5)


root.mainloop()
