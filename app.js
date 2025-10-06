// Application State
let selectedCertification = null;
let allQuestions = [];
let currentExam = [];
let currentQuestionIndex = 0;
let userAnswers = []; // Array of arrays for multiple selections
let timerInterval = null;
let timeRemaining = 720; // 12 minutes in seconds
const LETTERS = ['A', 'B', 'C', 'D', 'E', 'F'];

// Certification configurations
const CERTIFICATIONS = {
    'aws-developer': {
        name: 'AWS Certified Developer - Associate',
        code: 'DVA-C02',
        questionsFile: 'questions_aws_developer.json',
        description: 'DVA-C02 Certification Practice Exams',
        color: '#FF9900',
        provider: 'AWS'
    },
    'aws-ai': {
        name: 'AWS Certified AI Practitioner',
        code: 'AIF-C01',
        questionsFile: 'questions_aws_ai.json',
        description: 'AIF-C01 Certification Practice Exams',
        color: '#8B5CF6',
        provider: 'AWS'
    },
    'azure-developer': {
        name: 'Microsoft Certified: Azure Developer Associate',
        code: 'AZ-204',
        questionsFile: 'questions_azure_developer.json',
        description: 'AZ-204 Certification Practice Exams',
        color: '#0078D4',
        provider: 'Azure'
    },
    'azure-ai': {
        name: 'Microsoft Certified: Azure AI Engineer Associate',
        code: 'AI-102',
        questionsFile: 'questions_azure_ai.json',
        description: 'AI-102 Certification Practice Exams',
        color: '#00A4EF',
        provider: 'Azure'
    }
};

// DOM Elements
const pages = {
    certSelection: document.getElementById('cert-selection-page'),
    home: document.getElementById('home-page'),
    quiz: document.getElementById('quiz-page'),
    results: document.getElementById('results-page'),
    review: document.getElementById('review-page')
};

// Initialize Application
async function init() {
    try {
        // Setup event listeners
        setupEventListeners();
    } catch (error) {
        console.error('Error initializing application:', error);
        alert('Failed to initialize. Please refresh the page.');
    }
}

// Setup Event Listeners
function setupEventListeners() {
    // Certificate selection
    const certSelectButtons = document.querySelectorAll('.cert-select-btn');
    certSelectButtons.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const cert = e.currentTarget.dataset.cert;
            selectCertification(cert);
        });
    });
    
    // Quiz controls
    document.getElementById('start-exam-btn').addEventListener('click', startExam);
    document.getElementById('prev-btn').addEventListener('click', previousQuestion);
    document.getElementById('next-btn').addEventListener('click', nextQuestion);
    document.getElementById('retake-btn').addEventListener('click', () => showPage('home'));
    document.getElementById('review-btn').addEventListener('click', () => showPage('review'));
    document.getElementById('back-to-results-btn').addEventListener('click', () => showPage('results'));
}

// Select Certification
async function selectCertification(certType) {
    selectedCertification = certType;
    const certConfig = CERTIFICATIONS[certType];
    
    try {
        // Show loading
        showPage('home');
        document.querySelector('#home-page .header h1').textContent = certConfig.name;
        document.querySelector('#home-page .subtitle').textContent = certConfig.description;
        
        // Load questions for selected certification
        const response = await fetch(certConfig.questionsFile);
        allQuestions = await response.json();
        
        // Update question count in UI
        const questionCountEl = document.querySelector('#home-page .feature-card h3');
        if (questionCountEl && questionCountEl.textContent.includes('Questions')) {
            questionCountEl.textContent = `${allQuestions.length} Questions`;
        }
        
        console.log(`Loaded ${allQuestions.length} questions for ${certConfig.name}`);
    } catch (error) {
        console.error('Error loading certification questions:', error);
        alert(`Failed to load ${certConfig.name} questions. Please try again.`);
        showPage('certSelection');
    }
}

// Page Navigation
function showPage(pageName) {
    Object.values(pages).forEach(page => page.classList.remove('active'));
    pages[pageName].classList.add('active');
    
    if (pageName === 'review') {
        displayReview();
    }
}

// Start Exam
function startExam() {
    // Select 10 random questions
    currentExam = selectRandomQuestions(allQuestions, 10);
    currentQuestionIndex = 0;
    userAnswers = new Array(currentExam.length).fill(null).map(() => []); // Array of arrays for multiple selections
    timeRemaining = 720; // Reset timer to 12 minutes
    
    showPage('quiz');
    displayQuestion();
    startTimer();
}

// Select Random Questions
function selectRandomQuestions(questions, count) {
    const shuffled = [...questions].sort(() => Math.random() - 0.5);
    return shuffled.slice(0, count);
}

