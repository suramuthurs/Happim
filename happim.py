#!/usr/bin/python3

from tkinter import *
import PIL.Image as im
import PIL.ImageTk as imgtk

import getpass as gp
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import subprocess as sp
import os
import sys
import happim_data as hd
import pyperclip as pc

########### Initial Variables
#do not delete this line
#do not delete this line
#do not delete this line
#do not delete this line
#do not delete this line




user = gp.getuser()
cwd = os.getcwd()
sudo_home = os.path.join('/home', user)
happim_home = os.path.join(sudo_home, '.happim')
common_app_img_path = os.path.join(sudo_home, '.Appimages')
pswd = hd.pswd
before_saved_or_not = hd.before_saved_or_not
dct ={'icon_full_path':'',
       'appimage_full_path':'',
       'icon_file_name':'',
       'path_to_icon_file':'',
       'appimage_file_name':'',
       'path_to_appimage_file':''
        }

app_dict = hd.installed_apps
icon_dict = hd.installed_icons

happim_small= os.path.join(happim_home, 'happim_small.png')

####### functions



def start():
    if before_saved_or_not:
        password_field.insert(0, pswd)
        save_btn.select()
    else: save_btn.deselect()

def get_prefix():
    global prefix
    prefix = f'echo "{got_password}" | sudo -S' if sudo=='sudo' else f'echo "{got_password}" | sudo -c'

def hide():
    password_field.configure(show='*')
    check.configure(command=show, text='show password')

def show():
    password_field.configure(show='')
    check.configure(command=hide, text='hide password')

def hide_show_hidden_files():
    try:
        try: root.tk.call('tk_getOpenFile', 'dummy')
        except TclError: pass
        root.tk.call('set', '::tk::dialog::file::showHiddenBtn', '1')
        root.tk.call('set', '::tk::dialog::file::showHiddenVar', '0')
    except: pass
   

def refresh(): ex = sys.executable; os.execl(ex, ex, * sys.argv)

def getIcon():
    hide_show_hidden_files()
    fileType = [('image', '*.png'),('image', '*.jpg'),('image', '*.jpeg')]
    icon_full_path = fd.askopenfilename(initialdir=sudo_home, filetypes=fileType)
    iconlbl.config(text=icon_full_path, fg='green', font='Helvetica 12')
    rev = icon_full_path[::-1]
    idx = rev.find('/')
    onlyIcon = rev[:idx]
    icon_file_name = onlyIcon[::-1]
    path_to_icon = rev[idx+1:]
    path_to_icon_file = path_to_icon[::-1]
    dct['icon_full_path'] = icon_full_path
    dct['icon_file_name'] = icon_file_name
    dct['path_to_icon_file'] = path_to_icon_file
    
def getProg():
    hide_show_hidden_files()
    fileType = [('appImage file:', '*.AppImage')]
    appimage_full_path = fd.askopenfilename(initialdir=sudo_home, filetypes=fileType)
    progLbl.config(text=appimage_full_path, fg='green', font='Helvetica 12')
    rev = appimage_full_path[::-1]
    idx = rev.find('/')
    onlyProg = rev[:idx]
    appimage_file_name = onlyProg[::-1]
    path_to_appimage = rev[idx+1:]
    path_to_appimage_file = path_to_appimage[::-1]
    dct['appimage_full_path'] = appimage_full_path
    dct['appimage_file_name'] = appimage_file_name
    dct['path_to_appimage_file'] = path_to_appimage_file

