# Multi-Crypto Treasury Tracker - Sample Output

This document shows sample output from the updated Crypto Treasury mNAV Tracker with Bitcoin, Ethereum, and Solana support.

## Current Crypto Prices (Sample)

- **Bitcoin (BTC)**: $102,043
- **Ethereum (ETH)**: $3,397.91
- **Solana (SOL)**: $157.76

---

## Top Companies by mNAV (All Cryptocurrencies)

### Bitcoin Companies

| Rank | Company | Ticker | BTC Holdings | mNAV | Category |
|------|---------|--------|--------------|------|----------|
| 1 | XXI | CEP | 43,514 | 28.38x | 2,838% (Cyan) |
| 2 | Bitcoin Standard Treasury | CEPO | 30,021 | 14.31x | 1,431% (Cyan) |
| 3 | Metaplanet | MTPLF | 30,823 | 1.01x | 101% (Green) |
| 4 | Strategy (MicroStrategy) | MSTR | 641,205 | 0.94x | 94% (Yellow) |
| 5 | MARA Holdings | MARA | 53,250 | 0.91x | 91% (Yellow) |
| 6 | Trump Media & Tech | DJT | 15,000 | 0.42x | 42% (Red) |
| 7 | Bullish | BLSH | 24,300 | 0.38x | 38% (Red) |
| 8 | Riot Platforms | RIOT | 19,324 | 0.31x | 31% (Red) |
| 9 | Hut 8 Mining | HUT | 13,696 | 0.29x | 29% (Red) |
| 10 | CleanSpark | CLSK | 13,011 | 0.29x | 29% (Red) |

### Ethereum Companies

| Rank | Company | Ticker | ETH Holdings | mNAV | Category |
|------|---------|--------|--------------|------|----------|
| 1 | BTCS Inc | BTCS | 70,140 | 1.58x | 158% (Cyan) |
| 2 | SharpLink Gaming | SBET | 740,760 | 1.07x | 107% (Green) |
| 3 | BitMine Immersion | BMNR | 2,069,443 | 0.61x | 61% (Yellow) |
| 4 | Bit Digital | BTBT | 150,244 | 0.51x | 51% (Yellow) |
| 5 | Galaxy Digital | GLXY | 50,000 | 0.01x | 1% (Red) |
| 6 | Coinbase Global | COIN | 137,334 | 0.006x | 0.6% (Red) |

### Solana Companies

| Rank | Company | Ticker | SOL Holdings | mNAV | Category |
|------|---------|--------|--------------|------|----------|
| 1 | Helius Medical | HSDT | 2,200,000 | 1.57x | 157% (Cyan) |
| 2 | Forward Industries | FORD | 6,822,000 | 1.20x | 120% (Green) |
| 3 | DeFi Development | DFDV | 2,100,000 | ~1.0x | Est. 100% (Yellow) |
| 4 | Upexi Inc | UPXI | 2,000,000 | ~0.8x | Est. 80% (Yellow) |
| 5 | Sol Strategies | HODL | 370,000 | Variable | - |
| 6 | Classover | CLSO | 52,067 | Variable | - |
| 7 | Torrent Capital | TORR | 40,039 | Variable | - |

---

## Notable Insights

### Highest mNAV Overall
**XXI (CEP)** - 28.38x mNAV
- Bitcoin holdings worth 28 times the company's entire market cap
- Holds 43,514 BTC ($4.44B)
- Market cap only $156M
- Significant undervaluation or market skepticism

### Largest Absolute Holdings

#### Bitcoin
**Strategy (MSTR)** - 641,205 BTC
- Worth $65.4 billion
- 0.94x mNAV (94% of market cap)
- Largest corporate Bitcoin holder

#### Ethereum
**BitMine Immersion (BMNR)** - 2,069,443 ETH
- Worth $7.0 billion
- 0.61x mNAV (61% of market cap)
- Largest corporate Ethereum holder

