import feladat1
import time
class User():
    user_counter=0
    def __init__(self, nickname=None, difficulty=1):
        User.user_counter+=1
        self.index=User.user_counter
        self.score=0
        self.difficulty=difficulty
        if nickname==None:
            nickname=input("name: ")
        self.name=nickname
        self.counter=0 #how many tasks on a level correctly
        self.last_time=0
        self.last_score=0

    def solve(self, task):
        task.__str__()
        start_time=time.time()
        user_res=input()
        end_time=time.time()
        while user_res!="":
            try:
                user_res=float(user_res)
                break
            except:
                user_res=input()
        self.last_score=self.validate(task.result, user_res)
        self.last_time= end_time-start_time

    def validate(self, original, user_res ):
        if user_res==original:
            self.score+=1
            self.counter+=1
            if self.counter==2:
                self.difficulty+=1
                self.counter=0
            return 1
        else:
            self.difficulty-=1 if self.difficulty>1 else 0
            self.counter=max(0, self.counter-1)
            return 0
        
    
        