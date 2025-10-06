# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [2.0.0] - 2025-10-06

### 🎉 Major Release: Multi-Cloud Platform

### Added
- **Azure Certifications Support**
  - Microsoft Certified: Azure Developer Associate (AZ-204)
  - Microsoft Certified: Azure AI Engineer Associate (AI-102)
- **Multi-Cloud Interface**
  - Provider selection screen (AWS vs Azure)
  - Provider-specific branding and colors
  - Separate question banks per certification
- **21 Azure Developer Questions** covering:
  - Azure App Service & Functions
  - Container solutions (ACI, AKS)
  - Azure storage & Cosmos DB
  - Security (Key Vault, Managed Identity)
  - Messaging (Service Bus, Event Hubs)
- **21 Azure AI Questions** covering:
  - Azure Cognitive Services
  - Computer Vision & Custom Vision
  - NLP & Language services
  - Speech services
  - Bot Service & conversational AI
  - Azure Machine Learning
  - Responsible AI

### Changed
- **Renamed Question Files** for clarity:
  - `questions_full.json` → `questions_aws_developer.json`
  - `questions_ai.json` → `questions_aws_ai.json`
- **Updated Main Page Title**
  - "AWS Certification Practice" → "Cloud Certification Practice - AWS & Azure"
- **Reorganized Certification Cards**
  - Grouped by cloud provider (AWS/Azure)
  - Added provider badges
  - Updated color schemes per provider
- **Enhanced Styling**
  - Azure blue color scheme (#0078D4, #00A4EF)
  - AWS orange maintained (#FF9900)
  - Provider-specific hover effects
  - Improved card layout for 4 certifications

### Updated Documentation
- `README.md` - Multi-cloud platform overview
- `CERTIFICATIONS.md` - Detailed certification guide (NEW)
- `CHANGELOG.md` - Version history

### Technical Improvements
- Dynamic certification loading based on selection
- Updated `CERTIFICATIONS` config with 4 paths
- Color-coded UI per cloud provider
- Improved question bank management

---

## [1.5.0] - 2025-10-05

### Added
- **Dual Certification Paths**
  - AWS Certified Developer - Associate (DVA-C02)
  - AWS Certified AI Practitioner (AIF-C01)
- **Certification Selection Screen**
  - Beautiful card-based UI
  - Comparison grid for decision-making
  - Individual question counts per path

### Changed
- Added certification path selection before quiz
- Separated question banks by certification type
- Updated homepage to show selected certification info

---

## [1.4.0] - 2025-10-04

### Added
- **Comprehensive Testing Suite**
  - 70+ unit tests with Jest
  - 30+ E2E tests with Playwright
  - 80%+ code coverage
- **CI/CD Pipeline**
  - GitHub Actions workflow
  - Automated testing on every push
  - Deployment gates based on test results
- **Test Documentation**
  - TESTING.md with detailed testing guide
  - Test running instructions
  - Coverage reports

### Changed
- Improved code quality with ESLint
- Added validation scripts
- Enhanced error handling

---

## [1.3.0] - 2025-10-03

### Fixed
- **CSS Hover Bug**
  - Fixed persistent orange hover effect on unselected options
  - Updated `.option:hover` to `.option:hover:not(.selected)`
  - Improved visual feedback for selected options

### Changed
- **Question Quality Improvements**
  - Cleaned and validated all 122 questions
  - Removed truncated and poorly formatted questions
  - Enhanced explanations for clarity
  - Verified all options and answers

---

## [1.2.0] - 2025-10-02

### Added
- **Letter-Based Options (A, B, C, D, E, F)**
  - Changed from numeric (0-5) to professional letter format
  - Better matches real exam experience
- **Multiple Selection Support**
  - Can now select multiple answers per question
  - Checkbox-style interface
  - Proper scoring for multi-answer questions

### Changed
- Updated UI to show checkboxes instead of radio buttons
- Improved answer validation logic
- Enhanced results calculation for multiple selections

---

## [1.1.0] - 2025-10-01

### Added
- **Netlify Deployment**
  - Automatic deployment on every push
  - Live demo at roddanel1992-ai-questionnaire.netlify.app
  - CI/CD integration with GitHub
- **Custom ROD Logo**
  - Replaced AWS logo with custom "ROD" branding
  - Added glasses icon for personality
  - Improved logo visibility and styling

### Changed
- Better logo sizing and contrast
- Updated branding throughout the app

---

## [1.0.0] - 2025-09-30

### 🎉 Initial Release

### Added
- **Core Features**
  - 122 AWS DVA-C02 practice questions
  - 12-minute timed exams
  - 10 random questions per exam
  - Instant results and scoring
  - Detailed explanations
- **User Interface**
  - Modern gradient design
  - Responsive layout
  - Mobile-friendly
  - Smooth animations
- **Navigation**
  - Previous/Next question buttons
  - Progress bar
  - Question counter
- **Results Page**
  - Animated score circle
  - Pass/fail indicator (70% threshold)
  - Time taken display
  - Review and retake options
- **Review Mode**
  - See all questions with answers
  - Correct answers in green
  - Incorrect answers in red
  - Full explanations

### Documentation
- README.md with full documentation
- Setup instructions
- Customization guide

---

## Legend

- 🎉 Major release
- ✨ New feature
- 🐛 Bug fix
- 📚 Documentation
- 🔧 Technical improvement
- 🎨 UI/UX enhancement
- ⚡ Performance improvement

---

**For detailed information about each certification path, see [CERTIFICATIONS.md](CERTIFICATIONS.md)**
