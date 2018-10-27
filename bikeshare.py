import time
import calendar
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello there! Let\'s explore some interesting US bikeshare data!')


    """
    Get user input for city (chicago, new york city, washington)
    """
    city = input('Would you like to see data for the city Chicago, New York or Washington? ').casefold()

    while city not in CITY_DATA:
            print("Sorry, there's no data for that city!")
            city = input('Would you like to see data for Chicago, New York or Washington? ')

    """
    Ask user to view raw data
    """
    answer = input('Would you like to see the raw data from the city you chose? yes/no ')

    answer_data = ['yes', 'no']

    while answer not in answer_data:
            print("Sorry, that's not a valid answer!")
            answer = input('Would you like to see the raw data? yes/no ')

    index = 0

    while answer == answer_data[0]:
        df = pd.read_csv(CITY_DATA[city])
        print(df.loc[[0 + index, 1 + index, 2 + index, 3 + index, 4 + index]])
        index += 5
        answer = input('Would you like to see more raw data? yes/no ')


    """
    Get user input for month (all, january, february, ... , june)
    """
    month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

    month = input("Which month? January, February, March, April, May, June or all? ").casefold()

    while month not in month_list:
            print("Sorry, there's no data for that month!")
            month = input("Which month? January, February, March, April, May, June or all? ")


    """
    Get user input for day of week (all, monday, tuesday, ... sunday)
    """
    day = input('Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all? ').casefold()

    day_list = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')

    while day not in day_list:
            print("Sorry, there's no data for that day of the week!")
            day = input('Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all? ')

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

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    """
    Filter by month if applicable
    """
    if month != 'all':
        month_list = ['january', 'february', 'march', 'april', 'may', 'june']
        month = month_list.index(month) + 1
        df = df[df['month'] == month]

    """
    Filter by day of week if applicable
    """
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    """
    Display the most common month
    """
    popular_month = df.month.mode()[0]
    print('Most Frequent Start Month:', popular_month, '  (1=January, 2=February, 3=March, 4=April, 5=May, 6=June)')

    """
    Display the most common day of week
    """
    popular_day = df.day_of_week.mode()[0]
    print('Most Frequent Start Day:', popular_day)

    """
    Display the most common start hour
    """
    popular_hour = df.hour.mode()[0]
    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    df['start_station'] = df['Start Station']
    df['end_station'] = df['End Station']
    df['start_to_end_station'] = df['Start Station'] + " --- " + df['End Station']

    """
    Display most commonly used start station
    """
    popular_start_station = df.start_station.mode()[0]
    print('Most Frequent Start Station:', popular_start_station)

    """
    Display most commonly used end station
    """
    popular_end_station = df.end_station.mode()[0]
    print('Most Frequent End Station:', popular_end_station)

    """
    Display most frequent combination of start station and end station trip
    """
    popular_start_to_end_station = df.start_to_end_station.mode()[0]
    print('Most Frequent Start to End Station:', popular_start_to_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    """
    Display total travel time
    """
    total_travel_time = df['Trip Duration'].sum()
    days = total_travel_time // 86400

    total_travel_time %= 86400
    hours = total_travel_time // 3600

    total_travel_time %= 3600
    minutes = total_travel_time // 60

    total_travel_time %= 60
    seconds = int(total_travel_time)

    print('Total travel time:'"\n", days,"days", hours, "hours", minutes, "minutes", seconds, "seconds")

    """
    Display mean travel time
    """
    mean_travel_time = df['Trip Duration'].mean()
    days = mean_travel_time // 86400

    mean_travel_time %= 86400
    hours = mean_travel_time // 3600

    mean_travel_time %= 3600
    minutes = mean_travel_time // 60

    mean_travel_time %= 60
    seconds = int(mean_travel_time)

    print('Mean_travel_time:'"\n", days,"days", hours, "hours", minutes, "minutes", seconds, "seconds")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    """
    Display counts of user types
    """
    user_types = df['User Type'].value_counts()
    print("\n"'Count by user type:'"\n",user_types.to_string(header=None))

    """
    Display counts of gender
    """
    try:
        gender = df['Gender'].value_counts()
        print("\n"'Count by gender:'"\n",gender.to_string(header=None))

    except KeyError as e:
        print('No data for: {}'.format(e))

    """
    Display earliest, most recent, and most common year of birth
    """
    try:
        df['birth_year'] = df['Birth Year']

        birth_earliest = int(df['Birth Year'].min())
        print('Earliest birth year:', birth_earliest)

        birth_recent = int(df['Birth Year'].max())
        print('Most recent birth year:', birth_recent)

        popular_birth_year = int(df.birth_year.mode()[0])
        print('Most common birth year:', popular_birth_year)

    except KeyError as e:
        print('No data for: {}'.format(e))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