// Timer Functions
function startTimer() {
    updateTimerDisplay();
    
    timerInterval = setInterval(() => {
        timeRemaining--;
        updateTimerDisplay();
        
        // Warning when less than 2 minutes
        if (timeRemaining <= 120) {
            document.getElementById('timer').classList.add('warning');
        }
        
        // Time's up
        if (timeRemaining <= 0) {
            clearInterval(timerInterval);
            finishExam();
        }
    }, 1000);
}

function updateTimerDisplay() {
    const minutes = Math.floor(timeRemaining / 60);
    const seconds = timeRemaining % 60;
    document.getElementById('timer').textContent = 
        `${minutes}:${seconds.toString().padStart(2, '0')}`;
}

// Display Question
function displayQuestion() {
    const question = currentExam[currentQuestionIndex];
    
    // Update question text with selection instruction
    const correctCount = question.correctCount || 1;
    const instruction = correctCount === 1 ? "(Select 1)" : `(Select ${correctCount})`;
    document.getElementById('question-text').innerHTML = 
        `${question.question} <span class="selection-hint">${instruction}</span>`;
    
    // Update progress
    document.getElementById('current-question').textContent = currentQuestionIndex + 1;
    document.getElementById('total-questions').textContent = currentExam.length;
    
    const progressPercent = ((currentQuestionIndex + 1) / currentExam.length) * 100;
    document.getElementById('progress-fill').style.width = `${progressPercent}%`;
    
    // Display options
    const optionsContainer = document.getElementById('options-container');
    optionsContainer.innerHTML = '';
    
    question.options.forEach((text, index) => {
        const letter = LETTERS[index];
        const option = document.createElement('div');
        option.className = 'option';
        option.dataset.answer = letter;
        option.dataset.text = text;
        
        const currentAnswers = userAnswers[currentQuestionIndex] || [];
        if (currentAnswers.includes(letter)) {
            option.classList.add('selected');
        }
        
        option.innerHTML = `
            <div class="option-checkbox">
                <div class="checkbox ${currentAnswers.includes(letter) ? 'checked' : ''}"></div>
            </div>
            <div class="option-letter">${letter}</div>
            <div class="option-text">${text}</div>
        `;
        
        option.addEventListener('click', () => toggleAnswer(letter));
        optionsContainer.appendChild(option);
    });
    
    // Update navigation buttons
    updateNavigationButtons();
}

// Toggle Answer (for multiple selection)
function toggleAnswer(letter) {
    const currentAnswers = userAnswers[currentQuestionIndex] || [];
    const index = currentAnswers.indexOf(letter);
    
    if (index > -1) {
        // Remove answer
        currentAnswers.splice(index, 1);
    } else {
        // Add answer
        currentAnswers.push(letter);
    }
    
    userAnswers[currentQuestionIndex] = currentAnswers;
    
    // Update UI
    document.querySelectorAll('.option').forEach(opt => {
        const optLetter = opt.dataset.answer;
        const checkbox = opt.querySelector('.checkbox');
        
        if (currentAnswers.includes(optLetter)) {
            opt.classList.add('selected');
            checkbox.classList.add('checked');
        } else {
            opt.classList.remove('selected');
            checkbox.classList.remove('checked');
        }
    });
}

// Navigation
function previousQuestion() {
    if (currentQuestionIndex > 0) {
        currentQuestionIndex--;
        displayQuestion();
    }
}

function nextQuestion() {
    if (currentQuestionIndex < currentExam.length - 1) {
        currentQuestionIndex++;
        displayQuestion();
    } else {
        finishExam();
    }
}

function updateNavigationButtons() {
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');
    
    prevBtn.disabled = currentQuestionIndex === 0;
    
    if (currentQuestionIndex === currentExam.length - 1) {
        nextBtn.innerHTML = `
            Submit Exam
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="20 6 9 17 4 12"></polyline>
            </svg>
        `;
    } else {
        nextBtn.innerHTML = `
            Next
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
        `;
    }
}

// Finish Exam
function finishExam() {
    clearInterval(timerInterval);
    calculateResults();
    showPage('results');
}

// Calculate Results
function calculateResults() {
    let correctCount = 0;
    
    currentExam.forEach((question, index) => {
        const userAnswerLetters = userAnswers[index] || [];
        
        // Find the letter(s) corresponding to the correct answer
        const correctLetters = [];
        question.options.forEach((optionText, optIndex) => {
            if (optionText === question.answer || optionText.trim() === question.answer.trim()) {
                correctLetters.push(LETTERS[optIndex]);
            }
        });
        
        // Check if user's answer matches
        if (userAnswerLetters.length === correctLetters.length) {
            const sortedUser = [...userAnswerLetters].sort().join('');
            const sortedCorrect = [...correctLetters].sort().join('');
            if (sortedUser === sortedCorrect) {
                correctCount++;
            }
        }
    });
    
    const percentage = Math.round((correctCount / currentExam.length) * 100);
    const timeTaken = 720 - timeRemaining;
    
    // Display results
    displayResults(correctCount, percentage, timeTaken);
}

