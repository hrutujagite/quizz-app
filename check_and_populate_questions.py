import sqlite3
import os

def create_tables(conn):
    c = conn.cursor()
    
    # Create questions table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS questions
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  question TEXT NOT NULL,
                  option1 TEXT NOT NULL,
                  option2 TEXT NOT NULL,
                  option3 TEXT NOT NULL,
                  option4 TEXT NOT NULL,
                  correct_answer TEXT NOT NULL,
                  subject TEXT)''')
    
    conn.commit()

def check_and_populate_questions():
    try:
        # Create database if it doesn't exist
        if not os.path.exists('quiz.db'):
            print("Database file not found. Creating new database...")
            conn = sqlite3.connect('quiz.db')
            create_tables(conn)
            print("Database and tables created successfully!")
        else:
            conn = sqlite3.connect('quiz.db')
            print("Existing database found.")
        
        c = conn.cursor()
        
        # Check if subject column exists
        c.execute("PRAGMA table_info(questions)")
        columns = [column[1] for column in c.fetchall()]
        
        if 'subject' not in columns:
            print("Adding 'subject' column to questions table...")
            c.execute('ALTER TABLE questions ADD COLUMN subject TEXT')
            conn.commit()
            print("'subject' column added successfully!")
        else:
            print("'subject' column already exists in questions table")
        
        # Clear existing questions
        print("Clearing existing questions...")
        c.execute('DELETE FROM questions')
        conn.commit()
        print("Existing questions cleared.")
        
        # Insert all questions using executemany
        print("Adding new questions...")
        questions = [
            # CN Questions
            ("What does HTTP stand for?", "HyperText Transfer Protocol", "Hyperlink Transfer Protocol", "HighText Transfer Protocol", "Hyper Transfer Text Protocol", "1", "CN"),
            ("Which layer in OSI model is responsible for routing?", "Physical", "Data Link", "Network", "Transport", "3", "CN"),
            ("Which device connects two different networks?", "Hub", "Switch", "Router", "Repeater", "3", "CN"),
            ("Which protocol is used to find MAC address?", "IP", "ARP", "RARP", "TCP", "2", "CN"),
            ("Port number of HTTP?", "80", "21", "23", "110", "1", "CN"),
            ("Which protocol is connection-oriented?", "UDP", "IP", "TCP", "ARP", "3", "CN"),
            ("Which of the following is a transport layer protocol?", "FTP", "SMTP", "TCP", "DNS", "3", "CN"),
            ("What is the size of an IPv4 address?", "32 bits", "64 bits", "128 bits", "256 bits", "1", "CN"),
            ("What does DNS do?", "Translate domain to IP", "Transfer files", "Secure connection", "Route packets", "1", "CN"),
            ("Which layer encrypts data?", "Network", "Session", "Presentation", "Application", "3", "CN"),

            # OS Questions
            ("What is a process in OS?", "Program in execution", "Instruction", "Data structure", "Service", "1", "OS"),
            ("Which is not a type of scheduler?", "Long-term", "Short-term", "Medium-term", "Extra-term", "4", "OS"),
            ("What is thrashing?", "Disk error", "Excessive swapping", "Power failure", "Memory leak", "2", "OS"),
            ("Which algorithm avoids starvation?", "FCFS", "SJF", "Round Robin", "LIFO", "3", "OS"),
            ("What is a deadlock?", "A memory issue", "Process waiting forever", "CPU halt", "Device failure", "2", "OS"),
            ("Which is not a page replacement algorithm?", "LRU", "FIFO", "Optimal", "FastPage", "4", "OS"),
            ("Kernel is:", "Part of hardware", "Part of software", "Interface", "Compiler", "2", "OS"),
            ("Which is not an OS?", "Linux", "Windows", "Oracle", "macOS", "3", "OS"),
            ("Which system call creates a process?", "fork()", "exec()", "wait()", "exit()", "1", "OS"),
            ("What is segmentation?", "Divide process", "Divide memory", "Page fault", "Queue", "2", "OS"),

            # AOA Questions
            ("Which algorithm is used for sorting?", "DFS", "BFS", "Merge Sort", "Dijkstra", "3", "AOA"),
            ("What is time complexity of binary search?", "O(n)", "O(log n)", "O(n log n)", "O(1)", "2", "AOA"),
            ("What is greedy algorithm?", "Chooses optimal each step", "Backtracks", "Random guess", "Iterates full", "1", "AOA"),
            ("Which algorithm finds shortest path?", "Prim's", "Kruskal's", "Dijkstra's", "DFS", "3", "AOA"),
            ("What is dynamic programming?", "Top-down with memo", "Divide and conquer", "Greedy method", "Random", "1", "AOA"),
            ("What does DFS stand for?", "Depth First Search", "Data File System", "Dynamic Function", "Direct Form Search", "1", "AOA"),
            ("What is time complexity of Quick Sort average case?", "O(n)", "O(n^2)", "O(n log n)", "O(log n)", "3", "AOA"),
            ("Which algorithm is used in MST?", "Dijkstra", "Bellman-Ford", "Kruskal", "Floyd-Warshall", "3", "AOA"),
            ("What is backtracking?", "Try all possibilities", "Dynamic programming", "Greedy method", "Divide and Conquer", "1", "AOA"),
            ("What is the purpose of Big O notation?", "Measure time/memory", "Data structure", "System call", "Error", "1", "AOA"),

            # DBMS Questions
            ("Which key uniquely identifies a record?", "Primary key", "Foreign key", "Super key", "Composite key", "1", "DBMS"),
            ("Which command is used to delete all records?", "DELETE", "REMOVE", "TRUNCATE", "ERASE", "3", "DBMS"),
            ("What is normalization?", "Remove redundancy", "Add keys", "Delete data", "Indexing", "1", "DBMS"),
            ("Which is not a SQL command?", "SELECT", "INSERT", "REMOVE", "UPDATE", "3", "DBMS"),
            ("Which of the following is DDL?", "SELECT", "INSERT", "DELETE", "CREATE", "4", "DBMS"),
            ("What is foreign key?", "Unique identifier", "Links tables", "Auto increment", "Primary key", "2", "DBMS"),
            ("Which JOIN returns common records?", "LEFT JOIN", "RIGHT JOIN", "FULL JOIN", "INNER JOIN", "4", "DBMS"),
            ("What is ACID in DBMS?", "Atomicity, Consistency, Isolation, Durability", "Accuracy, Clarity, Integrity, Data", "All Conditions in Data", "None", "1", "DBMS"),
            ("Which SQL keyword is used to filter?", "WHERE", "ORDER", "FILTER", "SORT", "1", "DBMS"),
            ("What is the use of GROUP BY?", "Group rows by column", "Sort rows", "Filter data", "Update values", "1", "DBMS")
        ]
        
        c.executemany('''INSERT INTO questions 
                        (question, option1, option2, option3, option4, correct_answer, subject)
                        VALUES (?, ?, ?, ?, ?, ?, ?)''', questions)
        conn.commit()
        print("All questions added successfully!")
        
        # Print question counts for each subject
        print("\nQuestion counts by subject:")
        subjects = ['CN', 'OS', 'DBMS', 'AOA']
        for subject in subjects:
            c.execute('SELECT COUNT(*) FROM questions WHERE subject = ?', (subject,))
            count = c.fetchone()[0]
            print(f"{subject}: {count} questions")
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    check_and_populate_questions() 