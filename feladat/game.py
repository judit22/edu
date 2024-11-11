import numpy
import user
import history
import random 
import sys
import module
import calculator
import calc1 

class Game():
    def __init__(self,f=None, tasks=None):
        self.user=user.User()
        self.calculator=calc1.Calculator()
        self.user_history=history.History()
        mod=input("Choose a topic!\n 1: Arithmetics \n 2: Powers, exponential, logarithm \n 3: Units\n")
        while True:
            try:
                mod=int(mod)
                break
            except:
                print("choose from 1, 2, 3!")
                mod=input("Choose a topic!\n 1: Arithmetics \n 2: Powers, exponential, logarithm \n 3: Units\n")
        a=p=u=None
        for task in tasks:
            if "arithmetics" in task:
                a=1
            if "power" in task:
                p=1
            if "unit" in task:
                u=1
        if mod == 1:
            self.module=module.Arithmetics()
            if a:
                self.module.tasks.load(tasks[0]) 
        elif mod==2:
            self.module=module.Power()
            if p:
                self.module.tasks.load(tasks[1]) 
        else:
            self.module=module.Units()
            if u:  
                self.module.tasks.load(tasks[2])  
        if f:
            self.user_history=self.user_history.load(f)

        self.howmany_tasks=0

        if f"{self.user.name}{self.module.index}" in self.user_history.history.keys():
            #self.user.results.append(self.user_history.history[f"{self.user.name}{self.module.index}"][-2])
            self.user.results.append(self.user_history.history[f"{self.user.name}{self.module.index}"][-1])
            self.user.difficulty=self.user_history.history[f"{self.user.name}{self.module.index}"][-1][1]
            
    def choose_task(self):
        
        #diff=self.select_difficulty()
        #diff=self.calculate_difficulty()
        diff=self.calculator.calc_diff(game=self)
        r_diff=round(diff)
        if r_diff in self.module.tasks.storage.keys():
            number_of_tasks=len(self.module.tasks.storage[r_diff])
        else:
            d=len(self.module.tasks.storage)
            number_of_tasks=len(self.module.tasks.storage[d])
            index=random.randint(0,number_of_tasks-1)
            return self.module.tasks.storage[d][index], d
        index=random.randint(0,number_of_tasks-1)
        return self.module.tasks.storage[r_diff][index], diff
    
    

    def calculate_difficulty(self):
        diff=self.user.difficulty
        if len(self.user.results)>0:
            prev_diff=self.user.results[-1][-1]
            prev_time= self.user.results[-1][1]
            prev_score= self.user.results[-1][0]
            if prev_time==0: prev_time+=0.01
            success_rate=(prev_diff/prev_time)*prev_score #0 if wrong answer 
            max_diff_time_rate=0.5
            if success_rate>0:
                diff+=success_rate*max_diff_time_rate   
            else:
                diff-=(prev_diff/prev_time)*max_diff_time_rate
        else: #0 or 1 results
            diff=1
        if round(diff) not in self.module.tasks.storage.keys():  
            if diff>=len(self.module.tasks.storage.keys()):   #higher than the highest stored diff
                diff=list(self.module.tasks.storage.keys())[-1] #set to the highest
            else:
                diff=max(diff-1,1)                                #no such difficulty but not the highest available
        return diff
    

    """def calculate_difficulty(self): #JOL MUKODIK
        diff=self.user.difficulty
        avg_t=self.module.avg_time*diff
        if len(self.user.results)>1:
            t= self.user.results[-1][2] #last time
            res1=self.user.results[-1][0]
            res2=self.user.results[-2][0]
            if t<avg_t and res1>1 and res2>1:
                diff+=1           #last 2 answers correct and very short avg time
            elif avg_t<t and (res1>1 or res2>1): #at least one correct answer but not very short avg time
                diff+= (res1+res2)/2 * (avg_t-t)
            else:  #neither correct
                if t<avg_t:    
                    diff=max(diff-1, 1) 
                else: #avg_t>t
                    max(diff-(avg_t-t)/avg_t, 1)

        else: #0 or 1 results
            diff=1
        if diff not in self.module.tasks.storage.keys():  
            if diff>=len(self.module.tasks.storage.keys()):   #higher than the highest stored diff
                diff=list(self.module.tasks.storage.keys())[-1] #set to the highest
            else:
                diff=max(diff-1,1)                                #no such difficulty but not the highest available
        return diff
    """
    
    """def calculate_difficulty(self):
        
        mu=self.user.difficulty
        sigma=abs(self.user.difficulty-1)/2
        diff=numpy.random.normal(mu, sigma)
        diff=numpy.clip(diff, min(self.module.tasks.storage.keys()), max(self.module.tasks.storage.keys()))
        return diff"""


    """def select_difficulty(self):
        diff=self.user.difficulty
        if len(self.user.results)>1:
            t= (self.user.results[-1][2]+self.user.results[-2][2])/2 #last 2 times avg
        else:t=3

        if t<2.5:
            if diff>list(self.tasks.storage.keys())[-1]:
                diff=list(self.tasks.storage.keys())[-1]
            else:diff+=1
        
        if diff not in self.tasks.storage.keys():
            if diff>=len(self.tasks.storage.keys()):
                diff=list(self.tasks.storage.keys())[-1]
            else:
                diff-=1
        return diff
    """
    
    def play(self):
        self.module.generate_task()
        if self.howmany_tasks%5==0:
            self.module.generate_task()
        task,selected_diff=self.choose_task()
        self.user.solve(task, self.module, selected_diff)
        print(f"{self.user.name}'s score: {self.user.score:.2f}, time taken: {self.user.results[-1][1]: .2f}, level {self.user.difficulty:.2f}, task's difficulty:{task.difficulty},{selected_diff:.2f}")
        cont=input("press enter to continue")
        while cont=="":
            self.play()
            self.howmany_tasks+=1
        if cont!="":
            self.terminate()
   

    """def terminate(self):
        if f"{self.user.name}{self.module.index}" in self.user_history.history.keys():
            existing=self.user_history.history[f"{self.user.name}{self.module.index}"]
            existing.extend(self.user.results)
            self.user_history.history[f"{self.user.name}{self.module.index}"]=existing
        else:
            self.user_history.history[f"{self.user.name}{self.module.index}"]=self.user.results
        self.user_history.save('C:/Users/teves/Downloads/edu/userhistory.json')
    
        sys.exit(0)"""


    def terminate(self):
        if f"{self.user.name}{self.module.index}" in self.user_history.history.keys():
            existing=[self.user.results[-1]]
            self.user_history.history[f"{self.user.name}{self.module.index}"]=existing
        else:
            self.user_history.history[f"{self.user.name}{self.module.index}"]=[self.user.results[-1]]
        self.user_history.save('C:/Users/teves/Downloads/edu/userhistory.json')
        #self.module.tasks.save('C:/Users/teves/Downloads/edu/unittasks.json')
    
        sys.exit(0)