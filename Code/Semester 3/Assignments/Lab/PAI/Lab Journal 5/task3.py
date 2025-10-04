# Lab Journal 5 - Task 3: Data Visualization with Matplotlib
# Programming for Artificial Intelligence

import matplotlib.pyplot as plt
import numpy as np

def main():
    print("Lab Journal 5 - Task 3: Data Visualization with Matplotlib")
    
    # Sample data
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    
    # Create subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Line plots
    ax1.plot(x, y1, label='sin(x)', color='blue')
    ax1.plot(x, y2, label='cos(x)', color='red')
    ax1.set_title('Trigonometric Functions')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.legend()
    ax1.grid(True)
    
    # Bar chart
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [23, 45, 56, 78, 32]
    
    ax2.bar(categories, values, color=['red', 'blue', 'green', 'orange', 'purple'])
    ax2.set_title('Sample Bar Chart')
    ax2.set_xlabel('Categories')
    ax2.set_ylabel('Values')
    
    plt.tight_layout()
    plt.savefig('sample_plot.png')
    plt.show()
    
    # Histogram
    data = np.random.normal(50, 15, 1000)
    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=30, alpha=0.7, color='skyblue', edgecolor='black')
    plt.title('Normal Distribution Histogram')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    plt.savefig('histogram.png')
    plt.show()

if __name__ == "__main__":
    main()