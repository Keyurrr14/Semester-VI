import nltk
import os
from nltk.corpus import stopwords

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'dummy.txt')

with open(file_path, 'w') as file:
    file.write("The quick brown fox danced gracefully under the soft glow of the evening sky. With every leap and bound, it seemed to defy the laws of gravity, moving as if guided by an unseen melody. Nearby, a curious rabbit watched from behind a cluster of wildflowers, its ears twitching with each subtle rustle of leaves. The distant hum of a flowing stream added a gentle rhythm to the scene, blending natures sounds into a soothing symphony. Time felt slower here, as if the world beyond the forest's edge had momentarily ceased to exist.")

with open(file_path, 'r') as file:
    Stopwords = stopwords.words('english')
    wordsInFile = file.read()
    data = wordsInFile.split()

    print("Words in Stopwords: ", Stopwords, "\n")
    print("Words in File: ", data, "\n")

    data = [word for word in data if word.lower() not in Stopwords]

    print("Words in File after removing Stopwords: ", data, "\n") 