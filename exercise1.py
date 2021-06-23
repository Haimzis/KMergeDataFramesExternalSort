import pandas as pd
from utils import timer


@timer
def simple_sorting(data_path):
    df = pd.read_csv(data_path)
    sorted_df = df.sort_values(['data'])
    return sorted_df


if __name__ == '__main__':
    sorted_data, time = simple_sorting('./sample.csv')
    sorted_data.to_csv('sorting-step1.csv', index=False)
    with open('sorting-step1_process_time.txt', 'w') as f:
        f.write(str(time))
