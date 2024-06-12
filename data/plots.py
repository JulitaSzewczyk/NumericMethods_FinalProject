import os
import matplotlib.pyplot as plt
import pandas as pd


cities = ['gdańsk', 'kraków', 'warszawa', 'wrocław', 'szczecin']

for city in cities:
    # Load data
    approx_data_path = os.path.join('approximated_data', f'{city}_weather_data_final.csv')
    model_data_path = os.path.join('model_data', f'{city}_weather_data.csv')
    
    if not os.path.exists(approx_data_path) or not os.path.exists(model_data_path):
        print(f"Data file not found for {city}. Skipping...")
        continue
    
    approx_data = pd.read_csv(approx_data_path)
    model_data = pd.read_csv(model_data_path)

    # Calculate absolute error
    error = abs(approx_data['tavg'] - model_data['tavg'])

    # Plot error
    plt.figure(figsize=(10, 6))
    plt.plot(error)
    plt.title(f'Absolute Error plot for {city}')
    plt.xlabel('Index')
    plt.ylabel('Absolute Error')
    plt.show()