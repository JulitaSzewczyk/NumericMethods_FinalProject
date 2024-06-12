import os
import pandas as pd

import matplotlib.pyplot as plt

cities = ['gdańsk']

for city in cities:
    # Load data
    data_dir = r'C:\Users\ssiko\OneDrive\Pulpit\NumericMethods_FinalProject\plotting'
    approx_data_path = os.path.join(data_dir, f'{city}_weather_data_final.csv')
    model_data_path = os.path.join(data_dir, f'{city}_weather_data.csv')

    print(approx_data_path, model_data_path)
    
    if not os.path.exists(approx_data_path) or not os.path.exists(model_data_path):
        print(f"Data file not found for {city}. Skipping...")
        continue
    
    approx_data = pd.read_csv(approx_data_path)
    model_data = pd.read_csv(model_data_path)

    # Calculate absolute error for each column
    columns = approx_data.columns
    for column in columns:
        if column not in ['time', 'city']:
            approx_data[column] = pd.to_numeric(approx_data[column], errors='coerce')
            model_data[column] = pd.to_numeric(model_data[column], errors='coerce')
            error = abs(approx_data[column] - model_data[column])

            # Plot error
            plt.figure(figsize=(10, 6))
            plt.plot(error)
            plt.title(f'Absolute Error plot for {city} - {column}')
            plt.xlabel('Index')
            plt.ylabel('Absolute Error')
            plt.show()
