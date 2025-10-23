"""
Data Loading and Basic Exploration
This script demonstrates how to load and perform initial exploration of datasets.
"""

import pandas as pd
import numpy as np

def load_sales_data():
    """Load the sales dataset"""
    df = pd.read_csv('../data/sales_data.csv')
    return df

def load_customer_data():
    """Load the customer dataset"""
    df = pd.read_csv('../data/customer_data.csv')
    return df

def basic_info(df, dataset_name):
    """Display basic information about the dataset"""
    print(f"\n{'='*60}")
    print(f"Dataset: {dataset_name}")
    print(f"{'='*60}")
    
    print(f"\nShape: {df.shape[0]} rows × {df.shape[1]} columns")
    
    print(f"\nColumn Names and Types:")
    print(df.dtypes)
    
    print(f"\nFirst 5 rows:")
    print(df.head())
    
    print(f"\nBasic Statistics:")
    print(df.describe())
    
    print(f"\nMissing Values:")
    print(df.isnull().sum())
    
    return df

if __name__ == "__main__":
    print("Loading and exploring datasets...")
    
    # Load and explore sales data
    sales_df = load_sales_data()
    basic_info(sales_df, "Sales Data")
    
    # Load and explore customer data
    customer_df = load_customer_data()
    basic_info(customer_df, "Customer Data")
    
    print("\n✓ Data loading completed successfully!")
