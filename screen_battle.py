from readline import set_history_length
import tkinter as tk
from unicodedata import name

class Screen_Battle (tk.Frame):
    def __init__ (self, master, player1, player2, callback_on_exit):
        super().__init__(master)
        
        # Save references to the two player objects
        self.player1 = player1
        self.player2 = player2

        # Store the maximum number of hit points which are needed on the screen display.
        self.player1_max_hp = player1.hit_points
        self.player2_max_hp = player2.hit_points

        # Save the method reference to which we return control after this page Exits.
        self.callback_on_exit = callback_on_exit

        self.create_widgets()
        self.grid()
        
    def create_widgets (self):
       

       tk.Button(self, text= "Attack", font = "Impact 24", fg= "Red", command=self.attack_clicked).grid(row=1,column=3,columnspan = 3, sticky=tk.N, padx=(5,5))
       tk.Label(self, text="You", font=("Times New Roman", 12)).grid(row=0,column=0,sticky=tk.N, padx=(5,5))
       tk.Label(self, text="Computer", font=("Times New Roman", 12)).grid(row=0,column=1,sticky=tk.N, padx=(5,5))
       
       imageBig = tk.PhotoImage(file="images/" + self.player1.large_image)
        
       w= tk.Label (self,
                        image = imageBig, 
                         )
       w.photo = imageBig
       w.grid(row = 1, column = 0, sticky = tk.W)

       imageBig = tk.PhotoImage(file="images/" + self.player2.large_image)
        
       w= tk.Label (self,
                        image = imageBig, 
                         )
       w.photo = imageBig
       w.grid(row = 1, column = 1, sticky = tk.W)
       t = self.player1.hit_points 
       w = self.player2.hit_points

       tk.Label(self, text=f"{self.player1.hit_points}/ {t} HP", font=("Times New Roman", 12)).grid(row=2,column=0,sticky=tk.N, padx=(5,5))
       tk.Label(self, text=f"{self.player2.hit_points}/ {w} HP", font=("Times New Roman", 12)).grid(row=2,column=1,sticky=tk.N, padx=(5,5))

       r1 = tk.Label(self, text=f"", font=("Times New Roman", 12)).grid(row=1,rowspan = 2, column=5,sticky=tk.N, padx=(5,5))
       r2 = tk.Label(self, text=f"", font=("Times New Roman", 12)).grid(row=1,rowspan = 2, column=5,sticky=tk.N, padx=(5,5))
       v = tk.Label(self, text=f"", font=("Times New Roman", 12)).grid(row=2,column=5,sticky=tk.N, padx=(5,5))
       e = tk.Button(self, text= "", font = "Impact 24", fg= "Red", command=self.attack_clicked).grid(row=1,column=3,columnspan = 3, sticky=tk.N, padx=(5,5))
        



        
    def attack_clicked(self):
        ''' This method is called when the user presses the "Attack" button.
            
            This method does the following:
            1) Calls the character.attack method for both the player and (if still alive) the computer.
            2) Updates the labels on the top right with the results of the attacks.
            3) Determines if there was a victor, and if so display that info 
            4) If there is a victor, remove the Attack button.  Create an Exit button to replace it.  

            To remove a widget, use the destroy() method. For example:
    
                self.button.destroy()   
        '''    
        result1 = self.player1.attack(self.player2)
        result2 = self.player2.attack(self.player1)

        if self.player1.hitpoints == 0:
            winner = self.player2
        elif self.player2.hitpoints == 0:
            winner = self.player1


        
                                            
    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked. 
            It passes control back to the callback method. '''        
        self.callback_on_exit()
  
            
            
            
            