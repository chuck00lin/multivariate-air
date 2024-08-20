import os
import pandas as pd

def merge_station_data(station_name, folder_2022, folder_2023, output_folder):
    # Load data from 2022 and 2023
    file_2022 = os.path.join(folder_2022, f"{station_name}_2022.csv")
    file_2023 = os.path.join(folder_2023, f"{station_name}_2023.csv")
    
    try:
        df_2022 = pd.read_csv(file_2022, encoding='utf-8')
        df_2023 = pd.read_csv(file_2023, encoding='utf-8')
    except Exception as e:
        print(f"Error reading files for {station_name}: {e}")
        return
    
    # Combine the data
    combined_df = pd.concat([df_2022, df_2023]).sort_values(by=['日期', '測項'])

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Save the combined data to the new folder
    output_file = os.path.join(output_folder, f"{station_name}_2022_2023.csv")
    combined_df.to_csv(output_file, index=False)
    print(f"Combined data saved for {station_name}.")

def merge_all_stations(folder_2022, folder_2023, output_folder):
    # Get the list of station files from 2022 folder
    station_files = [f for f in os.listdir(folder_2022) if f.endswith('_2022.csv')]

    for station_file in station_files:
        station_name = station_file.split('_')[0]
        merge_station_data(station_name, folder_2022, folder_2023, output_folder)

# Set folder paths
folder_2022 = './air_2022'
folder_2023 = './air_2023'
output_folder = './air_2_year'

# Merge the data
merge_all_stations(folder_2022, folder_2023, output_folder)
