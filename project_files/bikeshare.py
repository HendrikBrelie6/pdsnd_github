# Importing

import time
import pandas as pd
import numpy as np
import datetime as dt


#Creating a dictionary with the data sources of the 3 cities

CITY_DATA = { 'chi': 'chicago.csv',
              'ny': 'new_york_city.csv',
              'was': 'washington.csv' }

MONTH_DATA = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'all']

DAY_DATA = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington).
    while True:
        city = input("Please enter the name of the city you would like to analyze. \nEnter from the following options: chi for chicago, ny for new york, and was for washington: ").lower()
        if city in CITY_DATA.keys():
            break
        else:
            print("Invalid input. Please double-check and enter again. Please make sure you use one of the abbreviations listed above.\n\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please enter the month you would like to analyze. \nEnter from the following options: jan, feb, mar, apr, may or jun. Or type all to analyze all months together:  ").lower()
        if month in MONTH_DATA:
            break
        else:
            print("Invalid input. Please double-check and enter again. Please make sure you use one of the abbreviations listed above.\n\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please enter the day you would like to analyze, \nEnter from the following options: monday, tuesday, wednesday, thursday, friday, saturday, sunday. Or type all to analyze all days together:  ").lower()
        if day in DAY_DATA:
            break
        else:
            print("Invalid input. Please double-check and enter again. Please make sure you use one of the abbreviations listed above!\n\n")
   
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.strftime('%A')
    # df['day'] = pd.to_datetime(df['day'], format='%A').dt.strftime('%a')
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = MONTH_DATA.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month_num = df['month'].mode()[0]
    most_common_month = MONTH_DATA[most_common_month_num]
    print("The most common month is ", most_common_month.capitalize())

    # TO DO: display the most common day of week
    most_common_day = df['day'].mode()[0]
    print('The most common day is ', most_common_day)

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common hour is ', most_common_hour)

    # print("\nThis took %s seconds." % (time.time() - start_time))
    # print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most common start station is ", common_start_station.capitalize())
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most common end station is ", common_end_station.capitalize())

    # TO DO: display most frequent combination of start station and end station trip
    df["trip"] = df['Start Station'] + " - " + df['End Station']
    common_trip = df['trip'].mode()[0]
    print("The most common trip is ", common_trip.capitalize())

    # print("\nThis took %s seconds." % (time.time() - start_time))
    # print('-'*40)


def trip_duration_stats(df):
   
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    # Convert the total travel time (in seconds) to hours, minutes, and seconds
    hours, remainder = divmod(total_travel_time, 3600)
    minutes, seconds = divmod(remainder, 60)
    # Format the total travel time as a string. Note the 02d means leading 0 if needed
    total_travel_formatted = f"{int(hours):,} hours // {int(minutes):,} min // {int(seconds):,} seconds"
    print("The total travel time in the time interval chosen was: ", total_travel_formatted)
    
    # TO DO: display mean travel time
    average_trip_duration=df['Trip Duration'].mean()
    # Convert the total travel time (in seconds) to hours, minutes, and seconds
    hours, remainder = divmod(average_trip_duration, 3600)
    minutes, seconds = divmod(remainder, 60)
    # Format the total travel time as a string. Note the 02d means leading 0 if needed
    average_trip_formatted = f"{int(hours):,} hours // {int(minutes):,} min // {int(seconds):,} seconds"
    print("The average travel time in the time interval chose was: ",average_trip_formatted)
    
    # print("\nThis took %s seconds." % (time.time() - start_time))
    # print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    count_user_types=df['User Type'].value_counts()
    # count_user_types_formatted = f"{count_user_types:,}"
    # print(count_user_types.values)
    print("The total count per each user type is:\n",count_user_types)
    # TO DO: Display counts of gender
    
    try:
        count_gender=df['Gender'].value_counts()
        print("\nThe total count per each gender is:\n",count_gender)
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_YOB=df['Birth Year'].min()
        print("\nThe earlist birth year is: ",int(earliest_YOB))
        most_recent_YOB=df['Birth Year'].max()
        print("The most recent birth year is: ",int(most_recent_YOB))
        most_common_YOB=df['Birth Year'].mode()
        print("The most common birth year is: ",int(most_common_YOB))
    except: 
        print("\nNote, Washington data does not contain gender or YOB information")
       
    # print("\nThis took %s seconds." % (time.time() - start_time))
    # print('-'*40)

def show_raw_data(df):
    """Displays raw data upon user request."""
    counter1 = 0 
    counter2 = 5
    # pd.set_option('display.max_columns',13)
    show_data = input ("\nWould you like to see the initial 5 rows of raw data? Please enter yes or no: ").lower()
    while show_data == 'yes':
        print(df.iloc[counter1:counter2,:])
        counter1 += 5
        counter2 += 5
        show_data = input ("\nWould you like to see 5 more rows of raw data? Please enter yes or no: ").lower()
            
    return df

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        # print(df.columns)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
