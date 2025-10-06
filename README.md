# Cloud Certification Practice - AWS & Azure

A modern, interactive web application for practicing cloud certification exams for both **AWS** and **Azure** platforms.

## 🌟 Certifications Covered

### AWS (Amazon Web Services)
- ☁️ **AWS Certified Developer - Associate (DVA-C02)** - 122 questions
- 🤖 **AWS Certified AI Practitioner (AIF-C01)** - 49 questions

### Azure (Microsoft)
- ☁️ **Microsoft Certified: Azure Developer Associate (AZ-204)** - 21 questions
- 🤖 **Microsoft Certified: Azure AI Engineer Associate (AI-102)** - 21 questions

## Features

✨ **Multi-Cloud Platform** - Practice for both AWS and Azure certifications
⏱️ **Timed Practice Exams** - 12-minute time limit for 10 random questions
📊 **Instant Results** - Detailed score breakdown and performance metrics
📚 **Answer Explanations** - Learn from detailed explanations for each question
🎨 **Beautiful Modern UI** - Responsive design that works on all devices
🔄 **Random Question Selection** - Different questions each time you practice
🔤 **Letter-Based Options** - Professional exam format (A, B, C, D, E, F)
✅ **Multiple Selection** - Support for questions with multiple correct answers
🧪 **Full Test Coverage** - Unit & E2E tests for production quality
🚀 **CI/CD Pipeline** - Automated testing and deployment

## How to Use

### Option 1: Open Directly in Browser
1. Simply open `index.html` in your web browser
2. Choose your certification path (AWS or Azure)
3. Click "Start Practice" on your selected certification
4. Answer the 10 questions within 12 minutes
5. Review your results and explanations

### Option 2: Run with a Local Server
```bash
# Using Python
python -m http.server 8000

# Using Node.js
npx http-server

# Then open http://localhost:8000 in your browser
```

## Exam Structure

- **Questions per Exam**: 10 questions (randomly selected)
- **Time Limit**: 12 minutes
- **Passing Score**: 70%
- **Question Types**: Multiple choice (2-6 options, letters A-F)
- **Multiple Selection**: Can select multiple answers per question
- **Test Coverage**: 80%+ unit and E2E tests

## Topics Covered

### AWS Certified Developer - Associate (DVA-C02)

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

### Azure Developer Associate (AZ-204)

- Developing Azure compute solutions (App Service, Functions, Containers)
- Azure storage solutions (Blob, Cosmos DB, Table Storage)
- Azure security implementations (Key Vault, Managed Identity)
- Monitoring, troubleshooting, and optimization
- Azure integrations and messaging (Service Bus, Event Hubs)

### AWS Certified AI Practitioner (AIF-C01)

- AWS AI/ML services fundamentals
- Amazon SageMaker
- Computer Vision, NLP, and Speech services
- Responsible AI principles
- AI model deployment and monitoring

### Azure AI Engineer Associate (AI-102)

- Azure Cognitive Services (Vision, Speech, Language)
- Azure Machine Learning
- Conversational AI (Bot Service, LUIS)
- Computer Vision and Custom Vision
- Form Recognizer and Document Intelligence
- Responsible AI practices

## File Structure

```
AWS exam/
├── index.html                      # Main HTML file
├── style.css                       # Styling and responsive design
├── app.js                          # Application logic and interactivity
├── questions_aws_developer.json    # AWS Developer questions (122)
├── questions_aws_ai.json          # AWS AI Practitioner questions (49)
├── questions_azure_developer.json # Azure Developer questions (21)
├── questions_azure_ai.json        # Azure AI Engineer questions (21)
├── tests/
│   ├── unit/
│   │   └── app.test.js            # Unit tests for business logic
│   └── e2e/
│       └── quiz.spec.js           # End-to-end user flow tests
├── .github/
│   └── workflows/
│       └── test.yml               # CI/CD pipeline
├── package.json                   # Node dependencies and scripts
├── playwright.config.js           # E2E test configuration
├── extract_full.py                # Question extraction script
└── README.md                      # This file
```

## Features in Detail

### Certification Selection
- Choose between AWS and Azure providers
- Select Developer or AI certification paths
- See question counts and exam details
- Beautiful card-based UI with provider branding

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

## Testing

### Run Tests

```bash
# Install dependencies
npm install

# Run all tests
npm test

# Run unit tests only
npm run test:unit

# Run E2E tests only
npm run test:e2e

# Run with UI (Playwright)
npm run test:e2e:ui

# Validate everything
npm run validate
```

### Test Coverage

- **Unit Tests**: 80%+ coverage of business logic
- **E2E Tests**: Complete user flow testing
- **Browser Testing**: Chrome, Firefox, Safari, Mobile
- **CI/CD**: Automated testing on every commit

See [TESTING.md](TESTING.md) for detailed testing documentation.

---

## Customization

### Adding Questions

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

In `app.js`, modify the `timeRemaining` variable:
```javascript
let timeRemaining = 720; // 12 minutes in seconds
```

### Changing Number of Questions

In `app.js`, modify the `startExam()` function:
```javascript
currentExam = selectRandomQuestions(allQuestions, 10); // Change 10 to your desired number
```

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
6. **Cross-Platform Learning** - Compare AWS and Azure approaches

## Live Demo

🚀 **[View Live Demo on Netlify](https://roddanel1992-ai-questionnaire.netlify.app/)**

## Deployment

This project automatically deploys to Netlify on every push to the main branch via GitHub Actions CI/CD pipeline.

## License

This project is for educational purposes. AWS, Azure, and their respective certification names are trademarks of their respective owners.

## Support

For issues or suggestions, please create an issue in the project repository.

---

**Good luck with your cloud certification journey! ☁️🚀**

*Supporting both AWS and Azure - Choose your cloud, master your path!*
