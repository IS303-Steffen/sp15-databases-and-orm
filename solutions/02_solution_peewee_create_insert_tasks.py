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
Using Peewee, create tasks.db. Define a Task model with:
    - id (AutoField)
    - description (TextField)
    - priority (IntegerField)
    - done (BooleanField) (with a default value of False)
    
Insert three tasks and print all rows.
'''

# Here is one potential solution. Remember there are often many different
# ways to solve a problem, so your solution may not look exactly the same.

from peewee import SqliteDatabase, Model, AutoField, TextField, IntegerField, BooleanField

db = SqliteDatabase('tasks.db')

class Task(Model):
    id = AutoField()
    description = TextField()
    priority = IntegerField()
    done = BooleanField(default = False)
    
    class Meta:
       database = db

db.connect(); db.create_tables([Task])

Task.create(description='Write report', priority = 3)
Task.create(description='Clean desk', priority = 2)
Task.create(description='Plan trip', priority = 4)

for t in Task.select():
    print(t.id, t.description, t.priority, t.done)
