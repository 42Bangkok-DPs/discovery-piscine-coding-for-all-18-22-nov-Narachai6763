
import math

def main():
 
    user_input = input("Give me a number: ")
    
    try:
       
        number = float(user_input)
        
      
        rounded_up = math.ceil(number)
        
      
        print(rounded_up)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
