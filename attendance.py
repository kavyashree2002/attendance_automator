from tkinter import * 
from PIL import ImageTk, Image 
def fun ( name_1 , name_2 ): 
        import pandas as pd 
        import numpy as np 
        attendance = pd . read_csv ( name_1 )   #read the csv file using read_csv()
        unique = attendance [ 'username' ].unique().tolist()    #converting the username column into list without any duplicates  
        data = pd . DataFrame () 
        for name in unique : 
               joined = attendance .loc[ attendance .username == name ][ attendance .useraction == 'joined' ][ "timestamp" ] 
               left = attendance .loc[ attendance .username == name ][ attendance .useraction == 'left' ][ "timestamp" ]     #getting the specified column from the csv file
               time_1 = pd . to_datetime ( joined )
               time_2 = pd . to_datetime ( left )   #converting data in string format to datetime 
               arr_1 = time_1 .to_numpy() 
               arr_2 = time_2 .to_numpy()     #converting a list into numpy array using numpy for easy calculation 
               sub = arr_2 - arr_1 
               newarr = np . array_split ( sub .astype( 'timedelta64[m]' ), 1 )  #breaking of various elements in a single subset and converting time from nanoseconds to minutes 
               sum = np . sum ( newarr )
               print(f"Then {name} stayed in the meet for for the duration of; {sum}")
               let = pd . DataFrame ( data ={ 'Name of the students' : [ name ], 'Time duration' : [ sum ]})
               data = data . append ( let )
               data . to_csv ( name_2 , index = False ) 
               print ("The output datas written to the csv file in the path:",  name_2  ) 
window = Tk ()    #creating an object for tkinder 
window . title ( "attendance automater" ) 
window . geometry ( '800x600' ) 
image1 = Image . open ( "C: \\ Users \\ YOGESH T \\ Downloads \\ my_bot.gif" ) 
test = ImageTk.PhotoImage( image1 ) 
label1 = Label ( image = test )   
label1 .image = test
label1 . place ( x = 0 , y = 0 )
lb1 = Label ( window , text = "Enter the file path need to be scanned:" )    #creating a lable 
lb1 . grid ( column = 0 , row = 0 )    #to give a position of the lable 
lb2 = Label ( window , text = " " ) 
lb2 . grid ( column = 0 , row = 4 ) 
name_1 = Entry ( window , width = 50 )   #to get a input from the user
name_1 . grid ( column = 1 , row = 0 ) 
lb1 = Label ( window , text = "Enter the file path to which output should be stored:" ) 
lb1 . grid ( column = 0 , row = 1 ) 
lb2 = Label ( window , text = " " ) 
lb2 . grid ( column = 0 , row = 4 ) 
name_2 = Entry ( window , width = 50 ) 
name_2 . grid ( column = 1 , row = 1 ) 
def clicked (): 
       res = fun ( name_1 . get (), name_2 . get ())
       lb2 . configure ( text = res ) 
btn = Button ( window , text = 'click to proceed' , command = clicked )  #to create a button
btn . grid ( column = 2 , row = 2 )
window . mainloop ()
