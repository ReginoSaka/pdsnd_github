import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('For which city would you like to see data for: Chicago, New York City, or Washington?\n')
        if city.lower() not in ('chicago','new york city','washington'):
            print('Invalid input for city. Please choose from Chicago, New York City, or Washington')
        else:
            city = city.lower()
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('For which month would you like to see data for: All, January, February,..., June?\n')
        month = month.lower()
        if month not in ('all', 'january', 'february','march','april','may','june'):
            print('Invalid input for month. Please choose from All, January, February,..., June')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('For which weekday would you like to see data for: All, Monday, Tuesday, ... Sunday\n')
        day = day.lower
        if day not in ('all', 'monday', 'tuesday','wednesday','thursday','friday','saturday', 'sunday'):
            
            print('Invalid input for weekday. Please choose from All, Monday, Tuesday, ... Sunday')
        else:
            break

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
    city_data = {'chicago':'chicago.csv','new york city':'new_york_city.csv','washington':'washington.csv'}
    df = pd.read_csv(city_data[city])
    
    # extract month and day of week from Start Time to create new columns
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if specified
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month']==month]
        
    # filter by day of week if specified
    if day != 'all':
        df = df[df['day_of_week']==day.title()]

    df = df.reset_index(drop=True)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
   
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('Most Common Month is:', common_month)

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    common_weekday = df['day_of_week'].mode()[0]
    print('Most Common Weekday is:', common_weekday)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station is:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Commonly Used End Station is:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    start_trip = df[['Start Station','End Station']].mode()['Start Station'][0]
    end_trip = df[['Start Station','End Station']].mode()['End Station'][0]
    print('Most Frequent Combination of Start and End Station:\n', (start_trip,end_trip))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_travel_time = round(total_travel_time/60,2)
    print('Total Travel Time:',total_travel_time,'hours')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_travel_time = round(mean_travel_time/60,2)
    print('Mean Travel Time:',mean_travel_time,'hours')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = pd.DataFrame(df['User Type'].value_counts())
    print('These are the Counts of User Types:\n',user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        # Only display Gender count if this information exists 
        gender = pd.DataFrame(df['Gender'].value_counts())
        print('These are the Counts of Gender:\n',gender)
    else:
        print('Gender stats cannot be calculated because Gender does not exist in the dataframe')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        # Only display Gender count if this information exists 
        earliest_year = int(df['Birth Year'].describe()['min'])
        print('This is the earliest year of birth:',earliest_year)
        
        most_recent_year = int(df['Birth Year'].describe()['max'])
        print('This is the most recent year of birth:',most_recent_year)

        common_year = int(df['Birth Year'].mode()[0])
        print('This is the most common year of birth:',common_year)
    else:
        print('Birth Year stats cannot be calculated because Birth Year does not exist in the dataframe')
        
    

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
        
        # Display option to display 5 entries of the raw data, this is repeated until the user enter 'no'
        i=0
        while True:
            raw_data = input('\nWould you like to see through the raw data? Enter yes or no.\n')
            if raw_data.lower() == 'yes':
                display(df.iloc[i:,].head())
                i=i+5
            else:
                break
        # Display option to restart the project
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
