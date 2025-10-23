"""
Statistical Analysis
This script demonstrates various statistical analysis techniques including
hypothesis testing, confidence intervals, and regression analysis.
"""

import pandas as pd
import numpy as np
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

def load_cleaned_data():
    """Load cleaned datasets"""
    sales_df = pd.read_csv('../data/sales_data_cleaned.csv', parse_dates=['date'])
    customer_df = pd.read_csv('../data/customer_data_cleaned.csv', parse_dates=['member_since'])
    return sales_df, customer_df

def descriptive_statistics(df, column_name):
    """Calculate descriptive statistics"""
    print(f"\nDescriptive Statistics for {column_name}:")
    print("-" * 50)
    print(f"Mean: {df[column_name].mean():.2f}")
    print(f"Median: {df[column_name].median():.2f}")
    print(f"Mode: {df[column_name].mode()[0]:.2f}")
    print(f"Std Dev: {df[column_name].std():.2f}")
    print(f"Min: {df[column_name].min():.2f}")
    print(f"Max: {df[column_name].max():.2f}")
    print(f"Range: {df[column_name].max() - df[column_name].min():.2f}")

def confidence_interval(df, column_name, confidence=0.95):
    """Calculate confidence interval"""
    data = df[column_name]
    n = len(data)
    mean = data.mean()
    se = stats.sem(data)
    interval = se * stats.t.ppf((1 + confidence) / 2, n - 1)
    
    print(f"\n{confidence*100}% Confidence Interval for {column_name}:")
    print(f"Lower bound: {mean - interval:.2f}")
    print(f"Upper bound: {mean + interval:.2f}")
    
    return mean - interval, mean + interval

def hypothesis_test_revenue_by_category(df):
    """Test if there's a significant difference in revenue between categories"""
    print("\n" + "="*60)
    print("Hypothesis Test: Revenue Difference Between Categories")
    print("="*60)
    
    # Get revenue for each category
    electronics = df[df['category'] == 'Electronics']['revenue']
    furniture = df[df['category'] == 'Furniture']['revenue']
    supplies = df[df['category'] == 'Supplies']['revenue']
    
    # Perform ANOVA test
    f_stat, p_value = stats.f_oneway(electronics, furniture, supplies)
    
    print(f"\nF-statistic: {f_stat:.4f}")
    print(f"P-value: {p_value:.4f}")
    
    if p_value < 0.05:
        print("Result: Significant difference in revenue between categories (p < 0.05)")
    else:
        print("Result: No significant difference in revenue between categories (p >= 0.05)")
    
    return f_stat, p_value

def hypothesis_test_satisfaction_by_gender(df):
    """Test if there's a significant difference in satisfaction between genders"""
    print("\n" + "="*60)
    print("Hypothesis Test: Satisfaction Difference Between Genders")
    print("="*60)
    
    male_satisfaction = df[df['gender'] == 'M']['satisfaction_score']
    female_satisfaction = df[df['gender'] == 'F']['satisfaction_score']
    
    # Perform t-test
    t_stat, p_value = stats.ttest_ind(male_satisfaction, female_satisfaction)
    
    print(f"\nMale satisfaction mean: {male_satisfaction.mean():.2f}")
    print(f"Female satisfaction mean: {female_satisfaction.mean():.2f}")
    print(f"\nT-statistic: {t_stat:.4f}")
    print(f"P-value: {p_value:.4f}")
    
    if p_value < 0.05:
        print("Result: Significant difference in satisfaction between genders (p < 0.05)")
    else:
        print("Result: No significant difference in satisfaction between genders (p >= 0.05)")
    
    return t_stat, p_value

def linear_regression_analysis(df):
    """Perform linear regression analysis"""
    print("\n" + "="*60)
    print("Linear Regression: Income vs Purchase Frequency")
    print("="*60)
    
    # Prepare data
    X = df[['income']].values
    y = df['purchase_frequency'].values
    
    # Fit model
    model = LinearRegression()
    model.fit(X, y)
    
    # Make predictions
    y_pred = model.predict(X)
    
    # Calculate metrics
    r2 = r2_score(y, y_pred)
    rmse = np.sqrt(mean_squared_error(y, y_pred))
    
    print(f"\nCoefficient (slope): {model.coef_[0]:.6f}")
    print(f"Intercept: {model.intercept_:.2f}")
    print(f"R² Score: {r2:.4f}")
    print(f"RMSE: {rmse:.2f}")
    
    if r2 > 0.5:
        print("Result: Strong relationship between income and purchase frequency")
    elif r2 > 0.3:
        print("Result: Moderate relationship between income and purchase frequency")
    else:
        print("Result: Weak relationship between income and purchase frequency")
    
    return model, r2, rmse

def correlation_test(df, col1, col2):
    """Test correlation between two variables"""
    print(f"\n" + "="*60)
    print(f"Correlation Test: {col1} vs {col2}")
    print("="*60)
    
    # Calculate Pearson correlation
    corr_coef, p_value = stats.pearsonr(df[col1], df[col2])
    
    print(f"\nPearson correlation coefficient: {corr_coef:.4f}")
    print(f"P-value: {p_value:.4f}")
    
    if abs(corr_coef) > 0.7:
        strength = "Strong"
    elif abs(corr_coef) > 0.4:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    direction = "positive" if corr_coef > 0 else "negative"
    
    print(f"Result: {strength} {direction} correlation")
    
    if p_value < 0.05:
        print("The correlation is statistically significant (p < 0.05)")
    else:
        print("The correlation is not statistically significant (p >= 0.05)")
    
    return corr_coef, p_value

if __name__ == "__main__":
    print("Starting statistical analysis...")
    
    # Load data
    sales_df, customer_df = load_cleaned_data()
    
    # Descriptive statistics
    print("\n" + "="*60)
    print("DESCRIPTIVE STATISTICS")
    print("="*60)
    descriptive_statistics(sales_df, 'revenue')
    descriptive_statistics(customer_df, 'satisfaction_score')
    
    # Confidence intervals
    print("\n" + "="*60)
    print("CONFIDENCE INTERVALS")
    print("="*60)
    confidence_interval(sales_df, 'revenue')
    confidence_interval(customer_df, 'satisfaction_score')
    
    # Hypothesis tests
    print("\n" + "="*60)
    print("HYPOTHESIS TESTS")
    print("="*60)
    hypothesis_test_revenue_by_category(sales_df)
    hypothesis_test_satisfaction_by_gender(customer_df)
    
    # Regression analysis
    print("\n" + "="*60)
    print("REGRESSION ANALYSIS")
    print("="*60)
    linear_regression_analysis(customer_df)
    
    # Correlation tests
    print("\n" + "="*60)
    print("CORRELATION TESTS")
    print("="*60)
    correlation_test(customer_df, 'income', 'purchase_frequency')
    correlation_test(customer_df, 'purchase_frequency', 'satisfaction_score')
    
    print("\n✓ Statistical analysis completed successfully!")
