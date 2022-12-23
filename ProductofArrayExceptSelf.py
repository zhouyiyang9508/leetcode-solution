from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    products = [0] * len(nums)
    products[0] = 1
    for i in range(1, len(nums)):
        products[i] = products[i - 1] * nums[i - 1]

    right = 1
    for i in range(len(nums) - 1, -1, -1):
        # 2nd product[i] means the product of i's  left side. 1st product[i] means the result
        products[i] = products[i] * right
        right *= nums[i]

    return products

if __name__ == '__main__':
    print(productExceptSelf([1,2,3,4]))