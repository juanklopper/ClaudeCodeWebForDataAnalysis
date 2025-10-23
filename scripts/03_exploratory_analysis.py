"""
Exploratory Data Analysis (EDA)
This script demonstrates various EDA techniques including summary statistics,
grouping, aggregation, and correlation analysis.
"""

import pandas as pd
import numpy as np

def load_cleaned_data():
    """Load cleaned datasets"""
    sales_df = pd.read_csv('../data/sales_data_cleaned.csv', parse_dates=['date'])
    customer_df = pd.read_csv('../data/customer_data_cleaned.csv', parse_dates=['member_since'])
    return sales_df, customer_df

def analyze_sales_by_category(df):
    """Analyze sales performance by category"""
    print("\n" + "="*60)
    print("Sales Analysis by Category")
    print("="*60)
    
    category_analysis = df.groupby('category').agg({
        'quantity': 'sum',
        'revenue': 'sum',
        'product': 'nunique'
    }).round(2)
    
    category_analysis.columns = ['Total Quantity', 'Total Revenue', 'Unique Products']
    category_analysis = category_analysis.sort_values('Total Revenue', ascending=False)
    
    print(category_analysis)
    return category_analysis

def analyze_sales_by_region(df):
    """Analyze sales performance by region"""
    print("\n" + "="*60)
    print("Sales Analysis by Region")
    print("="*60)
    
    region_analysis = df.groupby('region').agg({
        'quantity': 'sum',
        'revenue': 'sum',
        'product': 'count'
    }).round(2)
    
    region_analysis.columns = ['Total Quantity', 'Total Revenue', 'Number of Transactions']
    region_analysis = region_analysis.sort_values('Total Revenue', ascending=False)
    
    print(region_analysis)
    return region_analysis

def analyze_top_products(df, top_n=5):
    """Identify top-selling products"""
    print("\n" + "="*60)
    print(f"Top {top_n} Products by Revenue")
    print("="*60)
    
    product_analysis = df.groupby('product').agg({
        'quantity': 'sum',
        'revenue': 'sum'
    }).round(2)
    
    product_analysis.columns = ['Total Quantity', 'Total Revenue']
    top_products = product_analysis.sort_values('Total Revenue', ascending=False).head(top_n)
    
    print(top_products)
    return top_products

def analyze_customer_segments(df):
    """Analyze customer segments"""
    print("\n" + "="*60)
    print("Customer Analysis by Gender")
    print("="*60)
    
    # Calculate aggregated statistics by gender (means, not individual data)
    gender_analysis = df.groupby('gender').agg({
        'age': 'mean',
        'income': 'mean',
        'purchase_frequency': 'mean',
        'satisfaction_score': 'mean'
    }).round(2)
    
    # Print aggregated statistics only (no individual customer data)
    print(gender_analysis)
    
    print("\n" + "="*60)
    print("Customer Age Groups")
    print("="*60)
    
    # Create age groups
    df['age_group'] = pd.cut(df['age'], bins=[0, 30, 40, 50, 100], 
                              labels=['<30', '30-40', '40-50', '50+'])
    
    age_group_analysis = df.groupby('age_group').agg({
        'income': 'mean',
        'purchase_frequency': 'mean',
        'satisfaction_score': 'mean'
    }).round(2)
    
    print(age_group_analysis)
    return gender_analysis, age_group_analysis

def correlation_analysis(df):
    """Perform correlation analysis on customer data"""
    print("\n" + "="*60)
    print("Correlation Analysis")
    print("="*60)
    
    # Select numeric columns
    numeric_cols = ['age', 'income', 'purchase_frequency', 'satisfaction_score']
    correlation_matrix = df[numeric_cols].corr().round(3)
    
    print(correlation_matrix)
    return correlation_matrix

if __name__ == "__main__":
    print("Starting Exploratory Data Analysis...")
    
    # Load data
    sales_df, customer_df = load_cleaned_data()
    
    # Sales analysis
    category_stats = analyze_sales_by_category(sales_df)
    region_stats = analyze_sales_by_region(sales_df)
    top_products = analyze_top_products(sales_df)
    
    # Customer analysis
    gender_stats, age_stats = analyze_customer_segments(customer_df)
    correlation_matrix = correlation_analysis(customer_df)
    
    # Overall summary
    print("\n" + "="*60)
    print("Overall Summary")
    print("="*60)
    print(f"Total Revenue: ${sales_df['revenue'].sum():,.2f}")
    print(f"Total Transactions: {len(sales_df)}")
    print(f"Average Transaction Value: ${sales_df['revenue'].mean():,.2f}")
    print(f"Total Customers: {len(customer_df)}")
    print(f"Average Customer Satisfaction: {customer_df['satisfaction_score'].mean():.2f}/5.0")
    
    print("\n✓ Exploratory analysis completed successfully!")
