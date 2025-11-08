"""
Crypto Treasury Companies mNAV Tracker
Displays market cap to crypto holdings ratio for public companies holding Bitcoin, Ethereum, and Solana
"""

from flask import Flask, render_template, jsonify
import requests
from datetime import datetime
import time
import yfinance as yf

app = Flask(__name__)

# Crypto treasury companies data
# Format: {"name": str, "ticker": str, "crypto": str, "holdings": float, "website": str}
TREASURY_COMPANIES = [
    # Bitcoin Holdings
    {"name": "Strategy", "ticker": "MSTR", "crypto": "BTC", "holdings": 641205, "website": "https://www.microstrategy.com"},
    {"name": "MARA Holdings", "ticker": "MARA", "crypto": "BTC", "holdings": 53250, "website": "https://www.mara.com"},
    {"name": "XXI", "ticker": "CEP", "crypto": "BTC", "holdings": 43514, "website": "https://21.capital"},
    {"name": "Metaplanet", "ticker": "MTPLF", "crypto": "BTC", "holdings": 30823, "website": "https://www.metaplanet.co.jp"},
    {"name": "Bitcoin Standard Treasury", "ticker": "CEPO", "crypto": "BTC", "holdings": 30021, "website": "https://www.cepoworld.com"},
    {"name": "Bullish", "ticker": "BLSH", "crypto": "BTC", "holdings": 24300, "website": "https://bullish.com"},
    {"name": "Riot Platforms", "ticker": "RIOT", "crypto": "BTC", "holdings": 19324, "website": "https://www.riotplatforms.com"},
    {"name": "Trump Media & Tech", "ticker": "DJT", "crypto": "BTC", "holdings": 15000, "website": "https://www.tmtgcorp.com"},
    {"name": "Hut 8 Mining", "ticker": "HUT", "crypto": "BTC", "holdings": 13696, "website": "https://hut8.com"},
    {"name": "CleanSpark", "ticker": "CLSK", "crypto": "BTC", "holdings": 13011, "website": "https://www.cleanspark.com"},
    {"name": "Tesla", "ticker": "TSLA", "crypto": "BTC", "holdings": 11509, "website": "https://www.tesla.com"},
    {"name": "Block", "ticker": "SQ", "crypto": "BTC", "holdings": 8780, "website": "https://www.block.xyz"},
    {"name": "GD Culture Group", "ticker": "GDC", "crypto": "BTC", "holdings": 7500, "website": "https://www.gdculturegroup.com"},

    # Ethereum Holdings
    {"name": "BitMine Immersion", "ticker": "BMNR", "crypto": "ETH", "holdings": 2069443, "website": "https://www.bitmineimmersion.com"},
    {"name": "SharpLink Gaming", "ticker": "SBET", "crypto": "ETH", "holdings": 740760, "website": "https://www.sharplinkgaming.com"},
    {"name": "Bit Digital", "ticker": "BTBT", "crypto": "ETH", "holdings": 150244, "website": "https://www.bitdigital.com"},
    {"name": "Coinbase Global", "ticker": "COIN", "crypto": "ETH", "holdings": 137334, "website": "https://www.coinbase.com"},
    {"name": "BTCS Inc", "ticker": "BTCS", "crypto": "ETH", "holdings": 70140, "website": "https://www.btcs.com"},
    {"name": "Galaxy Digital", "ticker": "GLXY", "crypto": "ETH", "holdings": 50000, "website": "https://www.galaxydigital.io"},

    # Solana Holdings
    {"name": "Forward Industries", "ticker": "FORD", "crypto": "SOL", "holdings": 6822000, "website": "https://www.forwardindustries.com"},
    {"name": "Helius Medical", "ticker": "HSDT", "crypto": "SOL", "holdings": 2200000, "website": "https://www.heliusmedical.com"},
    {"name": "DeFi Development", "ticker": "DFDV", "crypto": "SOL", "holdings": 2100000, "website": "https://defidevelopmentcorp.com"},
    {"name": "Upexi Inc", "ticker": "UPXI", "crypto": "SOL", "holdings": 2000000, "website": "https://www.upexi.com"},
    {"name": "Sol Strategies", "ticker": "HODL", "crypto": "SOL", "holdings": 370000, "website": "https://solstrategies.com"},
    {"name": "Classover", "ticker": "CLSO", "crypto": "SOL", "holdings": 52067, "website": "https://www.classover.com"},
    {"name": "Torrent Capital", "ticker": "TORR", "crypto": "SOL", "holdings": 40039, "website": "https://www.torrentcapital.com"},
]


def get_crypto_prices():
    """Fetch current prices for Bitcoin, Ethereum, and Solana from CoinGecko API"""
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return {
            'BTC': data.get('bitcoin', {}).get('usd'),
            'ETH': data.get('ethereum', {}).get('usd'),
            'SOL': data.get('solana', {}).get('usd')
        }
    except Exception as e:
        print(f"Error fetching crypto prices: {e}")
        return {'BTC': None, 'ETH': None, 'SOL': None}


def get_market_cap(ticker):
    """Fetch market cap for a given ticker using yfinance library"""
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        # Try to get market cap from info
        market_cap = info.get('marketCap', None)

        if market_cap and market_cap > 0:
            return market_cap

        return None
    except Exception as e:
        print(f"Error fetching market cap for {ticker}: {e}")
        return None


def calculate_mnav(holdings, crypto_price, market_cap):
    """Calculate mNAV: (Crypto Holdings Value) / (Market Cap)"""
    if market_cap and market_cap > 0 and crypto_price:
        crypto_value = holdings * crypto_price
        mnav = crypto_value / market_cap
        return mnav
    return None


@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')


@app.route('/api/mnav-data')
def get_mnav_data():
    """API endpoint to get mNAV data for all companies"""
    crypto_prices = get_crypto_prices()

    if not any(crypto_prices.values()):
        return jsonify({"error": "Unable to fetch crypto prices"}), 500

    results = []

    for company in TREASURY_COMPANIES:
        # Add a small delay to avoid rate limiting
        time.sleep(0.1)

        crypto_type = company['crypto']
        crypto_price = crypto_prices.get(crypto_type)
        holdings = company['holdings']

        market_cap = get_market_cap(company['ticker'])
        mnav = calculate_mnav(holdings, crypto_price, market_cap)

        results.append({
            'name': company['name'],
            'ticker': company['ticker'],
            'crypto': crypto_type,
            'holdings': holdings,
            'crypto_value': holdings * crypto_price if crypto_price else None,
            'market_cap': market_cap,
            'mnav': mnav,
            'mnav_percentage': mnav * 100 if mnav else None,
            'website': company.get('website', '')
        })

    return jsonify({
        'timestamp': datetime.now().isoformat(),
        'crypto_prices': crypto_prices,
        'companies': results
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
