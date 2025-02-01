'''class Task:
    def __init__(self,task_id,des,pri):
        self.task_id=task_id
        self.des=des
        self.pri=pri

    def __repr__(self):    #private constructor
        return f"Task({self.task_id},{self.des},{self.pri})"
class Taskscheduler:
    def __init__(self):
        self.tasks=[]
    def add_task(self,task_id,des,pri):
        self.tasks.append(Task(task_id,des,pri))
        return f"Task{task_id} added"
    def remove_task(self,task_id):
        for task in self.tasks:
            if task.task_id==task_id:
                self.tasks.remove(task)
                return f"Task{task_id} removed"
            return f"Task{task_id} not found"
    def get_next_task(self):
        if not self.tasks:
            return "No tasks available"
        self.tasks.sort(key=lambda t:t.pri)
        next_task=self.tasks.pop(0)
        return f"Next task:{next_task}"
    
    def list_tasks(self):
         if not self.tasks:
            return "No tasks available"
         self.tasks.sort(key=lambda t:t.pri)
         return [repr(task) for task in self.tasks]
scheduler=Taskscheduler()
print(scheduler.list_tasks())
print(scheduler.add_task(1,"kill",2))
print(scheduler.add_task(2,"escape",3))
print(scheduler.add_task(3,"demolish",4))
print(scheduler.add_task(4,"new life",1))
print(scheduler.list_tasks())
print(scheduler.get_next_task())
print(scheduler.list_tasks())
print(scheduler.remove_task(1))'''




'''class drinks:
    def __init__(self,color,brand,quantity):
        self.color=color
        self.brand=brand
        self.quantity=quantity
drink1=drinks("black","coco cola","200ml")
drink2=drinks("red","string","200ml")'''


'''class library:
    def __int__(self):
        self.books=[]
    def add(self,    
'''
x=True
y=False
print(x&y)




        
    
