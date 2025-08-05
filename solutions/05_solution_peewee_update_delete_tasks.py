'''
OPTIONAL AI GUIDANCE PROMPT
---------------------------
I am a student in an introductory Python class. I am learning many coding
principles for the very first time. I am going to paste in the instructions
to a practice problem that my professor gave me to try before class.
Please be my kind tutor and walk me through how to solve the problem step
by step.

Don't just give me the full solution all at once (unless I later ask for
it). Instead, help me work through it gradually, with clear explanations
and small, easy-to-understand examples. Please use everyday language and
explain things in a simple, friendly way.

INSTRUCTIONS:
-------------
Update and delete records using Peewee and SQLite.

1. Import the following from peewee:
   SqliteDatabase, Model, AutoField, TextField, IntegerField, BooleanField

2. Create a database using:
   db = SqliteDatabase('tasks.db')

3. Define a Task model with:
   - id (AutoField)
   - description (TextField)
   - priority (IntegerField)
   - done (BooleanField, default should be False)

4. Inside the Task model, set Meta.database = db

5. Connect to the database and create the Task table

6. Add a few sample tasks using Task.create() if the table is empty

7. Update the task with id = 1 and set its done value to True

8. Delete the task with id = 2

9. Loop through all remaining tasks and print their id, description,
   priority, and done status
'''

# Here is one potential solution. Remember there are often many different
# ways to solve a problem, so your solution may not look exactly the same.

from peewee import SqliteDatabase, Model, AutoField, TextField, IntegerField, BooleanField

# Initialize the database
db = SqliteDatabase('tasks.db')

# Define the Task model
class Task(Model):
    id = AutoField()
    description = TextField()
    priority = IntegerField()
    done = BooleanField(default=False)

    class Meta:
        database = db

# Connect to the database and ensure the table exists
db.connect()
db.create_tables([Task])

# Add sample data (only if the table is empty)
if Task.select().count() == 0:
    Task.create(description='Buy groceries', priority=3)
    Task.create(description='Do laundry', priority=2)
    Task.create(description='Read a book', priority=1)

# Update the task with id=1 to be marked as done
Task.update(done=True).where(Task.id == 1).execute()

# Delete the task with id=2
Task.delete().where(Task.id == 2).execute()

# Print all remaining tasks
for t in Task.select():
    print(t.id, t.description, t.priority, t.done)
