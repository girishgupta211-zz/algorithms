# initializing list of foods temperatures 
batch = [15, 40, 26, 39, 30, 25, 21]

# initializing cut temperature 
cut = 26

# using assert to check for temperature greater than cut 
for i in batch:
    assert i >= 26, "Batch is Rejected"
    print(str(i) + " is O.K")
