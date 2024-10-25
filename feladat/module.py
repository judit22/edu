
import feladat1
import random 
import taskcollection

class Module():
    def __init__(self):
        self.tasks=taskcollection.TaskCollection()
    def generate_task(self):
        pass

class Arithmetics(Module):
    def __init__(self):
        super().__init__()
        self.index=1
        self.avg_time=3
        try:
            self.tasks.load('C:/Users/teves/Downloads/edu/arithmetics.json')
        except:
            pass
    def generate_task(self):
        if len(self.tasks.storage.keys())==0:
                self.tasks.storage[1]=[]
                self.tasks.storage[2]=[]
                self.tasks.storage[3]=[]

        num1=random.randint(1,30)
        num2=random.randint(1,50)
        for i in range(10):
            task=feladat1.Task(num1+num2+2*i, 1, f"{num1+i}+{num2+i}")
            self.tasks.storage[1].append(task)
        
        for i in range(1,5):
            num1=random.randint(1,6)
            num2=random.randint(1,6)
            if num1!=num2:
                task211=feladat1.Task(num1*2,4, f"{num1}/{num2} = x/{num2*2}")
                task221=feladat1.Task(num1*3,4, f"{num1}/{num2} = x/{num2*3}")
                task231=feladat1.Task(num1*5,4, f"{num1}/{num2} = x/{num2*5}")
                task212=feladat1.Task(num2*2,4, f"{num2}/{num1} = x/{num1*2}")
                task222=feladat1.Task(num2*3,4, f"{num2}/{num1} = x/{num1*3}")
                task232=feladat1.Task(num2*5,4, f"{num2}/{num1} = x/{num1*5}")
                task241=feladat1.Task(num2*2,4, f"{num1}/{num2} = {num1*2}/x")
                task251=feladat1.Task(num2*3,4, f"{num1}/{num2} = {num1*3}/x")
                task261=feladat1.Task(num2*5,4, f"{num1}/{num2} = {num1*5}/x")
                task242=feladat1.Task(num1*2,4, f"{num2}/{num1} = {num2*2}/x")
                task252=feladat1.Task(num1*3,4, f"{num2}/{num1} = {num2*3}/x")
                task262=feladat1.Task(num1*5,4, f"{num2}/{num1} = {num2*5}/x")
                task27=feladat1.Task(num1*num2,4, f"{num1}*{num2}")

                l=[task211,task221,task231,task212,task222,task232,
                task241,task251,task261,task242,task252,task262,task27]

                for task in l:
                    self.tasks.storage[4].append(task)


        for i in range(1,6):
            task31=feladat1.Task(num1*num2+num1+num2+i, 3, f"{num1}*{num2}+{num1+i+num2}")
            task32=feladat1.Task(num1+i+num2*num1, 3, f"{num1+i}+{num2}*{num1}")
            task33=feladat1.Task(num2+i+num2*num1, 3, f"{num2+i}+{num2}*{num1}")
            task341=feladat1.Task(num2*10-num1, 3, f"{num2*10}-{num1}= ")
            task342=feladat1.Task(num1*10-num2,  3, f"{num1*10}-{num2}= ")
            task343=feladat1.Task(num2*10-num2,  3, f"{num2*10}-{num2}= ")
            task344=feladat1.Task(num1*10-num1,  3, f"{num1*10}-{num1}= ")

            task351=feladat1.Task(num2*i-num1, 3, f"{num2*i}-{num1}= ")
            task352=feladat1.Task(num1*i-num2,  3, f"{num1*i}-{num2}= ")
            task353=feladat1.Task(num2*i-num2,  3, f"{num2*i}-{num2}= ")
            task354=feladat1.Task(num1*i-num1,  3, f"{num1*i}-{num1}= ")

            task361=feladat1.Task(num2*i-num1, 3, f"{num2}*{i}-{num1}= ")
            task362=feladat1.Task(num1*i-num2,  3, f"{num1}*{i}-{num2}= ")
            task363=feladat1.Task(num2*i-num2,  3, f"{num2}*{i}-{num2}= ")
            task364=feladat1.Task(num1*i-num1,  3, f"{num1}*{i}-{num1}= ")


            l=[task31,task32,task33, task341,task342,task343,task344,task351,task352,task353,
                task354,task361,task362,task363,task364]
            for task in l:
                self.tasks.storage[3].append(task)
        if num2>1:
            task51=feladat1.Task(num1**2,5 ,f"{num1}/{num2}= x/{num1*num2}")
            self.tasks.storage[5].append(task51)
        for i in range(1,8):
            task52=feladat1.Task((num2+i)*num2+num1**2 ,5 ,f"{num2+i}/{num1}+{num1}/{num2}= x/{num1*num2}")
            task53=feladat1.Task((num1+i)*num2+num1**2 ,5 ,f"{num1+i}/{num1} + {num1}/{num2}= x/{num1*num2}")
            task54=feladat1.Task((num2+i)*num1+num2**2 ,5 ,f"{num2+i}/{num2}+{num2}/{num1}= x/{num1*num2}")
            task55=feladat1.Task((num1+i)*num1+num2**2 ,5 ,f"{num1+i}/{num2}+{num2}/{num1}= x/{num1*num2}")

            l=[task52,task53,task54,task55]
            for task in l:
                self.tasks.storage[5].append(task)
            

        
