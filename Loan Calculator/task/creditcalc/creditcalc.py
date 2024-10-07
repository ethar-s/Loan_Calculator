#import
import math
import argparse

parse = argparse.ArgumentParser()



parse.add_argument('--principal')
parse.add_argument('--periods')
parse.add_argument('--payment')
parse.add_argument('--interest')
parse.add_argument('--type')
args = parse.parse_args()




if args.principal is not None:
    principal = int(args.principal)
else:
    principal = False
if args.periods is not None:
    periods = int(args.periods)
else:
    periods = False
if args.payment is not None:
    payment = float(args.payment)
else:
    payment = False
if args.interest != None:
    interest = float(args.interest)
    i = interest / 12 / 100
else:
    interest = False
if principal > 0 and periods > 0 and interest > 0 and args.type == 'annuity' and not payment:
    payment = principal * ((i * ((1 + i) ** periods)) / (((1 + i) ** periods) - 1))
    overpayment = (math.ceil(payment) * periods) - principal
    print('Your annuity payment = {payment}!'.format(payment=math.ceil(payment)))
    if overpayment > 0:
        print('Overpayment = {overpayment}!'.format(overpayment=math.ceil(overpayment)))
elif principal > 0 and periods > 0 and interest > 0 and args.type == 'diff' and not payment:
    f = periods
    f_sum = 0
    while f > 0:
        d = math.ceil((principal / periods) + (i * (principal-((principal * ((periods - (f - 1)) - 1)) / periods))))
        print('Month {number}: payment is {d}'.format(number = periods - (f - 1),d=d))
        f_sum += d
        if f == 1:
            f_sum = principal - f_sum
            print()
            print('Overpayment = {f_sum}'.format(f_sum=f_sum))
        f -= 1
elif principal > 0 and payment > 0 and interest > 0 and not periods:
    periods = math.ceil((math.log(payment / (payment - (i * principal)), 1 + i)))
    overpayment = (math.ceil(payment) * periods) - principal
    years_check = periods // 12
    rest_of_periods_check = periods % 12
    if years_check == 0 and periods > 1:
        print('It will take {months} months to repay this loan!'.format(months=int(periods)))
        print('Overpayment = {overpayment}!'.format(overpayment=math.ceil(overpayment)))
    elif years_check == 0 and periods == 1:
        print('It will take {month} month to repay this loan!'.format(month=periods))
        print('Overpayment = {overpayment}!'.format(overpayment=math.ceil(overpayment)))
    elif years_check > 0 and rest_of_periods_check == 0:
        if years_check == 1:
            print('It will take {year} year to repay this loan!'.format(year=years_check))
            print('Overpayment = {overpayment}!'.format(overpayment=math.ceil(overpayment)))
        elif years_check > 1:
            print('It will take {years} years to repay this loan!'.format(years=years_check))
            print('Overpayment = {overpayment}!'.format(overpayment=math.ceil(overpayment)))
    elif years_check > 0 and rest_of_periods_check > 1:
        if years_check == 1 and rest_of_periods_check == 1:
            print('It will take {year} year and {month} month to repay this loan!'.format(year=years_check,
                                                                                          month=rest_of_periods_check))
    elif years_check == 1 and rest_of_periods_check > 1:
        print('It will take {year} year and {months} month to repay this loan!'.format(year=years_check,
                                                                                       months=rest_of_periods_check))
    elif years_check > 1 and rest_of_periods_check == 1:
        print('It will take {years} years and {month} month to repay this loan!'.format(years=years_check,
                                                                                        month=rest_of_periods_check))
    elif years_check > 1 and rest_of_periods_check > 1:
        print('It will take {years} years and {months} month to repay this loan!'.format(years=years_check,
                                                                                             months=rest_of_periods_check))
elif periods and payment and interest and not principal:
    principal = payment / ((i * ((1 + i) ** periods)) / (((1 + i) ** periods) - 1))
    print('Your loan principal = {principal}!'.format(principal=principal))
else:
    print('Incorrect parameters')



