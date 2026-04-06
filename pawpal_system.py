from datetime import datetime, timedelta
from typing import List, Optional

class Task:
    def __init__(self, title: str, date_time: datetime, duration: int, recurring: bool = False, frequency: str = ""):
        self.title = title
        self.date_time = date_time
        self.duration = duration
        self.recurring = recurring
        self.frequency = frequency
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def reschedule(self, new_date_time: datetime):
        self.date_time = new_date_time

    def is_conflicting(self, other_task: 'Task') -> bool:
        # Simple conflict check: if time ranges overlap
        start1 = self.date_time
        end1 = start1 + timedelta(minutes=self.duration)
        start2 = other_task.date_time
        end2 = start2 + timedelta(minutes=other_task.duration)
        return max(start1, start2) < min(end1, end2)

    def generate_next_occurrence(self) -> Optional[datetime]:
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
        self.name = name
        self.species = species
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_task(self, task: Task):
        if task in self.tasks:
            self.tasks.remove(task)

    def get_upcoming_task(self) -> Optional[Task]:
        now = datetime.now()
        upcoming = [t for t in self.tasks if t.date_time > now and not t.completed]
        if upcoming:
            return min(upcoming, key=lambda t: t.date_time)
        return None

class Owner:
    def __init__(self, name: str, owner_id: str):
        self.name = name
        self.ID = owner_id
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        self.pets.append(pet)

    def remove_pet(self, pet: Pet):
        if pet in self.pets:
            self.pets.remove(pet)

    def get_all_tasks(self) -> List[Task]:
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks

    def view_schedule(self):
        # Placeholder: perhaps print or return a schedule
        pass

class Scheduler:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_task(self, task: Task):
        if task in self.tasks:
            self.tasks.remove(task)

    def get_tasks_for_day(self, date: datetime.date) -> List[Task]:
        return [t for t in self.tasks if t.date_time.date() == date]

    def sort_tasks(self) -> List[Task]:
        return sorted(self.tasks, key=lambda t: t.date_time)

    def detect_conflicts(self) -> List[tuple]:
        conflicts = []
        sorted_tasks = self.sort_tasks()
        for i in range(len(sorted_tasks) - 1):
            if sorted_tasks[i].is_conflicting(sorted_tasks[i + 1]):
                conflicts.append((sorted_tasks[i], sorted_tasks[i + 1]))
        return conflicts

    def generate_daily_schedule(self, date: datetime.date):
        # Placeholder: generate a schedule for the day
        pass
