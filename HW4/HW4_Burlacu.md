#### Homework 4 	---	 Alina Burlacu	---	11/08/2022

### <u>Q1: Merging *k sorted* lists into one sorted list</u> 

1. **Describe your algorithm in high-level pseudocode and explain why your algorithm meets *O(n log k)***

   ```pseudocode
   /*
   lists[k] // the sorted input lists, where k is sorted list of 10000 integers
   heap[k]  // minheap built from lists[k]
   result[n] // output array where n is total length of combined lists 
   li = index in lists[k]
   r = index in result[n]
   
   use min-heap to store k[i] where k is the sorted list, and i is the index
   since each list is already sorted, the smallest number will be at k[0]
   build the min-heap by inserting the value at k[0] of each list 
   
   use deleteMin() to remove the smallest element from the heap[k] and return 
   store the value in result[n] so we get a final sorted list
   
   #ref:https://cs.stackexchange.com/questions/12853/heap-give-an-on-lg-k-time-algorithm-to-merge-k-sorted-lists-into-one-so
   */
   
   // build the min-heap
   for li = 1:k                   // O(k)
     heap.insert(0, k)           // O(log k)
   
   // recursively: delete the min,insert the next value from that list into the heap
   while !heap.empty()           // O(n)
     li,k = heap.deleteMin();     // O(log k)
     result[r++] = lists[k][li]
     li++
     if (li < lists[k].length)    // make sure not end of list 
       heap.insert(li, k)         // O(log k)
   
   
   ```

2. **Describe why your algorithm supports *O(n log k)* time efficiency.** 

   O(k) for the number of elements(lists) used to build the `min-heap`

   2 * O(log k) for the insertion operations in `build_min_heap`

   O(log k) for `deleteMin()`

   O(n) for the number of elements in result output array

     = O(k) +2 * O(log k)  +O(n)

   = O(k  * log k + n  *  2 log k)

   = ***O(n log k)***














3. **Compare and write up a report about the performance difference between your *O(n log k)* and *O(n k)***

   According to my time efficiency function output, a traditional mergesort having *O(nk)* time seems to have taken less time to compute than the heap-merging algorithm I implemented for *O(n log k)* time. I'm not really sure why that is, honestly. I expected it to be the opposite way around, but after spending some time trying to mess with it and get it to work faster, I didn't get anywhere, so it is still the same.

```
Merge-Heap algorithm efficiency: {       
start: 75.859816   
end: 76.703023   
elapsed time: 0.843207}         

MergeSort algorithm efficiency: {       
start: 78.603412   
end: 78.603629   
elapsed time: 0.000217}     
```





















































### <u>Q2: 10-1 Comparison among lists</u> 

|                    | Unsorted,singly linked | Sorted, singly linked | Unsorted, doubly linked | Sorted, doubly linked |
| ------------------ | :-------------------------: | :-----------------------: | :-------------------------: | :-----------------------: |
| *Search(L,k)*      | **O(n)**<br /> since we can only traverse list linearly, time will be relative to number of items in list | **O(n)**<br />*same as unsorted | **O(n)**<br />*same as unsorted singly LL | **O(n)**<br />*same as unsorted |
| Insert(L,x)      | **O(1)**<br />since list unsorted, we can add node to head of list, not needing to update the rest of the list | **O(n)**<br />since already sorted, we first need to search list for correct insertion point, then insert | **O(1)**<br />*same as unsorted singly LL | **O(n)**<br />*same as sorted singly LL |
| Delete(L,x)      | **O(n)**<br />first we have to traverse list for node to delete, which is still linear time, then remove and update pointers of remaining nodes | **O(n)**<br />*same as unsorted | **O(1)**<br />since we have prev/next pointers for  each node, we just have to perform the remove node operation without traversing list | **O(1)**<br />*same as unsorted |
| Successor(L,x)   | **O(n)**<br />since list unsorted, we have to traverse the entire list to find the successor, which has same time as *Search(L,k)* | **O(1)**<br />if list already sorted, it will already have a next pointer to its successor | **O(n)**<br />*same as unsorted singly LL | **O(1)**<br />*same as sorted singly LL |
| Predecessor(L,x) | **O(n)**<br />since list unsorted, we may have to traverse entire list to find predecessor, since it could be before the node we select meaning the whole list would be traversed to get to the prev node | **O(n)**<br />*same as unsorted | **O(n)**<br />even if we have 2 pointers, we only need the prev pointer in this scenario, but the list is unsorted, so it could still require a full list traversal | **O(1)**<br />since list is sorted *and* has prev/next pointers, we already have the predecessor node in the prev pointer |
| Minimum(L)       | **O(n)**<br />will require linear time, since list unsorted, full list traversal is required until the smallest item is found (similar to *Search*) | **O(1)**<br />since list already sorted, we already have the min value to start with, since it would be the first node | **O(n)**<br />*same as unsorted singly LL | **O(1)**<br />*same as sorted singly LL |
| Maximum(L)       | **O(n)**<br />similar to finding *Minimum(L)*, a full traversal would be required | **O(n)**<br />although list is already sorted, the max value will be at the other end of it, meaning we'd have to fully traverse the list as well | **O(n)**<br />*same as unsorted singly LL | **O(n)**<br />*same as sorted singly LL |





