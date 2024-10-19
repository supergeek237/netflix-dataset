import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from clean_data import load_data
from year_analysis import plot_mpy, plot_gt, linreg_yd
from duration_analysis import plot_adg, plot_ady, dur_stat, fltr_long, fltr_short 
from genre_analysis import genre_count, gen_cor, gen_std

data_path = '/Users/josiahiles/pandas/dataset/netflix_titles.csv'
df = load_data(data_path)

slope, intercept = linreg_yd(df)

print(f'Year and Duration Regression Line : y = {slope:.2f}x + {intercept:.2f}')

genre_count(df)
plot_gt

print('Overall Duration Stats: ')
dur_stat(df)
print('Duration Stats for Long Movies: ')
dur_stat(fltr_long(df, 150))
print('Duration Stats for Short Movies: ')
dur_stat(fltr_short(df, 20))

std_drama, mean_drama = gen_std(df, 'Dramas')
print(f'Standard deviaton of Durations for Drama movies: {std_drama}')
print(f'Mean Duration for Drama movies: {mean_drama}')

gen_cor(df)

plot_mpy(df)
plot_adg(df)
plot_ady(df)












