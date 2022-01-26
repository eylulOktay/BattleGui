from email.mime import image
import tkinter as tk

class Screen_PrepareToBattle (tk.Frame):
    def __init__ (self, master, player1, player2, callback_on_commence_battle):
        super().__init__(master)

        # Save player character object references
        self.player1 = player1
        self.player2 = player2
        
        # Save the method reference to which we return control after the player hits "Next"
        self.callback_on_commence_battle = callback_on_commence_battle
        
        self.create_widgets()
        self.grid()
        
    
    def create_widgets (self):
        
        tk.Label(self, text="You", font=("Times New Roman", 12)).grid(row=0,column=0,sticky=tk.N, padx=(5,5))
        tk.Label(self, text="Computer", font=("Times New Roman", 12)).grid(row=0,column=1,sticky=tk.N, padx=(5,5))
       
        imageBig = tk.PhotoImage(file="images/" + self.player1.large_image)
        
        w= tk.Label (self,
                        image = imageBig, 
                         )
        w.photo = imageBig
        w.grid(row = 1, column = 0, sticky = tk.W)

        tk.Label(self, text=f"{self.player1.hit_points} HP", font=("Times New Roman", 12)).grid(row=2,column=0,sticky=tk.N, padx=(5,5))
        tk.Label(self, text=f"{self.player1.dexterity} Dexterity", font=("Times New Roman", 12)).grid(row=3,column=0,sticky=tk.N, padx=(5,5))
        tk.Label(self, text=f"{self.player1.strength} Strength", font=("Times New Roman", 12)).grid(row=4,column=0,sticky=tk.N, padx=(5,5))

        tk.Label(self, text=f"{self.player2.hit_points} HP", font=("Times New Roman", 12)).grid(row=2,column=1,sticky=tk.N, padx=(5,5))
        tk.Label(self, text=f"{self.player2.dexterity} Dexterity", font=("Times New Roman", 12)).grid(row=3,column=1,sticky=tk.N, padx=(5,5))
        tk.Label(self, text=f"{self.player2.strength} Strength", font=("Times New Roman", 12)).grid(row=4,column=1,sticky=tk.N, padx=(5,5))
        
        imageBig = tk.PhotoImage(file="images/" + self.player2.large_image)
        
        w= tk.Label (self,
                        image = imageBig, 
                         )
        w.photo = imageBig
        w.grid(row = 1, column = 1, sticky = tk.W)

        tk.Button(self, text= "Commence Battle!", font = "Impact 24", fg= "Red", command=self.commence_battle_clicked).grid(row = 5,column=3,columnspan = 2, sticky=tk.N, padx=(5,5))
        #
 
    def commence_battle_clicked(self):
        ''' This method is called when the Battle button is clicked. 
            It passes control back to the callback method. '''         
        self.callback_on_commence_battle()
            
        