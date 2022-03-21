#------------------------------------------#
# Title:CDInventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# Tessa, Mar 2022, added code to complete assignment
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects=[]

import pickle

class CD():
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        __str__ for formatting inventory entry

    """
    #-----Constructor------#
    
    def __init__(self, ID,name,artist):
    #-----Attributes-------#
        self.__cd_id=ID
        self.__cd_title=name
        self.__cd_artist=artist
    #------Properties------#
    
    @property
    def cd_id(self):
        return self.__cd_id
    
    @cd_id.setter
    def cd_id(self, value_pos):
        
        """Error handling for a non-integer entry in CD ID
        
        arguments: value_pos: the value paassed into the function for CD ID
        
        returns: none"""
        
        if type(value_pos) == int:
            self.__cd_id=value_pos
        else: 
            raise Exception ('The value for ID must be numeric')
        
    @property
    def cd_title(self):
        return self.__cd_title
    
    @cd_title.setter
    def cd_title(self, value_title):
        
        """Error handling for a non-string entry in title
        
        arguments: vaalue_title: the value paassed into the function for CD title
        
        returns: none"""
        
        if type(value_title)==str:
            self.__cd_title=value_title
        else:
            raise Exception ('CD name must be a string')
    
    @property
    def cd_artist(self):
        return self.__cd_artist 
    
    @cd_artist.setter
    def cd_artist(self, value_artist): 
        
        """Error handling for a non-string entry in artist name
        
        arguments: value_artist: the value paassed into the function for CD artist
        
        returns: none"""
        if type(value_artist)==str:
              self.__cd_artist=value_artist
        else:
              raise Exception ('Artist name must be a string')
    
    #------------Methods-------------#
    
    def __str__(self):
        return print ('{}' .format(str(self.__cd_id) +'\t' + self.__cd_title  + '\t\t' + self.__cd_artist))

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    
    @staticmethod
    def load_inventory(file_name):
        """Function to manage data ingestion from file to a list of objects

        Reads the data from file identified by file_name into a 2D table of objects
       

        Args:
            file_name (string): name of file used to read the data from

        Returns:
             table (list of objects): 2D data structure (list of objects) that holds current inventory
            
        """

        while True: #created loop to handle no existing file error and prompt user to begin creating entries
            try:  
                with open(file_name, 'rb') as objFile: #opening the file
                     table=pickle.load(objFile) #unpickling the data and defining as table
                     return table #returning the table
                     break
            except FileNotFoundError: #error handling
                print('\nNo CD Inventory currently exists.  Try selecting \'a\' from the menu to begin building library')
                return []
                break
        

    @staticmethod
    def save_inventory(file_name, lstInventory):
        """Function to save entries in memory to strFileName aka CdInventory.txt
        
            Args: 
                file_name:identifies the file to be written to
                table: parameter for lstTbl identified below
                
            Returns: None"""
        with open(file_name, 'wb') as objFile:#opening file
            pickle.dump(lstInventory, objFile)#pickling the data and writing to file

# -- PRESENTATION (Input/Output) -- #
class IO:
    
    
    """Handling Input / Output
        methods: 
            print_menu--displays menu to user
            menu_choice--getting user input
            show_inventory--displaying current inventory 
            get_entry--collects user input to create new object from CD class"""
    

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """
        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():#no additional error handling necessary
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):#no error handling necessary 
        """Displays current inventory table


        Args:
            table (list of objects): 2D data structure (list of objects) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for CD_object in lstOfCDObjects:
            CD_object.__str__()
        print('======================================')
        
    @staticmethod
    def get_entry(strIDloc, strTitleloc, stArtistloc):
        
        """Collects data from the user for an entr
        
        Args: 
            strIDloc: the id number for the entry
            strTitleloc: the title for the entry
            stArtistloc: the artist name for the entry
    
        Returns:
            lstRowloc: a list that will be converted to a dicRow and added to the lstTbl in another function"""
        while True: #testing for string that can be converted to integer for proper function with while try loop
            try:
                strIDloc = int(input('Enter ID: ').strip()) 
                strTitleloc = input('What is the CD\'s title? ').strip()
                strArtistloc = input('What is the Artist\'s name? ').strip()
                lstRowloc=CD(strIDloc,strTitleloc,strArtistloc)          #[str(strIDloc), strTitleloc, stArtistloc]
                break
            except :
                print('\n Invalid entry for ID number.  Must be integer')
        return lstRowloc

# -- Main Body of Script -- #

#start main loop
#try loop displays the current inventory and handles the possibility of no inventory existing 

lstOfCDObjects=FileIO.load_inventory(strFileName)

while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice() #Error handling addressed within function 
    # Process menu selection
         #process exit first
    if strChoice == 'x':
        break
    #process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled \n')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects=FileIO.load_inventory(strFileName)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
        #Any unexpected entry will just cancel the function and return to the menu (tested with special characters and integrers)
        #No additional error handling necessary 
    # process add a CD
    elif strChoice == 'a': #Error handling addressed in get_entry function
        # 3.3.1 Ask user for new ID, CD Title and Artist
        strID=''
        strTitle=''
        stArtist=''
        lstObject=IO.get_entry(strID, strTitle, stArtist)

        # Add item to the table
        lstOfCDObjects.append(lstObject)
      
        continue  # start loop back at top.
    # process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # process save inventory to file
    elif strChoice == 's': #Tested for user entering an integer rather than y/n and error handled by current code
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileIO.save_inventory(strFileName,lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')

