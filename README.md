# 🧠 Quiz App

A simple and interactive quiz web application built using **HTML**, **CSS**, and **JavaScript**. This project allows users to answer multiple-choice questions and get instant feedback, making it ideal for educational and self-assessment purposes.

## 🚀 Features

- ✅ Interactive multiple-choice questions
- ✅ Instant feedback on answer selection
- ✅ Score tracking
- ✅ Easy to customize questions
- ✅ Responsive UI for basic screen sizes

## 📁 Project Structure

quizz-app/
├── index.html # Main HTML structure
├── style.css # Styling for the quiz interface
├── script.js # JavaScript logic for quiz functionality
└── README.md # Project documentation


## 🛠️ How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/hrutujagite/quizz-app.git
   cd quizz-app
Open index.html

Use any modern browser (Chrome, Firefox, etc.)

Right-click and select “Open with Live Server” (if using VS Code + Live Server extension)

📌 Customization


To add your own questions, modify the questions array in script.js:
const questions = [
  {
    question: "What is 2 + 2?",
    answers: [
      { text: "4", correct: true },
      { text: "3", correct: false },
      { text: "5", correct: false },
      { text: "6", correct: false }
    ]
  },
  // Add more questions here
];

💡 Future Enhancements
Add timer functionality

Implement result storage using localStorage or backend

Add difficulty levels

Improve mobile responsiveness

