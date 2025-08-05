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
Create a music database using Peewee and SQLite with two models:
Artist and Album.

1. Import the following from peewee:
   SqliteDatabase, Model, AutoField, TextField, ForeignKeyField

2. Create a database using:
   db = SqliteDatabase('music.db')

3. Define an Artist model that inherits from Model. It should include:
   - An AutoField for the artist id
   - A TextField for the artist name

4. Inside the Artist model, define a Meta class and set database = db

5. Define an Album model that also inherits from Model. It should include:
   - An AutoField for the album id
   - A TextField for the album title
   - A ForeignKeyField that links to Artist
     (use backref='albums' to allow reverse access)

6. Inside the Album model, define a Meta class and set database = db

7. Connect to the database using:
   db.connect()

8. Create both tables using:
   db.create_tables([Artist, Album])

9. Create artist records using Artist.create():
   - One with the name 'Beatles'
   - One with the name 'Queen'
   - Save the results to variables so they can be used later

10. Create album records using Album.create() and link each to the
    appropriate artist:
    - Add two albums for the Beatles
    - Add two albums for Queen

11. Print a message like: "Albums by The Beatles:"

12. Loop through all Album records where artist is the Beatles and
    print each album title
'''

# Here is one potential solution. Remember there are often many different
# ways to solve a problem, so your solution may not look exactly the same.

from peewee import SqliteDatabase, Model, AutoField, TextField, ForeignKeyField

# Initialize the database
db = SqliteDatabase('music.db')

# Define the Artist model
class Artist(Model):
    id = AutoField()
    name = TextField()

    class Meta:
        database = db

# Define the Album model
class Album(Model):
    id = AutoField()
    title = TextField()
    artist = ForeignKeyField(Artist, backref='albums')

    class Meta:
        database = db

# Connect and create tables
db.connect()
db.create_tables([Artist, Album])

# Create artist records
beatles = Artist.create(name='Beatles')
queen = Artist.create(name='Queen')

# Create album records
Album.create(title='Abbey Road', artist=beatles)
Album.create(title='Let It Be', artist=beatles)
Album.create(title='A Night at the Opera', artist=queen)
Album.create(title='News of the World', artist=queen)

# Query and print albums by The Beatles
print("Albums by The Beatles:")
for al in Album.select().where(Album.artist == beatles):
    print(al.title)
