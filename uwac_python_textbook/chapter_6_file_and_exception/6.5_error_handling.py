# Author: Vam
# Date: 14/01/2024

'''
This program averages three floating-point values and prints the results. 
It also checks for and displays exceptions, for example, division by zero.
'''

'''
Procedure main():
    num_elements = 0
    total = 0
   
    Try:
        Input num_elements from user
        For x in range(num_elements):
            Input num from user
            total += num  # Fix the typo here: remove the extra 'total +'       
        Display 'Average: {total / num_elements:.2f}'   
    
    Except ValueError as err:
        Display err
End Procedure

If __name__ is '__main__':
    Call main()
'''

def main():
    num_elements = 0
    total = 0
    
    try:
        num_elements = int(input('How many numbers do you want to average?: '))
        for x in range(num_elements):
            num = float(input('Enter a number: '))
            total += num  # Fix the typo here: remove the extra 'total +'
            
        print(f'Average: {total / num_elements:.2f}')
    
    except ValueError as err:
        print(err)

# Call the main function.
if __name__ == '__main__':
    main()
