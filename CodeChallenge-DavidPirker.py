# Application - David Pirker

# Create a function to convert a number into words
    
    # Setup of the code:
    #
    # Function:
    # 1. Definition of unique numbers using a dictionary
    # 2. Creation of two-step processes (using if clauses), where:
    #   Step 1: Identify range of number
    #   Step 2: Define output based on number
    #
    # Execution of Example txt file

#%% Create function to convert integers to words
def num_to_word(num):
       
    # Step 1
    # create dict to specify unique words for numbers
    dict_num_to_word = { 0 : 'zero',
          # num > 0
          1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          # num > 10
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',
          # num > 20
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }
    
    
    # Step 2: Identify number and select case from dictionary     
    
    # error if number is negative  
    if (num < 0):
        return 'number is negative'   
    
    
    # if number is smaller than 20, select unique word                        
    if (num < 20):
        return dict_num_to_word[num]
    

    # if number is smaller than 100, select either unique number or combination of tens
    if (num < 100):
        if num % 10 == 0: return dict_num_to_word[num]
        else: return dict_num_to_word[num // 10 * 10] + '-' + dict_num_to_word[num % 10]
        
    
    # if number is smaller than 1000, select either 100s or a combination 
    if (num < 1000):
        if num % 100 == 0: return dict_num_to_word[num // 100] + ' hundred'
        else: return dict_num_to_word[num // 100] + ' hundred and ' + num_to_word(num % 100)
        
    
    # if number is smaller than 1mn, select either 1000s or a combination 
    if (num < 1000000):
        if num % 1000 == 0: return num_to_word(num // 1000) + ' thousand'
        else: return num_to_word(num // 1000) + ' thousand and ' + num_to_word(num % 1000)
        

    # if number is smaller than 1bn, select either mn(s) or a combination
    if (num < 1000000000):
        if (num % 1000000) == 0: return num_to_word(num // 1000000) + ' million'
        else: return num_to_word(num // 1000000) + ' million, ' + num_to_word(num % 1000000)
        

    # if number is smaller than 1tr, select either bn(s) or a combination
    if (num < 1000000000000):
        if (num % 1000000000) == 0: return num_to_word(num // 1000000000) + ' billion'
        else: return num_to_word(num // 1000000000) + ' billion, ' + num_to_word(num % 1000000000)
        
    
    # if number = trn
    if (num % 1000000000000 == 0): return num_to_word(num // 1000000000000) + ' trillion'
    else: return num_to_word(num // 1000000000000) + ' trillion, ' + num_to_word(num % 1000000000000)
    
    # the cases could be continued to account for quadtrillion, quintillion, etc.
    # but considering this is for a purpose used in finance I stopped at trillion.


#%% execute example

# Open txt file
text = open(r'D:\Bewerbungs Ordner\__2020\NinetyOne\TestInput.txt', 'r').read()

# Create list of digits by running through text strings
lst_num = [int(s) for s in text.split() if s.isdigit()]

# Run through list of numbers
for num in lst_num:
    print(num_to_word(num))

