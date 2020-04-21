import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

# Define sample labels
true_labels = [1, 1, 1, 2, 3, 1, 1, 2, 2, 1, 2, 1, 2, 2, 1, 1, 2, 1, 3, 3, 1, 3, 1, 3,
 2, 2, 1, 1, 2, 2, 2, 1, 3, 2, 2, 3, 1, 2, 1, 3, 1, 3, 2, 2, 2]
pred_labels = [1, 1, 1, 2, 3, 1, 1, 2, 2, 1, 2, 1, 2, 2, 1, 1, 2, 1, 3, 3, 1, 3, 2, 3,
 2, 2, 1, 1, 2, 3, 2, 1, 3, 2, 2, 3, 1, 2, 1, 3, 1, 3, 2, 2, 2]

# Create confusion matrix
confusion_mat = confusion_matrix(true_labels, pred_labels)

# Visualize confusion matrix
plt.imshow(confusion_mat, interpolation='nearest', cmap=plt.cm.gray)
plt.title('Confusion matrix')
plt.colorbar()
ticks = np.arange(3)
plt.xticks(ticks, ticks)
plt.yticks(ticks, ticks)
plt.ylabel('True labels')
plt.xlabel('Predicted labels')
plt.show()

# Classification report
targets = ['Class-1', 'Class-2', 'Class-3']
print('\n', classification_report(true_labels, pred_labels,
target_names=targets))
