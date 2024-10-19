import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def plot_adg(df):
    """cleans genres and visualises average movie duration based on genre for top genres"""
    get_gen = df[['listed_in', 'duration']].copy()

    # Split genre combinations
    get_gen['listed_in'] = get_gen['listed_in'].str.split(', ')
    get_gen = get_gen.explode('listed_in')

    get_gen = get_gen.drop_duplicates()

    average_dur = get_gen.groupby('listed_in')['duration'].mean()
    top_gen = get_gen['listed_in'].value_counts().head(10).index
    top_adg = average_dur[average_dur.index.isin(top_gen)]

    top_adg.plot(kind='bar', figsize=(15, 6))
    plt.title('Top 10 Average Movie Duration by Genre')
    plt.xlabel('Genre')
    plt.ylabel('Average Duration (minutes)')
    plt.xticks(rotation=90, ha='center')
    plt.tight_layout()
    plt.grid(True)
    plt.show()

    return average_dur

def plot_ady(df):
    """Creates a scatter plot for movie duration vs year"""
    df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')

    sns.lmplot(x='release_year', y='duration', data=df, aspect=2,
                scatter_kws={'s': 10}, line_kws={'color': 'red'})
    plt.title('Movie Duration vs Release Year')
    plt.xlabel('Release Year')
    plt.ylabel('Movie_duration (minutes)')
    plt.grid(True)
    plt.tight_layout
    plt.show()

def dur_stat(df):
    """prints statistics for movie durations"""
    durations = df['duration'].to_numpy()

    mu_dur = np.mean(durations)
    x_dur = np.median(durations)
    sigma_dur = np.std(durations)

    print(f'Mean Duration: {mu_dur:.2f} minutes.')
    print(f'Median Duration: {x_dur:.2f} minutes.')
    print(f"Standard Deviation: {sigma_dur:.2f}\n")

def fltr_long(df, min_dur):
    """filter movies that are longer than specified dur"""
    dur = df['duration'].to_numpy()
    mask = dur > min_dur

    long = df[mask]

    return long

def fltr_short(df, max_dur):
    """filter movies that are shorter than specified dur"""
    dur = df['duration'].to_numpy()
    mask = dur < max_dur

    short = df[mask]

    return short
