import random

movies = ['classmate', 'kgff', 'homme', 'fallimy']
movie = random.choice(movies)
display = ['_' for _ in movie]
print(' '.join(display))

for _ in range(10):
    guess = input("Enter a letter: ")

    
    for i in range(len(movie)):
        if movie[i] == guess:
            display[i] = guess
       
    print(' '.join(display))

    if '_' not in display:
        print("Y es The movie is:", movie)
        break
else:
    print("chance over the movie was:", movie)
