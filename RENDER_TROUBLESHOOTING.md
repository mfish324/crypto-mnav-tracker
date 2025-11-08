# Render Deployment Troubleshooting

## Check Auto-Deploy Settings

### Step 1: Verify Auto-Deploy is Enabled

1. Go to your Render Dashboard: https://dashboard.render.com
2. Click on your `crypto-mnav-tracker` service
3. Click **"Settings"** tab (left sidebar)
4. Scroll down to **"Build & Deploy"** section
5. Look for **"Auto-Deploy"** setting:
   - Should be set to **"Yes"**
   - If it says "No", click "Edit" and change to "Yes"

### Step 2: Check GitHub Connection

1. In Settings tab, look for **"Branch"** setting
2. Verify it's set to: `main`
3. Check **"Repository"** shows: `mfish324/crypto-mnav-tracker`

### Step 3: Manual Deploy (If Auto-Deploy Doesn't Work)

1. Go to your service dashboard
2. Click **"Manual Deploy"** button (top right)
3. Select **"Deploy latest commit"**
4. Click **"Deploy"**

This will force a new deployment with the latest code.

## Check Deployment Logs

1. Click **"Logs"** tab (left sidebar)
2. Look for errors in the build process
3. Common errors:
   - Dependency installation failures
   - Python version mismatches
   - Import errors

## Verify GitHub Webhook

1. Go to your GitHub repo: https://github.com/mfish324/crypto-mnav-tracker
2. Click **"Settings"** tab
3. Click **"Webhooks"** (left sidebar)
4. You should see a webhook for Render
5. Check:
   - Recent Deliveries - should show recent pushes
   - Response should be 200 OK

If no webhook exists:
- Render needs permission to add webhooks
- Re-authorize Render's GitHub access

## Re-connect GitHub (If Needed)

1. Render Dashboard → Account Settings
2. Click **"Connections"**
3. Find **"GitHub"**
4. Click **"Disconnect"** then **"Reconnect"**
5. Re-authorize with all permissions

## Force Deployment Commands

From your local machine:
```bash
# Make a small change to force deployment
cd crypto_mnav_tracker
git commit --allow-empty -m "Trigger Render deployment"
git push origin main
```

Or use Manual Deploy button in Render dashboard.

## Check Service Status

In Render Dashboard:
- **Events** tab shows all deployments
- Look for "Deploy triggered" events
- Check timestamps match your git pushes

## Contact Points

- Render Status: https://status.render.com
- Render Docs: https://render.com/docs
- Check if there are any ongoing incidents
