# PawPal+ Project Reflection

## 1. System Design
The app should have an input/remove function for tasks, it should also have a calendar function that abides by personal constraints, and output a plan that bases it off the constraints and preferences of the person using it. 
**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

My UML design includes four classes: Owner, Pet, Task, and Scheduler.

The Owner stores basic info (like ID) and manages a list of pets. The Pet represents each animal and holds its own tasks. The Task represents activities (e.g., feeding or walking) and includes details like time, recurrence, and completion status, along with logic for rescheduling and conflict detection. The Scheduler manages all tasks across pets, handling sorting, conflict detection, and daily scheduling.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

I made a few changes to improve the structure and make the app work more correctly. I added better connections between classes by giving each Task a reference to its Pet and each Pet a reference to its Owner, and these get set automatically when they’re added. This makes it easier to move between objects and keeps the data consistent. I also gave each Owner their own Scheduler and made sure that when tasks are added or removed from pets, they stay synced with the scheduler so everything is tracked in one place. I fixed the detect_conflicts method so it checks all tasks instead of just ones next to each other, which catches more conflicts even though it’s a bit slower. On top of that, I added a check to make sure task durations aren’t zero or negative, updated imports, and cleaned up type hints. Overall, these changes make the code cleaner, more reliable, and easier to manage.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
