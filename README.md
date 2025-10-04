# AWS DVA-C02 Certification Practice Website

A modern, interactive web application for practicing AWS Certified Developer - Associate (DVA-C02) certification exam questions.

## Features

✨ **139 Real Exam Questions** - Extracted from actual DVA-C02 practice materials
⏱️ **Timed Practice Exams** - 12-minute time limit for 10 random questions
📊 **Instant Results** - Detailed score breakdown and performance metrics
📚 **Answer Explanations** - Learn from detailed explanations for each question
🎨 **Beautiful Modern UI** - Responsive design that works on all devices
🔄 **Random Question Selection** - Different questions each time you practice

## How to Use

### Option 1: Open Directly in Browser
1. Simply open `index.html` in your web browser
2. Click "Start Practice Exam"
3. Answer the 10 questions within 12 minutes
4. Review your results and explanations

### Option 2: Run with a Local Server
```bash
# Using Python
python -m http.server 8000

# Using Node.js
npx http-server

# Then open http://localhost:8000 in your browser
```

## Exam Structure

- **Questions per Exam**: 10 questions (randomly selected from 139)
- **Time Limit**: 12 minutes
- **Passing Score**: 70%
- **Question Types**: Multiple choice (2-5 options)

## Topics Covered

The question bank covers all major DVA-C02 domains:

1. **Development with AWS Services** (32%)
   - Serverless applications (Lambda, API Gateway, Step Functions)
   - Container-based applications (ECS, ECR)
   - Storage services (S3, DynamoDB, ElastiCache)

2. **Security** (26%)
   - Authentication and authorization (IAM, Cognito)
   - Encryption (KMS, S3 encryption)
   - Secrets management (Systems Manager, Secrets Manager)

3. **Deployment** (24%)
   - CI/CD (CodePipeline, CodeBuild, CodeDeploy)
   - Infrastructure as Code (CloudFormation, SAM)
   - Deployment strategies (Blue/Green, Canary)

4. **Troubleshooting and Optimization** (18%)
   - Monitoring and logging (CloudWatch, X-Ray)
   - Performance optimization
   - Cost optimization

## File Structure

```
AWS exam/
├── index.html               # Main HTML file
├── style.css                # Styling and responsive design
├── app.js                   # Application logic and interactivity
├── questions_full.json      # Question bank (139 questions extracted from PDFs)
├── extract_full.py          # Python script to extract questions from PDF files
├── exam_questions with answers/  # Folder containing PDF exam dumps
└── README.md                # This file
```

## Features in Detail

### Timer
- 12-minute countdown timer
- Warning (red color) when less than 2 minutes remain
- Automatic submission when time expires

### Navigation
- Previous/Next buttons to navigate between questions
- Progress bar showing completion status
- Question counter (e.g., "Question 3 of 10")

### Results Page
- Animated score circle showing percentage
- Pass/Fail status (70% threshold)
- Detailed breakdown:
  - Correct/Incorrect answers
  - Time taken
  - Pass threshold
- Options to review answers or retake exam

### Review Mode
- See all questions with your answers
- Correct answers highlighted in green
- Your incorrect answers shown in red
- Detailed explanations for every question

## Customization

### Extracting More Questions

To re-extract questions from the PDF files:

1. Add your PDF files to the `exam_questions with answers/` folder
2. Run the extraction script:
```bash
python extract_full.py
```
3. The script will generate `questions_full.json` with all extracted questions

Each question follows this format:

```json
{
  "question": "Your question text here?",
  "options": [
    "Option A text",
    "Option B text",
    "Option C text",
    "Option D text"
  ],
  "answer": "Option A text",
  "explanation": "Explanation of why this answer is correct"
}
```

### Changing Time Limit

In `app.js`, modify the `timeRemaining` variable (line 9):
```javascript
let timeRemaining = 720; // 12 minutes in seconds
```

### Changing Number of Questions

In `app.js`, modify the `startExam()` function (line 49):
```javascript
currentExam = selectRandomQuestions(allQuestions, 10); // Change 10 to your desired number
```

### Changing Pass Threshold

The passing score is displayed in the results but not enforced. To change the display:
1. In `app.js`, find the `displayResults()` function
2. Modify the comparison on line 156: `if (percentage >= 70)`

## Browser Compatibility

- ✅ Chrome/Edge (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Opera
- ⚠️ Internet Explorer (not supported)

## Mobile Responsive

The application is fully responsive and works great on:
- 📱 Mobile phones
- 📱 Tablets
- 💻 Laptops
- 🖥️ Desktop computers

## Tips for Success

1. **Practice Regularly** - Take multiple practice exams
2. **Review Explanations** - Read why answers are correct
3. **Time Management** - Aim for ~1 minute per question
4. **Identify Weak Areas** - Focus on topics where you score low
5. **Retake Exams** - Questions are randomly selected each time

## License

This project is for educational purposes. AWS and AWS Certified Developer are trademarks of Amazon Web Services.

## Support

For issues or suggestions, please create an issue in the project repository.

---

**Good luck with your AWS DVA-C02 certification! 🚀**

