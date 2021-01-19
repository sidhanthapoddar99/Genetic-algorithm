from numpy.random import rand
import numpy as np
from multiprocessing import Pool
import time
import gc




ele_list="ABCDEFGHIJKLMNOPQRSTUVWXYZ  "
target="ALPHA CODE X LOAD TEST MAGIC K"*3
#target="ABCDE"
tlen=len(target)
tlen
min_fitness_val=10
#print(dnac(25))

def gfitness_cal(dna):
    f = 0
    for i in range(tlen):
        if (target[i] == dna[i]):
            f =f + 1
    return f

class gene_func:

    def to_char(self, x):
        return ele_list[x]

    def dnac(self):
        return ''.join(list(map(self.to_char, list(map(int, rand(tlen)*27)))))

class gene(gene_func):

    #fitness calculation function
    def fitness_cal(self):
        f = 0
        for i in range(tlen):
            if (target[i] == self.dna[i]):
                f =f + 1
            
        return f


    
    #manulaly create a DNA 
    def __init__(self,st=None,fit=None):
        if st==None:    
            self.dna = self.dnac()
        else:    
            self.dna = st
        if fit==None:    
            self.fit = self.fitness_cal()
        else:
            self.fit=fit
        
    #DNA mutation
    def mutation(self):
        pass
    
    #function for crossover
    def cross_over(self):
        pass

class Population:
    def __init__(self):
        self.arr=[]
    #minimum required fitness
    min_fit=min_fitness_val
    #max fitnss return
    def cross_connect(self):
        amt=int(len(self.arr)/2)
        i=0
        while i<amt:
            try:
                g=self.arr[i]
                sendc(g.dna)
                self.arr[i]=gene(recc())
                i+=1
            except:
                print("error in sockets") 
    
    def max_fitness(self):
        maxx=0
        for i in self.arr:
            if i.fit>maxx:
                maxx=i.fit
        return maxx
    #create a new population
    def create_population(self,pop_size):
        self.arr=[]
        i=0
        while i<pop_size:
            v=gene()
            if v.fit>=self.min_fit:
                self.arr+=[v]
                i+=1
                if(i%5==0):
                	print(i," -- ",v.dna,"   ---   ",v.fit)
                
    
    def get_gene(self,pop,old_max):
        size=len(pop.arr)
        min_fitness=int(rand(1)[0]*old_max)
        for i in range(1000):
            selected_gene=int(rand(1)[0]*size)
            #check if the dna quality matches the required mark or the max no of attempts have passed
            if pop.arr[selected_gene].fit>=min_fitness or i>200:
#                 if i>200:
#                     print("dna quality not found")
                return pop.arr[selected_gene].dna
            
    
    def cross_over_monte(self,old_pop,old_max,st,ed):
        dna1=self.get_gene(old_pop,old_max)
        dna2=self.get_gene(old_pop,old_max)
        #val=int(rand(1)*(tlen-1))
        val=int(rand(1)[0]*(ed-st)+st)
        return([dna1[:val]+dna2[val:],dna2[:val]+dna1[val:]])
    
    #create a population from crossover             
    def cross_popx(self,varrs):
        #print(pop_size)
        sta=time.time()
        pop_size,old_pop,max_old,ind,tot=varrs
        #print("processor ",ind)
        perp=len(old_pop.arr[0].dna)/tot
        st=ind*perp
        ed=st+perp
        #arr=old_pop.arr
        carr=[]
        i=0
        while i<pop_size:
            vx=self.cross_over_monte(old_pop,max_old,st,ed)
            v=gene(vx[0])
            if v.fit>=self.min_fit:
                carr+=[v]
                i+=1
                #print(v.dna,"   ---   ",v.fit)
            v=gene(vx[1])
            if v.fit>=self.min_fit:
                carr+=[v]
                i+=1
                #print(v.dna,"   ---   ",v.fit)
        if ind==0:        
        	print("\ntotal time=",(time.time()-sta))
        #print("processor ",ind)
        #print(carr)
        #print(carr[0].dna)
        return carr        
                
    def cross_pop(self,pop_size,old_pop,nop=4):
        max_old=old_pop.max_fitness()+1
        jobs=[]
        # for k in range(nop):
        #     p=mp(self.cross_popx(int(pop_size/nop),old_pop,max_old,k))
        #     jobs.append(p)
        #     p.start()
        # for proc in jobs:
        #     proc.join()
        p = Pool(nop)
        
        #workers = [p.apply_async(self.cross_popx, args=(int(pop_size/nop),old_pop,max_old,i,nop)) for i in range(nop)]
		
        #for w in workers:
        #	w.get()
        values=p.map(self.cross_popx, [[int(pop_size/nop),old_pop,max_old,i,nop] for i in range(nop)])
        
        #print(len(values[0]))
        for i in values:
        	self.arr+=i

        for i in range(0,len(self.arr)):
            #print(self.arr[i].dna,"  ---------- ",self.arr[i].fit)
            if self.arr[i].dna==target:
                print(self.arr[i].dna)
                return (1)
            #print(self.arr[i].)
        #print(len(pro_dict))
        return (0)    
    #mote carlo method of crossover rejection samaling

def get_unique(p):
    ar=[]
    for i in p.arr:
        ar+=[i.dna]

    return(len(set(ar))/len(ar))   

    




if __name__ == '__main__':

	print("input population size")
	psize=int(input())
	
	cops=Population()
	cops.create_population(psize)

	while True:
		print("enter the number of Population and no of processor to test with")
		cr=int(input())
		nop=int(input())
		print("\n-----------------start-----------------\n")
		cop=cops
		st=time.time()
		for i in range(cr):
			
			print("----------crossover ",i,"---------")
			copn=Population()
		#    k=copn.cross_pop(psize,cop)
			print(get_unique(cop))
		    #print("before-->",len(cop.arr))
			k=copn.cross_pop(psize,cop,nop)
			print(copn.max_fitness())
		    #print(get_unique(copn))
		    #print("after-->",len(cop.arr))
			print("printing length of ",len(copn.arr))
			if k==1:
				print("found")
				break
			del(cop)    
			cop=copn
			gc.collect()

		#print("\ntotal time=",(time.time()-st))
		print("\n-----------------end-------------------\n\n")   



    