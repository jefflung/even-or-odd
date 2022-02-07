#Task 3: Even or Odd using Functions

#Function to get the number from user keyboard

def get_number():
    number=int(input("Please enter a number:"))
    return number

#Function to determine if it is odd or even
def odd_even(number):
    if(number%2==0):
        answer="even"
    else:
        answer="odd"
    return answer

#Function to display the result
def display_result(answer):
    print("The answer is",answer)

number=get_number()
answer=odd_even(number)
display_result(answer)
