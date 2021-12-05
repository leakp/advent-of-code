import numpy as np

def read_test_data():
    with open("test_input3.txt", "r") as tf:
        test_data = tf.read().split('\n')
    return test_data

def read_puzzle_data():
    with open("input3.txt", "r") as tf:
        data = tf.read().split('\n')  
    return data

def get_power_consumption(data):
    gamma_list = []
    epsilon_list = []
    for a in range(len(data[0])):
        val = [int(l[a]) for l in data]
        counts = np.bincount(val)
        gamma_list.append(np.argmax(counts))
        epsilon_list.append( np.argmin(counts))
    gamma_int = int('0b'+''.join([str(i) for i in gamma_list]),2)
    epsilon_int = int('0b'+''.join([str(i) for i in epsilon_list]),2)
    power = gamma_int * epsilon_int
    return power, gamma_int, epsilon_int

def get_oxygen_rating(data, digit = 0, verbose = False):
    if len(data) == 1: #base case
        out_int = int('0b'+ data[0],2)
        return out_int
    else: # recursive case
        val = [int(l[digit]) for l in data]
        counts = np.bincount(val)
        #check if frequencies are the same, if so, put 1
        max_count = 1 if np.count_nonzero(counts == counts[0]) == len(counts) else np.argmax(counts) 
        new_data  = [l for l in data if l[digit] == str(max_count)]
        digit +=1 
        return get_oxygen_rating(new_data,digit)
    
def get_CO2_rating(data, digit = 0):
    if len(data) == 1: #base case
        out_int = int('0b'+ data[0],2)
        return out_int
    else: # recursive case
        val = [int(l[digit]) for l in data] # collect digit X from all elements
        counts = np.bincount(val)           # get frequencies
        #check if frequencies are the same, if so, put 1
        min_count = 0 if np.count_nonzero(counts == counts[0]) == len(counts) else np.argmin(counts) 
        new_data  = [l for l in data if l[digit] == str(min_count)] # only keeps the codes that have min at wanted index
        digit +=1 
        return get_CO2_rating(new_data,digit)

def get_life_support_rating(data):
    life_support = get_oxygen_rating(data) * get_CO2_rating(data)
    return life_support
    
def well_done(): #https://codegolf.stackexchange.com/questions/19123/draw-the-heart-shape
    x = "yeah"
    print(f"\t  {x}\t      {x}")
    print("\t"+str(x*2)+"    "+str(x*2))
    print("      "+str(x*6))
    print(str(" "*5)+str(x*6)+x[:2])
    print(str(" "*5)+str(x*6)+x[:2])
    print("      "+str(x*6))
    print("\t"+str(x*5))
    print("\t"+str(" "*2)+str(x*4)+x[0])
    print("\t"+str(" "*4)+str(x*3)+x[0])
    print("\t"+str(" "*7)+str(x*2))
    print("\t"+str(" "*10)+"v")
    
if __name__ == "__main__":
    test_data = read_test_data()
    data      = read_puzzle_data()
    
    # Part 1
    power, gamma, eps = get_power_consumption(test_data)
    print("\nPART 1")
    print("*"*3,"Example Data","*"*3)
    print("Gamma rate: ",gamma)
    print("Epsilon rate: ",eps)
    print("Power consumption: ", power)
    print(f"AOC says this should be 198. So our result is {power==198}!")
    print("-"*70)
    # puzzle data
    power, gamma, eps = get_power_consumption(data)
    print("*"*3,"Puzzle Data","*"*3)
    print("Power consumption: ", power)
    print("-"*70)
    
    # Part 2
    print("\nPART 2")
    print("*"*3,"Example Data","*"*3)
    oxy_test          = get_oxygen_rating(test_data)
    CO2_test          = get_CO2_rating(test_data)
    life_support_test = get_life_support_rating(test_data)
    print("Your oxygen generator rating is: ", oxy_test)
    print("Your CO2 scrubber rating is: ", CO2_test)
    print("Life support rating is:", life_support_test)
    print(f"AOC says this should be 230. So our result is {life_support_test==230}!")
    print("-"*70)
    # puzzle data
    life_support = get_life_support_rating(data)
    print("*"*3,"Puzzle Data","*"*3)
    print("Life support rating is:", life_support)
    print("-"*70)
    well_done()
    print("\n\nTschüssle, gell!\n\n")