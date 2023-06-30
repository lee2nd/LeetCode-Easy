# https://stackoverflow.com/questions/189645/how-can-i-break-out-of-multiple-loops?page=1&tab=scoredesc#tab-top

for a in range(10):
    for b in range(20):
        if something(a, b):
            # Break the inner loop...
            break
    else:
        # Continue if the inner loop wasn't broken.
        continue
    # Inner loop was broken, break the outer.
    break