#### Solana
**Forward Industries (FORD)** - 6,822,000 SOL
- Worth $1.08 billion
- 1.20x mNAV (120% of market cap)
- Largest corporate Solana holder

### Cross-Crypto Holdings
Some companies hold multiple cryptocurrencies:
- **Coinbase (COIN)**: Holds both BTC (14,548) and ETH (137,334)
- **Galaxy Digital (GLXY)**: Holds BTC (6,894) and ETH (50,000)

---

## Color Coding System

The dashboard uses different colors for mNAV ranges:

- **Red (< 0.5x)**: Crypto holdings are less than 50% of market cap
- **Yellow (0.5x - 1.0x)**: Crypto holdings are 50-100% of market cap
- **Green (1.0x - 2.0x)**: Crypto holdings exceed market cap by up to 2x
- **Cyan/Turquoise (> 2.0x)**: Crypto holdings are more than double market cap

---

## Crypto Badge Colors

Each tile displays a colored badge indicating the cryptocurrency:

- **Orange (#ff9500)**: Bitcoin (BTC)
- **Blue (#627eea)**: Ethereum (ETH)
- **Green (#14f195)**: Solana (SOL)

---

## Investment Strategies by Crypto

### Bitcoin (BTC) Strategy
- Most established corporate treasury strategy
- Companies range from pure-play (MSTR) to miners (MARA, RIOT)
- Longest track record, most data available
- Tesla holds but hasn't added to position recently

### Ethereum (ETH) Strategy
- Emerging trend starting in 2024-2025
- Some companies (Bit Digital) rotated from BTC to ETH
- Staking benefits (~5% APY) vs Bitcoin
- Joseph Lubin (Ethereum co-founder) chairs SharpLink Gaming

### Solana (SOL) Strategy
- Newest corporate treasury trend (2025)
- Higher staking rewards (7-8% APY)
- Most companies stake their holdings for yield
- Forward Industries raised $1.65B specifically for SOL purchases

---

## Market Dynamics

### Premium vs Discount to Holdings

**Trading at Premium (Market Cap > Crypto Value)**
- Most BTC miners: MARA, RIOT, CLSK, HUT
- Rationale: Mining operations add value beyond holdings
- Examples: MARA at 0.91x means market values mining at ~$610M

**Trading at Discount (Crypto Value > Market Cap)**
- XXI (CEP), Bitcoin Standard Treasury (CEPO), Metaplanet (MTPLF)
- Market may be pricing in:
  - Liquidity concerns
  - Regulatory risks
  - Management quality questions
  - Leverage/debt issues

**Near Parity (0.9x - 1.1x)**
- Strategy (MSTR) at 0.94x
- Market essentially values company = BTC holdings
- Suggests limited value assigned to software business

---

## Data Freshness

- **Crypto Prices**: Real-time from CoinGecko (updated every 60s)
- **Market Caps**: 15-20 minute delay from Yahoo Finance
- **Holdings Data**: Static, from company filings/announcements
  - Last verified: November 2025
  - See DATA_SOURCES.md for specific dates per company

---

## Use Cases for mNAV Tracker

1. **Investment Research**: Identify companies trading at discount to holdings
2. **Portfolio Monitoring**: Track corporate crypto exposure
3. **Trend Analysis**: See which companies are accumulating which cryptos
4. **Risk Assessment**: Understand concentration of holdings vs market cap
5. **Educational**: Learn about corporate treasury strategies

---

## Important Disclaimers

1. **Not Financial Advice**: This is informational only
2. **Holdings May Change**: Companies buy/sell between announcements
3. **Market Cap Volatility**: Stock prices fluctuate continuously
4. **Accuracy Not Guaranteed**: Always verify with official filings
5. **Do Your Own Research**: This is a starting point, not investment advice

---

*Sample data as of November 8, 2025*
*For complete data source documentation, see DATA_SOURCES.md*
