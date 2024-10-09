import feladat1
import taskcollection
import user
import random 

class Game():
    def __init__(self, user, tasks):
        self.user=user
        self.tasks=tasks
    
    def choose_task(self):
        
        diff=self.select_difficulty()
        
        number_of_tasks=len(self.tasks.storage[diff])
        index=random.randint(0,number_of_tasks-1)
        return self.tasks.storage[diff][index]
    
    def select_difficulty(self):
        diff=self.user.difficulty
        t=self.user.last_time
        pt=self.user.last_score

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
        print(f"{self.user.name}'s score: {self.user.score}, time taken: {self.user.last_time: .2f}, level {self.user.difficulty}")
        cont=input("press enter to continue")
        while cont=="":
            self.play()
       