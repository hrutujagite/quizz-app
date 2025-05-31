import sqlite3

def create_questions_table():
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    
    # Drop existing questions table if it exists
    c.execute('DROP TABLE IF EXISTS questions')
    
    # Create new questions table with subject field
    c.execute('''CREATE TABLE questions
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  subject TEXT NOT NULL,
                  question TEXT NOT NULL,
                  option_a TEXT NOT NULL,
                  option_b TEXT NOT NULL,
                  option_c TEXT NOT NULL,
                  option_d TEXT NOT NULL,
                  correct_option TEXT NOT NULL)''')
    
    conn.commit()
    conn.close()

def insert_questions():
    questions = [
        # Computer Networks (CN) Questions
        {
            'subject': 'CN',
            'question': 'What is the full form of TCP?',
            'option_a': 'Transmission Control Protocol',
            'option_b': 'Transfer Control Protocol',
            'option_c': 'Transmission Control Process',
            'option_d': 'Transfer Control Process',
            'correct_option': 'A'
        },
        {
            'subject': 'CN',
            'question': 'Which layer of OSI model is responsible for routing?',
            'option_a': 'Physical Layer',
            'option_b': 'Data Link Layer',
            'option_c': 'Network Layer',
            'option_d': 'Transport Layer',
            'correct_option': 'C'
        },
        {
            'subject': 'CN',
            'question': 'What is the default port number for HTTP?',
            'option_a': '80',
            'option_b': '443',
            'option_c': '21',
            'option_d': '25',
            'correct_option': 'A'
        },
        {
            'subject': 'CN',
            'question': 'Which protocol is used for secure communication over the internet?',
            'option_a': 'HTTP',
            'option_b': 'FTP',
            'option_c': 'HTTPS',
            'option_d': 'SMTP',
            'correct_option': 'C'
        },
        {
            'subject': 'CN',
            'question': 'What is the purpose of DNS?',
            'option_a': 'To provide security',
            'option_b': 'To convert domain names to IP addresses',
            'option_c': 'To manage email servers',
            'option_d': 'To handle file transfers',
            'correct_option': 'B'
        },

        # Operating Systems (OS) Questions
        {
            'subject': 'OS',
            'question': 'What is the main purpose of an operating system?',
            'option_a': 'To manage hardware resources',
            'option_b': 'To create documents',
            'option_c': 'To browse the internet',
            'option_d': 'To play games',
            'correct_option': 'A'
        },
        {
            'subject': 'OS',
            'question': 'Which scheduling algorithm provides the shortest average waiting time?',
            'option_a': 'FCFS',
            'option_b': 'SJF',
            'option_c': 'Round Robin',
            'option_d': 'Priority',
            'correct_option': 'B'
        },
        {
            'subject': 'OS',
            'question': 'What is virtual memory?',
            'option_a': 'A type of RAM',
            'option_b': 'A memory management technique',
            'option_c': 'A storage device',
            'option_d': 'A type of cache',
            'correct_option': 'B'
        },
        {
            'subject': 'OS',
            'question': 'Which of these is not a process state?',
            'option_a': 'Ready',
            'option_b': 'Running',
            'option_c': 'Waiting',
            'option_d': 'Sleeping',
            'correct_option': 'D'
        },
        {
            'subject': 'OS',
            'question': 'What is the purpose of a page table?',
            'option_a': 'To store file information',
            'option_b': 'To map virtual addresses to physical addresses',
            'option_c': 'To manage CPU scheduling',
            'option_d': 'To handle interrupts',
            'correct_option': 'B'
        },

        # Database Management Systems (DBMS) Questions
        {
            'subject': 'DBMS',
            'question': 'What is a primary key?',
            'option_a': 'A foreign key in another table',
            'option_b': 'A unique identifier for a record',
            'option_c': 'A type of index',
            'option_d': 'A constraint on data type',
            'correct_option': 'B'
        },
        {
            'subject': 'DBMS',
            'question': 'Which normal form eliminates partial dependencies?',
            'option_a': '1NF',
            'option_b': '2NF',
            'option_c': '3NF',
            'option_d': 'BCNF',
            'correct_option': 'B'
        },
        {
            'subject': 'DBMS',
            'question': 'What is ACID in database transactions?',
            'option_a': 'A database design principle',
            'option_b': 'A set of properties for reliable transactions',
            'option_c': 'A type of database',
            'option_d': 'A query optimization technique',
            'correct_option': 'B'
        },
        {
            'subject': 'DBMS',
            'question': 'Which SQL command is used to modify data?',
            'option_a': 'SELECT',
            'option_b': 'INSERT',
            'option_c': 'UPDATE',
            'option_d': 'DELETE',
            'correct_option': 'C'
        },
        {
            'subject': 'DBMS',
            'question': 'What is a foreign key?',
            'option_a': 'A primary key in another table',
            'option_b': 'A unique identifier',
            'option_c': 'A type of index',
            'option_d': 'A constraint on data type',
            'correct_option': 'A'
        },

        # Analysis of Algorithms (AOA) Questions
        {
            'subject': 'AOA',
            'question': 'What is the time complexity of binary search?',
            'option_a': 'O(n)',
            'option_b': 'O(log n)',
            'option_c': 'O(n log n)',
            'option_d': 'O(n²)',
            'correct_option': 'B'
        },
        {
            'subject': 'AOA',
            'question': 'Which sorting algorithm has the best average case time complexity?',
            'option_a': 'Bubble Sort',
            'option_b': 'Insertion Sort',
            'option_c': 'Quick Sort',
            'option_d': 'Selection Sort',
            'correct_option': 'C'
        },
        {
            'subject': 'AOA',
            'question': 'What is the space complexity of merge sort?',
            'option_a': 'O(1)',
            'option_b': 'O(n)',
            'option_c': 'O(log n)',
            'option_d': 'O(n²)',
            'correct_option': 'B'
        },
        {
            'subject': 'AOA',
            'question': 'Which data structure is best for implementing a priority queue?',
            'option_a': 'Array',
            'option_b': 'Linked List',
            'option_c': 'Heap',
            'option_d': 'Stack',
            'correct_option': 'C'
        },
        {
            'subject': 'AOA',
            'question': 'What is the time complexity of Dijkstra\'s algorithm?',
            'option_a': 'O(V²)',
            'option_b': 'O(V log V)',
            'option_c': 'O(V + E)',
            'option_d': 'O(E log V)',
            'correct_option': 'D'
        }
    ]

    try:
        conn = sqlite3.connect('quiz.db')
        c = conn.cursor()

        for q in questions:
            c.execute('''INSERT INTO questions 
                        (subject, question, option_a, option_b, option_c, option_d, correct_option)
                        VALUES (?, ?, ?, ?, ?, ?, ?)''',
                     (q['subject'], q['question'], q['option_a'], q['option_b'],
                      q['option_c'], q['option_d'], q['correct_option']))

        conn.commit()
        print("Questions inserted successfully!")
        
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    create_questions_table()
    insert_questions() 