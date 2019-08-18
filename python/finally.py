try: 
    k = 5//0 # exception raised 
    print(k) 
      
finally: 
    # this block is always executed  
    # regardless of exception generation. 
    print('This is always executed') 
