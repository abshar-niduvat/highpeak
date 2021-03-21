#Delcaration before file opening
goodies = {}
numberOfEmployee=0

#input file open
with open("input.txt") as f:
    content = f.read()
    content_list = content.splitlines()
    for ij in range(len(content_list)):
        #extracting number of employees
        if ij==0:
            (key, val) = content_list[ij].split(':')
            numberOfEmployee=int(val)
        elif ij>3:
            # extracting goodies item and price
            (key, val) = content_list[ij].split(":")
            goodies[key] = int(val)

#List of goodies prices
prices=list(goodies.values())

#Function for sorting list
def sort_val(arr):
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            # Select the smallest value
            if arr[j] < arr[minimum]:
                minimum = j
        arr[minimum], arr[i] = arr[i], arr[minimum]
    return arr

#Call for sorting list
prices=sort_val(prices)

#Core program, Finding minimum difference
min_value=prices[0]
max_value=prices[numberOfEmployee-1]
difference=max_value-min_value
for i in range(numberOfEmployee-1,(len(prices))):
    new_diff=int(prices[i])-int(prices[(i-(numberOfEmployee-1))])
    if (new_diff<difference):
        difference=new_diff
        min_value=prices[i-(numberOfEmployee-1)]
        max_value=prices[i]

#For writing to ouput file
file = open("output.txt", "w")
file.write("The goodies selected for distribution are:\n\n")
for ik in range(prices.index(min_value),prices.index(max_value)+1):
    for goody, price in goodies.items():
        if price == prices[ik]:
            file.write(str(goody)+':'+str(prices[ik])+'\n')
file.write("\nAnd the difference between the chosen goodie with highest price and the lowest price is "+str(difference))
file.close()