import sqlite3

def seed_database(db_path="healthcare.db"):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Create doctors table
    c.execute('''
    CREATE TABLE IF NOT EXISTS doctors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        specialty TEXT NOT NULL,
        photo TEXT
    )
    ''')

    # Create appointments table
    c.execute('''
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        date TEXT NOT NULL,
        time TEXT NOT NULL,
        doctor TEXT NOT NULL
    )
    ''')

    # Seed doctors
    c.execute('DELETE FROM doctors')
    doctors = [
        ('Dr. Alice Smith', 'General Physician', '/static/images/doctors/alice.png'),
        ('Dr. Bob Lee', 'Pediatrician', '/static/images/doctors/bob.png'),
        ('Dr. Carol White', 'Dermatologist', '/static/images/doctors/carol.png')
    ]
    c.executemany('INSERT INTO doctors (name, specialty, photo) VALUES (?, ?, ?)', doctors)

    # Seed appointments (empty for demo)
    c.execute('DELETE FROM appointments')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    seed_database()