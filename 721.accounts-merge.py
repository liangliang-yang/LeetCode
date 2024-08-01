#
# @lc app=leetcode id=721 lang=python
#
# [721] Accounts Merge
#

# @lc code=start

import collections

class Solution:
    def accountsMerge(self, accounts):
        # for each email, check the associated acct_ids
        graph = collections.defaultdict(set) # email -> {acct_id1, acct_id2}
        
        visited = [False] * len(accounts)
        
        # can't use name as key, people can have same name
        # accounts[i][0] is a name, ["John","johnsmith@mail.com","john_newyork@mail.com"]
        for acct_id, account in enumerate(accounts): # use index as acct_id
            emails = account[1:]
            for email in emails:
                graph[email].add(acct_id)
        
        res = [] 
        for acct_id, account in enumerate(accounts):
            if visited[acct_id]: # already visited this account, must add this, we could visit inside dfs
                continue # this is like 0-1 matrix, some 1s will be updated to # so we will skip those 1s
            name = account[0]
            connected_emails = set()
            self.dfs(accounts, graph, visited, acct_id, connected_emails)
            tmp = [name] + sorted(list(connected_emails))
            res.append(tmp)
            
        return res
    
    # dfs to add connected accounts, 像这样不断改变 connected_emails， 不要 dfs 返回
    def dfs(self, accounts, graph, visited, acct_id, connected_emails):
        if visited[acct_id]:
            return
        
        visited[acct_id] = True
        emails = accounts[acct_id][1:]
        for email in emails:
            connected_emails.add(email) # set.add() return nothing
            linked_ids = graph[email] #{id1, id2}
            for linked_id in linked_ids:
                self.dfs(accounts, graph, visited, linked_id, connected_emails)
                
        
        
# @lc code=end

