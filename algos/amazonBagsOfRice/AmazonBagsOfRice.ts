/*

You are shopping on Amazon.com for some bags of rice. Each listing displays the number of grains of rice that the bag contains.
You want to buy a perfect set of rice bags from the entire search results list, riceBags. A perfect set of rice bags, perfect, is defined as:
• The set contains at least two bags of rice.
• When the rice bags in the set perfect are sorted in increasing order by grain count, it satisfies the condition perfecti-perfect[= perfectfi+1] for all 1 s i< n. Here nis the size of the set and perfecti) is the number of rice grains in bag i.
Find the largest possible set perfect and return an integer, the size of that set. If no such set is possible, then return -1. It is guaranteed that all elements in riceBags are distinct.

Find the largest possible set perfect and return an integer, the size of that set. If no such set is possible, then return -1. It is guaranteed that all elements in riceBags are distinct.
Example
Let the bags of rice available on Amazon have grain counts [3, 9, 4, 2,
16]. The following are the perfect sets.
• Set perfect = [3, 9]. The size of this set is 2.
• Set perfect = [4, 2]. The size of this set is 2.
• Set perfect = [4, 16]. The size of this set Is 2.
• Set perfect = [4, 2, 16]. The size of this set is 3.
The size of the largest set Is 3. The image below illustrates the correct ordering of the purchased rice bags by grains of rice.

"""
def maxSetSize2(riceBags):
bag_list = sorted(riceBags, reverse=True)
max_len = -1

*/

// for i in range(len(bag_list)):
//     number = bag_list[i]
//     rice_set = [number]
//     for j in range(i + 1, len(bag_list)):
//         if number ** 0.5 == bag_list[j]:

//             rice_set.append(bag_list[j])
//             number = bag_list[j]
//     if len(rice_set) < 2:
//         continue
//     if len(rice_set) > max_len:
//         max_len = len(rice_set)

// return max_len
