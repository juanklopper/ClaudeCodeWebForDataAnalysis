# Outputs Directory

This directory contains generated visualizations and analysis results from running the scripts.

## Generated Files

When you run the analysis scripts, the following files will be created:

### From `scripts/04_visualization.py`:
- `revenue_by_category.png` - Bar chart showing total revenue by product category
- `sales_trend.png` - Line plot showing daily revenue trends
- `regional_distribution.png` - Pie chart showing revenue distribution by region
- `age_distribution.png` - Histogram of customer age distribution
- `income_vs_satisfaction.png` - Scatter plot of income vs satisfaction scores
- `correlation_heatmap.png` - Heatmap showing correlations between customer metrics

### From `examples/ml_prediction_example.py`:
- `feature_importance.png` - Bar chart showing feature importance from Random Forest model
- `predictions_comparison.png` - Actual vs predicted values for both models

## Note

These PNG files are generated automatically when you run the scripts and are excluded from version control via `.gitignore`. Run the scripts to regenerate them.
