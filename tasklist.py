import datetime
from typing import List

from task import Task

class TaskList(Task):
    """
    A list of tasks.

    === ATTRIBUTES == 
    length: the length of the list of tasks.
    tasks: a list of Task items.
    """
    length: int
    tasks: List[Task]

    


