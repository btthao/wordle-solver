import copy
import random
from words.acceptedWords import acceptedList
from words.solutions import solutionList

class Wordle:
    def __init__(self, solution, wordList):
        self.allWords = wordList
        self.filteredWords = wordList
        self.solution = solution
        self.solution_char_pos = self.get_char_pos(solution)
        self.guesses = 0
        
    def make_guess(self):
        self.guesses += 1

        # choose random word from filtered list
        return random.choice(self.filteredWords)
    
    def filter_list(self, guess, guessResult):
        self.filteredWords = [word for word in self.filteredWords if self.is_possible_solution(word, guess, guessResult)]
        
    def is_possible_solution(self, word, guess, guessResult):
        # c - correct; p - present; a - absent
        for i in range(len(guessResult)):
            if guessResult[i] == 'c' and word[i] != guess[i]:
                return False
            elif guessResult[i] == 'p':
                if guess[i] == word[i]:
                    return False
                elif guess[i] not in word:
                    return False
            elif guessResult[i] == 'a':
                absent = True
                for k in range(len(guess)):
                    if guess[k] == guess[i] and k != i and guessResult[k] != 'a':
                        absent = False
                        break
            
                if absent and guess[i] in word:
                    return False
                elif not absent and guess[i] == word[i]:
                    return False

        return True
    
    def gen_guess_result(self, guess):
        # c - correct; p - present; a - absent
        output = []
        solutionChars = copy.deepcopy(self.solution_char_pos)
    
        for i in range(len(guess)):
            char = guess[i]

            if char in solutionChars:
                charPosSolution = solutionChars[char]

                if i in charPosSolution:
                    output.append('c')
                    solutionChars[char] = [x for x in charPosSolution if x != i]
                else:
                    output.append('p')
                
            else:
                output.append('a')

        for k in range(len(output)):
            char = guess[k]
            if output[k] == 'p':
                charPosSolution = solutionChars[char]
                if len(charPosSolution) == 0:
                    output[k] = 'a'
                else:
                    solutionChars[char].pop()
        
        return ''.join(output)
    
    def get_char_pos(self, word):
        pos = {}
        
        for i in range(len(word)):
            char = word[i]
            if char in pos:
                pos[char].append(i)
            else:
                pos[char] = [i]
        
        return pos


wordList = solutionList


def play(solution, automate):
    
    game = Wordle(solution, wordList)
    guessResult = ''

    while len(game.filteredWords) > 0 and guessResult != 'ccccc':
        guess = game.make_guess()
        guessResult = game.gen_guess_result(guess)
        
        if automate == False:
            print(len(game.filteredWords), ' words left in filtered list')
            print ('current guess: ', guess)
            print('guess result: ', guessResult)
        
        game.filter_list(guess, guessResult)

    if guessResult == 'ccccc':
        print(solution, game.guesses, ' guesses')
        return game.guesses
    else:
        print('fail to find solution')
        return 'fail'

def automate():
    totalGames = 0
    totalGuesses = 0
    totalFails = 0
    totalCantSolve = 0
    worstGuess = 0
    bestGuess = 0

    for word in wordList:
        guessCount = play(word, automate=True)
        totalGames += 1
        if guessCount == 'fail':
            totalFails += 1
            totalCantSolve += 1
        else:
            if guessCount > 6:
                totalFails += 1
                
            totalGuesses += guessCount
                
            if guessCount < bestGuess or bestGuess == 0:
                bestGuess = guessCount
                    
            if guessCount > worstGuess:
                worstGuess = guessCount
        
    print('success rate: ', (totalGames - totalFails)*100/totalGames, '%')
    print('fail rate: ',  totalFails*100/totalGames, '%')
    print('avg guesses: ', totalGuesses/totalGames)
    print('best guess: ', bestGuess)
    print('worst guess: ', worstGuess)
    print('total cant solve: ', totalCantSolve)
       
# play 1 game:
# print(play('hover', automate=False))

# play multiple games:
automate()



