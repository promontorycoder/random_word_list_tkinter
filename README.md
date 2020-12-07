# rwtk.py

Program name: Random Word List Generator
Program Creator: promontorycoder

* Randomly choose six words from a 7,000 english word list for creating unique
    passphrases that are very secure
    
* Print passphrase list to text file if option to print chosen
    
* Creator used to help with python and tkinter learning.

Credits:
- Electronic Frontier Foundation (EFF):

* Word list extrapolated from EFF list available to the public via their
        website: eff.org       

________________________________________________________________________________

# REQUIREMENTS FOR UBUNTU 20.04
________________________________________________________________________________

1. python3:
    sudo apt-get install -y python3
    
2. tkinter: 
    sudo apt-get install -y python3-tk
    
________________________________________________________________________________

# GIT CLONE LINK
________________________________________________________________________________

To git clone into the repository folder, enter the following command into 
Terminal after navigating from within Terminal to the folder you'd like the
program folder to be cloned to.

git clone https://github.com/promontorycoder/random_-word_list_tkinter.git
________________________________________________________________________________

# INSTALLATION INSTRUCTIONS FOR UBUNTU 20.04
________________________________________________________________________________

#### Step 1: Acquire program files
    Copy files via git clone or other method to chosen install folder

#### Step 2: Make program files executable
    Open gnome-terminal and navigate to folder with downloaded program files
    Enter the following commands into gnome-terminal:
        chmod +x rwtk.py
        chmod +x random_word.desktop
        
#### Step 3: Edit files to reflect your directory structure
- Open csv_insp_start.desktop into text editor and change lines 5, 6 and 7 to 
match your file structure
    - Save and exit file
    
#### Step 4: Install tkinter if you do not already have it installed.
    Open gnome-terminal and execute the following commands:
* sudo apt-get install -y python3-tk
        
        
#### Step 5: Copy .desktop file to /usr/share/applications
    Open gnome-terminal and enter the following command:
* sudo cp web_insp.desktop /usr/share/applications
________________________________________________________________________________

![Screenshot](rwtk.png)
