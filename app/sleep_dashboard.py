import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="WHOOP Sleep Dashboard", layout="wide")

st.title("😴 WHOOP Sleep Data Dashboard")

# File uploader
uploaded_file = st.file_uploader("Upload your WHOOP sleeps.csv file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df['date'] = pd.to_datetime(df['Cycle start time'])
    df = df.sort_values('date')

    # Convert to hours
    df['asleep_hr'] = df['Asleep duration (min)'] / 60
    df['rem_hr'] = df['REM duration (min)'] / 60
    df['deep_hr'] = df['Deep (SWS) duration (min)'] / 60

    # Rolling average window
    roll_window = st.slider("Rolling Average Window", min_value=1, max_value=14, value=7)
    df['asleep_hr_roll'] = df['asleep_hr'].rolling(window=roll_window).mean()

    # Date range filter
    min_date = df['date'].min()
    max_date = df['date'].max()
    date_range = st.date_input("Select Date Range:", [min_date, max_date])

    df_filtered = df[(df['date'] >= pd.to_datetime(date_range[0])) & (df['date'] <= pd.to_datetime(date_range[1]))]

    st.subheader("Total Sleep Duration")
    st.line_chart(df_filtered.set_index('date')['asleep_hr'])

    st.subheader(f"{roll_window}-Day Rolling Average")
    st.line_chart(df_filtered.set_index('date')['asleep_hr_roll'])

    st.subheader("REM vs Deep Sleep")
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df_filtered['date'], df_filtered['rem_hr'], label='REM Sleep')
    ax.plot(df_filtered['date'], df_filtered['deep_hr'], label='Deep Sleep')
    ax.legend()
    st.pyplot(fig)

    st.write("Basic insights: Look for trends where total sleep is low + performance dips.")

import streamlit as st

st.title("💪 Workout vs Recovery Explorer")

sleep_file = st.file_uploader("Upload sleeps.csv", type="csv")
workout_file = st.file_uploader("Upload workouts.csv", type="csv")

if sleep_file and workout_file:
    # Load & clean sleep
    df_sleep = pd.read_csv(sleep_file)
    df_sleep['date'] = pd.to_datetime(df_sleep['Cycle start time']).dt.date
    df_sleep = df_sleep.rename(columns={
        'Asleep duration (min)': 'asleep_min',
        'Sleep performance %': 'sleep_perf'
    })
    df_sleep['asleep_hr'] = df_sleep['asleep_min'] / 60

    # Load & group workouts
    df_workouts = pd.read_csv(workout_file)
    df_workouts['Workout start time'] = pd.to_datetime(df_workouts['Workout start time'])
    df_workouts['date'] = df_workouts['Workout start time'].dt.date

    df_strain = df_workouts.groupby('date').agg({
        'Activity Strain': 'sum'
    }).reset_index().rename(columns={'Activity Strain': 'strain_score'})

    # Merge
    df_merged = pd.merge(df_sleep, df_strain, on='date', how='inner')

    st.write(df_merged.head())

    st.subheader("Workout Strain vs Sleep Performance")
    st.scatter_chart(df_merged[['strain_score', 'sleep_perf']])

    df_merged['strain_roll7'] = df_merged['strain_score'].rolling(window=7).mean()
    df_merged['sleep_perf_roll7'] = df_merged['sleep_perf'].rolling(window=7).mean()

    st.subheader("7-Day Rolling Average Trends")
    st.line_chart(df_merged[['date', 'strain_roll7', 'sleep_perf_roll7']].set_index('date'))
