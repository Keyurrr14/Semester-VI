import os
from collections import defaultdict

def create_sample_files():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sample_content = {
        'dummy1.txt': 'The quick brown fox jumps over the lazy dog.',
        'dummy2.txt': 'A quick brown dog runs in the park.',
        'dummy3.txt': 'The lazy fox sleeps under the tree.',
        'dummy4.txt': 'A dog and a fox play in the park.'
    }
    
    for filename, content in sample_content.items():
        with open(os.path.join(current_dir, filename), 'w') as f:
            f.write(content)

try:
    create_sample_files()
except IOError as e:
    print(f"Error creating sample files: {e}")
    exit(1)

current_dir = os.path.dirname(os.path.abspath(__file__))
files = ['dummy1.txt', 'dummy2.txt', 'dummy3.txt', 'dummy4.txt']
inverted_index = defaultdict(list)

for file in files:
    try:
        with open(os.path.join(current_dir, file), 'r') as f:
            words = f.read().lower().split()
            for word in words:
                word = word.strip('.,!?()[]{}":;')
                if file not in inverted_index[word]:
                    inverted_index[word].append(file)
    except FileNotFoundError:
        print(f"File {file} not found")

print("\nInverted Index:")
for word, docs in inverted_index.items():
    print(word, "->", docs)

def search_term(term):
    term = term.lower()
    if term in inverted_index:
        return inverted_index[term]
    return []

print("\nExample Searches:")
search_terms = ['quick', 'fox', 'Keyur']
for term in search_terms:
    result = search_term(term)
    if result:
        print(f"Documents containing '{term}': {result}")
    else:
        print(f"Term '{term}' not found in any document")



