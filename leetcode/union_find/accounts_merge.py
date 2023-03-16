'''
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.
'''

from collections import defaultdict


class Node:
    def __init__(self, email, account_name):
        self.email = email
        self.account_name = account_name
        self.parent = self
        self.rank = 1

    def _find(self):
        if self.parent != self:
            return self.parent._find()
        return self

    def union(self, neighbor):
        self_parent, neighbor_parent = self._find(), neighbor._find()
        if self_parent == neighbor_parent:
            return
        if self_parent.rank < neighbor_parent.rank:
            self_parent.parent = neighbor_parent
        elif self_parent.rank > neighbor_parent.rank:
            neighbor_parent.parent = self_parent
        else:
            self_parent.parent = neighbor_parent
            neighbor_parent.rank += 1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_node_map = defaultdict(Node)

        for account in accounts:
            account_name, emails = account[0], account[1:]
            base_node = None
            for idx, email in enumerate(emails):
                if email not in email_node_map:
                    email_node_map[email] = Node(email, account_name)

                if idx == 0:
                    base_node = email_node_map[email]
                else:
                    base_node.union(email_node_map[email])

        parent_node_email_map = defaultdict(list)
        for email_node in email_node_map.values():
            parent = email_node._find()
            parent_node_email_map[parent].append(email_node.email)

        res = []
        for parent_node, emails in parent_node_email_map.items():
            record = [parent_node.account_name] + sorted(emails)
            res.append(record)

        return res

