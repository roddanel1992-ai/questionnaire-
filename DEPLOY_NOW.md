# 🚀 Deploy to Netlify - 3 Simple Steps

Your code is ready and committed to Git! Follow these steps:

## Step 1: Create GitHub Repository (2 minutes)

1. Go to: **https://github.com/new**
2. Repository name: `aws-dva-c02-quiz` (or any name you like)
3. Make it **Public**
4. **DON'T** initialize with README (we already have files)
5. Click **"Create repository"**

## Step 2: Push Your Code (30 seconds)

Copy the commands from GitHub and run them, OR run these:

```bash
git remote add origin https://github.com/YOUR_USERNAME/aws-dva-c02-quiz.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username!

## Step 3: Connect to Netlify (1 minute)

1. Go to: **https://app.netlify.com/start**
2. Click **"Import from Git"**
3. Choose **"GitHub"**
4. Authorize Netlify to access GitHub
5. Select your repository: `aws-dva-c02-quiz`
6. Click **"Deploy site"**

**Done!** 🎉

Netlify will give you a public URL like:
`https://cosmic-cupcake-123456.netlify.app`

## Bonus: Automatic Updates

Every time you push changes to GitHub, Netlify automatically redeploys! 🔄

Example:
```bash
git add .
git commit -m "Updated questions"
git push
```

Your site updates in ~30 seconds!

---

## Alternative: Quick Deploy (No GitHub)

If you don't want GitHub, just:
1. Go to: **https://app.netlify.com/drop**
2. Drag the file: `rod-aws-quiz.zip`
3. Done! (But no auto-updates)

---

**Your app is ready!** All files are committed and waiting to be pushed. 🚀