class Power(Module):
    def __init__(self):
          super().__init__()
          self.index=2
          self.avg_time=3
    def generate_task(self):

        if len(self.tasks.storage.keys())==0:
            self.tasks.storage[1]=[]
            self.tasks.storage[2]=[]
            self.tasks.storage[3]=[]
            self.tasks.storage[4]=[]
        for i in range(1,5):
            if i not in self.tasks.storage.keys():
                self.tasks.storage[i]=[]
            
        num1=random.randint(2,5)
        num2=random.randint(2,3)
        task4=feladat1.Task(num1**num2, 1, f"{num1}^{num2}")
        task41=feladat1.Task(num2**num1, 1, f"{num2}^{num1}")
        self.tasks.storage[1].append(task4)
        self.tasks.storage[1].append(task41)

        task61= feladat1.Task(num1, 2, f"{num2}^x ={num2**num1}")
        self.tasks.storage[2].append(task61)
        task62=feladat1.Task(num1, 2, f"x^{num2}={num1**num2}")
        task63=feladat1.Task(num2, 2, f"x^{num1}={num2**num1}")
        self.tasks.storage[2].append(task62)
        self.tasks.storage[2].append(task63)
        
        num3=random.randint(2,9)
        task81=feladat1.Task(num3+num1, 4, f"{num2}^{num1}*{num2}^{num3} = {num2}^x")
        task82=feladat1.Task(num2+num1, 4, f"{num3}^{num2}*{num3}^{num1} = {num3}^x")
        task83=feladat1.Task(num2+num3, 4, f"{num1}^{num2}*{num1}^{num3} = {num1}^x")
        task84=feladat1.Task(num3*num1, 4, f"({num2}^{num1})^{num3} = {num2}^x")
        task85=feladat1.Task(num2*num1, 4, f"({num3}^{num1})^{num2} = {num3}^x")
        task86=feladat1.Task(num2*num3, 4, f"({num1}^{num2})^{num3} = {num1}^x")
        
        l=[task81,task82,task83, task84, task85, task86]
        for task in l:
            self.tasks.storage[4].append(task)

        if num2!=1:
            task71=feladat1.Task(num2**num1, 3, f'log_{num2}_x = {num1}')
            task72=feladat1.Task(num2, 3, f"log_x_{num2**num2} = {num2}")
            task73=feladat1.Task(num2, 3, f"log_x_{num2**num3} = {num3}")
            task74=feladat1.Task(num2, 3, f"log_x_{num2**num1} = {num1}")
            task75=feladat1.Task(num1, 3, f"log_{num2}_{num2**num1} = x")
            task76=feladat1.Task(num3, 3, f"log_{num2}_{num2**num3} = x")
            task77=feladat1.Task(num2, 3, f"log_{num2}_{num2**num2} = x")
            
            l=[task71,task72,task73,task74, task75, task76, task77]
            for task in l:
                self.tasks.storage[3].append(task)
    