// Display Results
function displayResults(correctCount, percentage, timeTaken) {
    // Update score circle
    const circumference = 2 * Math.PI * 90;
    const offset = circumference - (percentage / 100) * circumference;
    document.getElementById('score-progress').style.strokeDashoffset = offset;
    
    // Update score percentage
    document.getElementById('score-percentage').textContent = `${percentage}%`;
    
    // Update title and summary
    const resultsTitle = document.getElementById('results-title');
    const resultsSummary = document.getElementById('results-summary');
    
    if (percentage >= 70) {
        resultsTitle.textContent = '🎉 Congratulations!';
        resultsTitle.style.color = '#4caf50';
        resultsSummary.textContent = 'You passed the practice exam! You\'re well prepared for the AWS DVA-C02 certification.';
    } else {
        resultsTitle.textContent = '📚 Keep Practicing!';
        resultsTitle.style.color = '#FF9900';
        resultsSummary.textContent = 'Keep studying and try again. Review the explanations to improve your understanding.';
    }
    
    // Display detailed stats
    const minutes = Math.floor(timeTaken / 60);
    const seconds = timeTaken % 60;
    const timeStr = `${minutes}:${seconds.toString().padStart(2, '0')}`;
    
    const incorrectCount = currentExam.length - correctCount;
    
    document.getElementById('results-details').innerHTML = `
        <div class="result-stat">
            <span class="result-stat-label">Correct Answers</span>
            <span class="result-stat-value correct">${correctCount} / ${currentExam.length}</span>
        </div>
        <div class="result-stat">
            <span class="result-stat-label">Incorrect Answers</span>
            <span class="result-stat-value incorrect">${incorrectCount} / ${currentExam.length}</span>
        </div>
        <div class="result-stat">
            <span class="result-stat-label">Time Taken</span>
            <span class="result-stat-value">${timeStr}</span>
        </div>
        <div class="result-stat">
            <span class="result-stat-label">Pass Threshold</span>
            <span class="result-stat-value">70%</span>
        </div>
    `;
}

// Display Review
function displayReview() {
    const reviewContainer = document.getElementById('review-container');
    reviewContainer.innerHTML = '';
    
    currentExam.forEach((question, index) => {
        const userAnswerLetters = userAnswers[index] || [];
        
        // Find correct answer letter(s)
        const correctLetters = [];
        question.options.forEach((optionText, optIndex) => {
            if (optionText === question.answer || optionText.trim() === question.answer.trim()) {
                correctLetters.push(LETTERS[optIndex]);
            }
        });
        
        const sortedUser = [...userAnswerLetters].sort().join('');
        const sortedCorrect = [...correctLetters].sort().join('');
        const isCorrect = sortedUser === sortedCorrect && userAnswerLetters.length > 0;
        
        const reviewDiv = document.createElement('div');
        reviewDiv.className = 'review-question';
        
        const optionsHTML = question.options.map((text, optIndex) => {
            const letter = LETTERS[optIndex];
            let classes = ['review-option'];
            
            if (userAnswerLetters.includes(letter)) {
                classes.push('user-answer');
            }
            if (correctLetters.includes(letter)) {
                classes.push('correct-answer');
            }
            
            let badge = '';
            if (correctLetters.includes(letter)) {
                badge = '<span style="margin-left: auto; color: #4caf50; font-weight: bold;">✓ Correct</span>';
            } else if (userAnswerLetters.includes(letter)) {
                badge = '<span style="margin-left: auto; color: #ff4444; font-weight: bold;">✗ Wrong</span>';
            }
            
            return `
                <div class="${classes.join(' ')}">
                    <div class="option-letter">${letter}</div>
                    <div class="option-text">${text}</div>
                    ${badge}
                </div>
            `;
        }).join('');
        
        reviewDiv.innerHTML = `
            <div class="review-question-header">
                <span class="review-question-number">Question ${index + 1}</span>
                <span class="review-badge ${isCorrect ? 'correct' : 'incorrect'}">
                    ${isCorrect ? '✓ Correct' : '✗ Incorrect'}
                </span>
            </div>
            <div class="review-question-text">${question.question}</div>
            ${optionsHTML}
            <div class="review-explanation">
                <div class="review-explanation-title">Explanation:</div>
                <div class="review-explanation-text">${question.explanation || 'No explanation available.'}</div>
            </div>
        `;
        
        reviewContainer.appendChild(reviewDiv);
    });
}

// Initialize app when DOM is loaded
document.addEventListener('DOMContentLoaded', init);

