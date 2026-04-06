import pytest
from datetime import datetime
from pawpal_system import Task, Pet

def test_task_completion():
    """Test that mark_completed() changes task status from False to True."""
    task = Task("Test Task", datetime.now(), 30)
    assert not task.completed  # Initially False
    task.mark_completed()
    assert task.completed  # After marking, True

def test_pet_add_task_increases_count():
    """Test that adding a task to a pet increases the pet's task count."""
    pet = Pet("Buddy", "Dog")
    assert len(pet.tasks) == 0  # Initially empty
    task = Task("Walk Buddy", datetime.now(), 30)
    pet.add_task(task)
    assert len(pet.tasks) == 1  # After adding, count increases
    assert task.pet == pet  # Task references the pet