"""
Solutions for exercises/advanced/practice_data_and_ml.py
"""


def normalize_array(values):
    minimum, maximum = min(values), max(values)
    if maximum == minimum:
        return [0.0 for _ in values]
    return [(value - minimum) / (maximum - minimum) for value in values]


def train_simple_classifier(X, y):
    from sklearn.tree import DecisionTreeClassifier
    model = DecisionTreeClassifier(random_state=0)
    model.fit(X, y)
    return model


if __name__ == "__main__":
    print(normalize_array([10, 20, 30, 40]))
    clf = train_simple_classifier([[1, 0], [2, 1], [3, 0]], [0, 1, 0])
    print(clf.predict([[2, 1]]))
