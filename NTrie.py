
# Definition for a Node.
class NTrie(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class NTrieUtilities(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        if not root:
            return []
        queue = [root]
        answer = []
        while queue:
            nxt = []
            tmp = []
            for node in queue:
                tmp.append(node.val)
                answer.append(node.val)
                for c in node.children:
                    nxt.append(c)

            queue = nxt
        
        return answer

if __name__ == '__main__' : 
    s = NTrieUtilities()

    trie = NTrie(7, [NTrie(3, [NTrie(1, [NTrie(0, []), NTrie(4, [])]), NTrie(8, [NTrie(17, []), NTrie(18, [])])]), NTrie(15, []), NTrie(16, [])])
    
    triePrint = s.levelOrder(trie)

    print(triePrint)