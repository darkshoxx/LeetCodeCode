from typing import List
import pandas as pd
import numpy as np


class Solution:
    def find_employees(self, employee: pd.DataFrame) -> pd.DataFrame:
        has_boss = employee[[type(entry)==int for entry in employee["managerId"]]]
        noteworthy_employees = []
        for row in has_boss.index:
            empy = has_boss.iloc[row]
            my_manager_id = empy["managerId"]
            my_manager = employee[employee["id"]==my_manager_id]
            manager_salary = my_manager["salary"]
            if float(empy["salary"])> float(manager_salary.iloc[0]):
                noteworthy_employees.append(empy["id"])
        result = employee[employee["id"].isin(noteworthy_employees)]
        return pd.DataFrame({"Employee":list(result["name"])})



if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.find_employees
    checks = [solve_method(input) == output for input, output in zip(inputs, outputs)]
    print(checks)