import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
import joblib
 
# load the dataset
data = pd.read_csv("expenses_dataset.csv")

#Check first few rows (optional but good practice)
print(data.head())

# split into features and labels
x = data["Description"]
y = data["Category"]

#split data into training and testing sets(80% train, 20% test)
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

# create machine learning pipeline/ ignore common words and use n-grams
model = make_pipeline(
    TfidfVectorizer(ngram_range=(1,2)),
    MultinomialNB())

# train the model
model.fit(x_train, y_train) 

# make predictions on test data
predictions =model.predict(x_test)
# calculate accuracy
accuracy = accuracy_score(y_test, predictions)

print("\nClassification Report:\n")
print(classification_report(y_test, predictions))

print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, predictions))

print("Model Accuracy:", accuracy * 100, "%")

# save the model
joblib.dump(model, "expense_model.pkl")

# safe trained model
print("model trained and saved successfuly")











