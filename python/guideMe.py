#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Dec 02, 2017 12:08:08 PM
import sys
import random
import face_record as fs
import post_php as pphp

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import guideMe_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    guideMe_support.set_Tk_var()
    top = guideMe (root)
    guideMe_support.init(root, top)
    root.mainloop()

w = None
def create_guideMe(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    guideMe_support.set_Tk_var()
    top = guideMe (w)
    guideMe_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_guideMe():
    global w
    w.destroy()
    w = None


class guideMe:
    ID=1
    
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Arial Black} -size 24 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Rockwell Extra Bold} -size 24 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"

        top.geometry("669x444+346+61")
        top.title("guideMe")
        top.configure(background="#403737")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Label1 = Label(top)
        self.Label1.place(relx=0.16, rely=0.29, height=31, width=64)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Name''')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.06, rely=0.05, height=81, width=564)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#161616")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font9)
        self.Label2.configure(foreground="#858585")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''CMS guideMe''')

        self.Label3 = Label(top)
        self.Label3.place(relx=0.16, rely=0.63, height=31, width=64)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Languages''')

        self.Label4 = Label(top)
        self.Label4.place(relx=0.16, rely=0.41, height=31, width=64)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Experience''')

        self.Label5 = Label(top)
        self.Label5.place(relx=0.16, rely=0.52, height=31, width=64)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''City''')
        
        self.NameVal = StringVar()
        self.Entry1 = Entry(top,textvariable= self.NameVal)
        self.Entry1.place(relx=0.39, rely=0.29, relheight=0.07, relwidth=0.38)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")
        
        self.ExpVal = StringVar()
        self.Entry2 = Entry(top,textvariable = self.ExpVal)
        self.Entry2.place(relx=0.39, rely=0.41, relheight=0.07, relwidth=0.38)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")
        
        self.CityVal = StringVar()
        self.Entry3 = Entry(top,textvariable = self.CityVal)
        self.Entry3.place(relx=0.39, rely=0.52, relheight=0.07, relwidth=0.38)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#d9d9d9")
        self.Entry3.configure(highlightcolor="black")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(selectbackground="#c4c4c4")
        self.Entry3.configure(selectforeground="black")
        
        self.LangVal = StringVar()
        self.Entry4 = Entry(top,textvariable = self.LangVal)
        self.Entry4.place(relx=0.39, rely=0.63, relheight=0.07, relwidth=0.38)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(highlightbackground="#d9d9d9")
        self.Entry4.configure(highlightcolor="black")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(selectbackground="#c4c4c4")
        self.Entry4.configure(selectforeground="black")

        self.Button1 = Button(top,command=self.getrec)
        self.Button1.place(relx=0.36, rely=0.79, height=54, width=217)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font10)
        self.Button1.configure(foreground="#313131")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Scan Face''')

        self.Label6 = Label(top)
        self.Label6.place(relx=0.85, rely=0.36, height=41, width=37)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''ID''')
        self.Label6.configure(width=37)

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)


        self.IDVal = StringVar()
        self.Entry5 = Entry(top,textvariable= self.IDVal)
        self.Entry5.place(relx=0.84, rely=0.5, relheight=0.07, relwidth=0.1)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(insertbackground="black")
        READONLY = 'readonly'
        self.Entry5.configure(state=READONLY)
        self.Entry5.configure(width=64)
        
        
    def getrec(self):
        self.ID = random.randint(1,1000)
        self.IDVal.set(str(self.ID))
        print ("You ID id"+str(self.ID))
        print ("hi jd nocode avse ahi")
        fs.record(self.ID)        
        postrec = pphp.PostPHP(self.ID,self.NameVal.get(),int(self.ExpVal.get()),self.CityVal.get(),self.LangVal.get())
        postrec.post()
        print("Finally Thayi gyu")

if __name__ == '__main__':
    vp_start_gui()



