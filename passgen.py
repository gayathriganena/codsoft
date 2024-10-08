import tkinter
import random

r=tkinter.Tk()
r.title("Password Generator")
r.geometry("500x300")
r.config(bg="orange")

                                   # function to delay #
def update():                                   
    t1.config(text="")
    complexmsg.config(text="")

                                    # function to generate easy password, combination of uppercase and lowercase letters #
def weakpassword(l):
    p=""
    for i in range(l):
        ran=random.randrange(1,3)
        #print(ran)
        if ran==1:                                     # random uppercase
            p+=chr(random.randrange(65,91))
        else:                                          # random lowercase
            p+=chr(random.randrange(97,123))
    return p                                           # return password

                               # function to generate normal password, combination of uppercase and lowercase letters with number 0-9 #
def moderatepassword(l):
    print("Y")
    p=""
    for i in range(l):
        ran=random.randrange(1,4)
        #print(ran)
        if ran==1:                                     # random uppercase
            p+=chr(random.randrange(65,91))
        elif ran==2:                                   # random lowercase
            p+=chr(random.randrange(97,123))
        else:
            p+=chr(random.randrange(48,58))            # random number from 0-9
    return p                                           # return password

                             # function to generate hard password, combination of letters,numbers and some special characters #
def strongpassword(l):
    p=""
    for i in range(l):
        p+=chr(random.randrange(48,123))               # characters that have ascii code from 48 to 122 
    return p                                           # return password


                                      # main function #
def click():
    if length.get()=="":                          # if user do not pass length
        t1.config(text=f"# Empty bar")            # print this message, chane the text of t1 label
        r.after(2000,update)                      # delay then call update function
        return
        
    if length.get().isdigit():                                           # length should be in digit form

        l=int(length.get())
        if l>=5 and l<=50:                                               # length should be in given range

            if complexity.get() != "None":                               # radio box should be selected
                password=""
                
                if complexity.get()=="weak":                             # if user select easy 
                    password=weakpassword(l)
                    #print(password)
                    
                elif complexity.get()=="moderate":                         # if user select normal
                    password=moderatepassword(l)
                    #print(password)
                    
                else:
                    password=strongpassword(l)                             # if user select hard
                    #print(password)
                    
                rr=tkinter.Tk()                                         # create another window to show password
                rr.geometry("500x100")
                rr.config(bg="black")
                label=tkinter.Label(rr,text=password,bg="black",fg="orange",font=("Cascadia Code ExtraLight",15,"bold","italic"))
                label.pack(pady=20)
                #rr.mainloop()
    
            else:                                                        # if radio box is not selected
                complexmsg.config(text=f"# specify the complexity of password")
                r.after(2000,update)
            
    
        else:                                                            # if length is out of range
            t1.config(text=f"# length should be in between 5 to 50")
            r.after(2000,update)
    else:                                                                # if length is not in digit form
        t1.config(text=f"#length should be in digits only")
        r.after(2000,update)
    
    
heading=tkinter.Label(text="Password\nGenerator",bg="black",fg="orange",font=("Cascadia Code ExtraLight",15,"bold","italic"),padx=10)      # heading
heading.pack(anchor="nw",padx=10,pady=10)

                                    # frame f1 for length stringvar, entry widget #
                                    #=============================================#
f1=tkinter.Frame(r,bg="orange")
length=tkinter.StringVar()                           # tkinter string variable

t=tkinter.Label(f1,text="Password Length",fg="black",bg="orange",font=("Cascadia Code ExtraLight",12,"bold"))          # label
t.grid(row=0,column=0,padx=5)

lengthentry=tkinter.Entry(f1,text=length,bg="black",fg="orange",font=("Cascadia Code ExtraLight",10,"bold"),justify="center")      # entry widget iniliaze length value to its text
lengthentry.grid(row=0,column=1,padx=5)

t1=tkinter.Label(f1,text="",font=("Ariel",7),bg="orange",fg="black")                     # label to print all types of error messages related to length of password
t1.grid(row=1,column=1)

f1.pack(pady=20)


                                  # frame f2 for complexity stringvar, and radio button widget #
                                  #============================================================#
                                  
f2=tkinter.Frame(r,bg="orange")
complexity=tkinter.StringVar()                          # tkinter string variable
complexity.set(None)

radio1=tkinter.Radiobutton(f2,text="Weak",fg="black",bg="orange",font=("Cascadia Code ExtraLight",10,"bold"),variable=complexity,value="weak")     # radio button 1
radio1.grid(row=0,column=1)

radio2=tkinter.Radiobutton(f2,text="Moderate",fg="black",bg="orange",font=("Cascadia Code ExtraLight",10,"bold"),variable=complexity,value="moderate") # radio button 2
radio2.grid(row=0,column=2)

radio3=tkinter.Radiobutton(f2,text="Strong",fg="black",bg="orange",font=("Cascadia Code ExtraLight",10,"bold"),variable=complexity,value="strong")     # radio button 3
radio3.grid(row=0,column=3)

f2.pack()

complexmsg=tkinter.Label(r,text="",font=("Ariel",7),bg="orange",fg="black")            # label to print all types of messages related to radio button
complexmsg.pack()


                                   # f3 frame for buttons #
                                   #======================#
f3=tkinter.Frame(r,bg="orange")

b=tkinter.Button(f3,text="Generate",bg="black",fg="orange",font=("Cascadia Code ExtraLight",9,"bold"),command=click)     # button to generate password 
b.grid(row=0,column=0,padx=5)
b1=tkinter.Button(f3,text="Quit",bg="black",fg="orange",font=("Cascadia Code ExtraLight",9,"bold"),command=quit)         # button to quit the program
b1.grid(row=0,column=1,padx=5)

f3.pack(pady=10)



r.mainloop()
