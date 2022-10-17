try:

    from tkinter import *
    from tkinter import ttk
    from tkinter import filedialog
    from pytube import YouTube

    


except Exception as e:
    print(e)
Folder_Name = ""

#file location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")

    else:
        locationError.config(text="Please Choose Folder!!",fg="red")

#donwload video
def DownloadVideo():

    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text="")

        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()


        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()
            

        else:
            ytdError.config(text="Paste Link again!!",fg="red")




    #download function

    select.download(Folder_Name)
    ytdError.config(text="Download Completed!!")
root=Tk()
root.title('YouTube Downloader')
root.geometry('500x400')
root.columnconfigure(0,weight=1)
ytdLabel = Label(root,text="Paste Your Youtube Link",font=("jost",15))
ytdLabel.grid()


ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=60,textvariable=ytdEntryVar)
ytdEntry.grid()


ytdError = Label(root,text="Error Msg",fg="Red",font=("jost",10))
ytdError.grid()

saveLabel = Label(root,text="Enter File Location",font=("jost",15,"bold"))
saveLabel.grid()
saveEntry = Button(root,width=10,bg="red",fg="white",text="Choose Path",command=openLocation)
saveEntry.grid()

locationError = Label(root,text="Error Path",fg="red",font=("jost",10))
locationError.grid()

ytdQuality = Label(root,text="Select Quality",font=("jost",15))
ytdQuality.grid()

choices = ["720p","144p","Only Audio"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.grid()


downloadbtn = Button(root,text="Donwload",width=10,bg="red",fg="white",command=DownloadVideo)
downloadbtn.grid()

developerlabel = Label(root,text="\n\nDeveloper: Shamim_Hasan_Shihab",font=("jost",10))
developerlabel.grid()
root.mainloop()




#url=str(input('Input the youtube link:'))
#ytd=YouTube(url).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()



