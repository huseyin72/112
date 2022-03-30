#finding highest number in a list
def highest_number(list):
    highest = 0
    for i in list:
        if i > highest:
            highest = i
    return highest