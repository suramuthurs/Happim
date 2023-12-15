from tkinter import *
import os
import subprocess as sp
from tkinter import messagebox as mb
import getpass as gp
# variables
#Do bot remove this line
# Do not remove this line
# Do not remove this line
# Do not remove this line
# Do not remove this line
# Do not remove this line
sudo_home = os.path.join('/home', user)
happim_home = os.path.join(sudo_home, '.happim')
happim_dt = os.path.join('/usr', 'share', 'applications', 'happim.desktop')





#functions
def hide():
    pswd.configure(show='*')
    check.configure(command=show, text='show password')

def show():
    pswd.configure(show='')
    check.configure(command=hide, text='hide password')

def validate(*ret):
    pass_word = pswd.get()
    if sudo=='sudo':
        ch = os.system(f'echo {pass_word} | sudo -S --validate')
    else:
        cmd = f'su - {usr}'
        val = sp.Popen(cmd, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
        val.stdin.write(f"{pass_word}\n".encode())
        val.stdin.flush()
        ch = val.wait()
    if ch !=0: mb.showwarning('Wrong Password', f'Please Enter the correct {sudo} password')
    else: process()
    
def process():
    pass_word = pswd.get()
    root.destroy()
    os.system(f'{prefix} rm -r {happim_home}')
    os.system(f'{prefix} rm -r {happim_dt}')
    
    info = mb.showinfo('Success', "Happim has been uninstalled")
   

root = Tk()
root.geometry('300x150')
root.title('Confirm Password')
sudo_pswd = Label(root, text='Confirm your sudo password')
sudo_pswd.pack(side='top',padx=10, pady=10)
pswd = Entry(root, width=25, show='*')
pswd.pack(side='top', padx=10, pady=10)
pswd.focus_set()
check = Checkbutton(root, text='show password',command=show)
check.pack()
Button(root,text='Uninstall Happim', width=25, command=validate).pack(side='top')
root.bind('<Return>', validate)

#root mainloop
root.mainloop()
