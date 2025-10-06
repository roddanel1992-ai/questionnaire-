@echo off
echo ========================================
echo   Push to GitHub
echo ========================================
echo.
set /p TOKEN="Enter your GitHub token: "
echo.
echo Updating remote URL...
git remote set-url origin https://%TOKEN%@github.com/roddanel1992-ai/questionnaire-.git
echo.
echo Pushing to GitHub...
git push -u origin main
echo.
echo ========================================
echo   Done!
echo ========================================
echo.
echo Your code is now at:
echo https://github.com/roddanel1992-ai/questionnaire-
echo.
pause

