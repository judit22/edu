import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier  
from sklearn.preprocessing import StandardScaler

import numpy as np
import user
class Calculator():
    def __init__(self):
        training_data_x,training_data_y=pd.read_csv('C:/Users/teves/Downloads/generated_data_x1.csv'),pd.read_csv('C:/Users/teves/Downloads/generated_data_y1.csv')    
       
        X_train, X_test, y_train, y_test = train_test_split(training_data_x,
                                                             training_data_y,
                                                             test_size=0.33,
                                                             random_state=42)
        self.X_train=X_train.to_numpy()
        self.y_train=y_train.to_numpy()
        self.X_test=X_test.to_numpy()

        self.classifier=LogisticRegression(random_state=0, solver='lbfgs', max_iter=1000)
        #self.classifier = KNeighborsClassifier(n_neighbors=3)
        self.classifier.fit(self.X_train, self.y_train)

    def transform(self,X):
        temp=[0]*self.X_train.shape[1]
        X=X[-1]
        if X[0]>1:
            temp[-3]=1
        else: temp[-3]=0
        temp[-2]=X[1]
        temp[-1]=X[2]
        if round(X[3])>7:
            temp[6]=1
        else: temp[round(X[3])-1]=1
        temp[X[4]+11]=1
        if X[5]>6:
            temp[-4]=1
        else: temp[X[5]+22]=1
        return temp
    
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
        data=game.user.results
        if len(data)!=0:
            data=self.transform(data)
        else: return 1

        pred=int(self.classifier.predict(np.array(data).reshape(1,-1)))

        max_diff_time_rate=0.5
        prev_diff=int(np.where(data[11:22])[0]+1)
        prev_time= data[-2]
        #prev_score= data[0]
        prev_score=data[-3]
        diff=prev_diff
        if prev_score==0 and pred==2:
            pred=0
        if prev_time==0: prev_time+=0.01

        if pred>-1:
            success_rate=(diff/prev_time)*prev_score #0 if wrong answer
            if game.user.difficulty>= max(game.module.tasks.storage.keys()): #don't let user diff go further than the max lvl of tasks, thus decreasing the user lvl in case of a wrong answer won't result easier tasks
                game.user.difficulty=max(game.module.tasks.storage.keys())
            else: game.user.difficulty+=success_rate*max_diff_time_rate+pred/5
        else: game.user.diffuculty=max((diff-diff/prev_time)*max_diff_time_rate, 1)

        udif=round(game.user.difficulty)
        """if udif not in game.module.tasks.storage.keys():  
            if udif>=len(game.module.tasks.storage.keys()):   #higher than the highest stored diff
                udiff=list(game.module.tasks.storage.keys())[-1] #set to the highest
            else:
                udiff=max(udiff-1,1)       
            return udiff"""
        return float(game.user.difficulty)

            