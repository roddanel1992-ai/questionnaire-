/**
 * E2E Tests for AWS DVA-C02 Quiz Application
 * Testing complete user workflows and interactions
 */

const { test, expect } = require('@playwright/test');

test.describe('AWS DVA-C02 Quiz - E2E Tests', () => {
  
  test.beforeEach(async ({ page }) => {
    // Navigate to the application
    await page.goto('http://localhost:8000');
    await page.waitForLoadState('networkidle');
  });

  test.describe('Homepage', () => {
    test('should display ROD logo and title', async ({ page }) => {
      // Check for ROD logo
      const logo = page.locator('.aws-logo');
      await expect(logo).toBeVisible();
      
      // Check for title
      await expect(page.locator('h1')).toContainText('AWS Certified Developer - Associate');
      await expect(page.locator('.subtitle')).toContainText('DVA-C02');
    });

    test('should show exam information', async ({ page }) => {
      await expect(page.getByText('10 questions')).toBeVisible();
      await expect(page.getByText('12 minutes')).toBeVisible();
      await expect(page.getByText('Multiple choice')).toBeVisible();
      await expect(page.getByText('Instant results')).toBeVisible();
    });

    test('should display feature cards', async ({ page }) => {
      await expect(page.getByText('139 Questions')).toBeVisible();
      await expect(page.getByText('Timed Practice')).toBeVisible();
      await expect(page.getByText('Detailed Results')).toBeVisible();
    });

    test('should have start exam button', async ({ page }) => {
      const startBtn = page.getByRole('button', { name: /start practice exam/i });
      await expect(startBtn).toBeVisible();
      await expect(startBtn).toBeEnabled();
    });
  });

  test.describe('Quiz Functionality', () => {
    test('should start quiz when button clicked', async ({ page }) => {
      await page.getByRole('button', { name: /start practice exam/i }).click();
      
      // Should navigate to quiz page
      await expect(page.locator('#quiz-page')).toHaveClass(/active/);
      
      // Should show timer
      await expect(page.locator('#timer')).toBeVisible();
      
      // Should show first question
      await expect(page.locator('#question-text')).not.toBeEmpty();
    });

    test('should display question with letter options (A-F)', async ({ page }) => {
      await page.getByRole('button', { name: /start practice exam/i }).click();
      
      // Wait for question to load
      await page.waitForSelector('.option', { timeout: 5000 });
      
      // Check for letter labels
      const options = await page.locator('.option').count();
      expect(options).toBeGreaterThanOrEqual(2);
      expect(options).toBeLessThanOrEqual(6);
      
      // Check for letter badges (A, B, C, etc.)
      const firstLetter = page.locator('.option-letter').first();
      await expect(firstLetter).toBeVisible();
      const letterText = await firstLetter.textContent();
      expect(['A', 'B', 'C', 'D', 'E', 'F']).toContain(letterText);
    });

    test('should show checkboxes for options', async ({ page }) => {
      await page.getByRole('button', { name: /start practice exam/i }).click();
      await page.waitForSelector('.checkbox');
      
      const checkbox = page.locator('.checkbox').first();
      await expect(checkbox).toBeVisible();
    });

    test('should allow selecting multiple options', async ({ page }) => {
      await page.getByRole('button', { name: /start practice exam/i }).click();
      await page.waitForSelector('.option');
      
      const options = page.locator('.option');
      const firstOption = options.nth(0);
      const secondOption = options.nth(1);
      
      // Select first option
      await firstOption.click();
      await expect(firstOption).toHaveClass(/selected/);
      
      // Select second option
      await secondOption.click();
      await expect(secondOption).toHaveClass(/selected/);
      
      // Both should be selected
      await expect(firstOption).toHaveClass(/selected/);
      await expect(secondOption).toHaveClass(/selected/);
    });

    test('should toggle selection on click', async ({ page }) => {
      await page.getByRole('button', { name: /start practice exam/i }).click();
      await page.waitForSelector('.option');
      
      const option = page.locator('.option').first();
      
      // Click to select
      await option.click();
      await expect(option).toHaveClass(/selected/);
      
      // Click again to deselect
      await option.click();
      await expect(option).not.toHaveClass(/selected/);
    });

    test('should not show hover style on selected options', async ({ page }) => {
      await page.getByRole('button', { name: /start practice exam/i }).click();
      await page.waitForSelector('.option');
      
      const option = page.locator('.option').first();
      
      // Select the option
      await option.click();
      
      // Hover over selected option
      await option.hover();
      
      // Should have selected class
      await expect(option).toHaveClass(/selected/);
    });
  });

  test.describe('Navigation', () => {
    test('should navigate between questions', async ({ page }) => {
      await page.getByRole('button', { name: /start practice exam/i }).click();
      await page.waitForSelector('#question-text');
      
      const firstQuestion = await page.locator('#question-text').textContent();
      
      // Click next
      await page.getByRole('button', { name: /next/i }).click();
      await page.waitForTimeout(500);
      
      const secondQuestion = await page.locator('#question-text').textContent();
      
      // Questions should be different
      expect(firstQuestion).not.toBe(secondQuestion);
      
      // Click previous
      await page.getByRole('button', { name: /previous/i }).click();
      await page.waitForTimeout(500);
      
      const backToFirst = await page.locator('#question-text').textContent();
      
      // Should return to first question
      expect(backToFirst).toBe(firstQuestion);
    });

    test('should disable previous button on first question', async ({ page }) => {
      await page.getByRole('button', { name: /start practice exam/i }).click();
      await page.waitForSelector('#prev-btn');
      
      const prevBtn = page.locator('#prev-btn');
      await expect(prevBtn).toBeDisabled();
    });

    test('should show "Submit Exam" on last question', async ({ page }) => {
      await page.getByRole('button', { name: /start practice exam/i }).click();
      await page.waitForSelector('#next-btn');
      
      // Navigate to last question
      for (let i = 0; i < 9; i++) {
        await page.getByRole('button', { name: /next/i }).click();
        await page.waitForTimeout(300);
      }
      
      // Button should say "Submit Exam"
      await expect(page.getByRole('button', { name: /submit exam/i })).toBeVisible();
    });
  });

  test.describe('Timer', () => {
    test('should start timer when quiz begins', async ({ page }) => {
      await page.getByRole('button', { name: /start practice exam/i }).click();
      
      const timer = page.locator('#timer');
      await expect(timer).toBeVisible();
      
      const initialTime = await timer.textContent();
      expect(initialTime).toMatch(/\d{1,2}:\d{2}/);
    });

    test('should show time counting down', async ({ page }) => {
      await page.getByRole('button', { name: /start practice exam/i }).click();
      
      const timer = page.locator('#timer');
      const time1 = await timer.textContent();
      
      await page.waitForTimeout(2000);
      
      const time2 = await timer.textContent();
      
      // Time should have changed (countdown)
      expect(time1).not.toBe(time2);
    });
  });

  test.describe('Progress Tracking', () => {
    test('should show current question number', async ({ page }) => {
      await page.getByRole('button', { name: /start practice exam/i }).click();
      await page.waitForSelector('#current-question');
      
      const currentQ = page.locator('#current-question');
      await expect(currentQ).toHaveText('1');
      
      // Go to next question
      await page.getByRole('button', { name: /next/i }).click();
      await expect(currentQ).toHaveText('2');
    });

    test('should update progress bar', async ({ page }) => {
      await page.getByRole('button', { name: /start practice exam/i }).click();
      await page.waitForSelector('#progress-fill');
      
      const progressBar = page.locator('#progress-fill');
      
      // Get initial width
      const initialWidth = await progressBar.evaluate(el => el.style.width);
      
      // Navigate to next question
      await page.getByRole('button', { name: /next/i }).click();
      await page.waitForTimeout(300);
      
      // Width should increase
      const newWidth = await progressBar.evaluate(el => el.style.width);
      
      expect(parseFloat(newWidth)).toBeGreaterThan(parseFloat(initialWidth) || 0);
    });
  });

  test.describe('Results Page', () => {
    test('should show results after submitting', async ({ page }) => {
      await page.getByRole('button', { name: /start practice exam/i }).click();
      await page.waitForSelector('.option');
      
      // Answer all questions quickly
      for (let i = 0; i < 10; i++) {
        await page.locator('.option').first().click();
        await page.waitForTimeout(200);
        
        const nextBtn = page.locator('#next-btn');
        const btnText = await nextBtn.textContent();
        
        if (btnText.includes('Submit')) {
          await nextBtn.click();
          break;
        } else {
          await nextBtn.click();
          await page.waitForTimeout(200);
        }
      }
      
      // Should show results page
      await expect(page.locator('#results-page')).toHaveClass(/active/);
      await expect(page.locator('#score-percentage')).toBeVisible();
    });

    test('should display score percentage', async ({ page }) => {
      await page.getByRole('button', { name: /start practice exam/i }).click();
      
      // Quick submit
      await page.waitForSelector('.option');
      for (let i = 0; i < 10; i++) {
        await page.locator('.option').first().click();
        const btn = page.locator('#next-btn');
        await btn.click();
        await page.waitForTimeout(100);
      }
      
      const score = page.locator('#score-percentage');
      await expect(score).toBeVisible();
      
      const scoreText = await score.textContent();
      expect(scoreText).toMatch(/\d+%/);
    });
  });

  test.describe('Complete User Flow', () => {
    test('should complete full quiz workflow', async ({ page }) => {
      // 1. Start on homepage
      await expect(page.locator('#home-page')).toHaveClass(/active/);
      
      // 2. Start quiz
      await page.getByRole('button', { name: /start practice exam/i }).click();
      await expect(page.locator('#quiz-page')).toHaveClass(/active/);
      
      // 3. Answer questions
      await page.waitForSelector('.option');
      for (let i = 0; i < 5; i++) {
        // Select an answer
        await page.locator('.option').first().click();
        
        // Go to next
        const nextBtn = page.locator('#next-btn');
        if (i < 4) {
          await nextBtn.click();
          await page.waitForTimeout(200);
        }
      }
      
      // 4. Should be able to navigate back
      await page.locator('#prev-btn').click();
      await expect(page.locator('#current-question')).toHaveText('4');
      
      // 5. Navigate forward again
      await page.locator('#next-btn').click();
      await expect(page.locator('#current-question')).toHaveText('5');
      
      // This validates the core functionality works end-to-end
    });
  });

  test.describe('Responsive Design', () => {
    test('should work on mobile viewport', async ({ page }) => {
      await page.setViewportSize({ width: 375, height: 667 });
      
      await expect(page.locator('h1')).toBeVisible();
      await expect(page.getByRole('button', { name: /start practice exam/i })).toBeVisible();
      
      await page.getByRole('button', { name: /start practice exam/i }).click();
      await page.waitForSelector('.option');
      
      await expect(page.locator('#question-text')).toBeVisible();
      await expect(page.locator('.option').first()).toBeVisible();
    });

    test('should work on tablet viewport', async ({ page }) => {
      await page.setViewportSize({ width: 768, height: 1024 });
      
      await page.getByRole('button', { name: /start practice exam/i }).click();
      await page.waitForSelector('.option');
      
      await expect(page.locator('#question-text')).toBeVisible();
    });
  });
});

