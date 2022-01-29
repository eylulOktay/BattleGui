import tkinter as tk

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
        '''
        This method creates all of the (initial) widgets for the battle page.
        '''
        self.attack_bttn = tk.Button(self, text="Attack", font=("Times New Roman", 12), fg="Cyan",bg="Green",command=self.attack_clicked)
        self.attack_bttn.grid(row=0,column=0,rowspan=3,sticky=tk.NSEW, pady=(5,5), padx=(5,5))
        self.p1AttackLabel = tk.Label(self, text=" ",font=("Times New Roman", 12))
        self.p1AttackLabel.grid(row=0,column=1, sticky=tk.N)
        self.p2AttackLabel = tk.Label(self, text=" ", font=("Times New Roman", 12))
        self.p2AttackLabel.grid(row=1,column=1, sticky=tk.N)
        self.victorLabel = tk.Label(self, text=" ", font=("Times New Roman", 12), fg = "Red")
        self.victorLabel.grid(row=2,column=1, sticky=tk.N)
        tk.Label(self, text = "You", font=("Times New Roman", 12)).grid(row=3,column=0, sticky=tk.N)
        tk.Label(self, text = "Computer", font=("Times New Roman", 12)).grid(row=3,column=1, sticky=tk.N)
        image1 = tk.PhotoImage(file="images/" + self.player1.large_image);
        w = tk.Label (self,image = image1)
        w.photo = image1 # saving the image as a property is required for "saving" the image. It's odd.

        w.grid (row=4,column=0, sticky=tk.N)

        image2 = tk.PhotoImage(file="images/" + self.player2.large_image);
        w = tk.Label (self,image = image2)
        w.photo = image2 # saving the image as a property is required for "saving" the image. It's odd.

        w.grid (row=4,column=1, sticky=tk.N)
        self.health1 = tk.Label(self, text = f"{self.player1.hit_points}/{self.player1_max_hp}", font=("Times New Roman", 12))
        self.health1.grid(row=5,column=0, sticky=tk.N)
        self.health2 = tk.Label(self, text = f"{self.player2.hit_points}/{self.player2_max_hp}", font=("Times New Roman", 12))
        self.health2.grid(row=5,column=1, sticky=tk.N)
        
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
        #
        # TO DO
        #
        res1 = self.player1.attack(self.player2)
        
        self.p1AttackLabel["text"] = res1

        if (self.player2.hit_points>0):
            res2 = self.player2.attack(self.player1)
            self.p2AttackLabel["text"] = res2
        else:
            self.player2.hit_points = 0
            self.p2AttackLabel["text"] = ""
            self.victorLabel["text"] = f"{self.player1.name} has won. Woo."
            
        if (self.player1.hit_points <=0):
            self.player1.hit_points = 0
            self.victorLabel["text"] = f"{self.player2.name} has won. Woo."
        
        if (not self.player1.hit_points or not self.player2.hit_points):
            self.attack_bttn.destroy()
            tk.Button(self, text="Exit", font=("Times New Roman", 12), fg="Cyan",bg="Green",command=self.exit_clicked).grid(row=6,column=1, sticky=tk.E)

        self.health1["text"] = f"{self.player1.hit_points}/{self.player1_max_hp}"
        self.health2["text"] = f"{self.player2.hit_points}/{self.player2_max_hp}"
                                            
    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked. 
            It passes control back to the callback method. '''        
        self.callback_on_exit()
  
            
            
            
            