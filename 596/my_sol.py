from typing import List
import pandas as pd


class Solution:
    def find_classes(self, courses: pd.DataFrame) -> pd.DataFrame:
        frequency = courses.groupby(['class']).count()
        return pd.DataFrame(frequency[frequency["student"]>1].index)


if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.find_classes
    checks = [solve_method(input) == output for input, output in zip(inputs, outputs)]
    print(checks)