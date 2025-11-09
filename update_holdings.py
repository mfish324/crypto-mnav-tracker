"""
Script to help update crypto holdings for treasury companies
Run this daily to keep holdings data current
"""

import json
from datetime import datetime

# Instructions for updating holdings:
# 1. Check company announcements/filings
# 2. Update the holdings data below
# 3. Run this script: python update_holdings.py
# 4. Commit and push changes to GitHub

HOLDINGS_UPDATE_SOURCES = {
    "BTC": [
        "https://bitcointreasuries.net/",
        "https://www.coingecko.com/en/treasuries/bitcoin"
    ],
    "ETH": [
        "https://www.coingecko.com/en/treasuries/ethereum"
    ],
    "SOL": [
        "https://www.coingecko.com/en/treasuries/solana"
    ]
}

def print_update_guide():
    """Print guide for updating holdings"""
    print("=" * 60)
    print("CRYPTO TREASURY HOLDINGS UPDATE GUIDE")
    print("=" * 60)
    print()
    print("To update holdings data:")
    print()
    print("1. Check these sources for latest data:")
    for crypto, sources in HOLDINGS_UPDATE_SOURCES.items():
        print(f"\n   {crypto}:")
        for source in sources:
            print(f"   - {source}")

    print()
    print("2. Update holdings in app.py TREASURY_COMPANIES list")
    print()
    print("3. Run: git add app.py")
    print("   Run: git commit -m \"Update holdings data - [date]\"")
    print("   Run: git push origin main")
    print()
    print("4. Render will auto-deploy (or manual deploy)")
    print()
    print("=" * 60)
    print()
    print("Current data last updated: [Check app.py comments]")
    print()
    print("Recommended update frequency:")
    print("  - Bitcoin holdings: Weekly (active buyers)")
    print("  - Ethereum holdings: Bi-weekly")
    print("  - Solana holdings: Bi-weekly")
    print()
    print("=" * 60)

def create_update_log():
    """Create a log entry for this update"""
    timestamp = datetime.now().isoformat()
    log_entry = {
        "timestamp": timestamp,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "note": "Holdings data reviewed and updated"
    }

    try:
        with open('holdings_update_log.json', 'r') as f:
            log = json.load(f)
    except FileNotFoundError:
        log = []

    log.append(log_entry)

    # Keep only last 30 updates
    log = log[-30:]

    with open('holdings_update_log.json', 'w') as f:
        json.dump(log, f, indent=2)

    print(f"✅ Update logged: {log_entry['date']}")

if __name__ == "__main__":
    print_update_guide()

    response = input("Have you updated the holdings in app.py? (yes/no): ").strip().lower()

    if response == "yes":
        create_update_log()
        print()
        print("✅ Update complete!")
        print("📝 Next steps:")
        print("   1. git add app.py holdings_update_log.json")
        print(f"   2. git commit -m \"Update holdings data - {datetime.now().strftime('%Y-%m-%d')}\"")
        print("   3. git push origin main")
    else:
        print()
        print("❌ Please update holdings in app.py first, then run this script again.")
