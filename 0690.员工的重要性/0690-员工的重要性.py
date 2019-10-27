"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, i):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        d = {}
        for e in employees:
            d[e.id] = [e.importance, e.subordinates]
        ret, stack = 0, [i]
        while stack:
            i = stack.pop()
            ret += d[i][0]
            for n in d[i][1]:
                stack.append(n)
        return ret
            