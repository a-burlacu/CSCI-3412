# Final Exam Extra Credit Assignment 

### Alina Burlacu 

#### 12/11/22



**A[0..11]: 25, 13, 38, 42, 7, 30, 3, 16, 29, 17, 55, 26**

#### 1. Build and show a binary search tree (BST) using array A[0..11]. You read the array left to right and fill the key in the tree starting from the root; in this case, 25 is the root.

<img src="C:\Users\Alina\OneDrive - The University of Colorado Denver\Coding\CSCI-3412\Final\Q1.png" style="zoom:80%;" />

#### **2,3,4.** Show pre-order, in-order, and post-order traversals of the BST built above



> PREORDER:   25, 13, 7, 3, 16, 17, 38, 30, 29, 26, 42, 55

> INORDER:   3, 7, 13, 16, 17, 25, 26, 29, 30, 38, 42, 55

> POSTORDER:  3, 7, 17, 16, 13, 26,  29,  30, 55, 42 , 38, 25



#### **5.** From the BST above, add nodes 11, 35, and 45. And then remove 26, 16, and 25. Then show the final tree. You must apply the BST insertion/deletion algorithms discussed in the class.  

<img src="C:\Users\Alina\OneDrive - The University of Colorado Denver\Coding\CSCI-3412\Final\Q5.png" style="zoom: 25%;" />



#### **6.** Show the immediate successor of the new root node in the BST by applying the BST successor algorithms discussed in the class  



> The successor of the root node, 29, is  equal to the minimum key value in the current node's right subtree. So in this case, the successor is **30**. 

```python
def findSuccessor(currentNode):
    succ = None
    if currentNode.right not None:
        succ = getMinKey(currentNode.right)
```





#### **7.** We want to save the keys of a BST into an array. Then later we want to rebuild exactly the same BST by reading in the keys sequentially from the saved array. Describe a way to save the keys systematically.  [Hint: think of a tree traversal and homework 5] 



> To save the keys in order in an array, traverse the tree PREORDER:  
>
> - Get the root node
> - Visit the Left subtree
> - Visit the right subtree



#### **8.** Why is the BST not considered the best solution for all cases? Give an example where BST can be as bad as a linked list. What's an alternative solution to address the problem?  



> The underlying data structures of a BST are linked lists and sorted fixed arrays. For linked lists, the time it takes to search/select an element is ***O(n)***, If we can convert the BST to a Red-Black Tree, it would solve this problem, by improving the search time efficiency to ***O(lg n)***. 



#### **9.** Can the BST tree in **Q5** be a Red-Black BST tree? Verify your answer using four R-B tree properties.  If it is an R-B tree, you only need to show a properly colored tree satisfying the R-B tree properties. If not an R-B tree, prove why it can't be an R-B tree. 



> 1. Every node is either red or black
>
> 2. The root and leaves are black
>
> 3. If a node is red, it's parent is black
>
> 4. All simple paths from any node, *x* , to <u>all</u> descendant leaves must have the <u>same number of black nodes</u> (black height)
>
>    
>
>    No, it cannot. In this case, there is no way to color the nodes so that the black height of each path is equal. 



#### **10.**  Into the resulting tree of **Q5**, add 57 and 48. Then to balance the BST tree, perform RB-balancing operations as needed using recoloring and/or rotations as they get added. Draw a separate tree picture for each operation step. 

> 

#### **11.** For high-performing applications, balanced BST may not be a satisfying data structure for the **fast search operation**. What's an alternative to it? Give your explanation on why the performance of the selected alternative is better than that of BST. 

>
>
>

#### **12.** Summarize the basic ideas of a Skip List and explain how a skip list is built with the following sequences of nodes and Head/Tail toss results. Then show how node **29** is searched from the skip list. If the coin toss result is Head, go to the right but if Tail, go a level up. 

**Nodes: 13, 15, 17, 19, 22, 28, 29, 33, 37, 38**

**Coin toss results: H, T, T, T, H, H, T, H, H, T, H, H, H, T, T, H**

> 

#### **13.** Show a tabular form solution of the following 0/1 knapsack problem. **(1 pt)**

**Value   {5, 7, 3, 10, 12, 4, 10}**

**Weight {2, 3, 1, 5, 6, 2, 4}**

**Total Weight: 12**

> 

#### **14.** Show a solution to the Fractional knapsack problem with the same weight, value, and total weight configuration in **Q12** above.  

> 

#### **15.** Run the Levenshtein Edit Distance algorithm to count the minimum cost between "California" and "Colorado". Use the same assumption we made in the lecture.  Exercise it with pen and pencil first using the bottom-up table to understand the algorithm then verify your answer by running a program in the lecture note. 

> 

***For the following questions, use the graph (starting node: s, target node: t) below:***

<img src="C:\Users\Alina\OneDrive - The University of Colorado Denver\Coding\CSCI-3412\Final\TopologicalSortingGraph.JPG" alt="TopologicalSortingGraph" style="zoom:150%;" />

#### **16.** Show a DFS traversal. You may list the node labels in the sequence of traversal. (e.g., s --> A --> E --> , ... --> t) In this problem, 't' is not a terminal node. Treat it as a name of a node. Also, you may regard the graph as undirected

> 

#### **17.** Show a BFS traversal. You may list the node labels in the sequence of traversal.  In this problem, 't' is not a terminal node. Treat it as a name of a node. Also, you may regard the graph as undirected. 

> 

#### **18.** Show a result of the topological sorting of the graph using the simple algorithm as discussed in class. There might be multiple of them. Just list one of them. 

> 

#### **19.** Dijkstra's single-source shortest paths for all nodes. Exercise it with pen and pencil first to understand the algorithm then verify your answer by running your own program from HW6. Show the results of both exercises. 

> 

***With a given graph that has negative edges:***

<img src="C:\Users\Alina\OneDrive - The University of Colorado Denver\Coding\CSCI-3412\Final\Bellman-Ford.JPG" alt="Bellman-Ford" style="zoom:80%;" />

####  **20.** Find the Bellman-Ford shortest paths for all nodes from starting node a.

> 

***Using the graph below, solve the following problems:***

<img src="C:\Users\Alina\OneDrive - The University of Colorado Denver\Coding\CSCI-3412\Final\MST Problem.JPG" alt="MST Problem" style="zoom:150%;" />

#### **21.** Find the minimum spanning tree using the less efficient **Simple** algorithm. Be careful not to introduce a disconnected subgraph. Show the MST and total weight of the MST.  

> 

#### **22.** Find the minimum spanning tree using **Prim's** algorithm and list the edges in the order that they are added to the MST.  Prim’s algorithm can start at any vertex but without losing generality, you may start from D for easy comparison of your answers with others. Be careful not to form a cycle. 

> 

#### **23.** Find the minimum spanning tree using **Kruskal's** algorithm and list the edges in the order that they are added to the MST. Kruskal’s algorithm can start at any vertex but without losing generality, you may start from D for easy comparison of your answers with others. Be careful not to form a cycle.

> 

#### **24.** With the assumptions made in the lecture, build a Huffman tree to encode the following string, "EBBEATTETETZZALMET" using the frequency table built from the given string. Finally, show the encoded binary string of the original string.  

> 

#### **25.** [**Maxflow/Min cut**: Ford-Fulkerson Algorithm] You may go over the example on pp 726 - 727 of the **CLRS** textbook. Summarize all the steps applied in the process of finding the max flow of the graph in your own words. 

> 

#### **26.** Summarized the definitions and basic ideas of computational complexity (P, NP, NP-C, NP-Hard, P vs. NP) in your own words (Lecture slides: 3 - 14, 22-24)  

> 