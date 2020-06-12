class Solution:
    def isHappy(self, n:int) -> bool:
        is_loop_list = list()
        while(True):
            n = sum(list(map(lambda x: int(x)**2, str(n))))
            if n in is_loop_list:
                return False
            is_loop_list.append(n)
            if n==1 :
                return True

if __name__ == "__main__":
    solution = Solution(); val = None
    while(val is not 'q'):
        val = input("Enter test value (q for exit) : ")
        if val == 'q': break
        res = solution.isHappy(val); print_res = '' if res else 'not '
        print(f'{val} is {print_res}a happy number')
