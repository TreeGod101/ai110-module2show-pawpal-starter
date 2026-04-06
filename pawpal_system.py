from datetime import datetime, timedelta
from typing import List, Optional, Tuple

class Task:
    def __init__(self, title: str, date_time: datetime, duration: int, recurring: bool = False, frequency: str = ""):
        """Initialize a Task with title, date_time, duration, recurring, and frequency."""
        if duration <= 0:
            raise ValueError("Duration must be positive")
        self.title = title
        self.date_time = date_time
        self.duration = duration
        self.recurring = recurring
        self.frequency = frequency
        self.completed = False
        self.pet: Optional['Pet'] = None

    def mark_completed(self):
        """Mark the task as completed."""
        self.completed = True

    def reschedule(self, new_date_time: datetime):
        """Reschedule the task to a new date and time."""
        self.date_time = new_date_time

    def is_conflicting(self, other_task: 'Task') -> bool:
        """Check if this task conflicts with another task based on time overlap."""
        # Simple conflict check: if time ranges overlap
        start1 = self.date_time
        end1 = start1 + timedelta(minutes=self.duration)
        start2 = other_task.date_time
        end2 = start2 + timedelta(minutes=other_task.duration)
        return max(start1, start2) < min(end1, end2)

    def generate_next_occurrence(self) -> Optional[datetime]:
        """Generate the next occurrence of a recurring task."""
        if not self.recurring:
            return None
        # Simple implementation for daily, weekly, etc.
        if self.frequency == "daily":
            return self.date_time + timedelta(days=1)
        elif self.frequency == "weekly":
            return self.date_time + timedelta(weeks=1)
        # Add more frequencies as needed
        return None

class Pet:
    def __init__(self, name: str, species: str):
        """Initialize a Pet with name and species."""
        self.name = name
        self.species = species
        self.tasks: List[Task] = []
        self.owner: Optional['Owner'] = None

    def add_task(self, task: Task):
        """Add a task to the pet and set the task's pet reference."""
        self.tasks.append(task)
        task.pet = self
        if self.owner:
            self.owner.scheduler.add_task(task)

    def remove_task(self, task: Task):
        """Remove a task from the pet and update scheduler if applicable."""
        if task in self.tasks:
            self.tasks.remove(task)
            if self.owner:
                self.owner.scheduler.remove_task(task)

    def get_upcoming_task(self) -> Optional[Task]:
        """Get the next upcoming uncompleted task for the pet."""
        now = datetime.now()
        upcoming = [t for t in self.tasks if t.date_time > now and not t.completed]
        if upcoming:
            return min(upcoming, key=lambda t: t.date_time)
        return None

class Owner:
    def __init__(self, name: str, owner_id: str):
        """Initialize an Owner with name and ID, and create a scheduler."""
        self.name = name
        self.ID = owner_id
        self.pets: List[Pet] = []
        self.scheduler = Scheduler()

    def add_pet(self, pet: Pet):
        """Add a pet to the owner and set the pet's owner reference."""
        self.pets.append(pet)
        pet.owner = self

    def remove_pet(self, pet: Pet):
        """Remove a pet from the owner and clean up associated tasks."""
        if pet in self.pets:
            self.pets.remove(pet)
            pet.owner = None
            # Optionally remove pet's tasks from scheduler
            for task in pet.tasks:
                self.scheduler.remove_task(task)

    def get_all_tasks(self) -> List[Task]:
        """Get a list of all tasks from all pets owned by this owner."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks

    def view_schedule(self):
        """View the schedule (placeholder for implementation)."""
        pass

class Scheduler:
    def __init__(self):
        """Initialize a Scheduler with an empty task list."""
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        """Add a task to the scheduler."""
        self.tasks.append(task)

    def remove_task(self, task: Task):
        """Remove a task from the scheduler."""
        if task in self.tasks:
            self.tasks.remove(task)

    def get_tasks_for_day(self, date: datetime.date) -> List[Task]:
        """Get all tasks scheduled for a specific day."""
        return [t for t in self.tasks if t.date_time.date() == date]

    def sort_tasks(self) -> List[Task]:
        """Return a sorted list of tasks by date and time."""
        return sorted(self.tasks, key=lambda t: t.date_time)

    def detect_conflicts(self) -> List[Tuple['Task', 'Task']]:
        """Detect and return pairs of conflicting tasks."""
        conflicts = []
        for i in range(len(self.tasks)):
            for j in range(i + 1, len(self.tasks)):
                if self.tasks[i].is_conflicting(self.tasks[j]):
                    conflicts.append((self.tasks[i], self.tasks[j]))
        return conflicts

    def generate_daily_schedule(self, date: datetime.date):
        """Generate a daily schedule for a given date (placeholder)."""
        pass
