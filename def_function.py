# Seconds convert

def seconds_convert(seconds):
    hours = (seconds) // 3600
    minute = (seconds - (hours * 3600)) // 60
    remaining_seconds = (seconds - (hours * 3600) - (minute * 60))
    return (hours, minute, remaining_seconds)

hours, minute, remaining_seconds = seconds_convert(5000)

print(hours,minute,remaining_seconds)