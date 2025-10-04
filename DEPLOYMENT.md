# Deployment Guide - AWS DVA-C02 Quiz App

## Option 1: Netlify Drop (Easiest - No Account Required)

### Steps:
1. Go to **https://app.netlify.com/drop**
2. Drag and drop your entire project folder into the upload area
3. Netlify will deploy instantly and give you a public URL
4. Done! ✅

**Time:** ~1 minute

---

## Option 2: Vercel (Easy - Free Account)

### Steps:
1. Install Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Deploy from your project folder:
   ```bash
   vercel
   ```

3. Follow the prompts (login, confirm settings)
4. Your app will be deployed with a public URL

**Time:** ~3 minutes

---

## Option 3: Netlify CLI (Recommended for Updates)

### Steps:
1. Install Netlify CLI:
   ```bash
   npm install -g netlify-cli
   ```

2. Login to Netlify:
   ```bash
   netlify login
   ```

3. Deploy your site:
   ```bash
   netlify deploy --prod
   ```

4. Your app will be live with a public URL

**Time:** ~5 minutes

---

## Option 4: GitHub Pages (Good for Long-Term Hosting)

### Steps:
1. Create a GitHub repository
2. Push your code:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin YOUR_GITHUB_REPO_URL
   git push -u origin main
   ```

3. Go to GitHub repo → Settings → Pages
4. Select "Deploy from branch" → Choose "main" branch
5. Your site will be at: `https://yourusername.github.io/repo-name`

**Time:** ~10 minutes

---

## Option 5: AWS S3 + CloudFront (Professional Setup)

Perfect for an AWS certification site!

### Steps:
1. Create S3 bucket:
   ```bash
   aws s3 mb s3://rod-aws-quiz --region us-east-1
   ```

2. Configure bucket for static hosting:
   ```bash
   aws s3 website s3://rod-aws-quiz --index-document index.html
   ```

3. Upload files:
   ```bash
   aws s3 sync . s3://rod-aws-quiz --exclude ".git/*" --exclude "*.py" --exclude "*.md"
   ```

4. Make bucket public (bucket policy):
   ```json
   {
     "Version": "2012-10-17",
     "Statement": [{
       "Sid": "PublicReadGetObject",
       "Effect": "Allow",
       "Principal": "*",
       "Action": "s3:GetObject",
       "Resource": "arn:aws:s3:::rod-aws-quiz/*"
     }]
   }
   ```

5. (Optional) Add CloudFront distribution for HTTPS

**Time:** ~20 minutes

---

## Quick Deployment Commands

### For Netlify (Run from project folder):
```bash
# Install if needed
npm install -g netlify-cli

# Deploy
netlify deploy --prod
```

### For Vercel (Run from project folder):
```bash
# Install if needed
npm install -g vercel

# Deploy
vercel --prod
```

---

## Files Included in Deployment

✅ index.html  
✅ app.js  
✅ style.css  
✅ questions_full.json  
✅ README.md  
✅ UPDATES.md  
✅ extract_full.py (optional, for extracting more questions)

❌ exam_questions with answers/ (excluded - contains source PDFs)

---

## Post-Deployment

After deployment, you'll get a URL like:
- Netlify: `https://rod-aws-quiz.netlify.app`
- Vercel: `https://rod-aws-quiz.vercel.app`
- GitHub Pages: `https://yourusername.github.io/aws-quiz`

Share this URL with anyone for testing!

---

## Custom Domain (Optional)

If you have a custom domain, you can connect it:
1. In Netlify/Vercel dashboard, go to "Domain Settings"
2. Add your domain
3. Update DNS records as instructed
4. Wait for DNS propagation (~24 hours)

---

## Continuous Deployment

For automatic updates when you change files:

### Netlify:
1. Connect your GitHub repository in Netlify dashboard
2. Every push to `main` branch auto-deploys

### Vercel:
1. Link your GitHub repository in Vercel dashboard
2. Every commit auto-deploys

---

**Recommended:** Start with **Netlify Drop** for instant testing, then set up Netlify CLI for future updates!

