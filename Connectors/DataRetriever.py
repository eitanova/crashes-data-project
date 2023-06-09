import os

import requests
import pandas as pd
import zipfile


class DataRetriever:
    # Constructor
    def __init__(self, url):
        self.url = url
        self.df_data = pd.DataFrame()

    # Setters
    def retrieve_records(self, resource, selected_params=None, filters="limit=99999"):
        uri = f"{self.url}{resource}&{filters}"
        response = requests.get(uri)

        if response.status_code == 200:
            data = response.json()['result']['records']

            if selected_params:
                data = [{param: item[param] for param in selected_params} for item in data]

            self.df_data = pd.concat([self.df_data, pd.DataFrame(data)], ignore_index=True)
            return 200

        return 500

    def extract_data_zip(self, zip_path, zip_name, csv_file, selected_params):

        response = requests.get(zip_path)

        with open(zip_name, 'wb') as f:
            f.write(response.content)

        with zipfile.ZipFile(zip_name, 'r') as zip_ref:
            zip_ref.extract(csv_file)

        data = pd.read_csv(csv_file)

        if selected_params:
            data = data[selected_params]

        os.remove(csv_file)
        os.remove(zip_name)

        self.df_data = pd.concat([self.df_data, data], ignore_index=True)

    def rename_data(self, new_params):
        for old_name, new_name in new_params.items():
            if old_name in self.df_data.columns:
                if new_name not in self.df_data.columns:
                    self.df_data.rename(columns={old_name: new_name}, inplace=True)
                else:
                    self.df_data[new_name] = self.df_data[new_name].fillna(self.df_data[old_name])
                    del self.df_data[old_name]

    def set_col_data(self, col_name, col):
        self.df_data[col_name] = col

    def merge_data(self, df_data):
        self.df_data = pd.concat([self.df_data, df_data], ignore_index=True)

    def replace_data(self, new_data):
        self.df_data = new_data

    # Getters
    def get_data(self):
        return self.df_data

    def get_col_data(self, col_name):
        return self.df_data[col_name]
