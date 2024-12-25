from typing import List
import datetime
from task import Task

class TaskList:
    """
    A list of tasks.

    === ATTRIBUTES == 
    length: the length of the list of tasks.
    tasks: a list of Task items.
    """
    length: int
    tasks: List[Task]

    def __init__(self, tasks) -> None:
        '''
        Initializes a new TaskList.
        '''
        self.tasks = tasks
        self.length = len(tasks)
    
    def addTask(self, task) -> None:
        '''
        Appends the new task to the back of the list.
        '''
        self.tasks.append(task)

    def removeTask(self, task) -> None:
        '''
        Removes the task from the list
        '''
        self.tasks.remove(task)
    
    def printTasks(self) -> None: 
        '''
        Returns a list of each task, the number of tasks and the total time needed
        for this list formatted nicely.
        '''
        ret = ""
        counter = 1
        total_time = 0
        for task in self.tasks:
            ret += str(counter) + ". " + task.printTask()
            total_time += task.time
            counter +=1
        
        ret += "\ntotal time for all tasks: " + str(total_time) + " hour(s)" + "\n"

        print(ret)

if __name__ == "__main__":
    ### simple test ### 

    name1 = "finish math homework"
    name2 = "chemistry assignment"

    deadline1 = datetime.datetime(2023, 5, 15)
    deadline2 = datetime.datetime(2023, 5, 22)

    time1 = 2
    time2 = 1

    priority1 = 3
    priority2 = 2

    task1 = Task(name1, deadline1, time1, priority1)
    task2 = Task(name2, deadline2, time2, priority2)

    lst = [task1, task2]
    tasklist = TaskList(lst)

    tasklist.printTasks()

    task1.taskIPR()

    tasklist.printTasks()
