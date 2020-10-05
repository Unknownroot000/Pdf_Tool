from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import filedialog as fd
from functions import docx_files, pic_files, text_files

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
        self.set_button=Button(self.selection_frame,text='Set',command=self.file_field)
        self.set_button.grid(column=2,row=0,padx=5)
        
        self.file_label=Label(self.selection_frame,text='Format: ')
        self.file_label.grid(column=0,row=1,padx=5)
        self.from_menu=ttk.Combobox(self.selection_frame,values=self.options)
        self.from_menu.grid(column=1,row=1,padx=5)
        self.from_menu.current(0)
        self.convert_button=Button(self.selection_frame,text='convert',command=self.file_extension)
        self.convert_button.grid(column=2,row=1)
        
        self.result_label=Label(self.selection_frame,text='')
        self.result_label.grid(column=0,row=2,columnspan=3)
    
    def file_field(self):
        self.file_path=fd.askopenfilename()
        self.file_entry.delete(0,END)
        self.file_entry.insert(0,str(self.file_path))
        
    def file_extension(self):
        file_ext=self.file_path.split('\\')[-1]
        file_ext=file.split('.')[-1]
        file_formats={'pdf':text_files,"png":pic_files,'txt':text_files,'docx':docx_files}
        
        convert_to=self.from_menu.get()
        convertion=file_formats[convert_to]
        convertion=convertion(self.file_path)
        convertion()
        self.result_label.configure(text='File converted')
        
if __name__ == '__main__':
    root=Tk()
    root.title('PDF converter Tool')
    Pdf_Tool(root)
    root.mainloop()
