import tkinter as tk

class GuiGrid():
    def __init__(self,nbRow,nbColumn,windowSize = '500x500',text=' ',image='', background = ['black','white'], foreground = 'black', borderwith = 2):
        self.window = tk.Tk()
        self.window.geometry(windowSize)
        self.nbRow = nbRow
        self.nbColumn = nbColumn
        self.background = background
        self.foreground = foreground
        self.borderwith = borderwith
        self.text = text
        self.image = image 

        #We setup the grid so if we resize it it will resize the frame inside it
        [self.window.grid_rowconfigure(i,weight = 1) for i in range(self.nbRow)]
        [self.window.grid_columnconfigure(i, weight = 1) for i in range(self.nbColumn)]
        self.frame = []
        self.label = []
        for i in range(nbRow*nbColumn):
            self.frame.append(tk.Frame(self.window,bd=1,bg = background[0]))
            self.label.append(tk.Label(self.frame[i],text = ' ',bg = background[1], fg = foreground, bd = borderwith))
            self.frame[i].grid(row = int(i/nbColumn), column = i - int(i/nbColumn)*nbColumn, sticky = 'WESN')
            self.label[i].pack(fill='both', expand = True)

    def __getitem__(self,index):
        i,j,typeValue = index
        if typeValue==None:
            typeValue = 'text'
        return self.label[i*self.nbRow+j][typeValue]

    def __setitem__(self,index,value):
        i,j,typeValue = index
        if isinstance(value,tk.BitmapImage) or isinstance(value,tk.PhotoImage):
            self.label[i*self.nbRow+j]['image'] = value
        else:
            if typeValue==None:
                self.label[i*self.nbRow+j]['text'] = str(value)
            else:
                self.label[i*self.nbRow+j][typeValue] = value
        

    def update(self):
        self.window.update()

    def mainloop(self):
        self.window.mainloop()


    def clear(self,index = None):
        if index=='ALL':
            for i in range(self.nbRow*self.nbColumn):
                self.label[i]['text'] = self.text
                self.label[i]['image'] = self.image
                self.label[i]['bg'] = self.background[1]
                self.label[i]['fg'] = self.foreground
        else:
            for i in range(self.nbColumn*self.nbColumn):
                self.label[i]['text'] = self.text 



