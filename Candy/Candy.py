# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 19:25:21 2023

@author: ASUS
"""

def test(func, test_suite):
    '''
    
    Parameters
    ----------
    func : function
        A function to be tested
    
    test_suite : list
        A list of tuples containing an input value and the correct output
        
    Returns
    -------
    Correct if your output matches functions output, Error otherwise

    '''
    # apply the given function to each value given in test suite and compare the outputs
    
    from colorama import Back, init
    init(autoreset=True)

    for value, output in test_suite:
       
        if func(value) != output :
            print(Back.RED + "\nError")
            print(f"\nInput : {value}")
            print(f"Your output : {func(value)}  \nCorrect output : {output}")
            
        else:
            print(Back.GREEN + "\nCorrect")
            print(f"\nInput : {value}")
            print(f"Your output : {func(value)}  \nCorrect output : {output}")


            
         
def candy(ratings):
    """
    :type ratings: List[int]
    :rtype: int
    """

    # total number of candies
    candies = 1

    # number of candies for each child
    v = 1 

    # stores the first value after the ratings started decreasing
    dec = None

    # stores last operation performed
    ops = None

    # Since candies = 1, we start with second child

    for idx, rate in enumerate(ratings[1:]) :   

        # Since enumeration starts from 2nd index, ratings[idx] gives the value before rate

        # if current rating is greater than previous rating
        if ratings[idx] < rate : 
            
            # if index if not first and previous operation is >
            if idx != 0 and ops == '>' : 
                
                # update ops to latest operator, candies assigned to 2, add it to total candies 
                # and update start decreasing value to None
                ops = '<'
                v = 2
                candies += v 
                dec = None
            
            # if index is first or previous operation is <
            else :
                
                # increment candies assigned by 1 and add to total candies
                ops = '<'
                v += 1
                candies += v
        
        # if current rating is smaller than previous rating
        elif ratings[idx] > rate :

            # if index is not first and previous operation is <
            if idx != 0 and ops == '<' : 
                
                # update ops to latest operator, candies assigned to , add it to total candies 
                # and update start decreasing value to v
                ops = '>'
                dec = v
                v = 1
                candies += v 

            # if index is first or previous operation is >
            else :

                # if while decreasing, the current assigned candies is one less than the  
                # start decreasing value, then increment assigned candies by 2
                if v + 1 == dec :
                    v += 2
  
                # else increment assigned candies by 1
                else :
                    v += 1

                # update total candies
                ops = '>'
                candies += v
        
        # if current rating is equal to previous rating, then update start decreasing value to None,
        # ops to =, v to 1 and add to total candies
        else :
            
            dec = None
            ops = '='
            v = 1
            candies += v

    # return sum of assigned candies to each child
    return candies




d

l1 = [1,2,5,5,4,3,2,1]
l2 = [1,2,5,5,6,7,8,9]

l3 = [0,1,2,3,4,5]
l4 = [5,4,3,2,1,0]

l5 = [1,0,2]
l6 = [1,3,2]

l7 = [1,0,1,0,1,0]
l8 = [0,1,0,1,0,1]

l9 = [1,6,10,8,7,6,5]
l10 = [1,2,3,5,4,3,2,1]

l11 = [1,3,2,2,1]

l12 = [1,2,3,5,4,3,2,1,4,3,2,1]

l13 = [3,2,1,2,3]

# print(candy(l11))

test_suite = [(l1, 21), (l2, 21), (l3, 21), (l4, 21), (l5, 5), (l6, 4), (l7, 9), 
              (l8, 9), (l9, 18), (l10, 21), (l11, 7), (l12, 31)]

print(test(candy, test_suite))


