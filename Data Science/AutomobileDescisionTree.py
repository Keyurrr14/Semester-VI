import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

# 1. Create Automobile Industry dataset using arrays
# Feature 1: Engine size in liters
# Feature 2: Year of manufacture
# Feature 3: Fuel type (0 for Gasoline, 1 for Diesel)
# Feature 4: Mileage (miles per gallon)
# Target: Price category (0 for Cheap, 1 for Expensive)

# Example data
data = np.array([
    [1.5, 2015, 0, 30],  # 1.5L engine, 2015, Gasoline, 30 mpg
    [2.0, 2018, 1, 25],  # 2.0L engine, 2018, Diesel, 25 mpg
    [1.6, 2016, 0, 28],  # 1.6L engine, 2016, Gasoline, 28 mpg
    [2.5, 2020, 1, 20],  # 2.5L engine, 2020, Diesel, 20 mpg
    [3.0, 2017, 1, 18],  # 3.0L engine, 2017, Diesel, 18 mpg
    [1.8, 2019, 0, 32],  # 1.8L engine, 2019, Gasoline, 32 mpg
    [2.2, 2021, 1, 22],  # 2.2L engine, 2021, Diesel, 22 mpg
    [1.4, 2014, 0, 35],  # 1.4L engine, 2014, Gasoline, 35 mpg
])

# Target: 0 for Cheap, 1 for Expensive
target = np.array([0, 1, 0, 1, 1, 0, 1, 0])

# 2. Convert to DataFrame for ease of use
df = pd.DataFrame(data, columns=["Engine Size (L)", "Year of Manufacture", "Fuel Type (Gasoline=0, Diesel=1)", "Mileage (mpg)"])
df['Price Category'] = target

# 3. Split the dataset into features (X) and target (y)
X = df.drop(columns=['Price Category'])
y = df['Price Category']

# 4. Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Initialize the Decision Tree Classifier
clf = DecisionTreeClassifier(random_state=42)

# 6. Train the Decision Tree model
clf.fit(X_train, y_train)

# 7. Predict using the trained model
y_pred = clf.predict(X_test)

# 8. Evaluate the model
accuracy = metrics.accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# 9. Visualize the Decision Tree
plt.figure(figsize=(10, 8))
plot_tree(clf, feature_names=X.columns, class_names=["Cheap", "Expensive"], filled=True, rounded=True)
plt.title("Decision Tree for Automobile Price Classification")
plt.show()
