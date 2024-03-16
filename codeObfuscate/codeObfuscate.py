def main():
    #Two sample strings
    string1 = "This is an example string, "
    string2 = "This is some more text "
    
    #Concatenate strings together
    concatenated_string = string1 + string2
    print("Concatenated: ", concatenated_string)
    
    #Length
    print("String length: ", len(concatenated_string))
    
    #Accessing characters
    print("First character: ", concatenated_string[0])
    print("Last character: ", concatenated_string[-1])
    
    #Slicing
    print("Substring from index 7 to end:", concatenated_string[7:])
    print("Substring from index 0 to 5:", concatenated_string[:5])
    print("Substring from index 7 to 12:", concatenated_string[7:12])
    
    #String repetition
    repeated_string = string1 * 3
    print("Repeated: ", repeated_string)
    
    #Formatting
    name = "User"
    age = 21
    formatted_string = f"My name is {name} and I am {age} years old."
    print("Formatted string:", formatted_string)
    
    #String methods
    lowercase_string = concatenated_string.lower()
    print("Lowercase: ", lowercase_string)
    
    uppercase_string = concatenated_string.upper()
    print("Uppercase: ", uppercase_string)
    
    #Check if starts or ends with a specific substring
    print("Does the concatenated string start with 'This'? ", concatenated_string.startswith("This"))
    print("Does the concatenated string end with 'some!'? ", concatenated_string.endswith("some"))
    
    #Count occurrences 
    substring_count = concatenated_string.count("o")
    print("Number of occurrences of 'o' in concatenated string:", substring_count)
    
    #Find index
    substring_index = concatenated_string.find("text")
    print("Index of 'text' in concatenated string:", substring_index)
    
    reversed_string = concatenated_string[::-1]
    print("Reversed: ", reversed_string)

if __name__ == "__main__":
    main()