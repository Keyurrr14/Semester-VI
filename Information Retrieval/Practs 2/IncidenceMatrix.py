import numpy as np
from collections import defaultdict
import os

def create_sample_files():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sample_content = {
        'dummy1.txt': 'The quick brown fox jumps over the lazy dog.',
        'dummy2.txt': 'A quick brown dog runs in the park.',
        'dummy3.txt': 'The lazy fox sleeps under the tree.',
        'dummy4.txt': 'A dog and a fox play in the park.'
    }
    
    for filename in sample_content:
        with open(os.path.join(current_dir, filename), 'w') as f:
            f.write(sample_content[filename])

try:
    create_sample_files()
except IOError as e:
    print(f"Error creating sample files: {e}")
    exit(1)

current_dir = os.path.dirname(os.path.abspath(__file__))
files = ['dummy1.txt', 'dummy2.txt', 'dummy3.txt', 'dummy4.txt']

terms = set()
documents = {}
 
for file in files:
    try:
        file_path = os.path.join(current_dir, file)
        with open(file_path, 'r') as f:
            content = f.read().lower()
            words = [word.strip('.,!?()[]{}":;') for word in content.split()]
            documents[file] = words
            terms.update(words)
    except FileNotFoundError:
        print(f"Warning: File {file} not found. Skipping...")
        documents[file] = [] 

terms_list = sorted(terms)
incidence_matrix = [[0 for _ in range(len(files))] for _ in range(len(terms_list))]
for i in range(len(terms_list)):
    for j in range(len(files)):
        incidence_matrix[i][j] = 1 if terms_list[i] in documents[files[j]] else 0

matrix_size = f"{len(terms_list)} x {len(files)}"

print("\nIncidence Matrix:")
print("\nTerms:", terms_list)
print("\nDocuments:", files)
print("\nMatrix:")
for term_index in range(len(terms_list)):
    print(terms_list[term_index], incidence_matrix[term_index])
 