# Data Sources Documentation

This document provides detailed information about all data sources used in the Crypto Treasury mNAV Tracker application.

## Overview

The application aggregates data from multiple sources to calculate and display mNAV (Market cap to Net Asset Value) ratios for publicly traded companies holding cryptocurrency in their treasuries.

---

## 1. Cryptocurrency Price Data

### Source: CoinGecko API
- **Endpoint**: `https://api.coingecko.com/api/v3/simple/price`
- **API Type**: Free, public API (no API key required)
- **Update Frequency**: Real-time (updated every 60 seconds in the app)
- **Cryptocurrencies Tracked**:
  - Bitcoin (BTC)
  - Ethereum (ETH)
  - Solana (SOL)

### Implementation Details
- **Function**: `get_crypto_prices()` in `app.py`
- **Data Format**: Returns USD prices for all three cryptocurrencies
- **Error Handling**: Returns None values if API call fails
- **Rate Limiting**: No explicit rate limits for this endpoint, but we add 0.1s delays between requests

### Example Response
```json
{
  "bitcoin": {"usd": 102086},
  "ethereum": {"usd": 3500},
  "solana": {"usd": 225}
}
```

### Why CoinGecko?
- Well-established cryptocurrency data aggregator
- Free tier available without API key
- Reliable uptime and data accuracy
- Aggregates prices from multiple exchanges

---

## 2. Market Cap Data

### Source: Yahoo Finance (via yfinance library)
- **Library**: `yfinance` v0.2.28+
- **Data Type**: Real-time stock market data
- **API Type**: Unofficial Yahoo Finance API wrapper
- **Update Frequency**: Delayed 15-20 minutes (standard for free market data)

### Implementation Details
- **Function**: `get_market_cap(ticker)` in `app.py`
- **Data Retrieved**: Company market capitalization in USD
- **Method**: Creates a `yf.Ticker()` object and accesses `.info` dictionary
- **Timeout**: 10 seconds per request
- **Error Handling**: Returns None if ticker not found or data unavailable

### Example Code
```python
stock = yf.Ticker("MSTR")
info = stock.info
market_cap = info.get('marketCap', None)
```

### Limitations
- Some international tickers may not be available
- OTC (Over-The-Counter) stocks may have limited data
- Data is delayed, not real-time
- Some tickers may require different exchanges (e.g., ".TO" for Toronto)

### Why Yahoo Finance?
- Free access without API keys
- Comprehensive coverage of US and international stocks
- Well-maintained yfinance library
- Provides market cap directly without calculations

---

## 3. Crypto Holdings Data

### Source: Manual Curation from Multiple Sources

The crypto holdings data is manually maintained in `app.py` in the `TREASURY_COMPANIES` list. This data is sourced from:

#### Primary Sources:

1. **BitcoinTreasuries.net**
   - URL: https://bitcointreasuries.net/
   - Coverage: Bitcoin holdings
   - Update Frequency: Updated regularly by community
   - Reliability: Community-maintained, cross-referenced with company filings

2. **CoinGecko Treasuries**
   - Bitcoin: https://www.coingecko.com/en/treasuries/bitcoin
   - Ethereum: https://www.coingecko.com/en/treasuries/ethereum
   - Solana: https://www.coingecko.com/en/treasuries/solana
   - Coverage: All three cryptocurrencies
   - Reliability: Professional tracking service

3. **Company SEC Filings & Press Releases**
   - Direct source: 10-Q, 10-K, 8-K filings
   - Most accurate but requires manual checking
   - Examples:
     - MicroStrategy (now Strategy) quarterly reports
     - Tesla earnings calls
     - Mining company investor updates

#### Secondary Sources:

4. **CoinMarketCap Charts**
   - URL: https://coinmarketcap.com/charts/bitcoin-treasuries/
   - Coverage: Primarily Bitcoin

5. **Decrypt / Cointelegraph News**
   - Used for recent announcements and updates
   - Cross-referenced with official sources

### Data Structure
```python
{
    "name": "Company Name",
    "ticker": "TICK",  # Stock ticker symbol
    "crypto": "BTC",   # BTC, ETH, or SOL
    "holdings": 12345  # Amount of crypto held
}
```

### Bitcoin Holdings Sources

Data for the following companies sourced from BitcoinTreasuries.net and company filings:

- **Strategy (MSTR)**: 641,205 BTC - From Q3 2025 investor update
- **MARA Holdings**: 53,250 BTC - July 2025 social media update
- **XXI (CEP)**: 43,514 BTC - Company treasury report
- **Metaplanet (MTPLF)**: 30,823 BTC - September 2025 announcement
- **Bitcoin Standard Treasury (CEPO)**: 30,021 BTC - Company filings
- **Bullish (BLSH)**: 24,300 BTC - August 2025 IPO filing
- **Riot Platforms (RIOT)**: 19,324 BTC - Monthly production report
- **Trump Media & Tech (DJT)**: 15,000 BTC - Corporate announcement
- **Hut 8 Mining (HUT)**: 13,696 BTC - Quarterly report
- **CleanSpark (CLSK)**: 13,011 BTC - Company investor update
- **Tesla (TSLA)**: 11,509 BTC - Q2 2025 10-Q filing
- **Block (SQ)**: 8,780 BTC - Annual report
- **GD Culture Group (GDC)**: 7,500 BTC - Company filing

### Ethereum Holdings Sources

Data sourced from CoinGecko Ethereum Treasuries and company press releases:

- **BitMine Immersion (BMNR)**: 2,069,443 ETH - September 2025 announcement
- **SharpLink Gaming (SBET)**: 740,760 ETH - August 2025 investor update
- **Bit Digital (BTBT)**: 150,244 ETH - October 2025 quarterly report
- **Coinbase Global (COIN)**: 137,334 ETH - March 2025 10-K filing
- **BTCS Inc (BTCS)**: 70,140 ETH - Company balance sheet
- **Galaxy Digital (GLXY)**: 50,000 ETH (estimated) - Company reports

