# ask user to input a time in minutes and seconds, and the program will count down from that time and play out an alarm when done
import time, os
from playsound import playsound

alarm = "alarm_clock_sound.mp3"


def play_alarm(seconds):
    count_time = 0
    
    while count_time < seconds:
        time.sleep(1)
        count_time += 1
        
        time_left = seconds - count_time
        minutes_left, seconds_left = divmod(time_left, 60)
        
        print(f"\rAlarm timer: {minutes_left:02d}:{seconds_left:02d}", end='', flush =True)
    
    os.system("cls")
    print("Times up! ALARM TIME")
    playsound(alarm)


print("When would you like the alarm to sound?")
minutes = int(input("Please enter the time in minutes: "))
seconds = int(input("Please enter the time in seconds: "))
total_time = (minutes * 60) + seconds
play_alarm(total_time)