import numpy as np
from random import randint


class Point:
    def __init__(self, x, y, label):
        self.x = x
        self.y = y
        self.label = label

    def print(self):
        print(self.x, self.y, self.label)


def generate_negative_point():
    x = randint(0, 45)
    y = randint(0, 100)
    return Point(x, y, -1)


def generate_positive_point():
    x = randint(55, 100)
    y = randint(0, 100)
    return Point(x, y, 1)


def generate_coefficients():
    a = randint(-100, 100)
    b = randint(-100, 100)
    c = randint(-100, 100)
    return a, b, c


if __name__ == '__main__':
    # generating the random 100 points
    points = []
    for i in range(50):
        points.append(generate_positive_point())
        points.append(generate_negative_point())

    labels = np.array([])
    x = np.array([])
    y = np.array([])
    z = np.ones(100)  # considering all z equal to 1
    # separating the coordinates  x, y in separate numpy arrays for further calculations
    for point in points:
        x = np.append(x, [point.x])
        y = np.append(y, [point.y])
        labels = np.append(labels, [point.label])

    # shape = (3, 100) 3 rows, 100 columns
    np_points = np.array([x, y, z])
    # print(np_points)

    # coefficients shape = 3
    a, b, c = generate_coefficients()
    step = 1
    for _ in range(100):
        coefficients = np.array([a, b, c])
        print(coefficients)

        # calculating the position for each point towards the generated line
        # shape (100)
        X = np.dot(coefficients, np_points)
        # print(X)

        # trying to classify the above and below the line with 1 and -1
        # if an element is negative and the other is positive, they are on different sides of the line
        classified = (X > 0) * 1 + (X < 0) * -1
        # print(classified)

        misclassified = labels - classified
        # print(misclassified)

        errorCount = np.count_nonzero(misclassified)
        # print(errorCount)

        accuracy = (len(points) - errorCount) / len(points)
        print(f"Avem {errorCount} clasificari gresite.")
        print(f"Avem acuratetea totala de {accuracy * 100} %")

        if accuracy <= 0.5:
            step += -1
        else:
            step += 1

        # modify parameters
        a += step
        b += step
        c += step

