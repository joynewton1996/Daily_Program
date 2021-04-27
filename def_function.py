# Seconds convert

def seconds_convert(seconds):
    hour = seconds // 3600
    minute = (seconds - (hour * 3600)) // 60
    second = (seconds - (hour * 3600) - (minute * 60))
    return hour, minute, second


hours, minute, remaining_seconds = seconds_convert(5000)

print(hours, minute, remaining_seconds)


def luckey_number(name):
    number = len(name) * 9
    print("the luckey number " + name + " is : " + str(number))


luckey_number("hello")
