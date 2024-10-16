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
        self.results=[]

    def solve(self, task, module, selected_diff):
        avg_t=module.avg_time
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
        last_time= end_time-start_time
        score=self.validate(task.result, user_res)
        point_for_task=self.calc_score(score, last_time, module, selected_diff)
        self.results.append([point_for_task, task.difficulty, last_time])

    def calc_score(self, score, t, module, selected_diff):
        factor=selected_diff/self.difficulty
        avg_t=module.avg_time
        if score==1 and t<avg_t:
            score+=(avg_t/t)*factor
            self.score+=score
            self.difficulty+=0.3
        elif score==1:
            score+=(avg_t/t*0.5)*factor
            self.score+=(score)
            self.difficulty+=0.3
        else:
           self.difficulty=max(self.difficulty-0.3,0)
        return score


    def validate(self, original, user_res):
        if user_res==original:
            self.counter+=1
            if self.counter==3:
                self.difficulty+=0.5
                self.counter=0
            print("Good job!\n")
            return 1
        else:
            self.counter=max(0, self.counter-1)
            print("Not exactly...\n")
            return 0
        
    
        