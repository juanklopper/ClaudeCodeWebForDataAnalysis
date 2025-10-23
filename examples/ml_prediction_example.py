"""
Machine Learning Example
This script demonstrates a simple machine learning workflow for predicting
customer purchase frequency based on their characteristics.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt

def load_data():
    """Load customer data"""
    df = pd.read_csv('../data/customer_data.csv', parse_dates=['member_since'])
    return df

def prepare_features(df):
    """Prepare features for modeling"""
    # Create a copy to avoid modifying original data
    df_ml = df.copy()
    
    # Encode gender
    le = LabelEncoder()
    df_ml['gender_encoded'] = le.fit_transform(df_ml['gender'])
    
    # Calculate membership duration in days
    from datetime import datetime
    df_ml['membership_days'] = (datetime.now() - df_ml['member_since']).dt.days
    
    # Select features for modeling
    features = ['age', 'gender_encoded', 'income', 'membership_days', 'satisfaction_score']
    target = 'purchase_frequency'
    
    X = df_ml[features]
    y = df_ml[target]
    
    return X, y, features

def train_models(X, y):
    """Train multiple models and compare performance"""
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train Linear Regression
    lr_model = LinearRegression()
    lr_model.fit(X_train_scaled, y_train)
    lr_pred = lr_model.predict(X_test_scaled)
    
    # Train Random Forest
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train_scaled, y_train)
    rf_pred = rf_model.predict(X_test_scaled)
    
    return {
        'models': {'Linear Regression': lr_model, 'Random Forest': rf_model},
        'predictions': {'Linear Regression': lr_pred, 'Random Forest': rf_pred},
        'y_test': y_test,
        'scaler': scaler,
        'X_test': X_test
    }

def evaluate_models(results):
    """Evaluate model performance"""
    print("\n" + "="*60)
    print("MODEL PERFORMANCE COMPARISON")
    print("="*60)
    
    y_test = results['y_test']
    
    for model_name, predictions in results['predictions'].items():
        mse = mean_squared_error(y_test, predictions)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)
        
        print(f"\n{model_name}:")
        print(f"  RMSE: {rmse:.2f}")
        print(f"  MAE: {mae:.2f}")
        print(f"  R² Score: {r2:.4f}")

def feature_importance_analysis(results, feature_names):
    """Analyze feature importance from Random Forest model"""
    print("\n" + "="*60)
    print("FEATURE IMPORTANCE ANALYSIS")
    print("="*60)
    
    rf_model = results['models']['Random Forest']
    importances = rf_model.feature_importances_
    
    # Create a DataFrame for better visualization
    importance_df = pd.DataFrame({
        'Feature': feature_names,
        'Importance': importances
    }).sort_values('Importance', ascending=False)
    
    print("\n", importance_df.to_string(index=False))
    
    # Plot feature importance
    plt.figure(figsize=(10, 6))
    plt.barh(importance_df['Feature'], importance_df['Importance'], color='steelblue')
    plt.xlabel('Importance', fontsize=12)
    plt.ylabel('Feature', fontsize=12)
    plt.title('Feature Importance - Random Forest Model', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('../outputs/feature_importance.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("\n✓ Feature importance plot saved")

def plot_predictions(results):
    """Plot actual vs predicted values"""
    y_test = results['y_test']
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    for idx, (model_name, predictions) in enumerate(results['predictions'].items()):
        ax = axes[idx]
        ax.scatter(y_test, predictions, alpha=0.6, s=50)
        ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 
                'r--', lw=2, label='Perfect Prediction')
        ax.set_xlabel('Actual Purchase Frequency', fontsize=11)
        ax.set_ylabel('Predicted Purchase Frequency', fontsize=11)
        ax.set_title(f'{model_name}', fontsize=12, fontweight='bold')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('../outputs/predictions_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Predictions comparison plot saved")

def make_prediction(model, scaler, customer_data):
    """Make a prediction for a new customer"""
    # Example: Predict for a 35-year-old male, income $80000, 
    # member for 500 days, satisfaction score 4.5
    
    customer_features = np.array([[
        customer_data['age'],
        customer_data['gender_encoded'],
        customer_data['income'],
        customer_data['membership_days'],
        customer_data['satisfaction_score']
    ]])
    
    customer_features_scaled = scaler.transform(customer_features)
    prediction = model.predict(customer_features_scaled)
    
    return prediction[0]

if __name__ == "__main__":
    print("Starting Machine Learning Analysis...")
    
    # Create outputs directory
    import os
    os.makedirs('../outputs', exist_ok=True)
    
    # Load and prepare data
    print("\n1. Loading data...")
    df = load_data()
    
    print("2. Preparing features...")
    X, y, feature_names = prepare_features(df)
    print(f"   Features: {feature_names}")
    print(f"   Target: purchase_frequency")
    print(f"   Dataset size: {len(X)} samples")
    
    # Train models
    print("\n3. Training models...")
    results = train_models(X, y)
    print("   ✓ Models trained successfully")
    
    # Evaluate models
    print("\n4. Evaluating models...")
    evaluate_models(results)
    
    # Feature importance
    print("\n5. Analyzing feature importance...")
    feature_importance_analysis(results, feature_names)
    
    # Plot predictions
    print("\n6. Creating visualizations...")
    plot_predictions(results)
    
    # Example prediction
    print("\n" + "="*60)
    print("EXAMPLE PREDICTION")
    print("="*60)
    
    example_customer = {
        'age': 35,
        'gender_encoded': 1,  # Male
        'income': 80000,
        'membership_days': 500,
        'satisfaction_score': 4.5
    }
    
    rf_model = results['models']['Random Forest']
    scaler = results['scaler']
    
    predicted_frequency = make_prediction(rf_model, scaler, example_customer)
    
    print("\nCustomer Profile:")
    print(f"  Age: {example_customer['age']}")
    print(f"  Gender: Male")
    print(f"  Income: ${example_customer['income']:,}")
    print(f"  Membership Duration: {example_customer['membership_days']} days")
    print(f"  Satisfaction Score: {example_customer['satisfaction_score']}/5.0")
    print(f"\nPredicted Purchase Frequency: {predicted_frequency:.1f} purchases/year")
    
    print("\n✓ Machine learning analysis completed successfully!")
