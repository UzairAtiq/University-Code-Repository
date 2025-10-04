# Lab Journal 5 - Task 4: Statistical Analysis and Data Processing
# Programming for Artificial Intelligence

import statistics
import random
from collections import Counter

def generate_sample_data():
    """Generate sample data for analysis"""
    # Simulating student scores
    scores = [random.randint(60, 100) for _ in range(50)]
    return scores

def statistical_analysis(data):
    """Perform statistical analysis on data"""
    print("Statistical Analysis Results:")
    print(f"Dataset size: {len(data)}")
    print(f"Mean: {statistics.mean(data):.2f}")
    print(f"Median: {statistics.median(data):.2f}")
    print(f"Mode: {statistics.mode(data)}")
    print(f"Standard Deviation: {statistics.stdev(data):.2f}")
    print(f"Variance: {statistics.variance(data):.2f}")
    print(f"Min: {min(data)}, Max: {max(data)}")
    print(f"Range: {max(data) - min(data)}")

def frequency_analysis(data):
    """Analyze frequency distribution"""
    counter = Counter(data)
    print("\nFrequency Analysis:")
    print("Score ranges and their frequencies:")
    
    ranges = {
        'A (90-100)': 0,
        'B (80-89)': 0,
        'C (70-79)': 0,
        'D (60-69)': 0
    }
    
    for score in data:
        if 90 <= score <= 100:
            ranges['A (90-100)'] += 1
        elif 80 <= score <= 89:
            ranges['B (80-89)'] += 1
        elif 70 <= score <= 79:
            ranges['C (70-79)'] += 1
        else:
            ranges['D (60-69)'] += 1
    
    for grade_range, count in ranges.items():
        percentage = (count / len(data)) * 100
        print(f"{grade_range}: {count} students ({percentage:.1f}%)")

def data_cleaning(data):
    """Demonstrate basic data cleaning operations"""
    print("\nData Cleaning Operations:")
    
    # Remove outliers (scores outside 2 standard deviations)
    mean = statistics.mean(data)
    std_dev = statistics.stdev(data)
    
    cleaned_data = [x for x in data if abs(x - mean) <= 2 * std_dev]
    outliers = [x for x in data if abs(x - mean) > 2 * std_dev]
    
    print(f"Original data points: {len(data)}")
    print(f"Cleaned data points: {len(cleaned_data)}")
    print(f"Outliers removed: {len(outliers)}")
    if outliers:
        print(f"Outlier values: {outliers}")
    
    return cleaned_data

def main():
    print("Lab Journal 5 - Task 4: Statistical Analysis and Data Processing")
    
    # Generate and analyze sample data
    sample_scores = generate_sample_data()
    print(f"Sample data (first 10 values): {sample_scores[:10]}")
    print()
    
    # Perform statistical analysis
    statistical_analysis(sample_scores)
    
    # Frequency analysis
    frequency_analysis(sample_scores)
    
    # Data cleaning
    cleaned_scores = data_cleaning(sample_scores)
    
    print("\nAfter cleaning:")
    statistical_analysis(cleaned_scores)

if __name__ == "__main__":
    main()