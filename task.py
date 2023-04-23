import datetime
class Task:
    """
    A task the user wants to complete.

    === ATTRIBUTES == 
    name: the name of the task.
    deadline: (optional) when this task is due.
    time: hours the user needs/wants to complete the task.
    priority: the priority of the task on a scale of 1-3 (1 being highest priority, and 3 being lowest).
    status: whether the task is complete (1), in progress (2), or unfinished (3).
    """
    name: str
    deadline: datetime
    time: float
    priority: int
    status: int