def process(*evnts):
    save_pswd()
    get_prefix()
    path_to_icon_file = dct['path_to_icon_file']
    path_to_appimage_file = dct['path_to_appimage_file']
    icon_file_name = dct['icon_file_name']
    appimage_file_name = dct['appimage_file_name']
    destination_path = os.path.join(common_app_img_path, got_name)
    permanent_icon_path = os.path.join(destination_path, icon_file_name)
    permenant_app_path = os.path.join(destination_path, appimage_file_name)
    desktop_file_path = os.path.join('/usr', 'share', 'applications')
    desktop_file = got_name + '.desktop'
    desktop_file_src = os.path.join(happim_home, desktop_file)
    app_dict[got_name] = permenant_app_path
    icon_dict[got_name] = permanent_icon_path
    os.system( f'{prefix} mkdir -p {destination_path}')
    os.system(f'{prefix} chmod 777 {destination_path}')
    os.system(f'{prefix} cp {appimage_full_path} {destination_path}')
    os.system(f'{prefix} cp {icon_full_path} {destination_path}')
    os.system(f'{prefix} chmod +x {permenant_app_path}')
    txt = f'''   
[Desktop Entry]
Encoding=UTF-8
Name={got_name}
Exec={permenant_app_path}
Type=Application
Icon={permanent_icon_path}
MimeType=application/x-iso9660-appimage;
'''
    with open(desktop_file_src, 'w') as dt: dt.write(txt)
    os.system(f'{prefix} mv {desktop_file_src} {desktop_file_path}')
    with open('happim_data.py', 'r') as data:
        x = data.readlines()
        x[1] = f'installed_apps = {app_dict}\n'
        x[3] = f'installed_icons = {icon_dict}\n'
    with open('happim_data.py', 'w') as data: data.writelines(x)
    msg = f'''{got_name} has been installed successfully.

Click grid icon in dash to find {got_name} with other programs.
'''
    mb.showinfo('Success', msg)
    refresh()
        
def enter_pswd():
    if got_password=='':mb.showinfo(f'Enter {sudo} Password', f'Enter your {sudo} Password')
    else: return 1

def field_empty_msg():
    required_fields = (got_name, appimage_full_path, icon_full_path)
    blnk_msg = '''Fill the Required Field.
Ensure All the input fields are filled up.
Also ensure both Icon and appimage are selected.'''
    if any(x=='' for x in required_fields):
        mb.showinfo('Fill all the fields', blnk_msg)
    else: process()

def save_pswd():
    options = (f'pswd = "{got_password}"\n', 'before_saved_or_not = 1',
                'pswd = "{}"\n', 'before_saved_or_not = 0')
    with open('happim_data.py', 'r') as fl:
        x = fl.readlines()
        if save_var.get()==1:
            x[2] = options[0]; x[4] = options[1]
        else: x[2] = options[2]; x[4] = options[3]
    with open('happim_data.py', 'w') as fl: fl.writelines(x)
    
