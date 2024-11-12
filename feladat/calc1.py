import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier  
from sklearn.preprocessing import StandardScaler

import numpy as np
import user
class Calculator():
    def __init__(self):
        training_data_x,training_data_y=pd.read_csv('C:/Users/teves/Downloads/generated_data_x_new1.csv'),pd.read_csv('C:/Users/teves/Downloads/generated_data_y_new1.csv')    
        self.time_min, self.time_max=np.min(training_data_x['time']), np.max(training_data_x['time'])
        self.userlvl_min, self.userlvl_max=np.min(training_data_x['userlvl']), np.max(training_data_x['userlvl'])
        self.difficulty_min, self.difficulty_max=np.min(training_data_x['task difficulty']), np.max(training_data_x['task difficulty'])
        self.counter_min, self.counter_max=np.min(training_data_x['howmany_in_a_row']),np.max(training_data_x['howmany_in_a_row'])
        
        training_data_x=training_data_x.to_numpy()
        training_data_y=training_data_y.to_numpy()
        #self.classifier=LogisticRegression(random_state=0, solver='lbfgs', max_iter=1000)
        self.classifier = KNeighborsClassifier(n_neighbors=3)
        self.classifier.fit(training_data_x, training_data_y)

    def transform(self,X):
        if X[5]>7:X[5]=10
        X[0]=1 if X[0]>=1 else 0
        X[1]=(X[1]-self.time_min)/(self.time_max-self.time_min)
        X[3]=(X[3]-self.userlvl_min)/(self.userlvl_max-self.userlvl_min)
        X[4]=(X[4]-self.difficulty_min)/(self.difficulty_max-self.difficulty_min)
        X[5]=(X[5]-self.counter_min)/(self.counter_max-self.counter_min)
        del(X[2])
        return X
    
    def calc_score(User, score, t, module, selected_diff):
        user_diff=User.difficulty
        factor=round(selected_diff)/round(user_diff)
        avg_t=module.avg_time

        if score==1 and t<avg_t:
            score+=(avg_t/t)*factor
            User.score+=score
        elif score==1:
            score+=(avg_t/t*0.5)*factor
            User.score+=(score)

        return score

    def calc_diff(self, game):
        if len(game.user.results)!=0:
            data=game.user.results[-1]
            prev_diff=data[4]
            prev_time= data[1]
            data=self.transform(data)
            prev_score=data[0]
        else: return 1

        pred=int(self.classifier.predict(np.array(data).reshape(1,-1)))

        max_diff_time_rate=0.5

        if prev_time==0: prev_time+=0.01

        """if pred>-1:
            success_rate=(prev_diff/prev_time)*prev_score #0 if wrong answer
            if game.user.difficulty>= max(game.module.tasks.storage.keys()): #don't let user diff go further than the max lvl of tasks, thus decreasing the user lvl in case of a wrong answer won't result easier tasks
                game.user.difficulty=max(game.module.tasks.storage.keys())
            else: game.user.difficulty+=success_rate*max_diff_time_rate+pred/5
        else: game.user.diffuculty=max((prev_diff-prev_diff/prev_time)*max_diff_time_rate, 1)"""
        success_rate=(prev_diff/prev_time)*prev_score #0 if wrong answer
        if game.user.difficulty>= max(game.module.tasks.storage.keys()): #don't let user diff go further than the max lvl of tasks, thus decreasing the user lvl in case of a wrong answer won't result easier tasks
            if pred>0:
                game.user.difficulty=max(game.module.tasks.storage.keys())
            else:
                game.user.difficulty+=success_rate*max_diff_time_rate + pred/2

        elif pred>-1: game.user.difficulty+=success_rate*max_diff_time_rate * pred/3
        else: game.user.difficulty+=success_rate*max_diff_time_rate + pred/2
        
        #udif=round(game.user.difficulty)
        """if udif not in game.module.tasks.storage.keys():  
            if udif>=len(game.module.tasks.storage.keys()):   #higher than the highest stored diff
                udiff=list(game.module.tasks.storage.keys())[-1] #set to the highest
            else:
                udiff=max(udiff-1,1)       
            return udiff"""
        return float(game.user.difficulty)

            