class Units(Module):

    def __init__(self):
        super().__init__()
        self.index=3
        self.avg_time=3
    def generate_task(self):
        if len(self.tasks.storage.keys())==0:
            self.tasks.storage[1]=[]
            self.tasks.storage[2]=[]
            self.tasks.storage[3]=[]
            self.tasks.storage[4]=[]
            self.tasks.storage[5]=[]
            self.tasks.storage[6]=[]
            self.tasks.storage[7]=[]

        num1=random.randint(1,100)
        num2=random.randint(1,100)
        unit=random.choice(['m','l'])
        for i in range(1,5):
            task111=feladat1.Task(num1*i*10, 1, f"{num1*i*100} c{unit} = x d{unit}")
            task121=feladat1.Task(num2*i*10, 1, f"{num2*i*100} c{unit} = x d{unit}")
            task131=feladat1.Task(num1*i, 1, f"{num1*i*10} c{unit} = x d{unit}")
            task141=feladat1.Task(num2*i, 1, f"{num2*i*10} c{unit} = x d{unit}")
            task112=feladat1.Task(num1*i*10, 1, f"{num1*i*100} d{unit} = x {unit}")
            task122=feladat1.Task(num2*i*10, 1, f"{num2*i*100} d{unit} = x {unit}")
            task132=feladat1.Task(num1*i, 1, f"{num1*i*10} d{unit} = x {unit}")
            task142=feladat1.Task(num2*i, 1, f"{num2*i*10} d{unit} = x {unit}")
            task113=feladat1.Task(num1*i*10, 1, f"{num1*i*100} m{unit} = x c{unit}")
            task123=feladat1.Task(num2*i*10, 1, f"{num2*i*100} m{unit} = x c{unit}")
            task133=feladat1.Task(num1*i, 1, f"{num1*i*10} m{unit} = x c{unit}")
            task143=feladat1.Task(num2*i, 1, f"{num2*i*10} m{unit} = x c{unit}")
            task151=feladat1.Task(num1*i*1000, 1, f"{num1*i} km = x m")
            task152=feladat1.Task(num2*i*1000, 1, f"{num2*i} km = x m")
            task161=feladat1.Task(num1*i*100, 1, f"{num1*i} hl = x l")
            task162=feladat1.Task(num2*i*100, 1, f"{num2*i} hl = x l")
            task171=feladat1.Task(num1*i*1000, 1, f"{num1*i} kg = x g")
            task172=feladat1.Task(num2*i*1000, 1, f"{num2*i} kg = x g")
            task181=feladat1.Task(num1*i*1000, 1, f"{num1*i} t = x kg")
            task182=feladat1.Task(num2*i*1000, 1, f"{num2*i} t = x kg")
        
            task191=feladat1.Task(num1*i, 1, f"{num1*i*10} g = x dkg")
            task192=feladat1.Task(num2*i, 1, f"{num2*i*10} g = x dkg")
            task193=feladat1.Task(num1*i*10, 1, f"{num1*i*100} g = x dkg")
            task194=feladat1.Task(num2*i*10, 1, f"{num2*i*100} g = x dkg")


            task1112=feladat1.Task(num1*i*10, 1, f"x c{unit} =  {num1*i} d{unit}")
            task1212=feladat1.Task(num2*i*10, 1, f"x c{unit} = {num2*i} d{unit}")
            task1312=feladat1.Task(num1*i*100, 1, f"x c{unit} = {num1*i*10} d{unit}")
            task1412=feladat1.Task(num2*i*100, 1, f"x c{unit} = {num2*i*10} d{unit}")
            task1122=feladat1.Task(num1*i*100, 1, f"x d{unit} = {num1*i*10} {unit}")
            task1222=feladat1.Task(num2*i*100, 1, f"x d{unit} = {num2*i*10} {unit}")
            task1322=feladat1.Task(num1*i*10, 1, f"x d{unit} = {num1*i} {unit}")
            task1422=feladat1.Task(num2*i*10, 1, f" x d{unit} = {num2*i} {unit}")
            task1132=feladat1.Task(num1*i*100, 1, f"x m{unit} = {num1*i*10} c{unit}")
            task1232=feladat1.Task(num2*i*100, 1, f"x m{unit} = {num2*i*10} c{unit}")
            task1332=feladat1.Task(num1*i*10, 1, f"x m{unit} = {num1*i} c{unit}")
            task1432=feladat1.Task(num2*i*10, 1, f"x m{unit} = {num2*i} c{unit}")
            task1512=feladat1.Task(num1*i, 1, f"x km = {num1*i*1000} m")
            task1522=feladat1.Task(num2*i, 1, f"x km = {num2*i*1000}  m")
            task1612=feladat1.Task(num1*i, 1, f"x hl = {num1*i*100} l")
            task1622=feladat1.Task(num2*i, 1, f"x hl = {num2*i*100} l")
            task1712=feladat1.Task(num1*i, 1, f"x kg = {num1*i*1000} g")
            task1722=feladat1.Task(num2*i, 1, f"x kg = {num2*i*1000} g")
            task1812=feladat1.Task(num1*i, 1, f"x t = {num1*i*1000} kg")
            task1822=feladat1.Task(num2*i, 1, f"x t = {num2*i*1000} kg")
        
            task1912=feladat1.Task(num1*i*10, 1, f"x g = {num1*i} dkg")
            task1922=feladat1.Task(num2*i*10, 1, f"x g = {num2*i} dkg")
            task1932=feladat1.Task(num1*i, 1, f"x g = {num1*i*10} dkg")
            task1942=feladat1.Task(num2*i, 1, f"x g = {num2*i*10} dkg")

            l=[task111,task121,task131,task141,task112,task122,task132,task142,task113,
               task123,task133,task143,task151,task152,task161, task162,task171,task172,
               task181,task182,task191, task192,task193,task194,task1112,task1212,task1312,
               task1412,task1122,task1222,task1322,task1422,task1132,task1232,task1332,task1432,
               task1512,task1522,task1612, task1622,task1712,task1722,task1812,task1822,task1912,
                task1922,task1932,task1942]
            for task in l:
                self.tasks.storage[1].append(task)

        for i in range(1,5):
            task211=feladat1.Task(num1*i, 2, f"{num1*i*100}c{unit} = x {unit}")
            task221=feladat1.Task(num2*i, 2, f"{num2*i*100}c{unit} = x {unit}")
            task231=feladat1.Task(num1*i*10, 2, f"{num1*i*1000}c{unit} = x {unit}")
            task241=feladat1.Task(num2*i*10, 2, f"{num2*i*1000}c{unit} = x {unit}")
            task212=feladat1.Task(num1*i, 2, f"{num1*i*100}m{unit} = x d{unit}")
            task222=feladat1.Task(num2*i, 2, f"{num2*i*100}m{unit} = x d{unit}")
            task232=feladat1.Task(num1*i*10, 2, f"{num1*i*1000}m{unit} = x d{unit}")
            task242=feladat1.Task(num2*i*10, 2, f"{num2*i*1000}m{unit} = x d{unit}")
            task251=feladat1.Task(num1*i*100, 2, f"{num1*i} kg = x dkg")
            task252=feladat1.Task(num2*i*100, 2, f"{num2*i} kg = x dkg")

            task2112=feladat1.Task(num1*i*100, 2, f"x c{unit} = {num1*i} {unit}")
            task2212=feladat1.Task(num2*i*100, 2, f"x c{unit} = {num2*i} {unit}")
            task2312=feladat1.Task(num1*i*1000, 2, f"x c{unit} = {num1*i*10} {unit}")
            task2412=feladat1.Task(num2*i*1000, 2, f"x c{unit} = {num2*i*10} {unit}")
            task2122=feladat1.Task(num1*i*100, 2, f"x m{unit} = {num1*i} d{unit}")
            task2222=feladat1.Task(num2*i*100, 2, f"x m{unit} = {num2*i} d{unit}")
            task2322=feladat1.Task(num1*i*1000, 2, f"x m{unit} = {num1*i*10} d{unit}")
            task2422=feladat1.Task(num2*i*1000, 2, f"x m{unit} = {num2*i*1000} d{unit}")
            task2512=feladat1.Task(num1*i, 2, f"x kg = {num1*i*100}  dkg")
            task2522=feladat1.Task(num2*i, 2, f"x kg = {num2*i*100} dkg")

            l=[task211,task221,task231,task241,task212,task222,task232,task242,
               task251,task252,task2112,task2212,task2312,task2412,task2122,
               task2222,task2322,task2422,task2512,task2522]
            for task in l:
                self.tasks.storage[2].append(task)
            task311=feladat1.Task(num1*10000,3,f"{num1} km = x dm")
            task312=feladat1.Task(num2*10000,3,f"{num2} km = x dm")
            task321=feladat1.Task(num1*100000, 3,f"{num1} km = x cm")
            task322=feladat1.Task(num2*100000,3,f"{num2} km = x cm")
            task331=feladat1.Task(num1*1000,3,f"{num1} hl = x dl")
            task332=feladat1.Task(num2*1000,3,f"{num2} hl = x dl")
            task341=feladat1.Task(num1*10000, 3,f"{num1} hl = x cl")
            task342=feladat1.Task(num2*10000,3,f"{num2} hl = x cl")
            task351=feladat1.Task(num1*100000,3,f"{num1} t = x dkg")
            task352=feladat1.Task(num2*100000,3,f"{num2} t = x dkg")

            l=[task311,task312,task321,task322,task331,task332,task341,task342,task351,task352]
            for task in l:
                self.tasks.storage[3].append(task)
            
            for i in range(1,3):
                task411=feladat1.Task(num1+i,4,f"x km = {(num1+i)*10000} dm")
                task412=feladat1.Task(num2+i,4,f"x km = {(num2+i)*10000} dm")
                task421=feladat1.Task(num1+i, 4,f"x km = {(num1+i)*100000} cm")
                task422=feladat1.Task(num2+i,4,f"x km = {(num2+i)*100000} cm")
                task431=feladat1.Task(num1+i,4,f"x hl = {(num1+i)*1000} dl")
                task432=feladat1.Task(num2+i,4,f"x hl = {(num2+i)*1000} dl")
                task441=feladat1.Task(num1+i, 4,f"x hl = {(num1+i)*10000} cl")
                task442=feladat1.Task(num2+i,4,f"x hl = {(num2+i)*100000} cl")
                task451=feladat1.Task(num1+i,4,f"x t = {(num1+i)*100000} dkg")
                task452=feladat1.Task(num2+i,4,f"x t = {(num2+i)*100000} dkg")

                l=[task411,task412,task421,task422,task431,task432,task441,task442,task451,task452]
                for task in l:
                    self.tasks.storage[4].append(task)
            for i in range(8):
                task51=feladat1.Task((num1+i)/10 ,5,f"x km = {(num1+i)*100} m")
                task52=feladat1.Task((num1+i)/100 ,5,f"x km = {(num1+i)*10} m")
                task53=feladat1.Task((num1+i)/1000 ,5,f"x km = {num1+i} m")
                l=[task51,task52,task53]
                for task in l:
                    self.tasks.storage[5].append(task)
            
            for i in range(5):
                num1=random.randint(1,10)
                num2=random.randint(1,10)
                if num2>num1:
                    task611=feladat1.Task((num2-num1)*10,6,f"{num1} c{unit} + x m{unit} = {num2} c{unit}")
                    task612=feladat1.Task((num2-num1)*10,6,f"{num1} d{unit} + x c{unit} = {num2} d{unit}")
                    task613=feladat1.Task((num2-num1)*100,6,f"{num1} d{unit} + x m{unit} = {num2} d{unit}")
                    task614=feladat1.Task((num2-num1)*100 ,6,f"{num1} {unit} + x c{unit} = {num2} {unit}")
                
                    l=[task611,task612,task613,task614]
                    for task in l:
                        self.tasks.storage[6].append(task)

                    if num2*10>num2*100:
                        task615=feladat1.Task(num2*10-num1*100,7,f"{num1} {unit} + x m{unit} = {num2} c{unit}")
                        self.tasks.storage[7].append(task615)

                if num1>num2:
                    task621=feladat1.Task((num1-num2)*10,6,f"{num1} c{unit} - x m{unit} = {num2} c{unit}")
                    task622=feladat1.Task((num1-num2)*10,6,f"{num1} d{unit} - x c{unit} = {num2} d{unit}")
                    task623=feladat1.Task((num1-num2)*100,6,f"{num1} d{unit} - x m{unit} = {num2} d{unit}")
                    task624=feladat1.Task((num1-num2)*100 ,6,f"{num1} {unit} - x c{unit} = {num2} {unit}")
                    task625=feladat1.Task((num1-num2)*1000,6,f"{num1} {unit} - x m{unit} = {num2} {unit}")

                    l=[task621,task622,task623,task624,task625]
                    for task in l:
                        self.tasks.storage[6].append(task)
            for i in range(5):
                num1=random.randint(1,10)
                num2=random.randint(1,10)
                if num2>num1:
                    task711=feladat1.Task(num2*100-num1*10,7,f"{num1} c{unit} + x m{unit} = {num2} d{unit}")
                    task712=feladat1.Task(num2*100-num1*10,7,f"{num1} d{unit} + x c{unit} = {num2} {unit}")
                    task713=feladat1.Task(num2*1000-num1*100,7,f"{num1} d{unit} + x m{unit} = {num2} {unit}")
                    task715=feladat1.Task(num2*1000-num1*10,7,f"{num1} c{unit} + x m{unit} = {num2} {unit}")

                    l=[task711,task712,task713,task715]
                    for task in l:
                        self.tasks.storage[7].append(task)
                if num1*100<num2*10:
                    task714=feladat1.Task(num2*10-num1*100 ,7,f"{num1} d{unit} + x m{unit} = {num2} c{unit}")
                    self.tasks.storage[7].append(task714)
