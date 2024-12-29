# Approach 1

from typing import List

# Approach 1: Memoization
class Solution1:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        self.k = k
        self.n = len(nums) - k + 1
        self.sums = [sum(nums[:k])]
        for i in range(k, len(nums)):
            self.sums.append(self.sums[-1] - nums[i-k] + nums[i])  
        self.memo = [[-1]*4 for _ in range(self.n)]
        self.indices = []
        self.dp(0, 3)
        self.dfs(0, 3)
        return self.indices

    def dp(self, idx, rem):
        if rem == 0:
            return 0
        if idx >= len(self.sums):
            return float("-Inf") if rem > 0 else 0
        if self.memo[idx][rem] != -1:
            return self.memo[idx][rem]
        else:
            choice1 = self.sums[idx] + self.dp(idx+self.k, rem -1)
            choice2 = self.dp(idx+1, rem)
            self.memo[idx][rem] = max(choice1, choice2)
            return max(choice1, choice2)


    def dfs(self, idx, rem):
        if rem == 0 or idx >= len(self.sums):
            return
        choice1 = self.sums[idx] + self.dp(idx+self.k, rem -1)
        choice2 = self.dp(idx+1, rem)     
        if choice1 >= choice2:
            self.indices.append(idx)
            self.dfs(idx+self.k, rem-1)
        else:
            self.dfs(idx+1, rem)

# Approach 2: Tabulation
class Solution2:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefix_sum = [0]*(n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = (nums[i-1] + prefix_sum[i-1])
        best_sum = [[0]*(n + 1) for _ in range(4)]        
        best_index = [[0]*(n + 1) for _ in range(4)]        
        for subarray_count in range(1, 4):
            for ending in range(k*subarray_count, n+1):
                current_sum = prefix_sum[ending] - prefix_sum[ending-k] + best_sum[subarray_count-1][ending-k]
                if current_sum > best_sum[subarray_count][ending-1]:
                    best_sum[subarray_count][ending] = current_sum
                    best_index[subarray_count][ending] = ending-k
                else: 
                    best_sum[subarray_count][ending] = best_sum[subarray_count][ending-1]
                    best_index[subarray_count][ending] = best_index[subarray_count][ending-1]     
        result = [0, 0, 0]
        current_end = n
        for subarray in [3,2,1]:
            result[subarray-1] = best_index[subarray][current_end]
            current_end = best_index[subarray][current_end] 
        return result

# Approach 3: Three Pointers
class Solution3:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        from itertools import accumulate
        n = len(nums)
        max_sum = 0

        prefix_sum = [0] + list(accumulate(nums)) 

        left_max_index = [0]*n
        right_max_index = [0]*n
        result = [0, 0, 0]
        
        current_max_sum = prefix_sum[k]- prefix_sum[0]
        for left_index in range(k, n):
            current_sum = prefix_sum[left_index + 1] - prefix_sum[left_index + 1 - k]
            if current_sum > current_max_sum:
                left_max_index[left_index] = left_index + 1 - k
                current_max_sum = current_sum
            else:
                left_max_index[left_index] = left_max_index[left_index - 1]
                
        right_max_index[n-k] = n-k
        current_max_sum = prefix_sum[n]- prefix_sum[n-k]
        for right_index in range(n-k-1,-1,-1):
            current_sum = prefix_sum[right_index+k] - prefix_sum[right_index]
            if current_sum >= current_max_sum:
                right_max_index[right_index] = right_index
                current_max_sum = current_sum
            else:
                right_max_index[right_index] = right_max_index[right_index + 1]                
            
        for middle_index in range(k, n-2*k + 1):
            current_left = left_max_index[middle_index - 1]
            current_right = right_max_index[middle_index + k]
            current_sum = prefix_sum[current_left + k] - prefix_sum[current_left] + prefix_sum[current_right+k] - prefix_sum[current_right] + prefix_sum[middle_index + k] - prefix_sum[middle_index]
            if current_sum > max_sum:
                max_sum = current_sum
                result = [current_left, middle_index, current_right]
        return result

# Approach 4: Sliding Window
class Solution4:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        
        best_single_start = 0
        best_double_start = [0, k]
        best_triple_start = [0, k, k*2]
        current_window_sum_single = sum(nums[:k])
        current_window_sum_double = sum(nums[k:2*k])
        current_window_sum_triple = sum(nums[2*k:3*k])
        best_single_sum = current_window_sum_single
        best_double_sum = best_single_sum + current_window_sum_double
        best_triple_sum = best_double_sum + current_window_sum_triple
        single_start_index = 1
        double_start_index = k + 1
        triple_start_index = 2*k + 1
        while triple_start_index < len(nums) - k:
            current_window_sum_single += nums[single_start_index + k - 1] - nums[single_start_index - 1]
            current_window_sum_double += nums[double_start_index + k - 1] - nums[double_start_index - 1]
            current_window_sum_triple += nums[triple_start_index + k - 1] - nums[triple_start_index - 1]
            if current_window_sum_single > best_single_sum:
                best_single_sum = current_window_sum_single
                best_single_start = single_start_index
            if best_single_sum + current_window_sum_double > best_double_sum:
                best_double_sum = best_single_sum + current_window_sum_double
                best_double_start[0] = best_single_start
                best_double_start[1] = double_start_index
            if best_double_sum + current_window_sum_triple > best_triple_sum:
                best_triple_sum = best_double_sum + current_window_sum_triple
                best_triple_start[0] = best_double_start[0]
                best_triple_start[1] = best_double_start[1]
                best_triple_start[2] = triple_start_index
            single_start_index +=1
            double_start_index +=1
            triple_start_index +=1
        return best_triple_start



if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution1()
    solve_method = solution_object.maxSumOfThreeSubarrays
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]

    # print(checks)
    solution_object = Solution2()
    solve_method = solution_object.maxSumOfThreeSubarrays
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]

    # print(checks)    
    solution_object = Solution3()
    solve_method = solution_object.maxSumOfThreeSubarrays
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]

    print(checks)