def calculator():
    total = 0
    count = 0
    while True:
        num = raw_input("Enter a number: ")
        if num == 'done':
            print total, count, (total / count)
            break
        else:
            try:
                total += float(num)
            except:
                print "Invalid input"
                continue
        count += 1
        
calculator()

