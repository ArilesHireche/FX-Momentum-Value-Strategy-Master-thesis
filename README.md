Find the latest version of the paper attached. Work is still in progress, the future version will be uploaded in this repository as well.

# FX Momentum & Value Strategy Master's Thesis

## Overview

This repository contains the research and analysis for a Master's thesis that compares **Momentum** and **Value strategies** in foreign exchange (FX) markets. The study utilizes long-span historical data to evaluate cross-sectional returns and strategy performance.

## Research Objective

The thesis investigates whether momentum and value-based investment strategies generate statistically significant risk-adjusted returns in currency markets. By analyzing extensive historical data, this research aims to provide insights into:

- **Cross-sectional return dynamics** in FX markets
- **Strategy performance comparison and interactions** between momentum and value approaches
- **Long-term factor behavior** and persistence in currency returns
- **Risk-adjusted returns** (Sharpe ratios, Moments analysis, etc.)

## Repository Structure

```
FX-Momentum-Value-Strategy-Master-thesis/
├── README.md
├── Data/                          # Historical FX and economic data
├── Value/                     # Jupyter notebooks for analysis
│   ├── PPP Value Strategy.ipynb
├── Momentum/                           # Python utility functions
│   ├── Momentum strategy analysis.py
│   └── spot_rates_98-24.xls        #from Reuters Datastream 
└── data.py/                       # imports functions
```

## Key Findings

See 'FX_Momentum_Value_long_span_data.pdf' file to get the whole overview and conclusions of the paper.

## Data

- **Source**: [OECD, WorldBank Database, Refinitiv, Bloomberf]
- **Time Period**: [1998-2026]
- **Frequency**: [Monthly or Quarterly depending on the strategy]

## Methodology

### Momentum Strategy
Positions based on recent price trends and rate of change in currency valuations.

### Value Strategy
Positions based on fundamental valuation metrics relative to historical averages.

### Metrics Used
- Cumulative Returns
- Sharpe Ratio
- Skewness
- Excess kurtosis

## Requirements

- Python 3.8+
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the analysis notebooks in order:
```bash
jupyter notebook notebooks/01_data_preprocessing.ipynb
```

## Results

Detailed results and visualizations are available in the `results/` directory.

## Author

**ArilesHireche**

Master's Thesis, Université Paris Dauphine-PSL, 2026
