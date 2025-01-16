import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

# 1. Create Real Estate dataset using arrays
# Feature 1: House size in square feet
# Feature 2: Age of house (years)
# Feature 3: Location (encoded as 0 for Suburban, 1 for Urban)
# Target: 1 for Sold, 0 for Not Sold

# Example data
data = np.array([
    [1500, 10, 0],  # 1500 sq.ft, 10 years old, Suburban
    [2000, 5, 1],   # 2000 sq.ft, 5 years old, Urban
    [1200, 15, 0],  # 1200 sq.ft, 15 years old, Suburban
    [1800, 8, 1],   # 1800 sq.ft, 8 years old, Urban
    [2500, 2, 1],   # 2500 sq.ft, 2 years old, Urban
    [1300, 20, 0],  # 1300 sq.ft, 20 years old, Suburban
    [2200, 7, 1],   # 2200 sq.ft, 7 years old, Urban
    [1600, 12, 0],  # 1600 sq.ft, 12 years old, Suburban
])

# Target: Sold (1) or Not Sold (0)
target = np.array([1, 1, 0, 1, 1, 0, 1, 0])

# 2. Convert to DataFrame for ease of use
df = pd.DataFrame(data, columns=["House Size (sq.ft)", "Age of House (Years)", "Location (Urban=1, Suburban=0)"])
df['Sold'] = target

# 3. Split the dataset into features (X) and target (y)
X = df.drop(columns=['Sold'])
y = df['Sold']

# 4. Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Initialize the Decision Tree Classifier with modified parameters
clf = DecisionTreeClassifier(
    max_depth=5,                # Allows deeper trees (default is None)
    min_samples_split=2,        # Minimum samples required to split a node (default is 2)
    min_samples_leaf=1,         # Minimum samples required at leaf node (default is 1)
    random_state=42
)

# 6. Train the Decision Tree model
clf.fit(X_train, y_train)

# 7. Predict using the trained model
y_pred = clf.predict(X_test)

# 8. Evaluate the model
accuracy = metrics.accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# 9. Visualize the Decision Tree
plt.figure(figsize=(10, 8))
plot_tree(clf, feature_names=X.columns, class_names=["Not Sold", "Sold"], filled=True, rounded=True)
plt.title("Decision Tree for Real Estate Sales Prediction")
plt.show()
