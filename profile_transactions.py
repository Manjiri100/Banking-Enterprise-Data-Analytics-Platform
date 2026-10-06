import argparse
import pandas as pd


def profile(path):
    df = pd.read_parquet(path) if path.endswith('.parquet') else pd.read_csv(path)
    print('Rows:', len(df))
    print('Columns:', len(df.columns))
    print('\nMissing values:')
    print(df.isna().sum().sort_values(ascending=False))
    print('\nDuplicate transaction IDs:', df['transaction_id'].duplicated().sum())
    print('Negative amounts:', (df['amount'] < 0).sum())
    print('\nNumeric summary:')
    print(df[['amount']].describe())

if __name__ == '__main__':
    p=argparse.ArgumentParser(); p.add_argument('path'); args=p.parse_args(); profile(args.path)
