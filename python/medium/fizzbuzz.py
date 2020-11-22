# Edabit Fizzbuzz Challenge
# @url https://edabit.com/challenge/WXqH9qvvGkmx4dMvp
# @author Odai Athamneh
# @date 2020/11/21

def main():
    # test the output
    print(fizz_buzz(3))  # "Fizz"
    print(fizz_buzz(5))  # "Buzz"
    print(fizz_buzz(15)) # "FizzBuzz"
    print(fizz_buzz(4))  # "4"

def fizz_buzz(num):
    # set up some variables
    FIZZ_MULTIPLE = 3
    BUZZ_MULTIPLE = 5
    is_fizz = True if (num % FIZZ_MULTIPLE == 0) else False
    is_buzz = True if (num % BUZZ_MULTIPLE == 0) else False

    # determine output
    if (is_fizz and is_buzz):
        return "FizzBuzz"
    elif (is_fizz):
        return "Fizz"
    elif (is_buzz):
        return "Buzz"
    else:
        return str(num) # convert into string

main() # start main program