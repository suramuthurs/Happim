#!/usr/bin/python3
import os
import getpass as gp
from tkinter import *
from tkinter import messagebox as mb
import subprocess as sp

#variables
usr = gp.getuser()
cwd = os.getcwd()
sudo_home = os.path.join('/home', usr)
happim_home = os.path.join(sudo_home, '.happim')
appImages = os.path.join(sudo_home, '.Appimages')
uninstall = os.path.join(cwd, 'uninstall.py')
logo = os.path.join(cwd, 'happim_big.png')
new_pyfile = os.path.join(happim_home, 'happim.py')
icon = os.path.join(cwd,'happim_small.png')
new_icon = os.path.join(happim_home,'happim_small.png')

#functions
def find_sudo():
    scr='''#!/bin/bash
if command -v sudo; then
    echo "sudo"
else:
    echo "root"
fi
'''
    r = 'sudo' if 'sudo' in sp.getoutput(scr) else 'root'
    return r

sudo = find_sudo()

def hide():
    pswd.configure(show='*')
    check.configure(command=show, text='show password')

def show():
    pswd.configure(show='')
    check.configure(command=hide, text='hide password')

def validate(*ret):
    got_password = pswd.get()
    ch = os.system(f'echo {got_password} | sudo -S --validate')
    if sudo=='sudo':
        ch = os.system(f'echo {got_password} | sudo -S --validate')
    else:
        cmd = f'su - {usr}'
        val = sp.Popen(cmd, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
        val.stdin.write(f"{got_password}\n".encode())
        val.stdin.flush()
        ch = val.wait()
    if ch !=0: mb.showwarning('Wrong Password', f'Please Enter the correct {sudo} password')
    else: get_prefix()

def get_prefix():
    global prefix
    got_password = pswd.get()
    prefix = f'echo "{got_password}" | sudo -S' if sudo=='sudo' else f'echo "{got_password}" | sudo -c'
    process()
        



def process():
    got_password = pswd.get()
    root.destroy()
    icnnow = os.path.join(cwd, 'happim.png')
    appPath = os.path.join(happim_home, 'happim.sh')
    pyfile = os.path.join(cwd, 'happim.py')
    
    os.system(f'{prefix} mkdir -p {happim_home}')
    os.system(f'{prefix} mkdir -p {appImages}')
    os.system(f'{prefix} chmod 777 {happim_home}')
    os.system(f'{prefix} chmod 777 {appImages}')
   
    os.system(f'{prefix} cp -r {icnnow} {happim_home}')
    os.system(f'{prefix} cp -r {icon} {new_icon}')
    os.system(f'{prefix} cp -r {pyfile} {happim_home}')
    os.system(f'{prefix} chmod 777 {new_pyfile}')
    os.system(f'{prefix} cp -r {logo} {happim_home}')
    with open(new_pyfile, 'r') as sd:
        x = sd.readlines()
        x[19] = f'sudo ="{sudo}"\n'
    with open(new_pyfile, 'w') as sd:
        sd.writelines(x)
    
    shtxt =f'''#!/bin/bash
sudo_user="{usr}"
cd /home/$sudo_user/.happim
python3 happim.py'''
    with open(appPath, 'w') as shFile: shFile.write(shtxt)
    os.system(f'{prefix} chmod +x {appPath}')
    os.system(f'{prefix} cp -r {uninstall} {appImages}')
    happim_datafile = os.path.join(happim_home, 'happim_data.py')
    text = '''
installed_apps = {}
pswd = ""
installed_icons = {}
before_saved_or_not = 0
'''
    with open(happim_datafile, 'w') as df: df.write(text)
    icnPath = os.path.join(happim_home, 'happim.png')
    dtpath = os.path.join('/usr', 'share', 'applications')
    dtFile = os.path.join(happim_home, 'happim.desktop')
    txt = f'''   
[Desktop Entry]
Encoding=UTF-8
Name=Happim
Comment=Appimage Handler
Exec={appPath}
Type=Application
Icon={icnPath}
'''
    with open(dtFile, 'w') as fl: fl.write(txt)
    
    os.system(f'echo {got_password} | sudo -S mv {dtFile} {dtpath}')
    mb.showinfo('Success', 'Happim has been installed')
    print('Happim has been installed')        
        
#Design        
root = Tk()
root.geometry('300x150')
root.title(f'{sudo} Password')
sudo_pswd = Label(root, text=f'Enter your {sudo} password')
sudo_pswd.pack(side='top',padx=10, pady=10)
pswd = Entry(root, width=25, show='*')
pswd.pack(side='top', padx=10, pady=10)
pswd.focus_set()
check = Checkbutton(root, text='show password',command=show)
check.pack()
Button(root,text='Install Happim', width=25, command=validate).pack(side='top')
for x in [root, pswd]:
    x.bind('<Return>', validate)


#root mainloop
root.mainloop()




