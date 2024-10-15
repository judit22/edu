import feladat1
import taskcollection
import user
import history
import random 
import sys
import module

class Game():
    def __init__(self,f=None):
        self.user=user.User()
        self.user_history=history.History()
        
        mod=int(input("Choose a topic!\n 1: Arithmetics \n 2: Powers, exponential, logarithm \n 3: Units\n"))
        while mod=="":
            mod=int(input("Choose a topic!\n 1: Arithmetics \n 2: Powers, exponential, logarithm \n 3: Units\n"))
        if mod == 1:
            self.module=module.Arithmetics()
        elif mod==2:
            self.module=module.Power()
        else:
            self.module=module.Units()
                
        if f:
            self.user_history=self.user_history.load(f)
        self.howmany_tasks=0

        if self.user.name in self.user_history.history.keys():
            self.user.results.append(self.user_history.history[self.user.name][-2])
            self.user.results.append(self.user_history.history[self.user.name][-1])
            self.user.difficulty=self.user_history.history[self.user.name][-1][1]
            
    def choose_task(self):
        
        #diff=self.select_difficulty()
        diff=round(self.calculate_difficulty())
        number_of_tasks=len(self.module.tasks.storage[diff])
        index=random.randint(0,number_of_tasks-1)
        return self.module.tasks.storage[diff][index]
    
    def calculate_difficulty(self):
        diff=self.user.difficulty
        if len(self.user.results)>1:
            t= (self.user.results[-1][2]+self.user.results[-2][2])/2 #last 2 times avg
            res1=self.user.results[-1][0]
            res2=self.user.results[-2][0]
            if t<2.5 and res1==1 and res2 == 1: #last 2 answers correct and very short avg time
                diff+=1
            elif res1==1 or res2==1: #at least one correct answer but not very short avg time
                diff+=(res1+res2)/2 * 1/t
            else:
                diff=max(diff-1, 1) #neither correct
        else: #0 or 1 results
            diff=1
        if diff not in self.module.tasks.storage.keys():  
            if diff>=len(self.module.tasks.storage.keys()):   #higher than the highest stored diff
                diff=list(self.module.tasks.storage.keys())[-1] #set to the highest
            else:
                diff=max(diff-1,1)                                #no such difficulty but not the highest available
        return diff 

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
        task=self.choose_task()
        self.user.solve(task)
        print(f"{self.user.name}'s score: {self.user.score}, time taken: {self.user.results[-1][2]: .2f}, level {self.user.difficulty}")
        cont=input("press enter to continue")
        while cont=="":
            self.play()
            self.howmany_tasks+=1
        if cont!="":
            self.terminate()
   

    def terminate(self):
        if f"{self.user.name}{self.module.index}" in self.user_history.history.keys():
            existing=self.user_history.history[f"{self.user.name}{self.module.index}"]
            existing.extend(self.user.results)
            self.user_history.history[f"{self.user.name}{self.module.index}"]=existing
        else:
            self.user_history.history[f"{self.user.name}{self.module.index}"]=self.user.results
        self.user_history.save('C:/Users/teves/Downloads/edu/userhistory.json')
        """if self.module.index==1:
            self.module.tasks.save('C:/Users/teves/Downloads/edu/arithmetics.json')
        elif self.module.index==2:
            self.module.tasks.save('C:/Users/teves/Downloads/edu/powertasks.json')
        else:
            self.module.tasks.save('C:/Users/teves/Downloads/edu/unittasks.json')"""
        sys.exit(0)