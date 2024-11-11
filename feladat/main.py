import feladat1
import user
import taskcollection
import game
'''
user1=user.User("judit")
user2=user.User()
taskcoll=taskcollection.TaskCollection()
task1=feladat1.Task(5, 1, "3+2")
task2=feladat1.Task(30, 2, "10*3")
task3=feladat1.Task(9, 3, "3^2")
taskcoll.add(task1)
taskcoll.add(task2)
taskcoll.add(task3)
taskcoll.add(feladat1.Task(15,3,"3^2+3*2"))
taskcoll.load("C:/Users/teves/Downloads/sample.json")
taskcoll1=taskcollection.TaskCollection()
taskcoll1.load('C:/Users/teves/Downloads/gentasks.json')
'''

tasks=['C:/Users/teves/Downloads/edu/arithmetics.json','C:/Users/teves/Downloads/edu/power.json','C:/Users/teves/Downloads/edu/unittasks.json']
#g2=game.Game(tasks=tasks)

g2=game.Game('C:/Users/teves/Downloads/edu/userhistory.json',tasks)
g2.play()


#g1=game.Game(user2, taskcoll)
#g1.generate_task()
#g1.play()
