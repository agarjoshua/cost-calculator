def func():
    x = 70000
    # x *= 100
    commission = 0.02 * x
    paypal_to_offshore = 0.03 * x
    offshore_to_local = paypal_to_offshore * 0.15
    Local_to_mpesa = 62 #This is in kenyan shillings

    formula = x + commission + paypal_to_offshore + offshore_to_local + Local_to_mpesa

    print(commission)
    print(paypal_to_offshore)
    print(offshore_to_local)
    print(formula)

func()