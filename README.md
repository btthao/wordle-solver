###Solving Wordle:

#2 word lists:
- acceptedWords: list of acceptable words from wordle's source code (10638 words).
- solutions: list of all solutions from wordle's source code (2309 words).

#3 approaches:
- Brute force: filtering word list based on guess results.
- Letter frequency: filtering word list based on letter frequency, scoring each word based on how common its letters are, ignoring the words that are already known to be in the solution.
- Letter frequency and position (main.py): in case two words have the same letter frequency score, score each of them based on how likely each letter is in the correct position.

#Results:
**(Win rate means finding the word in <= 6 attempts)**
Results for brute-force approach might vary due to randomization.

1. Only use solution list: 2309 games

|                       | Win rate      | Average guess |  Best  | Worst | 
|-----------------------|---------------|---------------|--------|-------|
| Brute force           | 98.12%        | 4.14          | 1      | 9     |
| Frequency             | 99.96%        | 3.74          | 1      | 7     |
| Frequency + position  | 100%          | 3.69          | 1      | 6     |



2. Combine two lists: 12947 games

|                       | Win rate      | Average guess |  Best  | Worst | 
|-----------------------|---------------|---------------|--------|-------|
| Brute force           | 83.08%        | 5.19          | 1      | 17    |
| Frequency             | 96.35%        | 4.55          | 1      | 10    |
| Frequency + position  | 98.39%        | 4.40          | 1      | 9     |
