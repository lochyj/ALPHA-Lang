types = [
    "int",
    "null",
    "string",
    "char"
]

def parse_line(line: str):
    
    string = False;
    definition = False;
    
    for char in line:
        if char == '"':
            string = not string;
        elif char == '{':
            definition = True;
        elif string == '}':
            definition = False;
    
    
    words = line.split(' ');
    word_count = 0;
    for word in words:
        if word == '' or word == ' ':
            word_count += 1;
            continue;
        
        if word in types:
            if words < word_count:
                if words[word_count + 1].endswith(')'):
                    print(function)
            
            print(f"Type: {word}");
        else:
            print("Not a type :(");
        
        word_count += 1;