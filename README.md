# forHpn

# Partie SQL en ligne
 All queries are in query.sql file

 # Partie SQL hors ligne
 Response is in bigquery.sql file.
   
# Partie Python
1. The idea is to use try/catch construct with built-in facilities: ipaddress lib in Python.
   The code below validates the real-life IPv4, and real-life IPv6

   Code requirement: Python 3, ipaddress

   Instalation and execution:
   ```bash
    pip install -r requirements.txt

    python ipValidator.py input.txt 
   ```

2. Graphe
  
  The graph structure is a python class.
  ```python

  class NTrie(object):
      ''' N-Trie structure'''

    def __init__(self, val, children):
        self.val = val
        self.children = children
   ```
    Attributs:
    node: define the currente node value
    children: is an array of Node type. Each value of the array represente a children of current node. 

    Example of graph:
    ```python
    trie = NTrie(7, [NTrie(3, [NTrie(1, [NTrie(0, []), NTrie(4, [])]), NTrie(8, [NTrie(17, []), NTrie(18, [])])]), NTrie(15, []), NTrie(16, [])])
    ```
    this graph represente the one given in the exercice. 

  NTrieUtilities class have function that take a graph and out put all it value has describe in the exercice.

  Juste execute the following commande to run it juste:

  python NTrie.py 

# Partie PySpark
 Response is in  PrivateCount.ipynb notebook. 
