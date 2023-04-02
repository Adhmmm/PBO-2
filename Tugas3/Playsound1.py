
# Memakai Library Pygames dan Tkinter
from tkinter import * 
from tkinter import filedialog
import pygame.mixer as mixer
import os

mixer.init()

def play_song(song_name: StringVar, songs_list: Listbox, status: StringVar):
    song_name.set(songs_list.get(ACTIVE))

    mixer.music.load(songs_list.get(ACTIVE))
    mixer.music.play()

    status.set("Musik Mulai")

def stop_song(status: StringVar):
    mixer.music.stop()
    status.set("Musik Berhenti")


def load(listbox):
    os.chdir(filedialog.askdirectory(title='Buka Folder MP3'))

    tracks = os.listdir()
    
    for track in tracks:
        listbox.insert(END, track)

def pause_song(status: StringVar):
    mixer.music.unpause()
    status.set("Musik RESUMED")


root = Tk()
root.geometry('700x220')
root.title('Memutar MP3')
root.resizable(0, 0)

song_frame = LabelFrame(root, text='Musik', bg= 'LightGrey', width=400, height=80)
song_frame.place(y=80)

button_frame = LabelFrame(root, text='Pengaturan Tombol', bg='Turquoise', width=400, height=120)
button_frame.place(y=80)

listbox_frame = LabelFrame(root, text='Playlist', bg='RoyalBlue')
listbox_frame.place(x=400, y=0, height=200, width=300)

current_song = StringVar(root, value='Belum Memilih')

song_status = StringVar(root, value='Tidak Ada Lagu')

playlist = Listbox(listbox_frame, font=('Helvetica', 11), selectbackground='Green')

scroll_bar = Scrollbar(listbox_frame, orient=VERTICAL)
scroll_bar.pack(side=RIGHT, fill=BOTH)

playlist.config(yscrollcommand=scroll_bar.set)

scroll_bar.config(command=playlist.yview)

playlist.pack(fill=BOTH, padx=5, pady=5)

# Label Musik
Label(song_frame, text='Mendengarkan:', bg='LightBlue', font=('Times', 10, 'bold')).place(x=5, y=20)

song_lbl = Label(song_frame, textvariable=current_song, bg='Goldenrod', font=("Times", 12), width=25)
song_lbl.place(x=150, y=20)

# Tombol Pada Tampilan
pause_btn = Button(button_frame, text='Pause', bg='Cyan', font=("Georgia", 13), width=7,
                   command=lambda: pause_song(song_status))
pause_btn.place(x=150, y=20)

stop_btn = Button(button_frame, text='Stop', bg='Cyan', font=("Georgia", 13), width=7,
                 command=lambda: stop_song(song_status))
stop_btn.place(x=75, y=20)

play_btn = Button(button_frame, text='Play', bg='Cyan', font=("Georgia", 13), width=7,
                  command=lambda: play_song(current_song, playlist, song_status))

resume_btn = Button(button_frame, text='Resume', bg='Cyan', font=("Georgia", 13), width=7,
                    command=lambda: resume_btn(song_status))
resume_btn.place(x=230, y=20)

load_btn = Button(button_frame, text='Buka Folder', bg='Cyan', font=("Georgia", 13), width=35,
                  command=lambda: load(playlist))
load_btn.place(x=10, y=55)

Label(root, textvariable=song_status, bg='SteelBlue', font=('Times', 9), justify=LEFT). pack(side=BOTTOM, fill=X)

root.update()
root.mainloop()