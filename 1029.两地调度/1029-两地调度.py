class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        costs.sort(key=lambda x: x[0] - x[1])

        n = len(costs) // 2

        return sum(map(lambda x: x[0], costs[:n])) + sum(map(lambda x: x[1], costs[n:]))
        """
        #slow code
        tasks = costs
        n = len(tasks) // 2
        self.ret = float('inf')
        def h(tasks, index, a, b, cur):
            if index >= len(tasks):
                return
            if a == n and b == n:
                self.ret = min(self.ret, cur)
                return
            if a == n:
                cur += sum(map(lambda x: x[1], tasks[index:]))
                self.ret = min(self.ret, cur)
                return
            if b == n:
                cur += sum(map(lambda x: x[0], tasks[index:]))
                self.ret = min(self.ret, cur)
                return
            h(tasks, index+1, a+1, b, cur+tasks[index][0])
            h(tasks, index+1, a, b+1, cur+tasks[index][1])
        
        h(tasks, 0, 0, 0, 0)

        return self.ret
        """