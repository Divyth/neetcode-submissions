class DSU:
	def __init__(self, n):
		self.parent = [i for i in range(n)]
		self. rank = [0] * n 
	
	def find(self, x):
		if self.parent[x] != x:
			self.parent[x] = self.find(self.parent[x])
		return self.parent[x]
	
	def union(self, x, y):
		rx = self.find(x)
		ry = self.find(y)
		
		if rx == ry:
			return
			
		if self.rank[rx] < self.rank[ry]:
			self.parent[rx] = ry
		elif self.rank[ry] > self.rank[rx]:
			self.parent[ry] = rx
		else:
			self.parent[rx] = ry
			self.rank[rx] += 1
		
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        dsu = DSU(n)

        emailToAccount = {} # eamil to index ie initial name

        # step1 link email to account name if already in hashmap union current with index in hashmap
        for i, a in enumerate(accounts):
            for e in a[1:]: # from 1 because ignore name
                if e in emailToAccount:
                    dsu.union(i, emailToAccount[e])
                else:
                    emailToAccount[e] = i
        
        #step2  GROUP EMAILS BY ROOT PARENT
        mergedEmail = defaultdict(list)
        for e, i in emailToAccount.items():
            root = dsu.find(i)
            mergedEmail[root].append(e)

        #step 3 BUILD FINAL ANSWER

        res = []

        for i, emails in mergedEmail.items():
            name = accounts[i][0]
            res.append([name] + sorted(mergedEmail[i]))
        return res









