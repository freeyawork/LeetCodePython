class Solution:
    # @return an integer
    def totalNQueens(self, n):
        total = 0
        stack = []
        for i in range(0,n):
            stack.append([(0,i)])
        
        while stack:
            solution = stack.pop()
            cols = [elem[1] for elem in solution]
            row = len(solution)
            if row == n:
                total += 1
                continue
            for i in range(0,n):
                if not (i in cols) and self.safe(solution,(row,i)):
                    new_solution = solution + [(row,i)]
                    stack.append(new_solution)

        return total
    
                
    def safe(self,solution,loc):
        rows = [elem[0] for elem in solution]
        cols = [elem[1] for elem in solution]
        diffs = [cols[i]-rows[i] for i in range(0,len(rows))]
        adds =  [cols[i]+rows[i] for i in range(0,len(rows))]

        if loc[0] in rows:
            return False
        if loc[1] in cols:
            return False
        if loc[1]-loc[0] in diffs or loc[0]+loc[1] in adds:
            return False
        return True