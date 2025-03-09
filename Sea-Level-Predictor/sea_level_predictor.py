import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10,6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data', color='blue', s = 5)

    # Create first line of best fit
    reg1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = range(1880, 2051)
    y1 = reg1.intercept + reg1.slope * pd.Series(x1)
    plt.plot(x1, y1, label='Fit (All Data)', color='red')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    reg2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x2 = range(2000, 2051)
    y2 = reg2.intercept + reg2.slope * pd.Series(x2)
    plt.plot(x2, y2, label='Fit from 2000', color='green')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    #plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()