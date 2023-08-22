import sqlite3
conn = sqlite3.connect('vin.db') 
c = conn.cursor()

# c.execute('''
#            CREATE TABLE IF NOT EXISTS students
#            ([student_id] INTEGER PRIMARY KEY, [student_name] TEXT)
#           ''')

# c.execute('''
#       CREATE TABLE IF NOT EXISTS teachers
#       ([teacher_id] INTEGER PRIMARY KEY,[teacher_name] TEXT)
#           ''')


c.execute('''
          INSERT INTO students (student_id, student_name)

                VALUES
                (1,'vincent'),
                (2,'Jmaes'),
                (3,'Mwangi'),
                (4,'Faith'),
                (5,'Alvin')
          ''')
c.execute('''
          INSERT INTO teachers (teacher_id, teacher_name)

                VALUES
                (1,'Joho'),
                (2,'Mohammed'),
                (3,'Richard'),
                (4,'Dante'),
                (5,'Msengez')
          ''')



conn.commit()