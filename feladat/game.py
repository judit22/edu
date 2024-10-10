import feladat1
import taskcollection
import user
import random 
import sys

class Game():
    def __init__(self, user, tasks):
        self.user=user
        self.tasks=tasks
        self.user_history={}
        self.howmany_tasks=0
    

    def generate_task(self):
        num1=random.randint(1,9)
        num2=random.randint(1,9)

        task=feladat1.Task(num1+num2, 1, f"{num1}+{num2}")
        self.tasks.storage[1].append(task)

        task2=feladat1.Task(num1*num2, 2, f"{num1}*{num2}")
        self.tasks.storage[2].append(task2)

        task31=feladat1.Task(num1*num2+num1+num2, 3, f"{num1}*{num2}+{num1+num2}")
        task32=feladat1.Task(num1*num2+num1*num2, 3, f"{num1}*{num2}+{num1*num2}")
        task33=feladat1.Task(num1+num2*num1, 3, f"{num1}+{num2}*{num1}")
        task34=feladat1.Task(num2+num2*num1, 3, f"{num2}+{num2}*{num1}")

        l=[task31,task32,task33,task34]
        for task in l:
            self.tasks.storage[3].append(task)
        
        if num2 >=5 or num1>=6:
            num1=random.randint(1,5)
            num2=random.randint(1,3)
        task4=feladat1.Task(num1**num2, 4, f"{num1}^{num2}")
        self.tasks.storage[4].append(task4)

        task61= feladat1.Task(num1, 6, f"{num2}^x ={num2**num1}")
        task62=feladat1.Task(num1, 6, f"x^{num2}={num1**num2}")
        task63=feladat1.Task(num2, 6, f"x^{num1}={num2**num1}")

        l=[task61,task62,task63]
        for task in l:
            self.tasks.storage[6].append(task)

        num3=random.randint(1,9)
        task81=feladat1.Task(num3+num1, 8, f"{num2}^{num1}*{num2}^{num3} = {num2}^x")
        task82=feladat1.Task(num2+num1, 8, f"{num3}^{num2}*{num3}^{num1} = {num3}^x")
        task83=feladat1.Task(num2+num3, 8, f"{num1}^{num2}*{num1}^{num3} = {num1}^x")
        task84=feladat1.Task(num3*num1, 8, f"({num2}^{num1})^{num3} = {num2}^x")
        task85=feladat1.Task(num2*num1, 8, f"({num3}^{num1})^{num2} = {num3}^x")
        task86=feladat1.Task(num2*num3, 8, f"({num1}^{num2})^{num3} = {num1}^x")
        
        l=[task81,task82,task83, task84, task85, task86]
        for task in l:
            self.tasks.storage[8].append(task)

        if num2!=1:
            task71=feladat1.Task(num2**num1, 7, f'log_{num2}_x = {num1}')
            task72=feladat1.Task(num2, 7, f"log_x_{num2**num2} = {num2}")
            task73=feladat1.Task(num2, 7, f"log_x_{num2**num3} = {num3}")
            task74=feladat1.Task(num2, 7, f"log_x_{num2**num1} = {num1}")
            task75=feladat1.Task(num1, 7, f"log_{num2}_{num2**num1} = x")
            task76=feladat1.Task(num3, 7, f"log_{num2}_{num2**num3} = x")
            task77=feladat1.Task(num2, 7, f"log_{num2}_{num2**num2} = x")
            
            l=[task71,task72,task73,task74, task75, task76, task77]
            for task in l:
                self.tasks.storage[8].append(task)

            
    def choose_task(self):
        
        diff=self.select_difficulty()
        
        number_of_tasks=len(self.tasks.storage[diff])
        index=random.randint(0,number_of_tasks-1)
        return self.tasks.storage[diff][index]
    
    def select_difficulty(self):
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

    def play(self):
        if self.howmany_tasks%10==0:
            self.generate_task()
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
        if self.user.name in self.user_history.keys():
            self.user_history[self.user.name].append(self.user.results)
        else:
            self.user_history[self.user.name]=self.user.results
        self.tasks.save('C:/Users/teves/Downloads/gentasks.json')
        sys.exit(0)