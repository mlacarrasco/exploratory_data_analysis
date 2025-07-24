# Exploratory Data Analysis

A comprehensive toolkit and collection of methodologies for performing exploratory data analysis (EDA) on diverse datasets, with a focus on statistical insights, data visualization, and pattern discovery.

## Overview

This repository provides a systematic approach to exploratory data analysis, offering tools, templates, and best practices for understanding data characteristics, identifying patterns, and generating actionable insights. The framework supports various data types and domains, making it suitable for researchers, data scientists, and analysts across different fields.

## Author

**Miguel Carrasco**  
PhD in Informatics - Pierre et Marie Curie University (Sorbonne University)  
PhD in Engineering Sciences - Pontificia Universidad Católica de Chile  
Research Focus: Image Processing, Computer Vision, Human-Computer Interaction

## Key Features

### Comprehensive Analysis Pipeline
- **Data Profiling**: Automated data quality assessment and metadata extraction
- **Statistical Analysis**: Descriptive statistics, distributions, and correlation analysis
- **Missing Data Analysis**: Patterns and strategies for handling incomplete data
- **Outlier Detection**: Multiple methods for identifying and analyzing anomalies

### Advanced Visualization Suite
- **Univariate Analysis**: Histograms, box plots, density plots, and Q-Q plots
- **Bivariate Analysis**: Scatter plots, correlation heatmaps, and joint distributions
- **Multivariate Analysis**: Principal component analysis and dimensionality reduction
- **Interactive Dashboards**: Dynamic visualizations for data exploration

### Domain-Specific Templates
- **Image Data Analysis**: Tools for analyzing image datasets and visual patterns
- **Time Series Analysis**: Temporal pattern detection and trend analysis
- **Text Data Exploration**: Natural language processing and text analytics
- **Sensor Data Analysis**: IoT and measurement data exploration

## Visualization Gallery

The repository includes a comprehensive collection of visualization templates:

- **Distribution Analysis**: Histograms, KDE plots, Q-Q plots
- **Relationship Analysis**: Scatter plots, correlation matrices, pair plots
- **Categorical Analysis**: Bar charts, pie charts, stacked plots
- **Time Series**: Line plots, seasonal decomposition, autocorrelation
- **Multivariate**: Heatmaps, parallel coordinates, radar charts
- **Statistical**: Box plots, violin plots, strip charts

## Contact

**Miguel Carrasco**  
- Website: https://mlacarrasco.github.io/
- Email: [contact information]

For questions about the toolkit or collaboration opportunities, please open an issue or contact the author directly.

## Acknowledgments

- Statistical methods implementation inspired by classical EDA literature
- Visualization techniques adapted from modern data science best practices
- Special thanks to the open-source community for foundational libraries
- Contributors and users who have provided feedback and improvements

## Related Resources

- [Pandas Profiling](https://github.com/ydataai/pandas-profiling) - Automated EDA reports
- [Sweetviz](https://github.com/fbdesignpro/sweetviz) - Automated EDA visualizations
- [DataPrep](https://github.com/sfu-db/dataprep) - Data preparation and EDA toolkit
- [Plotly](https://plotly.com/python/) - Interactive visualization library

## Installation

### Requirements
```bash
Python >= 3.8
pandas >= 1.3.0
numpy >= 1.21.0
matplotlib >= 3.5.0
seaborn >= 0.11.0
plotly >= 5.0.0
scipy >= 1.7.0
scikit-learn >= 1.0.0
jupyter >= 1.0.0
```

### Setup
```bash
# Clone the repository
git clone https://github.com/mlacarrasco/exploratory_data_analysis.git
cd exploratory_data_analysis

# Install dependencies
pip install -r requirements.txt

# Install package in development mode
pip install -e .
```

## Usage

### Quick Start
```python
from eda_toolkit import EDAAnalyzer
import pandas as pd

# Load your dataset
data = pd.read_csv('your_dataset.csv')

# Initialize EDA analyzer
analyzer = EDAAnalyzer(data)

# Generate comprehensive report
report = analyzer.generate_report()

# Display summary statistics
analyzer.summary_statistics()

# Create visualization dashboard
analyzer.create_dashboard()
```

### Basic Analysis
```python
# Data profiling
profile = analyzer.profile_data()
print(f"Dataset shape: {profile['shape']}")
print(f"Missing values: {profile['missing_summary']}")

# Correlation analysis
correlation_matrix = analyzer.correlation_analysis()
analyzer.plot_correlation_heatmap()

# Distribution analysis
analyzer.plot_distributions()
analyzer.statistical_tests()
```

### Advanced Analysis
```python
# Outlier detection
outliers = analyzer.detect_outliers(method='iqr')
analyzer.visualize_outliers()

# Principal component analysis
pca_results = analyzer.pca_analysis(n_components=5)
analyzer.plot_pca_variance()

# Clustering analysis
clusters = analyzer.cluster_analysis(n_clusters=3)
analyzer.plot_clusters()
```
