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
        city=input('hello! please enter city that you like ..chicago, new york city, washington\n').lower()
        if city not in CITY_DATA.keys():
            print('pleas enter city name correctly..')
        else:
            break
            
        
    
    
        


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        months=['january', 'february', 'march', 'april', 'may','june','all']
        month=input('hello! please enter month that you like .. Which month - January, February, March, April, May, or June?or all\n').lower()
        if month not in months:
            print('please enter valid month..')
        else:
            break
            


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=['saturday', 'sunday','monday','tuesday','wednesday','thursday','friday','all']
    while True:
        day=input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday, or all?\n').lower()
        if day not in days:
            print('please enter valid day..')
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
    try:
        df=pd.read_csv(CITY_DATA[city])
        df['Start Time']=pd.to_datetime(df['Start Time'])
        df['month']=df['Start Time'].dt.month
        df['day of week']=df['Start Time'].dt.day_name()
        
        
        if month != 'all':
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month=months.index(month) +1
            df=df[df['month']==month]
            
            
        if day != 'all':
            
            days=['saturday', 'sunday','monday','tuesday','wednesday','thursday','friday','all']
            df=df[df['day of week']== day.title()]
            
  
    except:
        print(' unable open file ,the file can\'t read ')
        
    else:
        print('the procces continue succsess')
        
            
    
    
    
    
    
    
        
        
        
        
    
    


    return df



    


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    
    
    popular_month=df['month'].mode().max()
    
    print('the most common month is {}'.format(popular_month))



    # TO DO: display the most common day of week
    
    popular_day_of_week=df['day of week'].mode().max()
    
    print('the most common day of week  is {}'.format(popular_day_of_week))      
          
          


    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    
    popular_hour=df['hour'].mode().max()
          
    print('the most common start hour is {}'.format(popular_hour))      


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station=df['Start Station'].mode().max()
    
    print('most commonly used start station is... {}'.format(popular_start_station))


    # TO DO: display most commonly used end station
    popular_end_station=df['End Station'].mode().max()
    
    print('most commonly used end station is... {}'.format(popular_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    popular_all=(df['Start Station']+" ' And ' "+df['End Station']).mode().max()
    
    print('most frequent combination of start station and end station trip is... {}'.format(popular_all))
   


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    stravel_time=df['Trip Duration'].sum()
    print('total travel time is equal ..{}'.format(stravel_time))


    # TO DO: display mean travel time
    
    mtravel_time=df['Trip Duration'].mean()
    print('mean travel time is equal ..{}'.format(round(mtravel_time)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    num_users=df['User Type'].value_counts()
    print('counts of user types is..\n{}'.format(num_users))


    # TO DO: Display counts of gender
    if city != 'washington':
        num_gender=df['Gender'].value_counts()
        print('counts of gender is ..\n{}'.format(num_gender))
    else:
        print('sorry {} dont have data there about gender'.format(city))
        
        
    
    


    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        year_birth=df['Birth Year']
        
        print('earliest year of birth is...{}'.format(int(year_birth.min())))
        
        print('most recent year of birth is...{}'.format(int(year_birth.max())))
        
        print('most common year of birth is...{}'.format(int(year_birth.mode()[0])))
    else:
        print('sorry {} dont have data there about year birth'.format(city))
    
    
    
    
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def runing_data(df):
    ans=input('do you want display 5th of data: yes..or..no\n').lower()
    i=0
    while True:
        if ans =='no':
            print(' ok \n Statistics Computed come next')
            break
            
        elif ans == 'yes':
            print(df[i:i+5])
            ans=input('would like to see 5 more rows of the data please type  yes..or..no\n').lower()
            i+=5
        else:   
            print("please enter valid data ...yes or no")
            ans=input('do you want display 5 row of data: yes..or..no\n').lower()    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        runing_data(df)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
