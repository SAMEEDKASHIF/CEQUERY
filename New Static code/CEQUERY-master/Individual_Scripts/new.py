feedback_train = []
for line in open('../data/student_data/full_train.json', 'r'):
    feedback_train.append(line.strip())
    
feedback_test = []
for line in open('../data/student_data/full_test.json', 'r'):
    student_test.append(line.strip())

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(binary=True)
cv.fit(feedback_train_clean)
X = cv.transform(feedback_train_clean)
X_test = cv.transform(feedback_test_clean)

import re

REPLACE_NO_SPACE = re.compile("[.;:!\'?,\"()\[\]]")
REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")

def preprocess_feedback(feedback):
    feedback = [REPLACE_NO_SPACE.sub("", line.lower()) for line in feedback]
    feedback = [REPLACE_WITH_SPACE.sub(" ", line) for line in feedback]
    
    return feedback

feedback_train_clean = preprocess_feedback(feedback_train)
feedback_test_clean = preprocess_feedback(feedback_test)
