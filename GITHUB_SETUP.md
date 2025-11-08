# GitHub Setup Instructions

## Quick Start - Push to GitHub

Your repository has been initialized and all files have been committed locally. Follow these steps to push to GitHub:

### Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Fill in the details:
   - **Repository name**: `crypto-mnav-tracker` (or your preferred name)
   - **Description**: "Real-time mNAV tracker for Bitcoin, Ethereum, and Solana treasury companies"
   - **Visibility**: Public (recommended) or Private
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
3. Click "Create repository"

### Step 2: Push Your Code

After creating the repository, GitHub will show you commands. Use these commands:

```bash
cd crypto_mnav_tracker
git remote add origin https://github.com/YOUR_USERNAME/crypto-mnav-tracker.git
git branch -M main
git push -u origin main
```

**Replace `YOUR_USERNAME` with your actual GitHub username!**

### Alternative: Using SSH

If you prefer SSH (requires SSH key setup):

```bash
cd crypto_mnav_tracker
git remote add origin git@github.com:YOUR_USERNAME/crypto-mnav-tracker.git
git branch -M main
git push -u origin main
```

---

## Already Pushed? Update Your Repository

If you've already pushed and made changes:

```bash
cd crypto_mnav_tracker
git add .
git commit -m "Description of your changes"
git push
```

---

## What's Been Included

Your repository contains:

### Core Application
- `app.py` - Main Flask application
- `templates/index.html` - Web interface
- `requirements.txt` - Python dependencies

### Documentation
- `README.md` - Project overview and features
- `DATA_SOURCES.md` - Comprehensive data source documentation
- `DEPLOYMENT.md` - Deployment instructions for multiple platforms
- `SAMPLE_OUTPUT.md` - Sample data and interpretations
- `MULTI_CRYPTO_SAMPLE.md` - Multi-crypto sample output

### Deployment Files
- `Procfile` - Heroku deployment
- `render.yaml` - Render deployment
- `runtime.txt` - Python version specification
- `.gitignore` - Files to exclude from Git

### Utilities
- `start.bat` - Windows startup script

---

## Features Included

✅ Bitcoin (BTC) treasury tracking - 13 companies
✅ Ethereum (ETH) treasury tracking - 6 companies
✅ Solana (SOL) treasury tracking - 7 companies
✅ Real-time crypto prices from CoinGecko
✅ Live market cap data from Yahoo Finance
✅ Automatic mNAV calculation
✅ Neon cyberpunk UI with auto-refresh
✅ Clickable website and news links for each company
✅ Color-coded mNAV indicators
✅ Responsive design
✅ Ready for deployment to Render, Railway, Heroku, or Fly.io

---

## Next Steps After Pushing to GitHub

### 1. Deploy to Production

See `DEPLOYMENT.md` for detailed instructions. Quick start:

**Render (Recommended - Free Tier):**
1. Go to https://render.com
2. Sign in with GitHub
3. New → Web Service
4. Select your `crypto-mnav-tracker` repository
5. Click "Create Web Service"

**Railway:**
1. Go to https://railway.app
2. Sign in with GitHub
3. New Project → Deploy from GitHub
4. Select your repository

### 2. Customize

Edit `app.py` to:
- Add more companies
- Update holdings data
- Add new cryptocurrencies

### 3. Share

- Share your repository URL with collaborators
- Enable GitHub Issues for bug reports
- Add contributors via Settings → Collaborators

---

## Updating Holdings Data

Holdings data is static in `app.py`. To update:

1. Edit the `TREASURY_COMPANIES` list in `app.py`
2. Update company holdings, add new companies, or remove companies
3. Commit and push:
   ```bash
   git add app.py
   git commit -m "Update crypto holdings data"
   git push
   ```
4. If deployed, the platform will auto-deploy the changes

---

## Repository Settings (Recommended)

After pushing, configure your repository:

1. **Add Topics** (for discoverability):
   - Settings → Topics
   - Add: `bitcoin`, `ethereum`, `solana`, `crypto`, `flask`, `python`, `mnav`, `treasury`

2. **Add a Website URL**:
   - Settings → Website
   - Add your deployed URL (after deployment)

3. **Enable Issues**:
   - Already enabled by default
   - Users can report bugs or request features

4. **Add a License** (optional):
   - Add file → LICENSE
   - Suggested: MIT License

---

## Troubleshooting

### Permission Denied

If you get "Permission denied (publickey)":
- Use HTTPS instead of SSH: `https://github.com/USERNAME/repo.git`
- Or set up SSH keys: https://docs.github.com/en/authentication

### Authentication Failed

For HTTPS, use a Personal Access Token instead of password:
1. GitHub → Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Select `repo` scope
4. Use token as password when prompted

### Repository Already Exists

If you already created a repo with a README:
```bash
git pull origin main --allow-unrelated-histories
git push -u origin main
```

---

## GitHub Actions (Future Enhancement)

Consider adding GitHub Actions for:
- Automated testing
- Automatic data updates
- Deployment automation
- Code quality checks

Example workflow location: `.github/workflows/deploy.yml`

---

## Star Your Repository!

Don't forget to star your own repository to keep it easily accessible!

---

## Support

For Git/GitHub help:
- GitHub Docs: https://docs.github.com
- Git Documentation: https://git-scm.com/doc

For app-specific questions:
- Open an issue on your repository
- Check DEPLOYMENT.md for deployment issues

---

**Ready to push? Run the commands from Step 2 above!**

*Last Updated: November 8, 2025*
