def fibonacci(iterations, offSpring, currentVal, previousVal = 0):
    print(currentVal)
    if iterations == 1:
        return currentVal + previousVal
    else:
        iterations -= 1
        tmpVal = currentVal
        currentVal = currentVal + (previousVal * offSpring)
        previousVal = tmpVal
        # return fibonacci(iterations, currentVal, (currentVal + previousVal))
        return fibonacci(iterations, offSpring, currentVal, previousVal)


print(f"final total : {fibonacci(32, 3, 1)}")