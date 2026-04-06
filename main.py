from pawpal_system import Owner, Pet, Task
from datetime import datetime, timedelta

# Create an Owner
owner = Owner("John Doe", "001")

# Create two Pets
pet1 = Pet("Buddy", "Dog")
pet2 = Pet("Whiskers", "Cat")

# Add pets to owner
owner.add_pet(pet1)
owner.add_pet(pet2)

# Create tasks with different times (using today's date)
now = datetime.now()
task1 = Task("Walk Buddy", now.replace(hour=8, minute=0), 30)  # 8:00 AM
task2 = Task("Feed Whiskers", now.replace(hour=12, minute=0), 15)  # 12:00 PM
task3 = Task("Play with Buddy", now.replace(hour=18, minute=0), 45)  # 6:00 PM

# Add tasks to pets
pet1.add_task(task1)
pet1.add_task(task3)
pet2.add_task(task2)

# Get today's tasks from scheduler
today = now.date()
todays_tasks = owner.scheduler.get_tasks_for_day(today)

# Print Today's Schedule
print("Today's Schedule:")
if todays_tasks:
    for task in sorted(todays_tasks, key=lambda t: t.date_time):
        print(f"- {task.title} at {task.date_time.strftime('%H:%M')} for {task.pet.name if task.pet else 'Unknown'}")
else:
    print("No tasks scheduled for today.")
