import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

# 1. Create Mobile Phone Industry dataset using arrays
# Feature 1: Storage in GB
# Feature 2: RAM in GB
# Feature 3: Battery Capacity in mAh
# Feature 4: Brand (0 for Samsung, 1 for Apple, 2 for Xiaomi)
# Target: Price category (0 for Affordable, 1 for Expensive)

# Example data with more samples
data = np.array([
    [64, 4, 3000, 0],   # Samsung budget
    [128, 6, 3500, 1],  # Apple mid-range
    [256, 8, 4000, 2],  # Xiaomi flagship
    [64, 4, 3500, 0],   # Samsung budget
    [128, 6, 5000, 1],  # Apple mid-range
    [64, 4, 2800, 2],   # Xiaomi budget
    [256, 12, 5000, 0], # Samsung flagship
    [512, 8, 4500, 1],  # Apple flagship
    [32, 3, 2500, 0],   # Samsung ultra-budget
    [64, 3, 3000, 2],   # Xiaomi ultra-budget
    [128, 4, 3200, 0],  # Samsung lower-mid
    [256, 6, 4000, 1],  # Apple mid-range
    [512, 12, 5500, 2], # Xiaomi ultra-flagship
    [128, 8, 4500, 0],  # Samsung mid-range
    [256, 8, 4800, 1],  # Apple flagship
    [64, 6, 5000, 2],   # Xiaomi battery-focused
    [128, 12, 6000, 0], # Samsung battery-focused
    [512, 16, 4800, 1], # Apple ultra-flagship
    [256, 12, 5200, 2], # Xiaomi flagship
    [32, 2, 2800, 0],   # Samsung entry-level
])

# Target: expanded to match new data points
target = np.array([0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0])

# 2. Convert to DataFrame for ease of use
df = pd.DataFrame(data, columns=["Storage (GB)", "RAM (GB)", "Battery Capacity (mAh)", "Brand (Samsung=0, Apple=1, Xiaomi=2)"])
df['Price Category'] = target

# 3. Split the dataset into features (X) and target (y)
X = df.drop(columns=['Price Category'])
y = df['Price Category']

# 4. Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Initialize the Decision Tree Classifier with more detailed settings
clf = DecisionTreeClassifier(
    random_state=42,
    max_depth=None,             # No limit on depth, so the tree will grow fully
    min_samples_split=2,        # Allow splitting nodes with 2 samples
    min_samples_leaf=1,         # Allow leaves with a single sample
    max_features=None,          # Use all features for each split
)

# 6. Train the Decision Tree model
clf.fit(X_train, y_train)

# 7. Predict using the trained model
y_pred = clf.predict(X_test)

# 8. Evaluate the model
accuracy = metrics.accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# 9. Visualize the Decision Tree with more nodes
plt.figure(figsize=(15, 12))
plot_tree(clf, feature_names=X.columns, class_names=["Affordable", "Expensive"], 
          filled=True, rounded=True, fontsize=9)
plt.title("Decision Tree for Mobile Phone Price Classification (Detailed)")
plt.show()
