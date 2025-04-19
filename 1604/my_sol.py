from typing import List


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        minutes = [int(entry[3:5]) + 60*int(entry[:2]) for entry in keyTime]
        name_times = {}
        for i in range(len(keyName)):
            if keyName[i] not in name_times:
                name_times[keyName[i]] = [minutes[i]]
            else:
                name_times[keyName[i]].append(minutes[i])
        culprits = []
        for key, value in name_times.items():
            if len(value) > 2:
                value.sort()
                last_time = value[0]
                for index in range(2, len(value)):
                    if value[index] - last_time <= 60:
                        culprits.append(key)
                        break
                    last_time = value[index - 1]
        return sorted(culprits)

if __name__ == "__main__":
    from examples import inputs, outputs
    solution_object = Solution()
    solve_method = solution_object.alertNames
    checks = [solve_method(*input) == output for input, output in zip(inputs, outputs)]
    print(checks)