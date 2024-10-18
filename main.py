import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from clean_data import load_data
from year_analysis import plot_mpy
from duration_analysis import plot_adg, plot_ady
from genre_analysis import genre_count, gen_cor

data_path = "/Users/josiahiles/pandas/dataset/netflix_titles.csv"
df = load_data(data_path)
print(df.columns)

genre_count(df)
gen_cor(df)
plot_mpy(df)
plot_adg(df)
plot_ady(df)




