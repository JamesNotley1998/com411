def progress(operation, value):
    """
    Task 3: Display a message to indicate the progress of an operation.xx

    The function should display a message in the following format:
    '{operation} {status}.'

    Where {operation} is the value of the parameter passed to this function
    and
    {status} is 'has started' if the value of the parameter 'value' is 0
    {status} is 'is in progress ({value}% completed)' if the value of the parameter 'value' is between,
    but not including, 0 and 100
    {status} is 'has completed' if the value of the parameter 'value' is 100

Where {operation} is the value of the user input indicating the operation being started (If the value is 0)
Where {operation} is the numerical user input value indicating the operation 'is in progress (??% completed
IF the value is between 0 and 100 (but not including) (This number user input indicates the progress)

    :param operation: a string (User input) indicating the operation being started
    :param value: an integer (numerical user input) indicating the amount of progress made
    :return: does not return anything
    """

#nested
#Ask user is operation started
print("Has the operation started?")
operation_status = input()

value = int(input())

if operation_status == "yes":
    print("Operation has started")

else:
    print(f"is in progress ({value}? completed")
