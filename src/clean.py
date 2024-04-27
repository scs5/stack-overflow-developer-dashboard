import pandas as pd

DATA_RAW_FN = './data/survey_data_raw.csv'
DATA_CLEANED_FN = './data/survey_data_cleaned.csv'


def load_data():
    df = pd.read_csv(DATA_RAW_FN)
    return df


def clean_data(df):
    # Remove NAs
    df.replace('NA', '')
    
    # Save cleaned data
    df.to_csv(DATA_CLEANED_FN)


if __name__ == '__main__':
    df = load_data()
    clean_data(df)