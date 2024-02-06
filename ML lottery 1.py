import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
import random

def train_and_predict_lottery_numbers_nn(file_path, future_draws=3):
    # Read the Excel/CSV file
    data = pd.read_csv(file_path)  # Use pd.read_excel(file_path) for Excel files

    # Features (past lottery numbers)
    X = data.iloc[:, :6].values

    # Target (strong number)
    y = data['Strong Number'].values

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Standardize the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train a Neural Network model
    model = MLPRegressor(random_state=42)
    model.fit(X_train_scaled, y_train)

    # Predict lottery numbers for future draws
    future_numbers = [random.sample(range(1, 38), 6) for _ in range(future_draws)]
    predicted_strong_numbers = [int(model.predict(scaler.transform([numbers[:6]]))[0]) % 7 + 1 for numbers in future_numbers]

    print(f"Predicted lottery numbers using Neural Network for the future ({future_draws} draws):")
    for i, (numbers, predicted_strong_number) in enumerate(zip(future_numbers, predicted_strong_numbers)):
        print(f"Draw {i + 1}: Numbers {numbers}, Strong Number {predicted_strong_number}")

# Replace 'your_file_path.csv' with the path to your CSV file
train_and_predict_lottery_numbers_nn('C:\Lottery\Lotto.csv', future_draws=12)
