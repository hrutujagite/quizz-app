from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a secure secret key

# Database initialization
def init_db():
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    
    # Create users table with subject-specific scores
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT NOT NULL,
                  subject TEXT NOT NULL,
                  score INTEGER DEFAULT 0,
                  UNIQUE(username, subject))''')
    
    # Create questions table
    c.execute('''CREATE TABLE IF NOT EXISTS questions
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  question TEXT NOT NULL,
                  option1 TEXT NOT NULL,
                  option2 TEXT NOT NULL,
                  option3 TEXT NOT NULL,
                  option4 TEXT NOT NULL,
                  correct_answer TEXT NOT NULL,
                  subject TEXT NOT NULL)''')
    
    # Check if subject column exists in users table
    c.execute("PRAGMA table_info(users)")
    columns = [column[1] for column in c.fetchall()]
    if 'subject' not in columns:
        # Create a new table with the correct schema
        c.execute('''CREATE TABLE users_new 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     username TEXT NOT NULL,
                     subject TEXT NOT NULL,
                     score INTEGER DEFAULT 0,
                     UNIQUE(username, subject))''')
        # Copy existing data if any
        c.execute('INSERT INTO users_new (username, subject, score) SELECT username, "General", score FROM users')
        # Drop old table and rename new one
        c.execute('DROP TABLE users')
        c.execute('ALTER TABLE users_new RENAME TO users')
    
    conn.commit()
    conn.close()

# Initialize database
if not os.path.exists('quiz.db'):
    init_db()
else:
    # Check and update existing database
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    c.execute("PRAGMA table_info(users)")
    columns = [column[1] for column in c.fetchall()]
    if 'subject' not in columns:
        # Create a new table with the correct schema
        c.execute('''CREATE TABLE users_new 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     username TEXT NOT NULL,
                     subject TEXT NOT NULL,
                     score INTEGER DEFAULT 0,
                     UNIQUE(username, subject))''')
        # Copy existing data if any
        c.execute('INSERT INTO users_new (username, subject, score) SELECT username, "General", score FROM users')
        # Drop old table and rename new one
        c.execute('DROP TABLE users')
        c.execute('ALTER TABLE users_new RENAME TO users')
        conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        subject = request.form.get('subject')
        if username and subject:
            session['username'] = username
            session['subject'] = subject
            return redirect(url_for('quiz'))
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    if 'subject' not in session or 'username' not in session:
        return redirect(url_for('index'))
    
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    
    try:
        # Get questions for the selected subject
        c.execute('''SELECT id, question, option1, option2, option3, option4, correct_answer 
                    FROM questions 
                    WHERE subject = ?''', (session['subject'],))
        questions = c.fetchall()
        
        if not questions:
            # If no questions found, redirect to index with a message
            flash('No questions available for this subject yet.')
            return redirect(url_for('index'))
            
        return render_template('quiz.html', 
                             questions=questions, 
                             subject=session['subject'])
                             
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        flash('An error occurred while loading the quiz.')
        return redirect(url_for('index'))
        
    finally:
        conn.close()

@app.route('/result', methods=['POST'])
def result():
    if 'subject' not in session or 'username' not in session:
        return redirect(url_for('index'))
        
    score = 0
    total = 0
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    
    # Get all questions and their correct answers for the current subject
    c.execute('SELECT id, correct_answer FROM questions WHERE subject = ?', (session['subject'],))
    correct_answers = dict(c.fetchall())
    
    # Compare submitted answers with correct answers
    for question_id, correct_answer in correct_answers.items():
        answer_key = f'question_{question_id}'
        if answer_key in request.form:
            total += 1
            submitted_answer = request.form[answer_key]
            # Convert both to strings for comparison
            if str(submitted_answer) == str(correct_answer):
                score += 1
    
    # Update or insert user's score for the specific subject
    c.execute('''INSERT OR REPLACE INTO users (username, subject, score) 
                VALUES (?, ?, ?)''',
             (session['username'], session['subject'], score))
    conn.commit()
    
    conn.close()
    percentage = (score / total * 100) if total > 0 else 0
    return render_template('result.html', score=score, total=total, percentage=percentage, subject=session['subject'])

@app.route('/leaderboard', methods=['GET', 'POST'])
def leaderboard():
    # Get subject from form submission or query parameter
    subject = request.form.get('subject') or request.args.get('subject')
    
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    
    # Get all available subjects from users table
    c.execute('SELECT DISTINCT subject FROM users')
    available_subjects = [row[0] for row in c.fetchall()]
    
    # If no subjects found in users table, get them from questions table
    if not available_subjects:
        c.execute('SELECT DISTINCT subject FROM questions')
        available_subjects = [row[0] for row in c.fetchall()]
    
    # If no subject selected, use the first available subject
    if not subject and available_subjects:
        subject = available_subjects[0]
    
    # Get top 10 users for the selected subject
    if subject:
        try:
            # First get all scores for the subject
            c.execute('''SELECT username, score 
                        FROM users 
                        WHERE subject = ?
                        ORDER BY score DESC, username ASC''', (subject,))
            all_scores = c.fetchall()
            
            # Calculate ranks manually
            leaderboard_data = []
            current_rank = 1
            prev_score = None
            for i, (username, score) in enumerate(all_scores, 1):
                if score != prev_score:
                    current_rank = i
                leaderboard_data.append((username, score, current_rank))
                prev_score = score
                if i >= 10:  # Limit to top 10
                    break
        except sqlite3.OperationalError as e:
            print(f"Database error: {e}")
            leaderboard_data = []
    else:
        leaderboard_data = []
    
    conn.close()
    
    return render_template('leaderboard.html', 
                         leaderboard=leaderboard_data,
                         subjects=available_subjects,
                         selected_subject=subject)

if __name__ == '__main__':
    app.run(debug=True) 