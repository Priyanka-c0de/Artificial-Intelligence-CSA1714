import itertools

def solve_cryptarithmetic():
    # Puzzle words
    words = ["SEND", "MORE"]
    result = "MONEY"
    
    # Get all unique letters
    unique_letters = set("".join(words) + result)
    
    if len(unique_letters) > 10:
        print("Invalid puzzle: More than 10 unique letters.")
        return False
        
    letters = list(unique_letters)
    leading_letters = set(w[0] for w in words + [result])
    
    # Try all permutations of digits 0-9 matching the length of unique letters
    for perm in itertools.permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        
        # Rule check: No leading zero
        if any(mapping[letter] == 0 for letter in leading_letters):
            continue
            
        # Convert words to numbers
        def word_to_val(word):
            return int("".join(str(mapping[char]) for char in word))
            
        val1 = word_to_val(words[0])
        val2 = word_to_val(words[1])
        res_val = word_to_val(result)
        
        # Check if addition holds true
        if val1 + val2 == res_val:
            print("Solution Found:")
            for char, digit in sorted(mapping.items()):
                print(f"{char} -> {digit}")
            print(f"\nEquation: {val1} + {val2} = {res_val}")
            return True
            
    print("No solution found.")
    return False

solve_cryptarithmetic()