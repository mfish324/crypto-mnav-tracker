# Daily Holdings Update Process

This guide explains how to keep crypto holdings data current.

## Important Note

**Holdings data is static** and stored in `app.py`. While prices and market caps update automatically, crypto holdings must be updated manually because:
- No free API provides real-time treasury holdings
- Companies announce purchases at different times
- Data comes from SEC filings, press releases, and company announcements

---

## Quick Update Process (5-10 minutes)

### Step 1: Check for New Holdings Data

Visit these sources to see if companies have announced new purchases:

**Bitcoin:**
- https://bitcointreasuries.net/
- https://www.coingecko.com/en/treasuries/bitcoin
- Company Twitter/X accounts
- SEC Edgar filings

**Ethereum:**
- https://www.coingecko.com/en/treasuries/ethereum

**Solana:**
- https://www.coingecko.com/en/treasuries/solana

### Step 2: Update app.py

If you find new data:

1. Open `app.py`
2. Find the `TREASURY_COMPANIES` list (line ~25)
3. Update the `holdings` value for the company
4. Update the "Last verified" date in the comment

**Example:**
```python
# Before
{"name": "Strategy", "ticker": "MSTR", "crypto": "BTC", "holdings": 641205, ...}

# After (if they bought more)
{"name": "Strategy", "ticker": "MSTR", "crypto": "BTC", "holdings": 650000, ...}
```

### Step 3: Log the Update

```bash
python update_holdings.py
```

This script will:
- Guide you through the update process
- Create a log entry
- Show you the git commands to run

### Step 4: Deploy

```bash
git add app.py holdings_update_log.json
git commit -m "Update holdings data - $(date +%Y-%m-%d)"
git push origin main
```

Render will automatically deploy the changes (or click Manual Deploy).

---

## Recommended Update Schedule

| Crypto | Frequency | Reason |
|--------|-----------|--------|
| Bitcoin | Weekly | MicroStrategy and others buy frequently |
| Ethereum | Bi-weekly | Less frequent announcements |
| Solana | Bi-weekly | Newer trend, less frequent |

---

## Setting Up Daily Reminders

### Option 1: Calendar Reminder

Set a daily calendar reminder:
- **Time:** 9 AM (after market open)
- **Task:** "Check crypto treasury updates"
- **Duration:** 10 minutes
- **Link:** Add link to this file

### Option 2: GitHub Actions (Automated Reminder)

Create `.github/workflows/update-reminder.yml`:

```yaml
name: Holdings Update Reminder

on:
  schedule:
    - cron: '0 13 * * 1-5'  # 9 AM EST, weekdays

jobs:
  remind:
    runs-on: ubuntu-latest
    steps:
      - name: Create Issue
        uses: actions/github-script@v6
        with:
          script: |
            github.rest.issues.create({
              owner: context.repo.owner,
              repo: context.repo.repo,
              title: 'Weekly Holdings Update Reminder',
              body: 'Time to check for crypto holdings updates!\n\n[Update Guide](./DAILY_UPDATE_PROCESS.md)'
            })
```

This creates a GitHub issue every Monday reminding you to update.

### Option 3: Automated Scraping (Advanced)

For fully automated updates, you would need to:
1. Build web scrapers for each data source
2. Run them on a schedule (GitHub Actions / cron job)
3. Automatically create PRs with updates

**Note:** This is more complex and requires maintenance as websites change.

---

## Tracking Updates

### View Update History

Check `holdings_update_log.json` to see when data was last verified:

```bash
cat holdings_update_log.json
```

### Add to README

Add a badge showing last update:

```markdown
![Holdings Updated](https://img.shields.io/badge/Holdings%20Updated-2025--11--08-brightgreen)
```

---

## What Gets Updated Automatically vs Manually

### ✅ Automatic (No Action Needed)

- Crypto prices (BTC, ETH, SOL) - Every 60 seconds
- Market caps - Every page load
- mNAV calculations - Computed in real-time

### 📝 Manual (Requires Update)

- Crypto holdings amounts
- Company list (adding/removing companies)
- Company websites

---

## Automation Options (Future Enhancements)

If you want to reduce manual work:

### Option A: API Integration

**Paid Services:**
- CoinGecko Pro API ($129/month) - Has treasury data
- Messari API - Enterprise features
- Custom data providers

**Setup:**
- Subscribe to service
- Add API key to environment variables
- Update code to fetch from API instead of static data

### Option B: Web Scraping

**What you'd need:**
- Python scraping libraries (BeautifulSoup, Scrapy)
- GitHub Actions for scheduling
- Error handling for website changes

**Maintenance:**
- Update scrapers when sites change
- Handle rate limiting
- Verify data accuracy

### Option C: Manual with Notifications

**Current setup:**
- You manually check and update
- Takes 5-10 minutes per week
- Most reliable and accurate

---

## Quick Reference Commands

```bash
# Check current holdings in app.py
grep "holdings:" app.py

# Run update script
python update_holdings.py

# Commit changes
git add app.py holdings_update_log.json
git commit -m "Update holdings - $(date +%Y-%m-%d)"
git push origin main

# View update log
cat holdings_update_log.json | python -m json.tool
```

---

## Troubleshooting

### How do I know if data is outdated?

Check the "Last verified" comment in `app.py`:
```python
# Last verified: 2025-11-08
```

If it's more than a week old, time to update!

### Where do companies announce purchases?

- **SEC Filings:** 8-K forms (immediate), 10-Q (quarterly)
- **Press Releases:** Company investor relations pages
- **Social Media:** Twitter/X, especially CEO accounts
- **Aggregators:** BitcoinTreasuries.net, CoinGecko

### What if I miss an update?

No problem! The app still works with slightly outdated holdings. The mNAV calculations will just be based on old holdings numbers until you update.

---

## Contributing

If you find updated holdings data:
1. Create a GitHub issue with the source
2. Or submit a PR with the update
3. Include the source/link where you found the data

---

**Last updated:** November 8, 2025
