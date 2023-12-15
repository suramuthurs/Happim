# **Idea:**
The name of the project is Happim.
Happim stands for Handle Appimages.

The recent appimage format of linux softwares are light-weighed and excellent in performance,
But it has few drawbacks like:

1. By default, it is not listed among list of linux programs.
2. It doesn't have any specific icons to identify.
3. The appimage files are generally saved along with other files in our working directories. So due to oversight, there are chances of deletion of these files along with the other files.
4. The idea of providing icons and placing among other program doesn't have any gui method and involves several steps. 
5. For doing the above, one needs to have some technical knowledge

If there is a gui software, these app-image programs could have been installed just with one or two clicks. So that the icon to launch the appimage program will be available among other programs. I expanded this idea and created this project.

# **Purpose:**
	
	## 1. With Happim, You can install your favorite app-image applications
	You can install your favorite appimage-applications just in few clicks. Installing involves:
	1. Your favorite app-image applications are listed along with other programs installed so that you can directly launch your favorite app-image application by clicking.
	2. Your favorite icon is allocated to each and every appimage application. So identifying each and every app-image application becomes verymuch easier.
	3. All the appimage files installed is saved to a dedicated directory. And this directory is hidden by default. So deletion of these app-image files are avoided.
	4. Even if you uninstall Happim, your appimage files are safely placed in another directory and you can continue using them with someother methods you prefer.
	
	## 2. You can uninstall one or multiple app-image applications intalled:
	If you are not comfortable in any of your appimage-application, You don't need to keep in your computer unnecessarilly. You can uninstall one or more appimage applications just with few clicks.
	
	##3. Uninstall happim:
	If at all you're not happy with happim, you can uninstall the project completely. But it is ensured that all your app-image programs are stored in $Home/Appimages_installed_by_happim/ even after the uninstallation of Happim. So you can continue using your appimage-programs with your preferred method even after the removal of happim.
	
# Tested Distros:
Ubuntu 22.04, Fedora 39, Opensuse Leap 15.5, centOS.

# prerequisites:
	1. python3
	2. python3-pip
	3. python3-tk
	4. python3-pil
	5. xclip
	6. pyperclip
	
# **Installation:**

## **1. Update and install necessary packages:**

   ### __1. For Debian-based distributions (e.g., Ubuntu, Linux Mint):__
   
      	#### As sudo:
      
        ```
        sudo apt -y update && sudo apt -y install python3 python3-pip python3-tk python3-pil python3-pil.imagetk xclip xsel libfuse2; pip3 install pyperclip
        
        ```

      #### As root:
      
        ```
        apt -y update && apt -y install python3 python3-pip python3-tk python3-pil python3-pil.imagetk xclip xsel libfuse2; pip3 install pyperclip
      
        ```

   ### __2. For Red Hat-based distributions (e.g., Fedora, CentOS):__
   
	**After this procedure, If you get any import-error, Please read the next topic Failure in installing prerequisites**
   
      #### As sudo:
      
        ```
        sudo dnf -y install python3 python3-pip python3-tk python3-pillow python3-pillow-tk xclip xsel; pip3 install pyperclip
      
        ```

      #### As root:
      
        ```
        dnf -y install python3 python3-pip python3-tk python3-pillow python3-pillow-tk xclip xsel; pip3 install pyperclip
      
        ```

   ### __3. For Arch Linux:__
   
   	**After this procedure, If you get any import-error, Please read the next topic Failure in installing prerequisites**

   
      #### As sudo:
      
        ```
        sudo pacman -Sy --noconfirm python python-pip tk python-pillow xclip xsel; pip3 install pyperclip
      
        ```

      #### As root:
      
        ```
        pacman -Sy --noconfirm python python-pip tk python-pillow xclip xsel; pip3 install pyperclip
      
        ```

   ### __4. For openSUSE:__
   
   	**After this procedure, If you get any import-error, Please read the next topic Failure in installing prerequisites**

   
      #### As sudo:
      
        ```
        sudo zypper --non-interactive install python3 python3-pip python3-tk python3-pillow xclip xsel; pip3 install pyperclip
      
        ```

      #### As root:
      
        ```
        zypper --non-interactive install python3 python3-pip python3-tk python3-pillow xclip xsel; pip3 install pyperclip
      
        ```

   ### __5. For YUM-based distributions (e.g., RHEL, CentOS):__
   
   	**After this procedure, If you get any import-error, Please read the next topic Failure in installing prerequisites**

   
      #### As sudo:
      
        ```
        sudo yum -y install python3 python3-pip python3-tk python3-pillow xclip xsel; pip3 install pyperclip
      
        ```

      #### As root:
      
        ```
        yum -y install python3 python3-pip python3-tk python3-pillow xclip xsel; pip3 install pyperclip
      
        ```
        
