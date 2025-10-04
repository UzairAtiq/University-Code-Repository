# Lab Journal 5 - Task 5: Machine Learning Basics with scikit-learn
# Programming for Artificial Intelligence

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

def generate_ml_dataset():
    """Generate a simple dataset for machine learning"""
    # Simulating house prices based on size and rooms
    np.random.seed(42)
    
    # Features: house size (sqft), number of rooms
    house_sizes = np.random.randint(1000, 3000, 100)
    num_rooms = np.random.randint(1, 6, 100)
    
    # Target: price (simplified relationship)
    # Price = 100 * size + 5000 * rooms + noise
    prices = (100 * house_sizes + 5000 * num_rooms + 
              np.random.normal(0, 10000, 100))
    
    # Combine features
    X = np.column_stack((house_sizes, num_rooms))
    y = prices
    
    return X, y, house_sizes, num_rooms

def simple_linear_regression():
    """Demonstrate simple linear regression"""
    print("Machine Learning - Linear Regression Example")
    
    # Generate dataset
    X, y, sizes, rooms = generate_ml_dataset()
    
    print(f"Dataset shape: {X.shape}")
    print(f"Sample data:")
    for i in range(5):
        print(f"  House {i+1}: {sizes[i]} sqft, {rooms[i]} rooms → ${y[i]:,.2f}")
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Create and train model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Evaluate model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"\nModel Performance:")
    print(f"Mean Squared Error: {mse:,.2f}")
    print(f"R² Score: {r2:.3f}")
    
    # Display coefficients
    print(f"\nModel coefficients:")
    print(f"Size coefficient: ${model.coef_[0]:.2f} per sqft")
    print(f"Rooms coefficient: ${model.coef_[1]:,.2f} per room")
    print(f"Intercept: ${model.intercept_:,.2f}")
    
    # Make sample predictions
    print(f"\nSample predictions vs actual:")
    for i in range(5):
        actual = y_test.iloc[i] if hasattr(y_test, 'iloc') else y_test[i]
        predicted = y_pred[i]
        print(f"  Actual: ${actual:,.2f}, Predicted: ${predicted:,.2f}")

def classification_example():
    """Simple classification example using dummy data"""
    print("\n" + "="*50)
    print("Classification Example (Conceptual)")
    
    # Simulated student pass/fail based on study hours and attendance
    study_hours = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
    attendance = [60, 70, 80, 90, 95, 40, 65, 75, 85, 92]
    passed = [0, 0, 1, 1, 1, 0, 0, 1, 1, 1]  # 0: fail, 1: pass
    
    print("Sample classification data:")
    for i in range(len(study_hours)):
        result = "Pass" if passed[i] else "Fail"
        print(f"  {study_hours[i]} hrs study, {attendance[i]}% attendance → {result}")
    
    # Simple rule-based classifier
    print("\nSimple rule: Pass if (study_hours >= 5 AND attendance >= 75)")
    correct = 0
    
    for i in range(len(study_hours)):
        predicted = 1 if (study_hours[i] >= 5 and attendance[i] >= 75) else 0
        actual = passed[i]
        if predicted == actual:
            correct += 1
        
        pred_label = "Pass" if predicted else "Fail"
        actual_label = "Pass" if actual else "Fail"
        status = "✓" if predicted == actual else "✗"
        print(f"  Predicted: {pred_label}, Actual: {actual_label} {status}")
    
    accuracy = correct / len(study_hours)
    print(f"\nRule-based classifier accuracy: {accuracy:.1%}")

def main():
    print("Lab Journal 5 - Task 5: Machine Learning Basics")
    
    # Linear regression example
    simple_linear_regression()
    
    # Classification example
    classification_example()
    
    print("\n" + "="*50)
    print("Note: This demonstrates basic ML concepts.")
    print("In practice, you would use train/validation/test splits,")
    print("cross-validation, and more sophisticated evaluation metrics.")

if __name__ == "__main__":
    main()