### Solana Holdings Sources

Data sourced from CoinGecko Solana Treasuries and recent company announcements:

- **Forward Industries (FORD)**: 6,822,000 SOL - September 2025 PIPE announcement
- **Helius Medical (HSDT)**: 2,200,000 SOL - August 2025 purchase announcement
- **DeFi Development (DFDV)**: 2,100,000 SOL - Q2 2025 report
- **Upexi Inc (UPXI)**: 2,000,000 SOL - August 2025 advisory committee report
- **Sol Strategies (HODL)**: 370,000 SOL - August 2025 validator update
- **Classover (CLSO)**: 52,067 SOL - July 2025 announcement
- **Torrent Capital (TORR)**: 40,039 SOL - April 2025 filing

### Data Freshness and Accuracy

**Important Notes:**
1. **Holdings data is static** in the application code and requires manual updates
2. **Last verified**: November 2025
3. **Update responsibility**: Developers must periodically update the `TREASURY_COMPANIES` list
4. **Accuracy**: Cross-referenced from multiple sources where possible
5. **Volatility**: Companies frequently buy/sell crypto, so data can become outdated quickly

### Recommended Update Frequency
- **Bitcoin holdings**: Monthly (companies often announce monthly)
- **Ethereum holdings**: Quarterly (less frequent announcements)
- **Solana holdings**: Quarterly to Semi-annually (newer trend)

---

## 4. Calculated Metrics

### mNAV (Market cap to Net Asset Value)

**Formula:**
```
mNAV = Market Capitalization / (Crypto Holdings × Crypto Price)
```

**Calculation Function:** `calculate_mnav()` in `app.py`

**Example:**
- Company: Strategy (MSTR)
- BTC Holdings: 641,205 BTC
- BTC Price: $102,086
- Crypto Value: 641,205 × $102,086 = $65,458,053,630
- Market Cap: $69,519,482,880
- mNAV = $69,519,482,880 / $65,458,053,630 = 1.06x or 106%

**Interpretation:**
- **> 2.0x**: Trading at high premium - market cap more than 2x crypto value (Cyan)
- **1.0x - 2.0x**: Trading at premium - market cap exceeds crypto value (Green)
- **0.5x - 1.0x**: Trading at discount - market cap is 50-100% of crypto value (Yellow)
- **< 0.5x**: Trading at deep discount - market cap less than 50% of crypto value (Red)

---

## 5. Data Refresh Schedule

### In Application
- **Crypto Prices**: Fetched on every page load and auto-refresh (60 seconds)
- **Market Caps**: Fetched on every page load and auto-refresh (60 seconds)
- **Holdings Data**: Static, requires code update
- **mNAV Calculation**: Real-time based on latest price and market cap

### Manual Updates Required
Developers should update the `TREASURY_COMPANIES` list when:
1. Companies announce new crypto purchases
2. Companies sell crypto holdings
3. New companies announce treasury strategies
4. Companies change ticker symbols or names

---

## 6. Data Limitations and Disclaimers

### Accuracy
- **Holdings data may be outdated**: Companies buy/sell crypto between announcements
- **Market cap is delayed**: 15-20 minute delay on free market data
- **International stocks**: Some tickers may not have reliable data
- **OTC stocks**: Limited or no data available

### Reliability
- **API Dependencies**: Application relies on third-party APIs that could change
- **No API Keys**: Using free tiers which have rate limits
- **Community Data**: Some holdings data is community-sourced, not verified

### Legal Disclaimers
1. **Not Financial Advice**: This data is for informational purposes only
2. **No Guarantees**: Data accuracy not guaranteed
3. **No Liability**: Use at your own risk
4. **Research Required**: Always verify with official company filings

---

## 7. Future Improvements

### Potential Data Source Enhancements
1. **Automated Holdings Updates**: Scrape from BitcoinTreasuries.net API (if available)
2. **SEC Filing Integration**: Auto-parse 10-Q/10-K for holding updates
3. **Paid Market Data**: Integrate real-time market cap data
4. **Database Storage**: Move holdings data to database for easier updates
5. **Admin Panel**: Create UI for updating holdings without code changes
6. **Historical Tracking**: Store historical mNAV data for trend analysis
7. **Additional Cryptos**: Add support for other major cryptocurrencies (ADA, AVAX, etc.)

---

## 8. Contact & Updates

### For Data Updates
If you notice outdated holdings data, please:
1. Update the `TREASURY_COMPANIES` list in `app.py`
2. Cite the source (company filing, press release, etc.)
3. Note the date of the update

### Recommended Resources for Tracking
- BitcoinTreasuries.net
- CoinGecko Treasury pages
- Company investor relations pages
- SEC Edgar database (www.sec.gov/edgar)
- @DocumentingBTC on Twitter/X
- Crypto news sites (The Block, CoinDesk, Decrypt)

---

## Version History

- **v1.0** (Nov 2025): Initial version with BTC, ETH, SOL support
  - 13 BTC treasury companies
  - 6 ETH treasury companies
  - 7 SOL treasury companies
  - CoinGecko price data
  - Yahoo Finance market cap data

---

## Appendix: API Documentation Links

1. **CoinGecko API**: https://www.coingecko.com/en/api/documentation
2. **yfinance Library**: https://github.com/ranaroussi/yfinance
3. **Yahoo Finance**: https://finance.yahoo.com/
4. **SEC Edgar**: https://www.sec.gov/edgar
5. **BitcoinTreasuries.net**: https://bitcointreasuries.net/

---

*Last Updated: November 8, 2025*
