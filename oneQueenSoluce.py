import random
import timeit
import guiGrid

class Indidividu:
    def __init__(self, val = None):
        if val==None:
            self.val = random.sample(range(8),8)
        else:
            self.val = val
        self.nbconflict = self.fitness()

    def __str__(self):
        return str(self.val) 
        #return ' '.join(self.val)
    def __repr__(self):
        return str(self.val)

    def conflict(self,p1,p2):
        if p1[0] == p2[0] or p1[1]==p2[1]:
            return True
        else:
            for i in range(1,8):
                if (p1[0] in [p2[0]-i,p2[0]+i]) and (p1[1] in [p2[1]-i,p2[1]+i]):
                    return True
        return False
    
    def fitness(self):
        self.nbConflict = 0
        for i in range(8):
            for j in range(i+1,8):
                if(self.conflict([self.val[i],i],[self.val[j],j])):
                    self.nbConflict+=1
        return self.nbConflict

    def __getitem__(self,index):
        #assert index in range(8)
        return self.val[index]
    
    def __setitem__(self,index,value):
        #assert index in range(8)
        self.val[index] = value

def create_rand_pop(count):
    return [Indidividu() for i in range(count)]

def evaluate(pop):
    return sorted(pop, key=lambda ind: ind.fitness())

def selection(pop, hcount, lcount):
    result = pop[:hcount-1]
    result.extend(pop[-lcount:])
    return result

def croisement(ind1,ind2):
    newInd1 = Indidividu(ind1[:4] + ind2[4:])
    newInd2 = Indidividu(ind2[:4] + ind1[4:])
    return [newInd1,newInd2]

def mutation(ind):
   ind[random.randint(0,7)] = random.randint(0,7) 

def __eq__(self,other):
    return self.val == other.val

def display(ind, displayValue, gui, error=False):
    gui.clear('ALL')
    for i in range(8):
        if isinstance(displayValue,guiGrid.tk.BitmapImage):
            gui[ind.val[i],i,'image'] = displayValue
        else:
            gui[ind.val[i],i,'text'] = displayValue
    if error:
        for i in range(8):
            deg = 0
            for j in range(i+1,8):
                if(ind.conflict([ind.val[i],i],[ind.val[j],j])):
                    deg+=1
            if deg>5:
                gui[ind.val[i],i,'bg'] = 'red4'
            if deg>3:
                gui[ind.val[i],i,'bg'] = 'red3'
            if deg>=1:
                gui[ind.val[i],i,'bg'] = 'red2'
            if deg==0:
                gui[ind.val[i],i,'bg'] = 'green2'

    gui.update()

            

def algoloopSimple(displayEnd = False,displayEachStep = False, displayWithImage = False, displayError = False):
    start = timeit.default_timer()
    pop = create_rand_pop(25)
    gui = guiGrid.GuiGrid(8,8,'900x900')
    solIsFound = False
    if displayWithImage:
        displayItem = guiGrid.tk.BitmapImage(file='chess_piece_queen.xbm')
    else:
        displayItem = 'DAME'
    nbIteration = 0
    while not solIsFound:
        print('Iteration numero : ', nbIteration)
        nbIteration+=1
        solIsFound = pop[0].fitness()==0
        if not solIsFound:
            if displayEachStep:
                display(pop[0],displayItem,gui,displayError)
            pop = evaluate(pop)
            pop = selection(pop,10,4)
            for i in range(0,len(pop)-1,2):
                pop.extend(croisement(pop[i],pop[i+1]))
            for ind in pop:
                mutation(ind)
            pop.extend(create_rand_pop(5))
    time = timeit.default_timer()-start
    print(pop[0],' Time : ',time)
    if displayEnd:
        display(pop[0],displayItem,gui,displayError)
    gui.mainloop()  

algoloopSimple(True,True,False,True)
        
