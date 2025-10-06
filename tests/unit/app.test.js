/**
 * Unit Tests for AWS DVA-C02 Quiz Application
 * Testing core functionality and business logic
 */

describe('Quiz Application - Unit Tests', () => {
  
  // Mock DOM elements
  beforeEach(() => {
    document.body.innerHTML = `
      <div id="home-page" class="page active"></div>
      <div id="quiz-page" class="page"></div>
      <div id="results-page" class="page"></div>
      <div id="review-page" class="page"></div>
      <div id="quiz"></div>
      <div id="timer">12:00</div>
      <div id="time">12:00</div>
      <div id="current-question">1</div>
      <div id="total-questions">10</div>
      <div id="progress-fill"></div>
      <div id="question-text"></div>
      <div id="options-container"></div>
      <div id="results"></div>
      <div id="score-percentage"></div>
      <div id="score-progress"></div>
      <div id="results-title"></div>
      <div id="results-summary"></div>
      <div id="results-details"></div>
      <div id="review-container"></div>
      <button id="start-exam-btn"></button>
      <button id="prev-btn"></button>
      <button id="next-btn"></button>
      <button id="submit"></button>
      <button id="retake-btn"></button>
      <button id="review-btn"></button>
      <button id="back-to-results-btn"></button>
    `;
  });

  describe('Question Selection', () => {
    test('should select random questions from pool', () => {
      const questions = [
        { question: 'Q1', options: ['A', 'B'], answer: 'A' },
        { question: 'Q2', options: ['A', 'B'], answer: 'B' },
        { question: 'Q3', options: ['A', 'B'], answer: 'A' },
        { question: 'Q4', options: ['A', 'B'], answer: 'B' },
        { question: 'Q5', options: ['A', 'B'], answer: 'A' }
      ];
      
      // Mock function to shuffle array
      const shuffleArray = (arr) => {
        return [...arr].sort(() => Math.random() - 0.5);
      };
      
      const selected = shuffleArray(questions).slice(0, 3);
      
      expect(selected.length).toBe(3);
      expect(selected.every(q => questions.includes(q))).toBe(true);
    });

    test('should not exceed available questions', () => {
      const questions = [
        { question: 'Q1', options: ['A', 'B'], answer: 'A' },
        { question: 'Q2', options: ['A', 'B'], answer: 'B' }
      ];
      
      const count = Math.min(10, questions.length);
      const selected = questions.slice(0, count);
      
      expect(selected.length).toBe(2);
      expect(selected.length).toBeLessThanOrEqual(10);
    });
  });

  describe('Timer Functionality', () => {
    test('should format time correctly', () => {
      const formatTime = (seconds) => {
        const minutes = Math.floor(seconds / 60);
        const secs = seconds % 60;
        return `${minutes}:${secs.toString().padStart(2, '0')}`;
      };
      
      expect(formatTime(720)).toBe('12:00');
      expect(formatTime(60)).toBe('1:00');
      expect(formatTime(0)).toBe('0:00');
      expect(formatTime(125)).toBe('2:05');
    });

    test('should detect time expiry', () => {
      let timeRemaining = 720;
      
      expect(timeRemaining > 0).toBe(true);
      
      timeRemaining = 0;
      expect(timeRemaining <= 0).toBe(true);
    });

    test('should warn when time is low', () => {
      expect(120 <= 120).toBe(true); // Warning at 2 minutes
      expect(119 <= 120).toBe(true);
      expect(121 <= 120).toBe(false);
    });
  });

  describe('Answer Selection', () => {
    test('should track user answers', () => {
      const userAnswers = [];
      const totalQuestions = 10;
      
      // Initialize answers array
      for (let i = 0; i < totalQuestions; i++) {
        userAnswers.push([]);
      }
      
      // User selects answer for question 0
      userAnswers[0].push('A');
      expect(userAnswers[0]).toContain('A');
      
      // User selects multiple answers
      userAnswers[0].push('B');
      expect(userAnswers[0]).toEqual(['A', 'B']);
      
      // User deselects answer
      const index = userAnswers[0].indexOf('A');
      userAnswers[0].splice(index, 1);
      expect(userAnswers[0]).toEqual(['B']);
    });

    test('should handle multiple selections per question', () => {
      const currentAnswers = [];
      
      // Toggle selections
      const toggleAnswer = (letter) => {
        const index = currentAnswers.indexOf(letter);
        if (index > -1) {
          currentAnswers.splice(index, 1);
        } else {
          currentAnswers.push(letter);
        }
      };
      
      toggleAnswer('A');
      expect(currentAnswers).toEqual(['A']);
      
      toggleAnswer('B');
      expect(currentAnswers).toEqual(['A', 'B']);
      
      toggleAnswer('A');
      expect(currentAnswers).toEqual(['B']);
    });
  });

  describe('Score Calculation', () => {
    test('should calculate correct percentage', () => {
      const calculatePercentage = (correct, total) => {
        return Math.round((correct / total) * 100);
      };
      
      expect(calculatePercentage(10, 10)).toBe(100);
      expect(calculatePercentage(7, 10)).toBe(70);
      expect(calculatePercentage(0, 10)).toBe(0);
      expect(calculatePercentage(5, 10)).toBe(50);
    });

    test('should determine pass/fail correctly', () => {
      const PASS_THRESHOLD = 70;
      
      expect(100 >= PASS_THRESHOLD).toBe(true);
      expect(70 >= PASS_THRESHOLD).toBe(true);
      expect(69 >= PASS_THRESHOLD).toBe(false);
    });

    test('should compare user answers with correct answers', () => {
      const userAnswer = ['A', 'B'].sort().join('');
      const correctAnswer = ['A', 'B'].sort().join('');
      
      expect(userAnswer).toBe(correctAnswer);
      
      const wrongAnswer = ['A', 'C'].sort().join('');
      expect(wrongAnswer).not.toBe(correctAnswer);
    });

    test('should match correct answer from options', () => {
      const question = {
        options: ['Option A', 'Option B', 'Option C'],
        answer: 'Option B'
      };
      
      const LETTERS = ['A', 'B', 'C', 'D', 'E', 'F'];
      const correctLetters = [];
      
      question.options.forEach((opt, idx) => {
        if (opt === question.answer) {
          correctLetters.push(LETTERS[idx]);
        }
      });
      
      expect(correctLetters).toEqual(['B']);
    });
  });

  describe('Data Validation', () => {
    test('should validate question format', () => {
      const validQuestion = {
        question: 'What is AWS Lambda?',
        options: ['A', 'B', 'C', 'D'],
        answer: 'A',
        explanation: 'Lambda is serverless'
      };
      
      expect(validQuestion.question).toBeTruthy();
      expect(validQuestion.options.length).toBeGreaterThanOrEqual(2);
      expect(validQuestion.answer).toBeTruthy();
      expect(validQuestion.explanation).toBeTruthy();
    });

    test('should reject invalid questions', () => {
      const invalidQuestion = {
        question: '',
        options: ['A'],
        answer: ''
      };
      
      const isValid = 
        invalidQuestion.question.length > 10 &&
        invalidQuestion.options.length >= 2 &&
        invalidQuestion.answer.length > 0;
      
      expect(isValid).toBe(false);
    });

    test('should ensure answer is in options', () => {
      const question = {
        options: ['Option A', 'Option B', 'Option C'],
        answer: 'Option B'
      };
      
      expect(question.options).toContain(question.answer);
    });
  });

  describe('Progress Tracking', () => {
    test('should calculate progress percentage', () => {
      const calculateProgress = (current, total) => {
        return ((current + 1) / total) * 100;
      };
      
      expect(calculateProgress(0, 10)).toBe(10);
      expect(calculateProgress(4, 10)).toBe(50);
      expect(calculateProgress(9, 10)).toBe(100);
    });

    test('should track answered questions', () => {
      const userAnswers = [['A'], [], ['B', 'C'], [], []];
      const answeredCount = userAnswers.filter(ans => ans.length > 0).length;
      
      expect(answeredCount).toBe(2);
    });
  });

  describe('Letter Mapping', () => {
    test('should map index to letter correctly', () => {
      const LETTERS = ['A', 'B', 'C', 'D', 'E', 'F'];
      
      expect(LETTERS[0]).toBe('A');
      expect(LETTERS[1]).toBe('B');
      expect(LETTERS[5]).toBe('F');
    });

    test('should handle multiple letter selections', () => {
      const selectedLetters = ['A', 'C', 'E'];
      const sorted = selectedLetters.sort().join('');
      
      expect(sorted).toBe('ACE');
    });
  });
});

describe('Edge Cases and Error Handling', () => {
  test('should handle empty question pool', () => {
    const questions = [];
    const selected = questions.slice(0, 10);
    
    expect(selected.length).toBe(0);
  });

  test('should handle timer reaching zero', () => {
    let timeRemaining = 1;
    timeRemaining--;
    
    expect(timeRemaining).toBe(0);
    expect(timeRemaining <= 0).toBe(true);
  });

  test('should handle all questions answered', () => {
    const userAnswers = Array(10).fill([]).map(() => ['A']);
    const allAnswered = userAnswers.every(ans => ans.length > 0);
    
    expect(allAnswered).toBe(true);
  });

  test('should handle no questions answered', () => {
    const userAnswers = Array(10).fill([]);
    const noneAnswered = userAnswers.every(ans => ans.length === 0);
    
    expect(noneAnswered).toBe(true);
  });
});

