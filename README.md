The following readme file has been generated with Copilot. Do not hesitate to notice me directly any mistake I haven't noticed.

# FX Momentum & Value Strategy Master's Thesis

## Overview

This repository contains the research and analysis for a Master's thesis that compares **Momentum** and **Value strategies** in foreign exchange (FX) markets. The study utilizes long-span historical data to evaluate cross-sectional returns and strategy performance.

## Research Objective

The thesis investigates whether momentum and value-based investment strategies generate statistically significant risk-adjusted returns in currency markets. By analyzing extensive historical data, this research aims to provide insights into:

- **Cross-sectional return dynamics** in FX markets
- **Strategy performance comparison** between momentum and value approaches
- **Long-term factor behavior** and persistence in currency returns
- **Risk-adjusted returns** (Sharpe ratios, Sortino ratios, etc.)

## Repository Structure

```
FX-Momentum-Value-Strategy-Master-thesis/
├── README.md
├── data/                          # Historical FX and economic data
├── notebooks/                     # Jupyter notebooks for analysis
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_strategy_implementation.ipynb
│   ├── 03_momentum_analysis.ipynb
│   ├── 04_value_analysis.ipynb
│   └── 05_results_visualization.ipynb
├── src/                           # Python utility functions
│   ├── utils.py
│   └── strategy.py
└── results/                       # Generated outputs and visualizations
```

## Key Findings

*Add your main conclusions here after analysis is complete*

## Data

- **Source**: [Specify your data sources - central banks, financial databases, etc.]
- **Time Period**: [Specify your analysis period]
- **Currency Pairs**: [List the FX pairs analyzed]
- **Frequency**: [Daily, Monthly, etc.]

## Methodology

### Momentum Strategy
Positions based on recent price trends and rate of change in currency valuations.

### Value Strategy
Positions based on fundamental valuation metrics relative to historical averages.

### Metrics Used
- Cumulative Returns
- Sharpe Ratio
- Maximum Drawdown
- Hit Ratio
- Risk-Adjusted Returns

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

Master's Thesis, [University Name], 2026

## License

[Specify your preferred license]

## References

[Add relevant academic papers and references]

---

*Last Updated: 2026-04-30*
