# Edabit Fizzbuzz Challenge
# @url https://edabit.com/challenge/WXqH9qvvGkmx4dMvp
# @author Odai Athamneh
# @date 2020/11/21

def main():
    # test the output
    fizz_buzz(3) # "Fizz"
    fizz_buzz(5) # "Buzz"
    fizz_buzz(15) # "FizzBuzz"
    fizz_buzz(4) # "4"

def fizz_buzz(num):
    # set up some variables
    FIZZ_MULTIPLE = 3
    BUZZ_MULTIPLE = 5
    # is_fizz = true if (num % FIZZ_MULTIPLE == 0)

    if (num % FIZZ_MULTIPLE == 0):
        print("Fizz")
    elif (num % BUZZ_MULTIPLE == 0):
        print("Buzz")
    else:
        print(num)

main() # start main program