# Function to convert the date format
def convert24(hour,min,denotion):
      
    # Checking if last two elements of time
    # is AM and first two elements are 12
    if denotion == "AM" and hour == "12":
        return ('00:'+min)
          
    # remove the AM    
    elif denotion == "AM":
        return (hour+':'+min)
      
    # Checking if last two elements of time
    # is PM and first two elements are 12   
    elif denotion == "PM" and hour == "12":
        return (hour+':'+min)
          
    else:
          
        # add 12 to hours and remove PM
        military = str(int(hour) + 12)
        return (military+':'+min)
  
# Driver Code

print (convert24('12','30','AM'))
