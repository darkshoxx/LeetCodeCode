# Approach 1

from typing import List

# Approach 1 Top-Down Dynamic Programming

class Solution1:
    def numWays(self, words: List[str], target: str) -> int:
        dp =  [[-1] * len(target) for _ in range(len(words[0]))]
        char_frequency = [[0] * 26 for _ in range(len(words[0]))]
        for word in words:
            for index in range(len(word)):
                character = ord(word[index]) - 97
                char_frequency[index][character] +=1
        return self.get_words(words, target, 0, 0, dp, char_frequency)
    
    def get_words(self, words, target, words_index, target_index, dp, char_frequency ):
        if target_index == len(target):
            return 1
        if words_index == len(words[0]) or (len(words[0]) - words_index < len(target) - target_index):
            return 0
        if dp[words_index][target_index]!= -1:
            return dp[words_index][target_index]
        else:
            count_ways = 0
            curr_pos = ord(target[target_index]) - 97
            count_ways += self.get_words(words, target, words_index+1, target_index, dp, char_frequency)
            count_ways += char_frequency[words_index][curr_pos] * self.get_words(words, target, words_index+1, target_index +1, dp, char_frequency)
            dp[words_index][target_index] = count_ways % (10**9 + 7)
            return dp[words_index][target_index]

# Approach 2: Bottom-Up Dynamic Programming

class Solution2:
    def numWays(self, words: List[str], target: str) -> int:
        word_length = len(words[0])
        target_length = len(target)
        dp =  [[0] * (target_length+1) for _ in range(word_length+1)]
        char_frequency = [[0] * 26 for _ in range(word_length)]
        mod = 10**9+7
        for word in words:
            for index in range(len(word)):
                character = ord(word[index]) - 97
                char_frequency[index][character] +=1
        for curr_word in range(word_length+1):
            dp[curr_word][0] = 1
        for curr_word in range(1, word_length+1):
            for curr_target in range(1, target_length+1):
                dp[curr_word][curr_target] = dp[curr_word-1][curr_target]
                curr_pos = ord(target[curr_target-1]) - ord('a')
                dp[curr_word][curr_target] += char_frequency[curr_word-1][curr_pos]* dp[curr_word-1][curr_target-1] % mod
                dp[curr_word][curr_target] %= mod
        return dp[word_length][target_length]

# Approach 3: Optimized Bottom-Up Dynamic Programming

class Solution3:
    def numWays(self, words: List[str], target: str) -> int:
        word_length = len(words[0])
        target_length = len(target)
        dp_prev =  [0] * (target_length+1) 
        dp_curr =  [0] * (target_length+1) 
        char_frequency = [[0] * 26 for _ in range(word_length)]
        mod = 10**9+7
        for word in words:
            for index in range(len(word)):
                character = ord(word[index]) - 97
                char_frequency[index][character] +=1
        dp_prev[0] = 1
        for curr_word in range(1, word_length+1):
            dp_curr = dp_prev.copy()
            for curr_target in range(1, target_length+1):
                dp_curr[curr_target] = dp_prev[curr_target]
                curr_pos = ord(target[curr_target-1]) - ord('a')
                dp_curr[curr_target] += char_frequency[curr_word-1][curr_pos] * dp_prev[curr_target - 1] % mod
                dp_curr[curr_target] %= mod
            dp_prev = dp_curr.copy()
        return dp_curr[target_length]
    
if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution3()
    solve_method = solution_object.numWays
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]

    print(checks)