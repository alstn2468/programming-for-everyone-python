try :
    hours = int(input('Enter Hours : '))
    Rate = int(input('Enter Rate : '))

except :
    print('Error, please  enter numeric input')
    quit()

if hours > 40 :
    extra = hours - 40
    pay = (40 * Rate) + (extra * Rate * 1.5)

else :
    pay = hours * Rate

print('Pay : ', pay)
