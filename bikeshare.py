#important librares 
import time
import pandas as pd 
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }


cities = ['chicago', 'new york', 'washington']

months = ['january','february','march','april','may','june']

days = ['sunday','monday','wednesday','tuesday','thursday','friday','saturday']

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
        city = input("Which city you want to choose Chicago, New York City, Washington? ").lower()
        if city in cities:
            break

        # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("which month will you choose or you can write all to choose all months? ").lower()
        if month in months:
            break
        if month == 'all':
            break


        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which days you want to choose or or you can say all to choose all days? ").lower()
        if day in days:
            break
        if day == 'all':
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

    df = pd.read_csv(CITY_DATA[city])
    
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    
    
    df["month"] = df["Start Time"].dt.month
    

    if month != "all":
        month = months.index(month) + 1
        df = df[df["month"] == month ] 
        
    df["hour"] = df["Start Time"].dt.hour
    
    df["day_of_week"] = df["Start Time"].dt.weekday_name
    
    if day != "all":
        df = df[df["day_of_week"] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df["month"].value_counts().idxmax()
    print("The most common month is: ", common_month)

    # TO DO: display the most common day of week
    common_day = df["day_of_week"].value_counts().idxmax()
    print("The most common day is: ", common_day)
    
    # TO DO: display the most common start hour
    common_hour = df["hour"].value_counts().idxmax()
    print("The most common hour is: ", common_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df["Start Station"].value_counts().idxmax()
    print("The most common start station :", common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df ["End Station"].value_counts().idxmax()
    print("The most common end station :", common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_start_end_station = df[["End Station","Start Station"]].mode().loc[0]
    print("The most common start {} and end {} station: ".format(common_start_end_station[0],common_start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df["Trip Duration"].sum()
    print("Total time for tarvel: ",total_travel)

    # TO DO: display mean travel time
    mean_travel = df["Trip Duration"].mean()
    print("Mean time for tarvel: ",mean_travel)
    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    counts_of_user = df["User Type"].value_counts()
    
    
    print("The counts of user type: ",counts_of_user)
    
    
    print()
    
    # TO DO: Display counts of gender
    if (cities == 'new york' or cities == 'chicago'):
    	{
		 
		    counts_of_gender = df["Gender"].value_counts()
		    
		        
		        
		    print("The counts of gender: ",counts_of_gender)

		    # TO DO: Display earliest, most recent, and most common year of birth
		    birth_year = df["Birth Year"]
		    
		    earliest_year = birth_year.value_counts().min()
		    print("The earliest year is: ", earliest_year)
		    
		    recent_year = birth_year.value_counts().max()      
		    print("The earliest year is: ", recent_year)
		    
		    common_year = birth_year.value_counts().idxmax()
		    print("The most common year is: ", common_year)
		 }
	else {
	print("City does not have any data about Gender or Birth")
	}
    
    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    def display_data():
    	view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    	start_loc = 0
		while (view_data == 'yes'):
		  print(df.iloc[start_loc:start_loc + 5])
		  start_loc += 5
		  view_data = input("Do you wish to continue?: Enter yes or no.\n").lower()
		  if view_data == 'no':
		  	break

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

    
    #Sources 
    #https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.hour.html
    #https://stackoverflow.com/questions/15138973/how-to-get-the-number-of-the-most-frequent-value-in-a-column