def timeConversion(s):
    s = list(s)
    hour = int(s[0] + s[1])
    meridian = s[8]+ s[9]
    if meridian == 'AM':
        if hour == 12:
            s[0], s[1] = '0', '0'
            print("".join(s[: -2]))
        else:
            print("".join(s[: -2]))
    elif meridian == 'PM':
        if hour < 12:
            hour += 12
            hour = list(str(hour))
            s[0], s[1] = hour[0], hour[1]
            print("".join(s[: -2]))
        else:
            print("".join(s[: -2]))

if __name__ == '__main__':
    s = input()
    timeConversion(s)