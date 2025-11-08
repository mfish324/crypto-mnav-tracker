# Deployment Guide

This guide provides instructions for deploying the Crypto Treasury mNAV Tracker to various cloud platforms.

## Prerequisites

- GitHub account
- Account on chosen deployment platform
- Git installed locally

---

## Option 1: Deploy to Render (Recommended - Free Tier Available)

Render is a modern cloud platform that offers a free tier perfect for this application.

### Steps:

1. **Push to GitHub** (see GitHub section below)

2. **Sign up for Render**
   - Go to https://render.com
   - Sign up with your GitHub account

3. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select the `crypto_mnav_tracker` repository

4. **Configure the Service**
   - **Name**: `crypto-mnav-tracker` (or your preference)
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free (or paid for better performance)

5. **Deploy**
   - Click "Create Web Service"
   - Render will automatically deploy your app
   - Your app will be live at: `https://crypto-mnav-tracker-xxxx.onrender.com`

### Notes:
- Free tier spins down after 15 minutes of inactivity
- First load after inactivity may take 30-60 seconds
- Upgrade to paid plan ($7/month) for always-on service

---

## Option 2: Deploy to Railway

Railway offers a generous free tier and easy deployment.

### Steps:

1. **Push to GitHub** (see GitHub section below)

2. **Sign up for Railway**
   - Go to https://railway.app
   - Sign up with GitHub

3. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose `crypto_mnav_tracker`

4. **Configure**
   - Railway auto-detects Python
   - It will use the `Procfile` automatically
   - Add domain: Click "Settings" → "Generate Domain"

5. **Deploy**
   - Railway automatically deploys
   - Access at generated domain

### Notes:
- $5 free credit per month
- After credits, ~$5/month for small apps
- Automatic HTTPS

---

## Option 3: Deploy to Heroku

Heroku is a classic PaaS with extensive documentation.

### Steps:

1. **Install Heroku CLI**
   ```bash
   # Download from https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create Heroku App**
   ```bash
   cd crypto_mnav_tracker
   heroku create crypto-mnav-tracker
   ```

4. **Deploy**
   ```bash
   git push heroku main
   ```

5. **Open App**
   ```bash
   heroku open
   ```

### Notes:
- No free tier (starts at $5/month)
- Eco dynos ($5/month) sleep after 30 min inactivity
- Basic dynos ($7/month) are always-on

---

## Option 4: Deploy to Fly.io

Fly.io offers edge deployment close to users.

### Steps:

1. **Install Fly CLI**
   ```bash
   # Download from https://fly.io/docs/hands-on/install-flyctl/
   ```

2. **Login**
   ```bash
   fly auth login
   ```

3. **Launch App**
   ```bash
   cd crypto_mnav_tracker
   fly launch
   ```

4. **Follow Prompts**
   - Choose app name
   - Select region
   - Don't add PostgreSQL or Redis

5. **Deploy**
   ```bash
   fly deploy
   ```

### Notes:
- Generous free tier
- Edge deployment for low latency
- Automatic HTTPS

---

## Pushing to GitHub

### First Time Setup:

1. **Create GitHub Repository**
   - Go to https://github.com/new
   - Name: `crypto-mnav-tracker`
   - Description: "Real-time mNAV tracker for crypto treasury companies"
   - Public or Private: Your choice
   - Don't initialize with README (we already have files)

2. **Initialize Git Locally**
   ```bash
   cd crypto_mnav_tracker
   git init
   git add .
   git commit -m "Initial commit: Crypto Treasury mNAV Tracker"
   ```

3. **Add Remote and Push**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/crypto-mnav-tracker.git
   git branch -M main
   git push -u origin main
   ```

### Updating After Changes:

```bash
git add .
git commit -m "Description of changes"
git push
```

---

## Environment Variables

The app currently doesn't require any environment variables, but if you add features like API keys, set them in your platform:

### Render:
- Go to Dashboard → Environment → Add Environment Variable

### Railway:
- Go to Variables tab → Add Variable

### Heroku:
```bash
heroku config:set VARIABLE_NAME=value
```

### Fly.io:
```bash
fly secrets set VARIABLE_NAME=value
```

---

## Post-Deployment Checklist

After deploying, verify:

- [ ] App loads successfully
- [ ] Crypto prices are fetching (BTC, ETH, SOL)
- [ ] Company tiles are displaying
- [ ] Market cap data is loading
- [ ] mNAV calculations are correct
- [ ] Website links work
- [ ] News links work
- [ ] Auto-refresh works (wait 60 seconds)
- [ ] Responsive on mobile devices

---

## Custom Domain (Optional)

All platforms support custom domains:

### Render:
1. Go to Settings → Custom Domain
2. Add your domain
3. Update DNS records as shown

### Railway:
1. Settings → Domains → Custom Domain
2. Add CNAME record to your DNS

### Heroku:
```bash
heroku domains:add www.yourdomain.com
```

### Fly.io:
```bash
fly certs add yourdomain.com
```

---

## Monitoring & Logs

### View Logs:

**Render**: Dashboard → Logs tab

**Railway**: Deployments → Click deployment → Logs

**Heroku**:
```bash
heroku logs --tail
```

**Fly.io**:
```bash
fly logs
```

---

## Scaling (If Needed)

### Render:
- Upgrade to paid plan
- Settings → Instance Type

### Railway:
- Resources auto-scale
- Set limits in Settings

### Heroku:
```bash
heroku ps:scale web=2
```

### Fly.io:
```bash
fly scale count 2
```

---

## Troubleshooting

### App Won't Start

1. Check logs for errors
2. Verify requirements.txt has all dependencies
3. Ensure Python version compatibility
4. Check that PORT environment variable is used (platforms set this automatically)

### API Errors

1. Check if CoinGecko API is accessible
2. Verify yfinance can access Yahoo Finance
3. Check for rate limiting issues

### Slow Performance

1. Check if on free tier (may sleep/spin down)
2. Upgrade to paid tier for better performance
3. Consider caching crypto prices (future enhancement)

---

## Cost Estimates

| Platform | Free Tier | Paid (Always-On) |
|----------|-----------|------------------|
| Render | ✅ Yes (sleeps) | $7/month |
| Railway | $5 credit/month | ~$5/month |
| Heroku | ❌ No | $7/month |
| Fly.io | ✅ Yes (limits) | ~$5/month |

**Recommendation**: Start with Render's free tier, upgrade if needed.

---

## Beta Testing

For beta testing:

1. Deploy to a platform with free tier (Render recommended)
2. Share the URL with beta testers
3. Collect feedback via:
   - GitHub Issues
   - Google Forms
   - Discord/Slack channel
4. Monitor logs for errors
5. Track usage and performance

---

## Continuous Deployment

All platforms support automatic deployment from GitHub:

1. Push changes to GitHub main branch
2. Platform automatically rebuilds and deploys
3. No manual intervention needed

---

## Security Notes

- App has no authentication (public dashboard)
- No sensitive data stored
- Uses only public APIs
- HTTPS enabled by default on all platforms
- Consider adding rate limiting for production

---

## Future Enhancements for Production

1. **Caching**: Cache crypto prices to reduce API calls
2. **Database**: Store historical mNAV data
3. **Admin Panel**: Update holdings without code changes
4. **Analytics**: Track page views and user interactions
5. **Alerts**: Set up error monitoring (Sentry, etc.)
6. **CDN**: Serve static assets via CDN
7. **API Rate Limiting**: Prevent abuse

---

## Support

For deployment issues:
- Check platform-specific documentation
- Review application logs
- Open GitHub issue for app-specific problems

---

*Last Updated: November 8, 2025*
