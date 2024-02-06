import csv
import random
from collections import Counter
from statsmodels.tsa.arima.model import ARIMA
import numpy as np

lotto_draws = []


def load_historical_draws(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        for row in reader:
            draw = list(map(int, row[:6]))
            lotto_draws.append(draw)


def train_arima_model(data):
    model = ARIMA(data)
    model_fit = model.fit()
    return model_fit


def predict_next_draw(model_fit):
    future_predictions = model_fit.forecast(steps=1)[0]
    predictions = future_predictions.astype(int)
    return predictions


def update_model(new_draw):
    lotto_draws.append(new_draw)
    model = ARIMA(lotto_draws)
    model_fit = model.fit()
    return model_fit


def generate_random_draw():
    pass


def test_predictions(model_fit, iterations=100):
    prediction_accuracy = []

    for _ in range(iterations):
        predicted = predict_next_draw(model_fit)
        actual = generate_random_draw()

        match_count = sum(p == a for p, a in zip(predicted, actual))
        accuracy = match_count / len(predicted)
        prediction_accuracy.append(accuracy)

    print(np.mean(prediction_accuracy))


if __name__ == "__main__":
    load_historical_draws("C:\Lottery\Lotto.csv")

    model_fit = train_arima_model(lotto_draws)

    predicted = predict_next_draw(model_fit)
    print(predicted)

    model_fit = update_model(predicted)

    test_predictions(model_fit)
