import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn import cross_validation
from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

from utilities import visualize_classifier

data = np.loadtxt('wine.data.txt', delimiter=',' )


X, y = data[:, 1:], data[:, 0]
#print(X)
#print(y)
# Create Naive Bayes classifier
classifier = GaussianNB()

# Train the classifier
classifier.fit(X, y)

# Predict the values for training data
y_pred = classifier.predict(X)

# Compute accuracy
accuracy = 100.0 * (y == y_pred).sum() / X.shape[0]

#Split data into training and test data ()
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.25, random_state = 3)

classifier_new = GaussianNB()

classifier_new.fit(X_train, y_train)

y_test_pred = classifier_new.predict(X_test)
print(y_test)
print(y_test_pred)
# compute accuracy of the classifier
accuracy = 100.0 * (y_test == y_test_pred).sum() / X_test.shape[0]
print("Accuracy of the new classifier =", round(accuracy, 2), "%")


# Visualize the performance of the classifier
#visualize_classifier(classifier_new, X_test, y_test)

num_folds = 3
accuracy_values = cross_validation.cross_val_score(classifier, X, y, scoring='accuracy', cv=num_folds)
print("Accuracy: " + str(round(100*accuracy_values.mean(), 2)) + "%")

precision_values = cross_validation.cross_val_score(classifier, X, y, scoring='precision_weighted', cv=num_folds)
print("Precision: " + str(round(100*precision_values.mean(), 2)) + "%")

recall_values = cross_validation.cross_val_score(classifier, X, y, scoring='recall_weighted', cv=num_folds)
print("Recall: " + str(round(100*recall_values.mean(), 2)) + "%")

f1_values = cross_validation.cross_val_score(classifier, X, y, scoring='f1_weighted', cv=num_folds)
print("F1: " + str(round(100*f1_values.mean(), 2)) + "%")


# Create confusion matrix for y_train and X_train 
confusion_mat = confusion_matrix(y_train, classifier.predict(X_train))

# Visualize confusion matrix
plt.imshow(confusion_mat, interpolation='nearest', cmap=plt.cm.gray)
plt.title('Confusion matrix for the training data')
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
plt.title('Confusion matrix for the testing data')
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
