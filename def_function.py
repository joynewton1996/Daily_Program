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


def check_even_number(number):
    if number % 2 == 0:
        return True
    else:
        return False


print(check_even_number(44))


def check_storage(filesize):
    block_size = 4096
    # To calculate how many blocks are fully utilized
    full_block = filesize // block_size
    partial_block_reminder = filesize % block_size
    if partial_block_reminder > 0:
        return (full_block + 1) * block_size
    else:
        return filesize


print(check_storage(1))
print(check_storage(4096))
print(check_storage(4097))
print(check_storage(14000))


#


def format_name(first_name, last_name):
    a = first_name
    first_name = last_name
    last_name = a
    if first_name == "" and last_name == "":
        return first_name + last_name

    elif first_name and last_name != "":
        return ("Name: " + first_name + ", " + last_name)
    elif first_name == "" and last_name != 0:
        return ("Name: " + first_name + last_name)
    elif first_name != 0 and last_name == "":
        return ("Name: " + first_name)

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string
