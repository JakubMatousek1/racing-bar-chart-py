"""
Full guide here: https://www.youtube.com/watch?v=mr61PDiUvwY

Create folder bar_chart_race in your git folder
Right-click on the folder and open in PyCharm
Click on Terminal in PyCharm
Type pip install virtualenv
create new environment by typing: virtualenv venv
Activate virtual env by typing:
	.\venv\Scripts\activate (windows)
	source venv/bin/activate (ios)
Install package by typing:
	pip install git+https://github.com/programiz/bar_char_race.git@master
Type pip freeze
Install ffmpeg - for saving as a video
	Go here https://github.com/BtbN/FFmpeg-Builds/releases/ and download the latest version

Get data in csv where header is the name of bar
Get pictures of bars where the name of picture is identical to the name of header in the csv
"""

import bar_chart_race as bcr
import pandas as pd

df = pd.read_csv("bix_offered.csv",index_col="Date")

# replace empty values with 0
df.fillna(0.0, inplace=True)

def summary(values, ranks):
    total_offered = int(round(values.sum(), -2))
    s = f'Total: {total_offered:,.0f}'
    return {'x': .99, 'y': .06, 's': s, 'ha': 'right', 'size': 30}

# using the bar_chart_race package
bcr.bar_chart_race(
    df=df, # must be a DataFrame where each row represents a single period of time.
    filename="total_offered_per_market.mp4", # name of the video file
    img_label_folder="bar_image_labels", # specify location of image folder
    fig_kwargs={'figsize': (26, 15),'dpi': 120,'facecolor': '#F8FAFF'},# change the Figure properties
    orientation="h", # orientation of the bar: h or v
    sort="desc", # sort the bar for each period
    n_bars=10, # number of bars to display in each frame
    fixed_max=True, # to fix the maximum value of the axis
    steps_per_period=45, # smoothness of the animation
    period_length=2000, #1500 # time period in ms for each row
    colors=[
        '#6ECBCE', '#FF2243', '#FFC33D', '#CE9673', '#FFA0FF', '#6501E5', '#F79522', '#699AF8', '#34718E', '#00DBCD',
        '#00A3FF', '#F8A737', '#56BD5B', '#D40CE5', '#6936F9', '#FF317B', '#0000F3', '#FFA0A0', '#31FF83', '#0556F3'
    ],# custom set of colors
    title={'label': 'Incoming contacts to 1st line since 2013', 'size': 50,'weight': 'bold','pad': 40}, # title and its styles
    period_label={'x': .95, 'y': .15,'ha': 'right','va': 'center','size': 72,'weight': 'semibold'},# adjust the position and style of the period label
    bar_label_font={'size': 27},# style the bar label text
    tick_label_font={'size': 27},  # style the labels in x and y axis
    bar_kwargs={'alpha': .99, 'lw': 0},
    bar_texttemplate='{x:,.0f}',# adjust the bar label format
    period_template='{x:.0f}', # adjust the period label format
    period_summary_func=summary
)
