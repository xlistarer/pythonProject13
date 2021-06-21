class Koni:
    def init(self, x,y,prev=None):
        self.x=x
        self.y=y
        self.prev=prev
    def graph(self):
        answer=[]
        if self.x-2>=0:
            if self.y-1>=0:
                answer.append(Koni(self.x-2,self.y-1,self))
            if self.y+1<8:
                answer.append(Koni(self.x - 2, self.y + 1, self))

        if self.x + 2< 8:
            if self.y - 1 >= 0:
                answer.append(Koni(self.x + 2, self.y - 1, self))
            if self.y + 1 < 8:
                answer.append(Koni(self.x + 2, self.y + 1, self))
        if self.x-1>=0:
            if self.y-2>=0:
                answer.append(Koni(self.x-1,self.y-2,self))
            if self.y+2<8:
                answer.append(Koni(self.x - 1, self.y + 2, self))

        if self.x + 1< 8:
            if self.y - 2 >= 0:
                answer.append(Koni(self.x + 1, self.y - 2, self))
            if self.y + 2 < 8:
                answer.append(Koni(self.x + 1, self.y + 2, self))
        return answer

class Doska:
     def init(self,startx,starty,finx,finy):
         self.startx=startx
         self.starty = starty
         self.finx = finx
         self.finy = finy
         self.fig=[Koni(self.finx,self.finy)]
     def hod(self):

         while self.findpyt()==None:
             answer=[]
             for i in self.fig:
                 answer+=i.graph()
             self.fig=answer
         return self.findpyt()


     def findpyt(self):
         for i in self.fig:
            if i.x==self.startx and i.y==self.starty:
                return self.pyt(i)
         return None

     def pyt(self,kon):
         pyt=f'{kon.x}, {kon.y} \n'
         n=0
         while kon.prev:
             kon=kon.prev
             n+=1
             pyt+=f'{kon.x}, {kon.y} \n'
         pyt += f' hodov {n}'
         return pyt

doska=Doska(0,0,7,7)
print(doska.hod())
