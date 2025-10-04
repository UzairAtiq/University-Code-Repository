# Lab Journal 5 - Task 2: Data Analysis with Pandas
# Programming for Artificial Intelligence

import pandas as pd
import numpy as np

def main():
    print("Lab Journal 5 - Task 2: Data Analysis with Pandas")
    
    # Create sample dataset
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        'Age': [25, 30, 35, 28, 32],
        'Score': [95, 87, 92, 88, 91],
        'City': ['New York', 'London', 'Tokyo', 'Paris', 'Sydney']
    }
    
    df = pd.DataFrame(data)
    print("Sample DataFrame:")
    print(df)
    print()
    
    # Basic DataFrame operations
    print(f"DataFrame shape: {df.shape}")
    print(f"Column names: {list(df.columns)}")
    print(f"Data types:\n{df.dtypes}")
    print()
    
    # Statistical analysis
    print("Statistical summary:")
    print(df.describe())
    print()
    
    # Data filtering
    high_scorers = df[df['Score'] > 90]
    print("High scorers (Score > 90):")
    print(high_scorers)
    print()
    
    # Grouping and aggregation
    avg_score_by_city = df.groupby('City')['Score'].mean()
    print("Average score by city:")
    print(avg_score_by_city)

if __name__ == "__main__":
    main()