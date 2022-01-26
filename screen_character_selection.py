import tkinter as tk

class Screen_CharacterSelection (tk.Frame):
    def __init__ (self, master, roster, callback_on_selected):
        super().__init__(master)
       # Save the CharacterRoster  
        self.roster = roster
        # Save the method reference to which we return control after the player hits "Character Selected"
        self.callback_on_selected = callback_on_selected

        self.grid()
        self.create_widgets()
        
    def create_widgets (self):

        self.character_index = tk.StringVar()
        self.character_index.set(None)


        tk.Label(self, text="Hit Points", font=("Times New Roman", 12)).grid(row=0,column=2,sticky=tk.N, padx=(5,5))
        tk.Label(self, text="Dexterity", font=("Times New Roman", 12)).grid(row=0,column=3,sticky=tk.N, padx=(5,5))
        tk.Label(self, text="Strength", font=("Times New Roman", 12)).grid(row=0,column=4,sticky=tk.N, padx=(5,5))

        for i in range (self.roster.get_number_of_characters()):
            character = self.roster.character_list[i]
            tk.Radiobutton (self, text= character.name, variable = self.character_index, value = i).grid(row = i+1,column = 0, sticky = tk.W) 
       
            imageSmall = tk.PhotoImage(file="images/" + character.small_image)
        
            w= tk.Label (self,
                        image = imageSmall, 
                         )
            w.photo = imageSmall
            w.grid(row = i+1, column = 1, sticky = tk.W)

    
            tk.Label(self, text=character.hit_points, font=("Times New Roman", 12)).grid(row=i+1,column=2,sticky=tk.N, padx=(5,5))
            tk.Label(self, text=character.dexterity, font=("Times New Roman", 12)).grid(row=i+1,column=3,sticky=tk.N, padx=(5,5))
            tk.Label(self, text=character.strength, font=("Times New Roman", 12)).grid(row=i+1,column=4,sticky=tk.N, padx=(5,5))

        tk.Button(self, text= "Character Selected", font = "Impact 24", fg= "Red", command=self.selected_clicked).grid(row=self.roster.get_number_of_characters()+1,column=3,columnspan = 2, sticky=tk.N, padx=(5,5))



        

       

        

        '''
        This method creates all of the widgets character selector page.
        The information about each character should be derived from self.roster, 
        which is a CharacterRoster loaded from battle_characters.txt. 
        The layout should NOT be hard-coded: if you re-order, alter, or remove entries 
        in battle_characters.txt, the layout should automatically reflect those changes. 
        
        ########
        
        
        The radio buttons on this page should all use the variable "self.character_index_index".  
        The values of the radio buttons must be a number equally the position of the character in the list. 
        For example, if the characters listed are Troll, Elf, Human, and Dwarf.  self.character_index would equal 0 
        for the Troll, 1 for the Elf, and so forth.  
        
        The variable self.character_index has been instantiated for your convenience below.
        
        ########

        Here is some sample code for including an image on a page:   (char is a Character object)
            
            imageSmall = tkinter.PhotoImage(file="images/" + char.small_image);
            w= tkinter.Label (self,
                        image = imageSmall, 
                         )
            w.photo = imageSmall # saving the image as a property is required for "saving" the image. It's odd.

            w.grid (ADD PARAMETERS HERE)
        '''
       
        
       
 
    def selected_clicked(self):
        ''' This method is to be called when the "Character Selected!" button is clicked. 
            Notice that it passes self.character_index back to the callback method. '''         
        self.callback_on_selected(self.character_index.get())