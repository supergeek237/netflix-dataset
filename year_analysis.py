import matplotlib.pyplot as plt

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

