import datetime
class Task:
    """
    A task the user wants to complete.

    === ATTRIBUTES == 
    name: the name of the task. this cannot be updated once you've created a task.
    deadline: (optional) when this task is due.
    time: hours the user needs/wants to complete the task.
    priority: the priority of the task: high priority (1), medium priority (2), low priority (3).
    status: whether the task is complete (1), in progress (2), or unfinished (3).
    """
    name: str
    deadline: datetime
    time: float
    priority: int
    status: int

    def __init__(self, name, deadline, time, priority, status) -> None:
        '''
        Initializes a new Task.
        '''
        self.name = name
        self.deadline = deadline
        self.time = time
        self.priority = priority
        self.status = status
    
    ### UPDATE METHODS ###
    ### the following methods update Task attributes except for <name>.

    def updateDeadline(self, new_deadline) -> None:
        self.deadline = new_deadline
    
    def updateTime(self, new_time) -> None:
        self.time = new_time
    
    def updatePriority(self, new_priority) -> None:
        self.priority = new_priority
    
    def updateStatus(self, new_status) -> None:
        self.status = new_status
    
    def printTask(self) -> str:
        '''
        Returns a string of the Task and all of its attributes formatted nicely.
        '''
        n = self.name
        d = str(self.deadline)
        t = str(self.time)
        p = {1: "high", 2: "medium", 3: "low"}
        s = {1: "complete", 2: "in-progress", 3: "incomplete"}

        string = "task: " + n + "\n" + "\ndeadline: " + d + "\ntime needed: " + t + " hour(s)" + "\npriority: " + p[self.priority] + "\nstatus: " + s[self.status] + '\n'

        return string
    
if __name__ == "__main__":
    ### simple test ###

    name = "finish math homework"
    deadline = datetime.datetime(2023, 5, 17)
    time = 2
    priority = 1
    status = 3

    newTask = Task(name, deadline, time, priority, status)
    print(newTask.printTask())

    new_deadline = datetime.datetime(2023, 5, 19)
    new_time = 1

    newTask.updateDeadline(new_deadline)
    newTask.updateTime(new_time)

    print(newTask.printTask())

