from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    def dfs(start, tmp_res, tmp_array) :
        if tmp_res > target:
            return
        if tmp_res == target:
            output.append(tmp_array[:])
            return
        for i in range(start, len(candidates)):
            tmp_array.append(candidates[i])
            dfs(i, tmp_res + candidates[i], tmp_array)
            tmp_array.pop()
    output = []
    dfs(0, 0, [])
    return output


if __name__ == '__main__':
    print(combinationSum([2,3,6,7], 7))