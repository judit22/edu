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
    

    def generate_task(self):
        num1=random.randint(1,9)
        num2=random.randint(1,9)
        task_type=random.randint(1,4)
        if task_type==1: # +
            task=feladat1.Task(num1+num2, 1, f"{num1}+{num2}=")
            self.tasks.storage[1].append(task)
        elif task_type==2: # *
            task=feladat1.Task(num1*num2, 2, f"{num1}*{num2}=")
            self.tasks.storage[2].append(task)
        elif task_type==3: # 
            task=feladat1.Task(num1*num2+num1+num2, 3, f"{num1}*{num2}+{num1+num2}=")
            task1=feladat1.Task(num1*num2+num1*num2, 1, f"{num1}*{num2}+{num1*num2}=")
            task2=feladat1.Task(num1+num2*num1, 3, f"{num1}+{num2}*{num1}=")
            task3=feladat1.Task(num2+num2*num1, 3, f"{num2}+{num2}*{num1}=")

            self.tasks.storage[3].append(task)
            self.tasks.storage[3].append(task1)
            self.tasks.storage[3].append(task2)
            self.tasks.storage[3].append(task3)
        else:
            if num2 >5 and num1>6:
                num1=random.randint(1,5)
                num2=random.randint(1,3)
            task=feladat1.Task(num1**num2, 4, f"{num1}^{num2}=")

            self.tasks.storage[4].append(task)
            self.tasks.storage[4].append(task1)
            
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
        task=self.choose_task()
        self.user.solve(task)
        print(f"{self.user.name}'s score: {self.user.score}, time taken: {self.user.results[-1][2]: .2f}, level {self.user.difficulty}")
        cont=input("press enter to continue")
        while cont=="":
            self.play()
        if cont!="":
            self.terminate()
   

    def terminate(self):
        if self.user.name in self.user_history.keys():
            self.user_history[self.user.name].append(self.user.results)
        else:
            self.user_history[self.user.name]=self.user.results
        self.tasks.save('C:/Users/teves/Downloads/gentasks.json')
        sys.exit(0)