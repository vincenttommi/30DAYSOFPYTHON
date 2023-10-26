"""


Searching algorithms in python - very basic neccessity when  storing
data structures



"""
#linear search  - a sequential search is made over all items one by one

def linear_search(values,search_for):
    #declaring a variable and initialising 0
    search_at = 0
    search_res = False
    
    #Matching the value with each data element
    while search_at < len(values) and search_res is False:
        if values[search_at]  == search_for:
            search_res = True
        else:
            search_at  = search_at + 1
    return search_res

#declaring values to which data is searched from
l  = [64,34,25,12, 22,11,90]

print(linear_search(l,4))
print(linear_search(l,11))
            