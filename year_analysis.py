import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def plot_mpy(df):
    """visualises the number of movies release per year"""
    movies_py = df.groupby('release_year').size()

    movies_py.plot(kind='line', figsize=(10, 6))
    plt.title('Number of Movies Released to Netflix Per Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Movies')
    plt.grid(True)
    plt.show()

    return movies_py

def plot_gt(df):
    """visualisese trend of genre releases over time"""
        
    get_gen = df[['listed_in', 'release_year']].copy()
    get_gen['listed_in'] = get_gen['listed_in'].str.split(', ')
    get_gen = get_gen.explode('listed_in')

    trend = get_gen.groupby(['release_year', 'listed_in']).size().unstack().fillna(0)
    top_gen = trend.sum().sort_values(ascending=False).head(10).index

    trend[top_gen].plot(figsize=(12, 6))
    plt.title('Trend of Top 10 Genres Over Time')
    plt.xlabel('Release Year')
    plt.ylabel('Number of titles')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def linreg_yd(df):
    X = df['release_year'].to_numpy()
    y = df['duration'].to_numpy()

    X = np.vstack([X, np.ones(len(X))]).T

    beta, intercept = np.linalg.lstsq(X, y, rcond=None)[0]

    print(f'Beta Slope: {beta:.2f} ')
    print(f'Intercept: {intercept:.2f}')

    return beta, intercept
