def max_value(s):

    filtered_chars = [char for char in s if char.isalpha()]
    
    return max(filtered_chars) if filtered_chars else None

result = max_value("Hello World")
print(result)