Kindly modify the above commands as needed for your specific use case if required.

## **2. Troubles in installing prerequisites and Solution**

	Some linux distros give import error due to the python version change and change in the module application. In that case, the following method should be followed.
	
	###**1. Access as root user.**
	If you know your su password, access as root by typing su. If you have only sudo access, you can very well create root access by typing the following in the terminal
	
```
sudo passwd
```
	You will be prompted to type your current (sudo) password. Upon success, You will be prompted for your new password. Type your preferred password. Confirm it once again when you are prompted to confirm. This is your root password. Type su in the terminal. when prompted type your new root password and login.
	
	###**2. Ensure python3 is installed by typing python3 --version
	###**3. Check for import Error
		Type python3 in the terminal and you'll get into interactive mode. type:
```
import tkinter
import PIL
import pyperclip
```

If you get import error, the respective module needs to be installed.

	###**4. Install tkinter, pillow, pyperclip with the following method
	
	Other methods give import error in some distros as i have seen
	
```
python3 -m pip install --upgrade pip;python3 -m pip install --upgrade Pillow; -m pip install --upgrade ; pip3 install python3-tk
```

	###**5. Install xclip
	
```

#If the package manager is yum(like Fedora, rhel):

sudo yum install epel-release.noarch; sudo yum install xclip


#If the package manager is dnf(like centOS):

sudo dnf install epel-release; sudo dnf install xclip


#If the package manager is zypper(like openSUSE):

zypper install xclip


#If the package manager is pacman(like Arch linux and manjora):

pacman -Syu x-clip
```

Now you can install Happim

## **3.Installation**

### __1. Git Clone from terminal__

'''

git clone https://github.com/suramuthurs/Happim.git

'''

### __2. Change directory to the downloaded directory:__

'''

cd Happim

'''

### __3. Type the following to install__

'''

python3 install.py

'''

### __4. When it prompts for sudo or root password, type the password and enter.The Happim application will be installed in seconds.__


Now you'll find the happim logo in the list of installed applications. You can add to your favorite by right-clicking it. 

# **4. Usage:**
## **1.Installing App-image application:**

1. Download the required appimage file from its official website and download your preferred icon from the internet. Icon should be either png or jpg or jpeg formate.

2. Lauch the happim apllication from its logo found in list of programs

3. Type the sudo password or root password (whichever is applicable to your distro) in the relevant field.

4. Type the application's name in the relevant field. (Eg., Firefox or Kdenlive etc.,)

5. Select the icon you have downloaded by clicking the button.

6. Select the appimage file you have downloaded by clicking the button.

7. Click 'Install'.

Your preferred Appimage-application now will be found in the list of applications. You can right-click and add to favorites if you want.

## *2. Uninstall one or multiple app-image application(s):

1. Select the tab 'Uninstall Apps'

2. You will find the list of installed app-i0mage applications. Select one or more application(s) you want to uninstall.

3. Fill the sudo or root password (whichever is applicable to your distro) in the relevant field. Ignore if you had saved before.	

4. Click the button 'Uninstall'

5. You will be prompted whether you are sure to uninstall. Once you click 'Yes', the selected app-image applications will be uninstalled in seconds.

## **3. Uninstall Happim:**

In case, if you are not satisfied with our app, You can very well uninstall it. No worries, All the Appimage-applications you installed will be saved in a separate folder even after uninstalling Happim. The folder in which your appimage-files saved will be $Home / Appimages_installed_by_happim/

1. Select the tab 'uninstall Happim'
2. Click the 'copy' button. This will copy the path in which all your appimage files will be stored after uninstalling happim.
3. Paste the path in a text-editor for reference so that you will be able use these appimage applications in future.
4. Click uninstall.
5. Confirm when it is prompted.
6. Confirm once again with your sudo password or root password (whichever is applicable to your distro) when it is prompted.
7. Happim will be uninstalled in seconds. But you can find your installed apps in $Home/Appimages_installed_by_happim/

# Additional Options:
1. Option to show the password while typing
2. Option to save password to avoid typing password each and everytime

# Caution on saving password:
The option of saving password is given only for the sake of conveniency.
It is saved only in your local machine.
Password saved is NOT ENCRYPTED.
This password can be accessed programmatically if someone else has access to your computer and if he/she can understand the coding.
It is requested to use this option if you are sure that you are the only user of your computer. And also if you are sure that your computer can't be accessed by anybodyelse through SSH / screensharing softwares or any other similar protocols.

# You are Welcome Users and Engineers:
You may be a user or developer! Any, Even if you think that it is very small or silly, Your feedback are welcome. Not necessarilly  that you should provide your contribution only technically. If you have any ideas to be implemented, You are most welcome.  Also I appreciate the technical contributions as well.
