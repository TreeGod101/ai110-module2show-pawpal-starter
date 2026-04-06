import pytest

from pawpal import PawPal  # Assuming PawPal is the main class or module

def test_add_task():
    pawpal = PawPal()
    task_id = pawpal.add_task("Walk the dog")
    assert task_id is not None
    assert len(pawpal.tasks) == 1
    assert pawpal.tasks[task_id].description == "Walk the dog"
    assert not pawpal.tasks[task_id].completed

def test_add_multiple_tasks():
    pawpal = PawPal()
    pawpal.add_task("Feed the cat")
    pawpal.add_task("Groom the bird")
    assert len(pawpal.tasks) == 2

def test_complete_task():
    pawpal = PawPal()
    task_id = pawpal.add_task("Clean the cage")
    pawpal.complete_task(task_id)
    assert pawpal.tasks[task_id].completed

def test_complete_nonexistent_task():
    pawpal = PawPal()
    with pytest.raises(ValueError):
        pawpal.complete_task(999)  # Assuming invalid ID raises error

def test_complete_already_completed_task():
    pawpal = PawPal()
    task_id = pawpal.add_task("Bath the fish")
    pawpal.complete_task(task_id)
    # Assuming completing again does nothing or raises error
    pawpal.complete_task(task_id)  # Should not raise or handle gracefully
    assert pawpal.tasks[task_id].completed