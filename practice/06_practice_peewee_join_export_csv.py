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
Export album and artist data from a database to an Excel file
using Peewee and Pandas.

1. Import pandas and the needed classes from peewee:
   SqliteDatabase, Model, AutoField, TextField, ForeignKeyField

2. Create a database using:
   db = SqliteDatabase('music.db')

3. Define an Artist model with:
   - id (AutoField)
   - name (TextField)
   - Set Meta.database = db

4. Define an Album model with:
   - id (AutoField)
   - title (TextField)
   - artist (ForeignKeyField linked to Artist, use backref='albums')
   - Set Meta.database = db

5. Loop through all Album records joined with Artist and collect the
   data into a list of dictionaries with keys 'artist' and 'title'

6. Create a Pandas DataFrame from that list

7. Use DataFrame.to_excel() to export the data to an Excel file
   called 'artist_albums.xlsx'
'''


