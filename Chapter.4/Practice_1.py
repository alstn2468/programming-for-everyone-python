def computepay(hours, rate) :
    if hours > 40 :
        extra = hours - 40
        pay = (40 * rate) + (extra * rate * 1.5)

    else :
        pay = hours * rate

    return pay

hours = int(input("Enter Hours: "))
rate = int(input("Enter Rate: "))

pay = computepay(hours, rate)

print("Pay: ", pay)
