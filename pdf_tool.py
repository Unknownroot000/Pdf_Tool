from tkinter import *
from tkinter.ttk import *
from tkinter import ttk

class Pdf_Tool(object):
    def __init__(self,master):
        frame=Frame(master)
        frame.grid()
        self.options=['Text','Docx','Picture','Pdf']
        
        self.selection_frame=LabelFrame(root,text='Pdf convertion Tool',height=100,width=100)
        self.selection_frame.grid(column=0,row=0,padx=10,pady=10)
        
        self.file_label=Label(self.selection_frame,text='File: ')
        self.file_label.grid(column=0,row=0,padx=5)
        self.file_entry=Entry(self.selection_frame,width=25)
        self.file_entry.grid(column=1,row=0,padx=5)
        self.set_button=Button(self.selection_frame,text='Set')
        self.set_button.grid(column=2,row=0,padx=5)
        
        self.file_label=Label(self.selection_frame,text='Format: ')
        self.file_label.grid(column=0,row=1,padx=5)
        self.from_menu=ttk.Combobox(self.selection_frame,values=self.options)
        self.from_menu.grid(column=1,row=1,padx=5)
        self.from_menu.current(0)
        self.convert_button=Button(self.selection_frame,text='convert')
        self.convert_button.grid(column=2,row=1)
        
        self.result_label=Label(self.selection_frame,text='')
        self.result_label.grid(column=0,row=2,columnspan=3)
        
if __name__ == '__main__':
    root=Tk()
    root.title('PDF converter Tool')
    Pdf_Tool(root)
    root.mainloop()