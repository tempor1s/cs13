class Solver(object):
    def __init__(self):
        self.dict = self.build_dict()

    def build_dict(self):
        """Build a dictonary with keys of sorted letters and a value that is a list of words that are that sorted word."""
        # empty dictonary that we will put a mapping of the real dictonary in
        dictonary = {}
        # open the dictonary that comes on unix machines
        with open("/usr/share/dict/words", "r") as f:
            # loop through every word
            for word in f:
                # clean the word
                word = word.strip().lower()
                # create a sorted version of the word
                sorted_word = ''.join(sorted(word))
                # either create a entry with the sorted word and new dict as value, or append the word to the entry that already exists
                dictonary.setdefault(sorted_word, []).append(word)
        # return the created dictonary
        return dictonary

    def solve_word(self, word):
        # sort the inputed word so that we can look it up 
        sorted_input = ''.join(sorted(word)) 

        if sorted_input in self.dict:
            return self.dict[sorted_input] 
        else:
            return None

    def solve_words(self, words):
        # List to add solved words to
        output = []
        # loop through the given words
        for word in words:
            # solve the single word
            solved_words = self.solve_word(word)
            # check to make sure there are words
            if solved_words is not None:
                # if there is only one option for the given word
                if len(solved_words) == 1:
                    # add the single word to our output array
                    output.extend(solved_words)
                else:
                    # add the full array of solved word options
                    output.append(solved_words)
        # return the final word list
        return output

if __name__ == "__main__":
    solver = Solver()
    words = ['shast', 'doore', 'ditnic', 'catili'] 
    solved_words = solver.solve_words(words)
    print(solved_words)
