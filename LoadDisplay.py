# import all of the libraries
import tkinter as tk;
from tkinter import PhotoImage;
import random;
# import all of the scripts needed


# player values
playerHealth = 5000;
global cardHealth;
global cardDefence;
cardBuffs = [0, 0];

# game varibles
turncounter = 0;
currentCards = 50;
global firstTurn;
global turnSelect;

# ***** GUI SETTINGS ***********
window = tk.Tk();
window.geometry("480x320"); #Sets resolution
window.configure(bg="black"); # sets the background to black
window.overrideredirect(True); # makes the window borderless
window.eval('tk::PlaceWindow . center'); # center the app on the screen

#Background image
bg = PhotoImage(file = "background.png"); # gets background image
backgroundImage = tk.Label( window, image = bg); #creates a label for the background image
backgroundImage.place(relx = 0.5,rely= 0.5,anchor='center'); # places the image on the screen

# Player 1 GUI LABEL
playerGUI = tk.Label(window, text=playerHealth,bg='black', fg='red', width='4');
playerGUI.config(font=('Arial bold',100));
playerGUI.place(relx = 0.5,rely= 0.5,anchor='center');

# updates the player health GUI
def updateGUI():
    playerGUI.config(text = playerHealth);
    playerGUI.place(relx = 0.5,rely= 0.5,anchor='center');

# randomly checks to see who goes first
def turnSelection():
   random.seed(10);
   turnSelect = random.choice([0, 1]);
   return turnSelect;
      


input();
