# Crypto Treasury mNAV Tracker

A real-time web dashboard displaying the mNAV (Market cap to Net Asset Value) ratio for publicly traded companies holding Bitcoin, Ethereum, and Solana in their treasuries.

## What is mNAV?

mNAV = (Crypto Holdings Value) / (Market Cap)

This ratio shows how much of a company's market capitalization is backed by their crypto holdings:
- **< 0.5x**: Low crypto backing (red)
- **0.5x - 1.0x**: Medium crypto backing (yellow)
- **1.0x - 2.0x**: High crypto backing (green)
- **> 2.0x**: Very high crypto backing (cyan)

## Features

- Real-time price tracking for Bitcoin, Ethereum, and Solana
- Live market cap data for 26+ crypto treasury companies
- Multi-cryptocurrency support (BTC, ETH, SOL)
- Color-coded crypto badges for easy identification
- Auto-refreshing dashboard (updates every 60 seconds)
- Neon-styled cyberpunk UI with glowing effects
- Responsive grid layout
- Sorted by mNAV ratio (highest first)

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

## Companies Tracked

The dashboard tracks crypto holdings across three major cryptocurrencies:

### Bitcoin (BTC) - 13 Companies
- Strategy (formerly MicroStrategy) - MSTR
- MARA Holdings - MARA
- XXI - CEP
- Metaplanet - MTPLF
- Bitcoin Standard Treasury - CEPO
- Riot Platforms - RIOT
- Tesla - TSLA
- And more...

### Ethereum (ETH) - 6 Companies
- BitMine Immersion - BMNR
- SharpLink Gaming - SBET
- Bit Digital - BTBT
- Coinbase Global - COIN
- BTCS Inc - BTCS
- Galaxy Digital - GLXY

### Solana (SOL) - 7 Companies
- Forward Industries - FORD
- Helius Medical - HSDT
- DeFi Development - DFDV
- Upexi Inc - UPXI
- Sol Strategies - HODL
- Classover - CLSO
- Torrent Capital - TORR

## Data Sources

- **Crypto Prices (BTC/ETH/SOL)**: CoinGecko API (free, no API key required)
- **Market Cap**: Yahoo Finance via yfinance library (free, no API key required)
- **Crypto Holdings**: Manually curated from multiple sources:
  - BitcoinTreasuries.net
  - CoinGecko Treasury pages
  - Company SEC filings and press releases
  - See **DATA_SOURCES.md** for complete documentation

## Notes

- Market cap data may not be available for all tickers (especially OTC/international stocks)
- Crypto holdings data is static and must be updated manually in the code
- Holdings data sourced from company filings, BitcoinTreasuries.net, and CoinGecko
- The application includes a small delay between API calls to avoid rate limiting
- Auto-refresh happens every 60 seconds to stay within API rate limits
- For detailed information about data sources, see **DATA_SOURCES.md**

## Customization

To add or update companies, edit the `TREASURY_COMPANIES` list in `app.py`:

```python
TREASURY_COMPANIES = [
    {"name": "Company Name", "ticker": "TICK", "crypto": "BTC", "holdings": 12345},
    {"name": "Another Company", "ticker": "ANTH", "crypto": "ETH", "holdings": 67890},
    {"name": "SOL Company", "ticker": "SOLC", "crypto": "SOL", "holdings": 100000},
    # Add more companies here
]
```

**Supported crypto values**: `"BTC"`, `"ETH"`, `"SOL"`

## Troubleshooting

If you encounter rate limiting issues:
- Increase the `time.sleep()` value in `app.py`
- Increase the auto-refresh interval in `index.html` (currently 60000ms)

If market cap data is not loading for certain tickers:
- Verify the ticker symbol is correct
- Some international stocks may require different API endpoints
