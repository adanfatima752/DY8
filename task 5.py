def greet(language_code):
    if language_code == 'en':
        print("Hello")
    elif language_code == 'es':
        print("Hola")
    elif language_code == 'fr':
        print("Bonjour")
    else:
        print("Unknown language code")

# Test the function with each language code
greet('en')  # Output: Hello
greet('es')  # Output: Hola
greet('fr')  # Output: Bonjour
