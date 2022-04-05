# Here we have to convert 12 hour format to 24 hour Railway time format
def timeConversion(s):
    # Processing Input: Input value is in string,so we have separate each character and store it in a list
    s = list(s)
    # Eg: '12:00:00AM'
    # Hour value is at index 0 and 1, meridian value is at index 8 and 9
    hour = int(s[0] + s[1])
    meridian = s[8] + s[9]
    # prioritizing condition is important for optimal time complexity
    # In real time project, time complexity is purely depends upon the input meridian(AM or PM).
    # We can't say number of inputs in 'AM' is higher/lower or number of inputs in 'PM' is higher/lower, it varies on time to time.
 
    # 1. From "12:00:00AM" to "12:59:59AM" - period of 1 hour
    # 2. From "01:00:00AM" to "12:59:59PM" - period of 12 hour
    # 3. From "01:00:00PM" to "11:59:59PM" - period of 11 hour

    # Now, we can easily prioritize conditions based upon the higher number of time period

    if (meridian == 'AM' and hour != 12) or (meridian == 'PM' and hour == 12): # satisfies 2nd point and this is most possibility of 12 hours time period
        print("".join(s[: -2]))
    
    elif meridian == 'PM' and hour < 12: # satisfies 4th point and this is most possiblility of 11 hours time period

        # check hour is less than 12. If so, add the hour value to 12 and just replace hour value in the postion s[0] and s[1] 
        hour += 12
        hour = list(str(hour))
        s[0], s[1] = hour[0], hour[1]
        # join function in list is used here to join each character to form a string and neglect s[8] and s[9] i.e., meridian value
        print("".join(s[: -2]))

    elif meridian == 'AM' and hour == 12: # satisfies 1st point and this is least possibility
        s[0], s[1] = '0', '0'
        print("".join(s[: -2]))
        
if __name__ == '__main__':
    # In the first of console get time as a string and store it in variable 's'  
    s = input()
    # That's all in main function, just call the function 'timeConversion' and pass the argument s
    timeConversion(s)