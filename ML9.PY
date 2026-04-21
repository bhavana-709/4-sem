import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
import matplotlib.pyplot as plt

# Dataset
X = np.array([
    [150, 0],
    [170, 1],
    [120, 0],
    [140, 1],
    [200, 1],
    [130, 0]
])

y = np.array(['Apple', 'Orange', 'Apple', 'Orange', 'Melon', 'Apple'])

# Model
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X, y)

# Rules
tree_rules = export_text(clf, feature_names=['Weight', 'Texture'])
print("Decision Tree Rules:\n", tree_rules)

# Plot
plt.figure(figsize=(10, 6))
plot_tree(clf, filled=True,
          feature_names=['Weight', 'Texture'],
          class_names=np.unique(y))
plt.show()