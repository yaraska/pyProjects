# -*- coding: utf-8 -*-import tracebackimport osimport datetimefrom Tkinter import *import tkMessageBoximport Tkinterimport tkFileDialogfrom ttk import *import systry:                #Draws GUI and defines button actions        class GUI(Frame):                          def __init__(self, parent):                        Frame.__init__(self, parent)                           self.parent = parent                        self.initUI()                def initUI(self):                        self.parent.title("Drive Walker")                        self.style = Style()                        self.style.theme_use("default")                        self.columnconfigure(0, pad=3, weight=1)                        self.columnconfigure(1, pad=3, weight=1)                        self.columnconfigure(2, pad=3, weight=1)                        self.columnconfigure(3, pad=3, weight=1)                        self.rowconfigure(0, pad=3, weight=1)                        self.rowconfigure(1, pad=3, weight=1)                        self.rowconfigure(2, pad=3, weight=1)                        self.rowconfigure(3, pad=3, weight=1)                        global C1var, C2var, C3var                        C1var = IntVar()                        C2var = IntVar()                        C3var = IntVar()                        global entry                        entry = Entry(self)                        entry.grid(row=2, columnspan=2)                        global extension                        extension = Entry(self)                        extension.grid(row=1, columnspan=2, column=2)                                        drive = Label(self, text='Select Drive(s):')                        drive.grid(row=0, column=0, sticky='E')                                        ext = Label(self, text='Enter Search Extension: (eg. .xls)')                        ext.grid(row=1, column=0, columnspan=2, sticky='W')                        out = Button(self, text="Select Output Directory", command = select)                        out.grid(row=2, columnspan=2, column=2)                                        ok = Button(self, text="Begin", command = begin)                        ok.grid(row=3, column=1)                                        halt = Button(self, text="Cancel", command = stop)                        halt.grid(row=3, column=2)                                        C1 = Checkbutton(self, text="X:", variable=C1var, onvalue = 1, offvalue = 0)                        C1.grid(row=0, column=1, sticky='E')                        C2 = Checkbutton(self, text="N:", variable=C2var, onvalue = 1, offvalue = 0)                        C2.grid(row=0, column=2)                        C3 = Checkbutton(self, text="C:", variable=C3var, onvalue = 1, offvalue = 0)                        C3.grid(row=0, column=3, sticky='W')                        self.pack()                                                        def begin():            global search, output            search = extension.get()            output = entry.get()            root.destroy()        def select():            entry.insert(0,(tkFileDialog.askdirectory(title = 'Select Output Log Directory')))                    def stop():                root.destroy()            sys.exit()        def main():            global root              root = Tk()            root.resizable(width=FALSE, height=FALSE)            app = GUI(root)            root.mainloop()        if __name__ == '__main__':           main()          #Defines variables and creates the text log file        global count        count = 0        list = []        now = datetime.datetime.now()        suffix = now.strftime("%Y-%m-%d_%H-%M")        log = open(output+'\listing_%s.txt' %suffix,'w')        #Appends selections to list        if C1var.get() == 1:           list.append('X')        if C2var.get() == 1:           list.append('N')        if C3var.get() == 1:           list.append('C')                   #Defines the walker function        def walker(drive):                path = drive + ':/'                os.chdir(path)                for root, dirnames, filenames in os.walk(path):                    for file in filenames:                        if file.endswith(search):                                global count                                name = os.path.join(root, file)                                log.write (name)                                log.write ('\n')                                print name                                count += 1        for locale in list:                walker(locale)                                        #saves and creates the txt in location specified        print 'Total number of files found: ',count        log.close()        print 'Walk Completed'        print 'Press Enter to exit:'        raw_input()except:        traceback.print_exc()        #Above keeps output window open for debugging purposes if error thrown        print 'Press Enter to exit:'        raw_input()