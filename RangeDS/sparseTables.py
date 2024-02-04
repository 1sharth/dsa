from math import ceil, log2, floor


class SparseTable:

    def __init__(self, arr:list, func) -> None:
        n = len(arr)
        k = ceil(log2(n))
        self.st = [[0 for _ in range(n)] for __ in range(k+1)]
        self.func = func
        self.st[0] = arr[:]
        for i in range(1,k+1):
            j = 0
            while j+2**i-1 < n:
                self.st[i][j] = func(self.st[i-1][j], self.st[i-1][j+2**(i-1)])
                j+=1


    def build_table(self, arr:list, func) -> list:
        self(arr, func)
        return self.st

    def get_range_slow(self,l:int,r:int, init:int=0) -> int:
        res = init
        k = len(self.st)
        for i in range(k,-1,-1):
            if 2**i <= r-l+1:
                res = self.func(res, self.st[i][l])
                l=l+(2**i)
        return res
    
    def get_range_fast(self,l:int,r:int) -> int:
        k = floor(log2(r-l+1))
        return self.func(self.st[k][l], self.st[k][r-2**k + 1])
    
    def __str__(self):
        return str(self.st)
    
    def __repl__(self):
        return str(self.st)
    

# sum_table = SparseTable([3,5,43,2,6,7,53],lambda x,y: min(x,y))
# print(sum_table.get_range_slow(0,0,999999),sum_table.get_range_fast(0,0))
# print(sum_table.get_range_slow(0,1,999999),sum_table.get_range_fast(0,1))
# print(sum_table.get_range_slow(0,2,999999),sum_table.get_range_fast(0,2))
# print(sum_table.get_range_slow(0,3,999999),sum_table.get_range_fast(0,3))

# sum_table = SparseTable([1,4,1],lambda x,y: min(x,y))
# print(sum_table.get_range_slow(1,1,999999),sum_table.get_range_fast(1,1))
# print(sum_table.get_range_slow(1,2,999999),sum_table.get_range_fast(1,2))

n=int(input())
arr = [int(_) for _ in input().split(" ")]
min_table = SparseTable(arr,lambda x,y: min(x,y))
for _ in range(int(input())):
	l,r = [int(_) for _ in input().split(" ")]
	print(min_table.get_range_fast(l,r))
