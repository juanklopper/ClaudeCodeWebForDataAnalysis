"""
Data Cleaning and Preprocessing
This script demonstrates data cleaning techniques including handling missing values,
duplicates, and data type conversions.
"""

import pandas as pd
import numpy as np
from datetime import datetime

def load_data():
    """Load the datasets"""
    sales_df = pd.read_csv('../data/sales_data.csv')
    customer_df = pd.read_csv('../data/customer_data.csv')
    return sales_df, customer_df

def clean_sales_data(df):
    """Clean sales dataset"""
    print("\nCleaning Sales Data...")
    
    # Convert date column to datetime
    df['date'] = pd.to_datetime(df['date'])
    print(f"✓ Converted 'date' to datetime format")
    
    # Create additional date features
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day_of_week'] = df['date'].dt.day_name()
    print(f"✓ Created date-based features")
    
    # Check for and remove duplicates
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        df = df.drop_duplicates()
        print(f"✓ Removed {duplicates} duplicate rows")
    else:
        print(f"✓ No duplicates found")
    
    # Verify revenue calculation
    df['calculated_revenue'] = df['quantity'] * df['price']
    revenue_mismatch = (abs(df['revenue'] - df['calculated_revenue']) > 0.01).sum()
    if revenue_mismatch > 0:
        print(f"⚠ Found {revenue_mismatch} revenue calculation mismatches")
        df['revenue'] = df['calculated_revenue']
    df = df.drop('calculated_revenue', axis=1)
    
    return df

def clean_customer_data(df):
    """Clean customer dataset"""
    print("\nCleaning Customer Data...")
    
    # Convert member_since to datetime
    df['member_since'] = pd.to_datetime(df['member_since'])
    print(f"✓ Converted 'member_since' to datetime format")
    
    # Calculate membership duration in days
    df['membership_days'] = (datetime.now() - df['member_since']).dt.days
    print(f"✓ Calculated membership duration")
    
    # Standardize gender column
    df['gender'] = df['gender'].str.upper()
    print(f"✓ Standardized gender values")
    
    # Check for outliers in age
    age_outliers = ((df['age'] < 18) | (df['age'] > 100)).sum()
    if age_outliers > 0:
        print(f"⚠ Found {age_outliers} age outliers")
    else:
        print(f"✓ No age outliers found")
    
    return df

def save_cleaned_data(sales_df, customer_df):
    """Save cleaned datasets"""
    sales_df.to_csv('../data/sales_data_cleaned.csv', index=False)
    customer_df.to_csv('../data/customer_data_cleaned.csv', index=False)
    print("\n✓ Cleaned data saved successfully!")

if __name__ == "__main__":
    print("Starting data cleaning process...")
    
    # Load data
    sales_df, customer_df = load_data()
    
    # Clean datasets
    sales_df_clean = clean_sales_data(sales_df)
    customer_df_clean = clean_customer_data(customer_df)
    
    # Save cleaned data
    save_cleaned_data(sales_df_clean, customer_df_clean)
    
    print("\n" + "="*60)
    print("Data Cleaning Summary")
    print("="*60)
    print(f"Sales Data: {sales_df_clean.shape[0]} rows × {sales_df_clean.shape[1]} columns")
    print(f"Customer Data: {customer_df_clean.shape[0]} rows × {customer_df_clean.shape[1]} columns")
