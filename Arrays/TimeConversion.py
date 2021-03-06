"""
Time Conversion program (Hackerrank)
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example


Input '12:01:00AM'.


Return '00:01:00'.

Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

string s: a time in  hour format
Returns

string: the time in  hour format
Input Format

A single string  that represents a time in -hour clock format (i.e.:  or ).

Constraints

All input times are valid
Sample Input 0

07:05:45PM
Sample Output 0

19:05:45


Hints : You will have to learn about split(), join(), substring(), 

"""

def timeConversion(string : str) : 
    #   getting each part of the string
    new_str = string.split(":")
    hours = new_str[0]
    minutes = new_str[1]
    seconds = new_str[2][:2]
    am_pm = new_str[2][2:]

    #   variable holding the result of the array
    result = ""

    #   checking if the time is PM
    if am_pm == 'PM' : 
        if int(hours) < 12 : 
            hours = str(int(hours) + 12)

    #   checking if the time is AM
    if am_pm == 'AM' : 
        if int(hours) == 12 : 
            hours = "00"
    
    #   returning the output in the correct format
    return ":".join([str(hours), str(minutes), str(seconds)])


if __name__ == '__main__' : 
    print(timeConversion("12:40:22AM"))