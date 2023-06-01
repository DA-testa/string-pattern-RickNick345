# python3
def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    key = input()
    if key[0] == "F":
        #fileName = input()
        fileName = "tests/06" 
        f = open(fileName, "r")
        pattern= f.readline()
        data = f.readline()
    
    elif key[0] == "I":
        pattern = input()
        data = input()
    else:
        print("error")
        return
    
    return (pattern.rstrip(), data.rstrip())

def get_occurrences(pattern, data):
    output = []
    Alphabet = 256 # alphabet covers whole ASCII set
    PrimeNum = 89 # minimizes hash collisions (Skaitlis ar kuru dala hash rezultātu)
    PatternHash = 0
    DataHash = 0
     # Calculating the hash value of the pattern and the sliding window of the data
    for i in range(len(pattern)):
        PatternHash = (Alphabet * PatternHash + ord(pattern[i])) % PrimeNum
        DataHash = (Alphabet * DataHash + ord(data[i])) % PrimeNum
    for i in range(len(data) - len(pattern) + 1): # going through data using sliding window
        if PatternHash == DataHash:
            match = True
            for j in range(len(pattern)):
                if data[i + j] != pattern[j]:
                    match = False
                    break
            if match:        
                output.append(i)

        if i < len(data) - len(pattern): # Calculating hash value for next window of data
            DataHash = (Alphabet * (DataHash - ord(data[i]) * 
            (Alphabet ** (len(pattern )-1))) + # == alphabet^len(pattern)-1
            ord(data[i + len(pattern)])) % PrimeNum # ** means exponentiation
            
            if DataHash < 0:
                DataHash += PrimeNum

    if len(output) == 0:
        return -1                       
    return output

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

