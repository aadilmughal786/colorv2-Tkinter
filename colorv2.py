from tkinter import *
#--------------- main window --------------
root = Tk()
root.title("colorv2")
root.resizable(0,0)

#------------------ variables -------------------------
vsr = IntVar()
vsg = IntVar()
vsb = IntVar()
mainrgb = StringVar()
mainrgb.set("#000000")
bgr = "red"
bgg = "green"
bgb = "blue"
don = StringVar()
don2 = StringVar()

#--------------------- functions ----------------------

def scale_effectR(value):
    labR["bg"] = f"#{int(value):02x}0000"
    labR["text"] = f"{int(value):02x}"
    labR["fg"] = "white"
    mainrgb.set("#"+f"{int(value):02x}" + mainrgb.get()[3:5] + mainrgb.get()[5:7])
    labmain["bg"] = "#"+f"{int(value):02x}" + mainrgb.get()[3:5] + mainrgb.get()[5:7]
    code =  labname["fg"] = "#"+f"{int(value):02x}" + mainrgb.get()[3:5] + mainrgb.get()[5:7]
    don2.set(f"Color Code : {code}       | R = {code[1:3]} | G = {code[3:5]} | B = {code[5:7]}")

def scale_effectG(value):
    labG["bg"] = f"#00{int(value):02x}00"
    labG["text"] = f"{int(value):02x}"
    labG["fg"] = "white"
    mainrgb.set("#"+mainrgb.get()[1:3]+ f"{int(value):02x}" + mainrgb.get()[5:7])
    labmain["bg"] = "#"+mainrgb.get()[1:3]+ f"{int(value):02x}" + mainrgb.get()[5:7]
    code = labname["fg"] = "#"+mainrgb.get()[1:3]+ f"{int(value):02x}" + mainrgb.get()[5:7]
    don2.set(f"Color Code : {code}       | R = {code[1:3]} | G = {code[3:5]} | B = {code[5:7]}")

def scale_effectB(value):
    labB["bg"] = f"#0000{int(value):02x}"
    labB["text"] = f"{int(value):02x}"
    labB["fg"] = "white"
    mainrgb.set("#" + mainrgb.get()[1:3] + mainrgb.get()[3:5]+f"{int(value):02x}")
    labmain["bg"] = "#" + mainrgb.get()[1:3] + mainrgb.get()[3:5]+f"{int(value):02x}"
    code = labname["fg"] = "#" + mainrgb.get()[1:3] + mainrgb.get()[3:5]+f"{int(value):02x}"
    don2.set(f"Color Code : {code}       | R = {code[1:3]} | G = {code[3:5]} | B = {code[5:7]}")



#------------------main label for compound color ---------------------
lab0 = Label(root,width = 10,height = 3)
lab0.grid(row = 0,column = 0,sticky = "ewns")

lab0 = Label(root,width = 10,height = 2)
lab0.grid(row = 0,column = 6,sticky = "ewns")

labmain = Label(root,width = 30+20,height = 5,fg = "white",bg = "red",font = "bold 12",text = "R+G+B",borderwidth=2, relief="solid",textvariable = mainrgb)
labmain.grid(row = 1,column = 1,columnspan = 5,sticky = "ewns")

lab0 = Label(root,height = 2)
lab0.grid(row = 2,column = 0,sticky = "ewns")
#--------------------- three RGB label-------------------
labR = Label(root,width = 10,height = 5,font = "bold 12",text = "R",borderwidth=2, relief="solid",bg = bgr)
labR.grid(row = 3,column = 1,sticky = "ewns")

labG = Label(root,width = 10,height = 5,font = "bold 12",text = "G",borderwidth=2, relief="solid",bg = bgg)
labG.grid(row = 3,column = 3,sticky = "ewns")

labB = Label(root,width = 10,height = 5,font = "bold 12",text = "B",borderwidth=2, relief="solid",bg = bgb)
labB.grid(row = 3,column = 5,sticky = "ewns")

# -------------------label and scalbar from 0 to 255 -----------------------

lab0 = Label(root,width = 10,height = 2)
lab0.grid(row = 4,column = 0,sticky = "ewns")

labRS = Label(root,text = "Red Component : ")
labRS.grid(row = 5,column = 1,sticky = "ewns",columnspan = 2,pady = (15,0))

SR = Scale( root, variable = vsr,from_ = 0, to = 255,orient = HORIZONTAL,command =lambda x:scale_effectR(x) )
SR.grid(row = 5,column = 3,columnspan = 3,sticky = "ewns")

labGS = Label(root,text = "Green Component : ")
labGS.grid(row = 6,column = 1,sticky = "ewns",columnspan = 2,pady = (15,0))

SG = Scale( root, variable = vsg,from_ = 0, to = 255,orient = HORIZONTAL,command =lambda x:scale_effectG(x)) 
SG.grid(row = 6,column = 3,columnspan = 3,sticky = "ewns")

labBS = Label(root,text = "Blue Component : ")
labBS.grid(row = 7,column = 1,sticky = "ewns",columnspan = 2,pady = (15,0))

SB = Scale( root, variable = vsb,from_ = 0, to = 255,orient = HORIZONTAL,command =lambda x:scale_effectB(x)) 
SB.grid(row = 7,column = 3,columnspan = 3,sticky = "ewns")
#------------------------ color discription --------------------------------------
lab0 = Label(root,width = 10,height = 2)
lab0.grid(row = 8,column = 0,sticky = "ewns")

ent0 = Entry(root,textvariable = don2)
ent0.grid(row = 9,column = 1,columnspan = 5,sticky = "ewns")

lab0 = Label(root,width = 10,height = 1)
lab0.grid(row = 10,column = 0,sticky = "ewns")

# name of devloper , text color same as color of main label
labname = Label(root,text = "Devloper : Aadil Mugal , version : v1.0",font = (("Times New Roman"), 15))
labname.grid(row = 11,column = 1,sticky = "ewns",columnspan = 5)

lab0 = Label(root,width = 10,height = 4)
lab0.grid(row = 12,column = 0,sticky = "ewns")

#------------------------ for initial main label background --------------------------------
labmain["bg"] = mainrgb.get()
#------------------- event loop(for event handling  -------------------
root.mainloop()
