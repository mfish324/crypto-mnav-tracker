# Sample mNAV Data Output

This document shows sample output from the Crypto Treasury mNAV Tracker.

## Sample Data (as of testing)

**Bitcoin Price**: $102,086

### Companies Sorted by mNAV Ratio

| Rank | Company | Ticker | mNAV | Status |
|------|---------|--------|------|--------|
| 1 | XXI | CEP | 28.39x | 2,839% (cyan - very high) |
| 2 | Bitcoin Standard Treasury | CEPO | 14.32x | 1,432% (cyan - very high) |
| 3 | GD Culture Group | GDC | 3.45x | 345% (cyan - very high) |
| 4 | Metaplanet | MTPLF | 1.01x | 101% (green - high) |
| 5 | Strategy (MicroStrategy) | MSTR | 0.94x | 94% (yellow - medium) |
| 6 | MARA Holdings | MARA | 0.91x | 91% (yellow - medium) |
| 7 | Trump Media & Tech | DJT | 0.42x | 42% (red - low) |
| 8 | Bullish | BLSH | 0.38x | 38% (red - low) |
| 9 | Riot Platforms | RIOT | 0.31x | 31% (red - low) |
| 10 | Hut 8 Mining | HUT | 0.29x | 29% (red - low) |
| 11 | CleanSpark | CLSK | 0.29x | 29% (red - low) |
| 12 | Galaxy Digital | GLXY | 0.06x | 6% (red - low) |
| 13 | Coinbase Global | COIN | 0.02x | 2% (red - low) |
| 14 | Tesla | TSLA | 0.0008x | 0.08% (red - low) |

## Color Coding

The dashboard uses neon colors to indicate mNAV ranges:

- **Red**: mNAV < 0.5x (Less than 50% of market cap is backed by crypto)
- **Yellow**: 0.5x ≤ mNAV < 1.0x (50-100% backing)
- **Green**: 1.0x ≤ mNAV < 2.0x (Over 100% backing - crypto worth more than market cap!)
- **Cyan**: mNAV ≥ 2.0x (Very high crypto backing relative to market cap)

## Interpretation

### High mNAV (>1.0x)
Companies with mNAV > 1.0 have crypto holdings worth more than their entire market capitalization. This suggests:
- The market values the company LESS than just its crypto holdings
- Potential undervaluation opportunity
- Market may be pricing in risks or concerns

### Medium mNAV (0.5x - 1.0x)
- Crypto holdings represent a significant portion of market cap
- Company likely focused on crypto strategy
- Examples: Strategy (MSTR), MARA

### Low mNAV (<0.5x)
- Crypto holdings are a smaller part of the business
- Company has other significant operations
- Examples: Tesla, Coinbase (which has other business operations beyond just holding crypto)

## Notes

- Some companies may not have data available (international tickers, OTC stocks)
- BTC holdings are based on publicly disclosed information and may not reflect the latest purchases
- Market caps fluctuate throughout trading hours
- The dashboard auto-refreshes every 60 seconds