def check_password():
    if enter_pswd():
        if sudo=='sudo':
            ch = os.system(f'echo {got_password} | sudo -S --validate')
        else:
            cmd = f'su - {usr}'
            val = sp.Popen(cmd, shell=True, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
            val.stdin.write(f"{got_password}\n".encode())
            val.stdin.flush()
            ch = val.wait()
        if ch !=0: mb.showwarning('Wrong Password', f'Please Enter the correct {sudo} password')
        else: field_empty_msg()

def initialize(*ee):
    #other variables
    global got_name
    global got_password
    global icon_full_path
    global appimage_full_path
    got_name = name.get().replace(' ', '_')
    got_password = password_field.get()
    icon_full_path = dct['icon_full_path']
    appimage_full_path = dct['appimage_full_path']
    check_password()

def sure_uninstall(*evnt):
    global got_password
    got_password = password_field.get()
    get_prefix()
    save_pswd()
    old_path = os.path.join(common_app_img_path, '*')
    new_path = os.path.join(sudo_home, 'Appimages_installed_by_happim')
    
    if enter_pswd():
        popup = mb.askyesno('Warning', 'Are you sure to uninstall Happim?')
        if popup:
            os.system(f'{prefix} mkdir -p {new_path}')
            os.system(f'{prefix} mv {old_path} {new_path}')
            uninstall = os.path.join(new_path, 'uninstall.py')
            os.system(f'{prefix} rm -r {common_app_img_path}')
            os.system(f'{prefix} chmod 777 {uninstall}')
            with open(uninstall, 'r') as add:
                x = add.readlines()
                x[8] = f'user = "{user}"\n'
                x[9] = f"prefix = '{prefix}'\n"
                x[10] = f'sudo = "{sudo}"\n'
            with open(uninstall, 'w') as add:
                add.writelines(x)
            os.system(f'python3 {uninstall}')
            root.destroy()
            

def select_item(*args):
    global selected_apps
    dict =[]
    for x in listbox.curselection():
        y = listbox.get(x)
        dict.append(y)
    selected_apps = list(set(dict))
    
    
def bye():
    get_prefix()
    save_pswd()
    for x in selected_apps:
        dsktp_file = x + '.desktop'
        dsktp_file_path = os.path.join('/usr', 'share', 'applications', dsktp_file)
        remove_app = os.path.join(common_app_img_path, x)
        os.system(f'{prefix} rm -r {remove_app}')
        os.system(f'{prefix} rm -r {dsktp_file_path}')
        app_dict.pop(x)
        icon_dict.pop(x)
    with open('happim_data.py', 'r') as open_data:
        x = open_data.readlines()
        x[1] = f'installed_apps = {app_dict}\n'
        x[3] = f'installed_icons = {icon_dict}\n'
    with open('happim_data.py', 'w') as open_data:
        open_data.writelines(x)
    
    if len(selected_apps)==1:
        removed = mb.showinfo('Success', f'The Appimage {selected_apps[0]} has been removed Successfully')
    else:
        removed = mb.showinfo('Success', f'Your requested {len(selected_apps)} apps have been removed')
    refresh()


def warn(*e):
    select_item()
    global got_password
    got_password = password_field.get()
    if enter_pswd():
        if len(selected_apps)==0:
            mb.showinfo('Select Apps', 'Select the Apps you want to remove')
        else:
            if len(selected_apps) == 1:
                warning = f'Are you sure to remove {selected_apps[0]}?'
            else:
                warning = f'Are you sure to remove these {len(selected_apps)} apps?'
            msgbx = mb.askyesno('Warning',warning)
            if msgbx: bye()

def change_focus(wdg): wdg.focus_set()
    
            

def copy_path(): pc.copy(f"/home/{user}/Appimages_installed_by_happim/")

   

########## Design
root = Tk()
root.geometry('570x690')
root.title('Happim - Handle Appimages')

imgPath= os.path.join(happim_home, 'happim_big.png')
happim_small = imgtk.PhotoImage(file='happim_small.png')
root.iconphoto(False, happim_small)




root.after_idle(start)
 

img = im.open(imgPath)
resized = img.resize((118,182))
ph = imgtk.PhotoImage(resized)
lblImg = Label(root, image=ph)
lblImg.pack(side='top')

mglWdg = Frame(root, height=40)
mglWdg.pack(side='top', padx=10, pady=10)

pswdWdgt =Frame(mglWdg)
pswdWdgt.pack(side='left',padx=0, pady=0)
password_label = Label(pswdWdgt, text=f'Your {sudo} Password', fg='black')
password_label.pack(side='top', padx=15, pady=0)
password_field = Entry(pswdWdgt, width=25, show= '*')
password_field.pack(side='top',padx=15, pady=5)
password_field.focus_set()

ch_frame = Frame(mglWdg)
ch_frame.pack(side='right')

check = Checkbutton(ch_frame, text='show password',fg='black', command=show)
check.pack(side='top', padx=15, pady=0)
save_var = IntVar()

save_btn = Checkbutton(ch_frame, variable=save_var, fg='black', text='Save Password')
save_btn.pack(side='top', padx=15, pady=5)

caution_frame = Frame(root)
caution_frame.pack(side='top', pady=13)


caution_title = Label(caution_frame, text="Use 'Save Password' option with Caution", font='Helvetica 12 underline', fg='brown4', bg='grey99')
caution_title.pack(pady=0, side='top')

caution_text = '''Your Password is saved in your local machine and it is NOT encrypted.
Avoid to save password if you think if there are some risks involved. '''

caution_text = Label(caution_frame,text=caution_text,width=450)
caution_text.pack(side='top', pady=0)

btmFrame = ttk.Notebook(root, width=560)
btmFrame.pack(side='top',padx=15,pady=10)

tab1 = ttk.Frame(btmFrame) 
tab3 = ttk.Frame(btmFrame)
tab4 = ttk.Frame(btmFrame)

btmFrame.add(tab1, text='Install from Computer')
btmFrame.add(tab3, text='Uninstall Apps')
btmFrame.add(tab4, text='Uninstall Happim')


nameDes = Label(tab1, width=25,text='Application Name(Eg: Firefox)',bg='grey75', fg='black')
nameDes.pack(side='top',pady=15)
name = Entry(tab1, width=25)
name.pack(side='top',padx=10, pady=2)



iconlbl = Label(tab1, bg='grey75')
iconlbl.pack(side='top',pady=3)
icnbtn = Button(tab1, width=25, text='select Icon' , command=getIcon)
icnbtn.pack(side='top', padx=10, pady=0)

progLbl = Label(tab1, bg='grey75')
progLbl.pack(side='top',pady=3)
prgbtn = Button(tab1, width=25, text='select AppImage File', command=getProg)
prgbtn.pack(side='top', padx=10, pady= 0)


create = Button(tab1, width=25, text='Install', command=initialize)
create.pack(side='top', padx=10, pady=25)


#### tab3 design
listbox = Listbox(tab3, selectmode = "multiple")
listbox.pack(side='top', expand = True, fill = 'both')
installed_apps = [x for x in app_dict.keys()]
for x in installed_apps: listbox.insert(END, x)


remove_button = Button(tab3, text='Uninstall', command=warn)
remove_button.pack(side='bottom', padx=10, pady=5)



#### tab4 design
uninstall_title = Label(tab4, text='Uninstall Happim', font='Helvetica 12 underline', bg='grey75', fg='black')
uninstall_title.pack(side='top', pady=10)
info_txt = '''All your Appimage apps are safe even if you uninstall Happim.
Before uninstalling. Kindly copy the following path.
Your Appimage applications are available in the following folder'''
text_appimage_path = f"/home/{user}/Appimages_installed_by_happim/"

Label(tab4, text=info_txt, font='Helvetica 12', bg='grey75', fg='black').pack(side='top', pady=15)

file_path_frame = Frame(tab4, bg='grey75')
file_path_frame.pack(side='top',pady=15)
copy_text_frame = Frame(file_path_frame, bg='grey75')
copy_text_frame.pack(side='left', padx=5)
copy_text = Label(copy_text_frame, text=text_appimage_path, font='Helvetica 12 underline', fg='blue', bg='grey75')
copy_text.pack(side='top')
copy_button = Button(file_path_frame, text='Copy', command=copy_path)
copy_button.pack(side='right',padx=5)

uninstall_button = Button(tab4, text='Uninstall Happim', fg='black', command=sure_uninstall)
uninstall_button.pack(side='top',padx=10, pady=15)

###common configurations
for x in [prgbtn, icnbtn, create, uninstall_button, remove_button, copy_button]:
    x.configure(bg='grey40', fg='white')



stl = ttk.Style()
 
stl.theme_create('happim', settings={
    ".": {
        "configure": {
            "background": 'grey75',
            "font": '#002451'
        }
    },
    "TNotebook": {
        "configure": {
            "background":'grey75',
            "tabmargins": [0, 0, 0, 0], 
        }
    },
    "TNotebook.Tab": {
        "configure": {
            "background": 'grey75', 
            "padding": [18, 7, 18, 7], 
            "font":"#002451",
            
        },
        "map": {
            "background": [("selected", 'grey75')],
            "expand": [("selected", [0, 0, 0, 0])] 
        }
    }
})
 
stl.theme_use('happim')





for x in [root,
          lblImg,
          password_label,
          check,
          save_btn,
          mglWdg,
          pswdWdgt,
          ch_frame,
          caution_text,
          caution_frame]:
    x.configure(bg='grey99')


#bind Logics
tab_idx = btmFrame.index(btmFrame.select())
if tab_idx==0:
    password_field.bind('<Return>', lambda y: change_focus(tab1))
    for x in [name, icnbtn, prgbtn, tab1, create]:
        x.bind('<Return>', initialize)
elif tab_idx==1:
    password_field.bind('<Return>', lambda y: change_focus(tab3))
    for x in [root, tab3]:
        x.bind('<Return>', warn)
else:
    password_field.bind('<Return>', lambda y: change_focus(tab4))
    tab4.bind('<Return>', sure_uninstall)

listbox.bind('<ButtonRelease>', select_item)
listbox.bind('<FocusIn>', select_item)
tab4.bind('<Return>', sure_uninstall)
    
#root mainloop 
root.mainloop()








