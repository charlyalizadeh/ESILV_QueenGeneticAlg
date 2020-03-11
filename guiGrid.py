import tkinter as tk

class GuiGrid():
    def __init__(self,nbRow,nbColumn,windowSize = '500x500',text=' ',image='', background = 'white', foreground = 'black', borderwith = 2, activebg=None,activefg=None):
        self.window = tk.Tk()
        self.window.geometry(windowSize)
        self.nbRow = nbRow
        self.nbColumn = nbColumn
        activebg = background if activebg==None else activebg
        activefg = foreground if activefg==None else activefg
        self.attributes = {}
        self.attributes['bg'] = background
        self.attributes['fg'] = foreground
        self.attributes['bd'] = borderwith
        self.attributes['text'] = text
        self.attributes['image'] = image 

        #We setup the grid so if we resize it it will resize the frame inside it
        [self.window.grid_rowconfigure(i,weight = 1) for i in range(self.nbRow)]
        [self.window.grid_columnconfigure(i, weight = 1) for i in range(self.nbColumn)]
        self.frame = []
        self.label = []
        for i in range(nbRow*nbColumn):
            self.frame.append(tk.Frame(self.window,bd=1,bg = 'black'))
            self.label.append(tk.Label(self.frame[i],text = ' ',bg = background, fg = foreground, bd = borderwith, activebackground = activebg, activeforeground = activefg))
            self.frame[i].grid(row = int(i/nbColumn), column = i - int(i/nbColumn)*nbColumn, sticky = 'WESN')
            self.label[i].pack(fill='both', expand = True)

    def __getitem__(self,index):
        i,j,typeValue = index
        return self.label[i*self.nbRow+j][typeValue]

    def __setitem__(self,index,value):
        i,j,typeValue = index
        self.label[i*self.nbRow+j][typeValue] = value 

    def update(self):
        self.window.update()

    def mainloop(self):
        self.window.mainloop()


    def clear(self,index = 'ALL'):
        if index=='ALL':
            for i in range(self.nbRow*self.nbColumn):
                self.label[i]['text'] = self.attributes['text']
                self.label[i]['image'] = self.attributes['image']
                self.label[i]['bg'] = self.attributes['bg']
                self.label[i]['fg'] = self.attributes['fg']
        else:
            for i in range(self.nbColumn*self.nbColumn):
                self.label[i][index] = self.attributes[index]


