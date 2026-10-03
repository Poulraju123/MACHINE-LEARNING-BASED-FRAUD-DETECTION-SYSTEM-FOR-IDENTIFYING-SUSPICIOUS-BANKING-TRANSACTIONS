"""
Machine Learning-Based Fraud Detection System
Detects suspicious banking transactions using classification algorithms
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, roc_curve, auc
import warnings
warnings.filterwarnings('ignore')

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 8)
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10

def generate_transaction_dataset(n_samples=5000, fraud_rate=0.05, random_state=42):
    """Generate synthetic transaction dataset with fraud labels"""
    np.random.seed(random_state)
    
    data = []
    n_fraud = int(n_samples * fraud_rate)
    n_legitimate = n_samples - n_fraud
    
    # Legitimate transactions
    for i in range(n_legitimate):
        amount = np.random.lognormal(mean=4.5, sigma=1.2)
        frequency = np.random.poisson(lam=3)
        hour = np.random.randint(0, 24)
        day_of_week = np.random.randint(0, 7)
        location = np.random.choice(['Home', 'Work', 'Travel', 'Online'], p=[0.5, 0.3, 0.1, 0.1])
        device_type = np.random.choice(['Mobile', 'Desktop', 'ATM'], p=[0.6, 0.3, 0.1])
        account_age = np.random.randint(1, 20)
        prev_fraud = 0
        
        data.append({
            'Transaction_ID': f'T{i:06d}',
            'Amount': amount,
            'Frequency': frequency,
            'Hour': hour,
            'Day_of_Week': day_of_week,
            'Location': location,
            'Device_Type': device_type,
            'Account_Age': account_age,
            'Previous_Fraud': prev_fraud,
            'Fraud': 0
        })
    
    # Fraudulent transactions
    for i in range(n_fraud):
        amount = np.random.lognormal(mean=5.5, sigma=1.5)  # Higher amounts
        frequency = np.random.poisson(lam=8)  # Higher frequency
        hour = np.random.choice([2, 3, 4, 5, 23])  # Unusual hours
        day_of_week = np.random.randint(0, 7)
        location = np.random.choice(['Unknown', 'Foreign', 'Travel'], p=[0.5, 0.3, 0.2])
        device_type = np.random.choice(['Mobile', 'Desktop', 'ATM'], p=[0.5, 0.4, 0.1])
        account_age = np.random.randint(0, 3)  # Newer accounts
        prev_fraud = np.random.choice([0, 1], p=[0.7, 0.3])
        
        data.append({
            'Transaction_ID': f'T{n_legitimate+i:06d}',
            'Amount': amount,
            'Frequency': frequency,
            'Hour': hour,
            'Day_of_Week': day_of_week,
            'Location': location,
            'Device_Type': device_type,
            'Account_Age': account_age,
            'Previous_Fraud': prev_fraud,
            'Fraud': 1
        })
    
    df = pd.DataFrame(data)
    df = df.sample(frac=1, random_state=random_state).reset_index(drop=True)
    return df

def prepare_features(df):
    """Prepare features for modeling"""
    df_copy = df.copy()
    
    # Encode categorical variables
    le_location = LabelEncoder()
    le_device = LabelEncoder()
    df_copy['Location_Encoded'] = le_location.fit_transform(df_copy['Location'])
    df_copy['Device_Type_Encoded'] = le_device.fit_transform(df_copy['Device_Type'])
    
    # Select features
    feature_cols = ['Amount', 'Frequency', 'Hour', 'Day_of_Week', 'Location_Encoded',
                   'Device_Type_Encoded', 'Account_Age', 'Previous_Fraud']
    
    X = df_copy[feature_cols]
    y = df_copy['Fraud']
    
    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_scaled = pd.DataFrame(X_scaled, columns=feature_cols)
    
    return X_scaled, y, scaler, le_location, le_device

def train_models(X_train, X_test, y_train, y_test):
    """Train multiple fraud detection models"""
    models = {}
    results = []
    predictions = {}
    
    # Logistic Regression
    print("Training Logistic Regression...")
    lr = LogisticRegression(max_iter=1000, random_state=42)
    lr.fit(X_train, y_train)
    y_pred_lr = lr.predict(X_test)
    y_pred_proba_lr = lr.predict_proba(X_test)[:, 1]
    
    models['Logistic Regression'] = lr
    predictions['Logistic Regression'] = (y_pred_lr, y_pred_proba_lr)
    results.append({
        'Model': 'Logistic Regression',
        'Accuracy': accuracy_score(y_test, y_pred_lr),
        'Precision': precision_score(y_test, y_pred_lr),
        'Recall': recall_score(y_test, y_pred_lr),
        'F1_Score': f1_score(y_test, y_pred_lr),
        'ROC_AUC': roc_auc_score(y_test, y_pred_proba_lr)
    })
    
    # Random Forest
    print("Training Random Forest...")
    rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    rf.fit(X_train, y_train)
    y_pred_rf = rf.predict(X_test)
    y_pred_proba_rf = rf.predict_proba(X_test)[:, 1]
    
    models['Random Forest'] = rf
    predictions['Random Forest'] = (y_pred_rf, y_pred_proba_rf)
    results.append({
        'Model': 'Random Forest',
        'Accuracy': accuracy_score(y_test, y_pred_rf),
        'Precision': precision_score(y_test, y_pred_rf),
        'Recall': recall_score(y_test, y_pred_rf),
        'F1_Score': f1_score(y_test, y_pred_rf),
        'ROC_AUC': roc_auc_score(y_test, y_pred_proba_rf)
    })
    
    # Gradient Boosting
    print("Training Gradient Boosting...")
    gb = GradientBoostingClassifier(n_estimators=100, random_state=42)
    gb.fit(X_train, y_train)
    y_pred_gb = gb.predict(X_test)
    y_pred_proba_gb = gb.predict_proba(X_test)[:, 1]
    
    models['Gradient Boosting'] = gb
    predictions['Gradient Boosting'] = (y_pred_gb, y_pred_proba_gb)
    results.append({
        'Model': 'Gradient Boosting',
        'Accuracy': accuracy_score(y_test, y_pred_gb),
        'Precision': precision_score(y_test, y_pred_gb),
        'Recall': recall_score(y_test, y_pred_gb),
        'F1_Score': f1_score(y_test, y_pred_gb),
        'ROC_AUC': roc_auc_score(y_test, y_pred_proba_gb)
    })
    
    return models, pd.DataFrame(results), predictions, y_test

def plot_fraud_distribution(df):
    """Plot fraud distribution"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    fraud_counts = df['Fraud'].value_counts()
    colors = ['#2ecc71', '#e74c3c']
    
    axes[0].bar(['Legitimate', 'Fraudulent'], [fraud_counts[0], fraud_counts[1]], 
               color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
    axes[0].set_ylabel('Count', fontsize=11, fontweight='bold')
    axes[0].set_title('Transaction Distribution', fontsize=12, fontweight='bold')
    axes[0].grid(axis='y', alpha=0.3)
    for i, v in enumerate([fraud_counts[0], fraud_counts[1]]):
        axes[0].text(i, v + 50, str(v), ha='center', fontweight='bold')
    
    # Pie chart
    axes[1].pie([fraud_counts[0], fraud_counts[1]], labels=['Legitimate', 'Fraudulent'],
               colors=colors, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 11, 'weight': 'bold'})
    axes[1].set_title('Fraud Rate Distribution', fontsize=12, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/fraud_distribution.png', dpi=300, bbox_inches='tight')
    print("Saved: fraud_distribution.png")
    plt.close()

def plot_model_comparison(results_df):
    """Plot model performance comparison"""
    fig, axes = plt.subplots(2, 3, figsize=(14, 8))
    
    colors = ['#3498db', '#e74c3c', '#2ecc71']
    metrics = ['Accuracy', 'Precision', 'Recall', 'F1_Score', 'ROC_AUC']
    
    for idx, metric in enumerate(metrics):
        row = idx // 3
        col = idx % 3
        
        axes[row, col].bar(results_df['Model'], results_df[metric], color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
        axes[row, col].set_ylabel(metric, fontsize=11, fontweight='bold')
        axes[row, col].set_title(f'{metric} Comparison', fontsize=12, fontweight='bold')
        axes[row, col].set_ylim([0, 1.1])
        axes[row, col].grid(axis='y', alpha=0.3)
        axes[row, col].tick_params(axis='x', rotation=45)
        
        for i, v in enumerate(results_df[metric]):
            axes[row, col].text(i, v + 0.02, f'{v:.3f}', ha='center', fontweight='bold', fontsize=9)
    
    # Remove extra subplot
    fig.delaxes(axes[1, 2])
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/fraud_model_comparison.png', dpi=300, bbox_inches='tight')
    print("Saved: fraud_model_comparison.png")
    plt.close()

def plot_confusion_matrices(models, predictions, y_test):
    """Plot confusion matrices for all models"""
    fig, axes = plt.subplots(1, 3, figsize=(14, 4))
    
    for idx, (model_name, (y_pred, _)) in enumerate(predictions.items()):
        cm = confusion_matrix(y_test, y_pred)
        
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[idx], 
                   cbar_kws={'label': 'Count'}, annot_kws={'fontsize': 12, 'weight': 'bold'})
        axes[idx].set_xlabel('Predicted', fontsize=11, fontweight='bold')
        axes[idx].set_ylabel('Actual', fontsize=11, fontweight='bold')
        axes[idx].set_title(f'{model_name}', fontsize=12, fontweight='bold')
        axes[idx].set_xticklabels(['Legitimate', 'Fraud'])
        axes[idx].set_yticklabels(['Legitimate', 'Fraud'])
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/fraud_confusion_matrices.png', dpi=300, bbox_inches='tight')
    print("Saved: fraud_confusion_matrices.png")
    plt.close()

def plot_roc_curves(models, predictions, y_test):
    """Plot ROC curves for all models"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    colors = ['#3498db', '#e74c3c', '#2ecc71']
    
    for (model_name, (_, y_pred_proba)), color in zip(predictions.items(), colors):
        fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
        roc_auc = auc(fpr, tpr)
        ax.plot(fpr, tpr, color=color, lw=2.5, label=f'{model_name} (AUC = {roc_auc:.3f})')
    
    ax.plot([0, 1], [0, 1], 'k--', lw=2, label='Random Classifier')
    ax.set_xlabel('False Positive Rate', fontsize=11, fontweight='bold')
    ax.set_ylabel('True Positive Rate', fontsize=11, fontweight='bold')
    ax.set_title('ROC Curves - Fraud Detection Models', fontsize=12, fontweight='bold')
    ax.legend(loc='lower right', fontsize=10)
    ax.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/fraud_roc_curves.png', dpi=300, bbox_inches='tight')
    print("Saved: fraud_roc_curves.png")
    plt.close()

def plot_feature_importance(models):
    """Plot feature importance"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    feature_names = ['Amount', 'Frequency', 'Hour', 'Day_of_Week', 'Location', 'Device_Type', 'Account_Age', 'Prev_Fraud']
    
    # Random Forest
    rf = models['Random Forest']
    importance_rf = pd.DataFrame({
        'Feature': feature_names,
        'Importance': rf.feature_importances_
    }).sort_values('Importance', ascending=False)
    
    axes[0].barh(importance_rf['Feature'], importance_rf['Importance'], 
                color='#3498db', alpha=0.8, edgecolor='black', linewidth=1.5)
    axes[0].set_xlabel('Importance', fontsize=11, fontweight='bold')
    axes[0].set_title('Random Forest - Feature Importance', fontsize=12, fontweight='bold')
    axes[0].invert_yaxis()
    axes[0].grid(axis='x', alpha=0.3)
    
    # Gradient Boosting
    gb = models['Gradient Boosting']
    importance_gb = pd.DataFrame({
        'Feature': feature_names,
        'Importance': gb.feature_importances_
    }).sort_values('Importance', ascending=False)
    
    axes[1].barh(importance_gb['Feature'], importance_gb['Importance'],
                color='#e74c3c', alpha=0.8, edgecolor='black', linewidth=1.5)
    axes[1].set_xlabel('Importance', fontsize=11, fontweight='bold')
    axes[1].set_title('Gradient Boosting - Feature Importance', fontsize=12, fontweight='bold')
    axes[1].invert_yaxis()
    axes[1].grid(axis='x', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/fraud_feature_importance.png', dpi=300, bbox_inches='tight')
    print("Saved: fraud_feature_importance.png")
    plt.close()

def plot_transaction_analysis(df):
    """Plot transaction analysis by amount and location"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 8))
    
    # Amount distribution
    legitimate = df[df['Fraud'] == 0]['Amount']
    fraudulent = df[df['Fraud'] == 1]['Amount']
    
    axes[0, 0].hist([legitimate, fraudulent], bins=30, label=['Legitimate', 'Fraudulent'],
                   color=['#2ecc71', '#e74c3c'], alpha=0.7, edgecolor='black', linewidth=1.5)
    axes[0, 0].set_xlabel('Transaction Amount', fontsize=11, fontweight='bold')
    axes[0, 0].set_ylabel('Frequency', fontsize=11, fontweight='bold')
    axes[0, 0].set_title('Amount Distribution by Fraud Status', fontsize=12, fontweight='bold')
    axes[0, 0].legend()
    axes[0, 0].grid(axis='y', alpha=0.3)
    
    # Frequency distribution
    axes[0, 1].hist([df[df['Fraud'] == 0]['Frequency'], df[df['Fraud'] == 1]['Frequency']], 
                   bins=15, label=['Legitimate', 'Fraudulent'],
                   color=['#2ecc71', '#e74c3c'], alpha=0.7, edgecolor='black', linewidth=1.5)
    axes[0, 1].set_xlabel('Transaction Frequency', fontsize=11, fontweight='bold')
    axes[0, 1].set_ylabel('Count', fontsize=11, fontweight='bold')
    axes[0, 1].set_title('Frequency Distribution by Fraud Status', fontsize=12, fontweight='bold')
    axes[0, 1].legend()
    axes[0, 1].grid(axis='y', alpha=0.3)
    
    # Location analysis
    location_fraud = df.groupby('Location')['Fraud'].agg(['sum', 'count'])
    location_fraud['fraud_rate'] = location_fraud['sum'] / location_fraud['count']
    
    axes[1, 0].bar(location_fraud.index, location_fraud['fraud_rate'], 
                  color='#9b59b6', alpha=0.8, edgecolor='black', linewidth=1.5)
    axes[1, 0].set_ylabel('Fraud Rate', fontsize=11, fontweight='bold')
    axes[1, 0].set_title('Fraud Rate by Location', fontsize=12, fontweight='bold')
    axes[1, 0].tick_params(axis='x', rotation=45)
    axes[1, 0].grid(axis='y', alpha=0.3)
    
    # Hour analysis
    hour_fraud = df.groupby('Hour')['Fraud'].agg(['sum', 'count'])
    hour_fraud['fraud_rate'] = hour_fraud['sum'] / hour_fraud['count']
    
    axes[1, 1].plot(hour_fraud.index, hour_fraud['fraud_rate'], marker='o', linewidth=2.5, 
                   markersize=8, color='#e67e22', markerfacecolor='#e67e22', markeredgecolor='black', markeredgewidth=1.5)
    axes[1, 1].set_xlabel('Hour of Day', fontsize=11, fontweight='bold')
    axes[1, 1].set_ylabel('Fraud Rate', fontsize=11, fontweight='bold')
    axes[1, 1].set_title('Fraud Rate by Hour of Day', fontsize=12, fontweight='bold')
    axes[1, 1].grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/fraud_transaction_analysis.png', dpi=300, bbox_inches='tight')
    print("Saved: fraud_transaction_analysis.png")
    plt.close()

def main():
    print("="*80)
    print("MACHINE LEARNING-BASED FRAUD DETECTION SYSTEM")
    print("="*80)
    
    # Generate dataset
    print("\n[1] Generating synthetic transaction dataset...")
    df = generate_transaction_dataset(n_samples=5000, fraud_rate=0.05)
    df.to_csv('/home/ubuntu/fraud_data.csv', index=False)
    print(f"Dataset generated: {len(df)} transactions")
    print(f"Fraud cases: {df['Fraud'].sum()} ({df['Fraud'].mean()*100:.2f}%)")
    
    # Prepare features
    print("\n[2] Preparing features...")
    X, y, scaler, le_location, le_device = prepare_features(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"Training set: {len(X_train)}, Test set: {len(X_test)}")
    
    # Train models
    print("\n[3] Training fraud detection models...")
    models, results_df, predictions, y_test = train_models(X_train, X_test, y_train, y_test)
    results_df.to_csv('/home/ubuntu/fraud_model_results.csv', index=False)
    print("\nModel Results:")
    print(results_df.to_string(index=False))
    
    # Generate visualizations
    print("\n[4] Generating visualizations...")
    plot_fraud_distribution(df)
    plot_model_comparison(results_df)
    plot_confusion_matrices(models, predictions, y_test)
    plot_roc_curves(models, predictions, y_test)
    plot_feature_importance(models)
    plot_transaction_analysis(df)
    
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE - All visualizations saved")
    print("="*80)

if __name__ == "__main__":
    main()
