# Matemaatilised avaldised

Järgnevates ülesannetes tegeleme matemaatiliste avaldistega, kindlasti enne lahendamist tutvu ka vastavate materjalidega - [Matemaatilised avaldised](https://pydoc.pages.taltech.ee/introduction/math.html).

Samuti põgusalt tutvume funktsiooni kirjutamisega, aga räägime sellest rohkem juba järgmisel nädalal.
Funktsiooni kohta saad veidi lugeda siit - [Funktsiooni mõiste ja kasutamine](https://pydoc.pages.taltech.ee/function/func_overview.html).
Iga ülesande juurde on kaasa antud mall, kuidas see peaks välja nägema, sinu ülesandeks on lihtsalt ette antud kohta oma kood kirjutada,
midagi rohkemat tegema ei pea.

## 1. Sum and difference
* Loo muutuja `sum`, mille väärtus on muutujate `num_a` ja `num_b` summa.
* Loo muutuja `difference`, mille väärtus on muutujate `num_a` ja `num_b` vahe.

### Mall

def sum_and_difference(num_a: int, num_b: int) -> tuple:
    """Return the sum and difference of given variables num_a and num_b."""
    # Write your code here
    sum = num_a + num_b
    difference = num_a - num_b
    return sum, difference


## 2. Float division
* Loo muutuja `division`, mille väärtus on muutujate `num_a` ja `num_b` jagatis.
* Muutujad `num_a` ja `num_b` on täisarvud, kuid nende jagatis võib olla ujukomaarv, ümardada pole vaja.

### mall

def float_division(num_a: int, num_b: int) -> float:
    """Divide given variables num_a and num_b and return the result."""
    # Write your code here
    division = num_a / num_b
    return division


## 3. Integer division
* Loo muutuja `division`, mille väärtus on muutujate `num_a` ja `num_b` täisarvuline jagatis.
* Kui arvud ei jagu omavahel täpselt, siis peab vastus olema ümardatud alla.

### Mall

def integer_division(num_a: int, num_b: int) -> int:
    """Divide given variables num_a and num_b and return the result rounded down."""
    # Write your code here
    division = num_a // num_b
    return division


## 4. Powerful operations
* Loo muutuja `multiply_numbers`, mille väärtus on muutujate `num_a` ja `num_b` korrutis.
* Loo muutuja `power`, mille väärtus on `num_a` astmes `num_b`.
* Loo muutuja `remainder`, mille väärtus on `num_a` ja `num_b` jagamise jääk.

### Mall

def powerful_operations(num_a: int, num_b: int) -> tuple:
    """Return the product of given variables, num_a to the power of num_b and the remainder of division of variables."""
    # Write your code here
    multiply_numbers = num_a * num_b
    power = num_a ** num_b
    remainder = num_a % num_b
    return multiply_numbers, power, remainder


## 5. Find average
* Loo muutuja `average`, mille väärtus on `num_a` ja `num_b` aritmeetiline keskmine.

### Mall

def find_average(num_a: int, num_b: int) -> float:
    """Return the average of given variables."""
    # Write your code here
    average = (num_a + num_b) / 2
    return average


## 6. Area of a circle
* Arvuta ringi pindala, raadiuseks kasuta ette antud muutujat `radius`.
* Arvutamiseks kasuta konstanti [math.pi](https://pydoc.pages.taltech.ee/introduction/math.html#konstantid).
* Vastus ümarda kahe komakohani ja salvesta see muutujasse `circle_area`.

### Mall

def area_of_a_circle(radius: float) -> float:
    """Calculate and return the area of a circle."""
    # Write your code here
    circle_area = math.pi * radius ** 2
    circle_area = round(circle_area, 2)
    return circle_area



## 7. Area of an equilateral triangle* Arvuta võrdkülgse kolmnurga pindala, külje pikkuseks kasuta ette antud muutujat `side_length`.
* Vastus ümarda lähima täisarvuni ja salvesta see muutujasse `triangle_area`.

### Mall

def area_of_an_equilateral_triangle(side_length: float) -> int:
    """Calculate and return the area of an equilateral triangle."""
    # Write your code here
    p = (side_length * 3 ) / 2
    triangle_area = math.sqrt(p * (p - side_length) ** 3)
    triangle_area = round(triangle_area)
    return triangle_area


## 8. Calculate discriminant
* Loo muutuja `discriminant`, mille väärtuseks on arvutatud [diskriminant](https://et.wikipedia.org/wiki/Ruutv%C3%B5rrand#Diskriminant). 
* Diskriminanti saab leida valemiga `b² - 4ac`.
* Muutujad `a`, `b` ja `c` on parameetritena ette antud.

### Mall

def calculate_discriminant(a: int, b: int, c: int) -> int:
    """Calculate discriminant with given variables and return the result."""
    # Write your code here
    discriminant = b ** 2 - 4 * a * c
    return discriminant


## 9. Calculate hypotenuse length
* Loo muutuja `c`, mille väärtuseks on kahe kaateti pikkuste `a` ja `b` abil arvutatud hüpotenuusi pikkus.
* Hüpotenuusi pikkus võib olla ujukoma arv, kaatetite pikkused on alati positiivsed täisarvud.
* Meeldetuletus: Pythagorase teoreemist `a² + b² = c²`.

### Mall

def calculate_hypotenuse_length(a: int, b: int) -> float:
    """Return the length of hypotenuse when the lengths of the catheti are given."""
    # Write your code here
    c = math.sqrt(a ** 2 + b ** 2)
    return c


## 10. Calculate cathetus length
* Loo muutuja `b`, mille väärtuseks on hüpotenuusi pikkuse `c` ja ühe kaateti pikkuse `a` abil arvutatud teise kaateti pikkus.
* Hüpotenuusi ja ette antud kaateti pikkused on alati positiivsed täisarvud.
* Võib eeldada, et hüpotenuusi pikkus on alati suurem kui kaateti pikkus.
* Arvutatava kaateti pikkus võib olla ujukoma arv.

### Mall

def calculate_cathetus_length(a: int, c: int) -> float:
    """Return the length of cathetus when the lengths of the second cathetus and hypotenuse are given."""
    # Write your code here
    b = math.sqrt(c ** 2 - a ** 2)
    return b


## 11. Time converter
* Sekundid on antud muutujana `seconds`, arvuta sekunditest tunnid ja minutid matemaatiliste valemite järgi ning salvesta
  need vastavalt muutujatesse `hours` ja `minutes`.
* Mõistlik oleks kasutada täisarvulist jagamist (//) ja jääkfunktsiooni e. modulot (%).

### Mall

def time_converter(seconds: int) -> str:
    """Convert time in seconds to hours and minutes."""
    # Write your code here
    minutes = seconds // 60
    hours = minutes // 60
    minutes = minutes % 60
    return f"{seconds} sekundit on {hours} tund(i) ja {minutes} minut(it)."


## 12. Student helper
* Kooliõpilasel ei jää erinevate nurkade siinused ja koosinused meelde, aita tal need välja arvutada.
* Ette on antud nurga suurus kraadides muutujana `angle`, salvesta nurga siinused ja koosinused vastavalt
 muutujatesse `sine` ja `cosine` ning ümarda vastused ühe komakohani.
* Kasuta lahendamiseks juba [olemasolevaid funktsioone](https://pydoc.pages.taltech.ee/introduction/math.html#trigonomeetrilised-funktsioonid).

### Mall

def student_helper(angle: int) -> str:
    """Return the sine and cosine of the given angle in degrees."""
    # Write your code here
    sine = round(math.sin(math.radians(angle)), 1)
    cosine = math.cos(math.radians(angle))
    return f"Nurk: {angle}, siinus: {sine}, koosinus: {cosine}."


## 13. Greetings
* Mõningaid matemaatilisi operaatoreid saab ka teiste andmetüüpidega kasutada, näiteks sõnedega. Seda nüüd proovimegi.
* Loo muutuja `lots_of_heys`, mille väärtuseks on sõne, milles on `n` korda sõne "Hey".
* Näiteks kui `n` on 4, siis tuleks "HeyHeyHeyHey", aga kui `n` on 2, siis "HeyHey" jne.

### Mall

def greetings(n: int) -> str:
    """Return a string that contains "Hey" n times."""
    # Write your code here
    lots_of_heys = "Hey" * n
    return lots_of_heys


## 14. Adding numbers
* Ette on antud täisarvud `num_a` ja `num_b`.
* Loo muutuja `string_numbers`, mille väärtuseks on ühes sõnes kõrvuti `num_a` ja `num_b`.
* Näiteks kui `num_a` on 1 ja `num_b` on 2, siis `string_numbers` väärtuseks on "12". 
  Kui `num_a` on 123 ja `num_b` on 456, siis `string_numbers` on "123456" jne.

### Mall

def adding_numbers(num_a: int, num_b: int) -> str:
    """Return given numbers added together as a string."""
    # Write your code here
    string_numbers = str(num_a) + str(num_b)
    return string_numbers
