"""
Data Visualization
This script demonstrates various data visualization techniques using matplotlib and seaborn.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

def load_cleaned_data():
    """Load cleaned datasets"""
    sales_df = pd.read_csv('../data/sales_data_cleaned.csv', parse_dates=['date'])
    customer_df = pd.read_csv('../data/customer_data_cleaned.csv', parse_dates=['member_since'])
    return sales_df, customer_df

def plot_revenue_by_category(df):
    """Create bar plot of revenue by category"""
    print("Creating revenue by category plot...")
    
    category_revenue = df.groupby('category')['revenue'].sum().sort_values(ascending=False)
    
    plt.figure(figsize=(10, 6))
    category_revenue.plot(kind='bar', color='steelblue')
    plt.title('Total Revenue by Category', fontsize=16, fontweight='bold')
    plt.xlabel('Category', fontsize=12)
    plt.ylabel('Revenue ($)', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('../outputs/revenue_by_category.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Revenue by category plot saved")

def plot_sales_trend(df):
    """Create line plot of sales trend over time"""
    print("Creating sales trend plot...")
    
    daily_revenue = df.groupby('date')['revenue'].sum()
    
    plt.figure(figsize=(12, 6))
    plt.plot(daily_revenue.index, daily_revenue.values, marker='o', linewidth=2, color='darkgreen')
    plt.title('Daily Revenue Trend', fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Revenue ($)', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('../outputs/sales_trend.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Sales trend plot saved")

def plot_regional_distribution(df):
    """Create pie chart of sales by region"""
    print("Creating regional distribution plot...")
    
    region_revenue = df.groupby('region')['revenue'].sum()
    
    plt.figure(figsize=(10, 8))
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
    plt.pie(region_revenue.values, labels=region_revenue.index, autopct='%1.1f%%',
            colors=colors, startangle=90)
    plt.title('Revenue Distribution by Region', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('../outputs/regional_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Regional distribution plot saved")

def plot_customer_age_distribution(df):
    """Create histogram of customer age distribution"""
    print("Creating customer age distribution plot...")
    
    plt.figure(figsize=(10, 6))
    plt.hist(df['age'], bins=15, color='coral', edgecolor='black', alpha=0.7)
    plt.title('Customer Age Distribution', fontsize=16, fontweight='bold')
    plt.xlabel('Age', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('../outputs/age_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Age distribution plot saved")

def plot_income_vs_satisfaction(df):
    """Create scatter plot of income vs satisfaction"""
    print("Creating income vs satisfaction plot...")
    
    plt.figure(figsize=(10, 6))
    plt.scatter(df['income'], df['satisfaction_score'], alpha=0.6, s=100, color='purple')
    plt.title('Income vs Customer Satisfaction', fontsize=16, fontweight='bold')
    plt.xlabel('Income ($)', fontsize=12)
    plt.ylabel('Satisfaction Score', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('../outputs/income_vs_satisfaction.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Income vs satisfaction plot saved")

def plot_correlation_heatmap(df):
    """Create correlation heatmap"""
    print("Creating correlation heatmap...")
    
    numeric_cols = ['age', 'income', 'purchase_frequency', 'satisfaction_score']
    correlation_matrix = df[numeric_cols].corr()
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0,
                square=True, linewidths=1, cbar_kws={"shrink": 0.8})
    plt.title('Correlation Heatmap - Customer Metrics', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('../outputs/correlation_heatmap.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Correlation heatmap saved")

if __name__ == "__main__":
    print("Starting data visualization...")
    
    # Create outputs directory
    import os
    os.makedirs('../outputs', exist_ok=True)
    
    # Load data
    sales_df, customer_df = load_cleaned_data()
    
    # Create visualizations
    plot_revenue_by_category(sales_df)
    plot_sales_trend(sales_df)
    plot_regional_distribution(sales_df)
    plot_customer_age_distribution(customer_df)
    plot_income_vs_satisfaction(customer_df)
    plot_correlation_heatmap(customer_df)
    
    print("\n✓ All visualizations completed successfully!")
    print("Plots saved in the 'outputs' directory")