### <u>Q3: 11.1-2 Bit vector</u>

Each bit in the bit vector would represent whether an element in the set exists or not, like a TRUE or FALSE, where 1 = TRUE and 0 = FALSE or vice versa. So we would essentially have a list of "yes/no"s to search through instead of searching for an actual element value; we can simply search whether or not it's corresponding key exists (0) or not (1). 









### <u>Q4: 11.1-3 Direct-address table</u>

We can use an unsorted doubly linked list to store satellite data of duplicate keys, and implement the direct-address table using hashing with chaining. 

INSERT: *O(1)* since each added node will be the new head of the linked list

DELETE: *O(1)* since each node will have a prev & next pointer, we already have the location of any node to be deleted

SEARCH: *O(1)*  since  duplicate keys will be hashed to the same slot, so the load factor will be constant

 *   the load factor, *a* =  *# of elements/# of slots* 

 *   the time complexity is *O(1 + a)* 

     







### <u>Q5:</u> 

```pseu
OUTPUT:

### Max_heapify: ITERATIVE

Unsorted array: [39, -21, -48, -13, 38, -28, -48, -43, 12, -22]           
Time Elapsed: 2.1000000000048757e-06           
Sorted array: [39, 38, 12, -13, -21, -28, -48, -43, -48, -22]
---

### Max_heapify: RECURSIVE

Unsorted array: [29, 45, -28, -3, 22, -5, 40, -42, 10, 29]           
Time Elapsed: 9.000000000813912e-07           
Sorted array: [45, 40, 29, 29, 22, -5, -3, -42, 10, -28]
---
```















### <u>Extra Credit:</u>

**1.)**  YES, I've been through the tutorials, also found this one which was really useful:  [Extracting Data from HTML with BeautifulSoup](https://www.pluralsight.com/guides/extracting-data-html-beautifulsoup)



**2.)** 	Here's just the first 5 from my `links.JSON` file

```
[
 {
  "No.": 1,
  "name": "Center for Undergraduate Exploration and Advising",
  "telephone": "1+ 303-315-1940",
  "url": "https://www.ucdenver.edu/center-for-undergraduate-exploration-and-advising"
 },
 {
  "No.": 2,
  "name": "Commencement",
  "telephone": "Not found",
  "url": "https://www.ucdenver.edu/commencement"
 },
 {
  "No.": 3,
  "name": "Counseling Center",
  "telephone": "1+ 303-315-7270",
  "url": "https://www.ucdenver.edu/counseling-center"
 },
 {
  "No.": 4,
  "name": "First Year Experiences",
  "telephone": "1+ 303-315-2133",
  "url": "https://www.ucdenver.edu/first-year-experiences"
 },
 {
  "No.": 5,
  "name": "Health Programs",
  "telephone": "Not found",
  "url": "https://www.ucdenver.edu/programs/health-programs"
 },
```



























**3.)** 

 HTML code generated by Pandas `to_html()` function: 

```
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Cases</th>
      <th>Confirmed cases</th>
      <th>Probable cases</th>
      <th>Deaths among cases</th>
      <th>Deaths due to COVID-19</th>
      <th>Total hospitalized</th>
      <th>Total outbreaks</th>
      <th>Test Encounters</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1,674,577</td>
      <td>1,511,639 (90.27%)</td>
      <td>162,938 (9.73%)</td>
      <td>13,428</td>
      <td>14,154</td>
      <td>69,739</td>
      <td>9,966</td>
      <td>20,500,652</td>
    </tr>
  </tbody>
</table>
```





From `covid_data.html` file: 

|      | Cases     | Confirmed cases    | Probable cases  | Deaths among cases | Deaths due to COVID-19 | Total hospitalized | Total outbreaks | Test Encounters |
| ---- | --------- | ------------------ | --------------- | ------------------ | ---------------------- | ------------------ | --------------- | --------------- |
| 0    | 1,674,577 | 1,511,639 (90.27%) | 162,938 (9.73%) | 13,428             | 14,154                 | 69,739             | 9,966           | 20,500,652      |
