import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn import cross_validation
from sklearn.tree import DecisionTreeClassifier
from utilities import visualize_classifier

from utilities import visualize_classifier

# Load input data
data = np.loadtxt("wine.data.txt", delimiter=',')
X, y = data[:,1:], data[:, 0]

# Split data into training and testing datasets
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y,
test_size=0.25, random_state=5)

# Decision Trees classifier
params = {'random_state': 0, 'max_depth': 4}
classifier = DecisionTreeClassifier(**params)
classifier.fit(X_train, y_train)
#visualize_classifier(classifier, X_train, y_train, 'Training dataset')

y_test_pred = classifier.predict(X_test)

# Create confusion matrix for y_train and X_train 
confusion_mat = confusion_matrix(y_train, classifier.predict(X_train))

# Visualize confusion matrix
plt.imshow(confusion_mat, interpolation='nearest', cmap=plt.cm.gray)
plt.title('Confusion matrix with training data ')
plt.colorbar()
ticks = np.arange(3)
plt.xticks(ticks, ticks)
plt.yticks(ticks, ticks)
plt.ylabel('True labels')
plt.xlabel('Predicted labels')
plt.show()

#classification report
class_names = ['Class-0', 'Class-1', 'Class-2']
print("\n" + "#"*40)
print("\n Classifier performance on training dataset \n")
print(classification_report(y_train, classifier.predict(X_train),
target_names=class_names))
print("#"*40 + "\n")
print("#"*40)

# Create confusion matrix for y_test and y_test_prediction. The differences
confusion_mat = confusion_matrix(y_test, y_test_pred)

# Visualize confusion matrix
plt.imshow(confusion_mat, interpolation='nearest', cmap=plt.cm.gray)
plt.title('Confusion matrix with testing data')
plt.colorbar()
ticks = np.arange(3)
plt.xticks(ticks, ticks)
plt.yticks(ticks, ticks)
plt.ylabel('True labels')
plt.xlabel('Predicted labels')
plt.show()

print("\n Classifier performance on_test dataset\n")
print(classification_report(y_test, y_test_pred, target_names=class_names))
print("#"*40 + "\n")
