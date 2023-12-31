"""Loop exercises."""


def sum_between(start: int, end: int) -> int:
    numbers = list(range(start, end + 1))
    total = 0
    for nr in number:
        total = total + nr
    return total

    print(sum_between(3, 5))
    print(sum_between(5, 5))

def sum_of_even_numbers(n: int) -> int:
    result = 0
    for num in range(n + 1):
        if num % 2 == 0:
            result += num
    return result

def sum_of_multiples(n: int, end: int) -> int:
    result = 0
    for num in range(n, end + 1):
        if num % n == 0:
            result += num
    return result

def cross_sum(numbers: str) -> int:
    result = 0
    for digit in numbers:
        result += int(digit)
    return result

def multiply_between(start: int, end: int) -> int:
    result = 1
    for num in range(start, end + 1):
        result *= num
    return result

def make_hola_string(count: int) -> str:
    return "hola" * count

def compound_interest(amount: int, years: int, rate: int) -> float:
    for _ in range(years):
        amount += amount * (rate / 100)
    return amount

def remove_vowels(original_string: str) -> str:
    vowels = "AEIOUÕÄÖÜaeiouõäöü"
    result = ""
    for char in original_string:
        if char not in vowels:
            result += char
    return result

if __name__ == '__main':
    print(sum_between(3, 5))  # => 12
    print(sum_between(5, 5))  # => 5
   
    print(sum_of_even_numbers(5))  # => 6
    print(sum_of_even_numbers(0))  # => 0

    print(sum_of_multiples(3, 10))  # => 18
    print(sum_of_multiples(7, 10))  # => 7
    print(sum_of_multiples(11, 10))  # => 0

    print(cross_sum("1234"))  # => 10
    print(cross_sum("0"))  # => 0
    print(cross_sum("4129458"))  # => 33

    print(multiply_between(1, 3))  # => 6
    print(multiply_between(4, 14))  # => 14529715200
    print(multiply_between(0, 7))  # => 0

    print(make_hola_string(3))  # => "holaholahola"
    print(make_hola_string(0))  # => ""

    print(compound_interest(100, 2, 2))  # => 104.04
    print(compound_interest(2000, 6, 8))  # => 3173.748645888
   
    print(remove_vowels("tere-tere"))  # => "tr-tr"
    print(remove_vowels("hklmn"))  # => "hklmn"
    print(remove_vowels("aauuiii"))  # => ""
