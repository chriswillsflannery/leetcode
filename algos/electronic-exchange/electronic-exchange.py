"""
You work in an electronic exchange. Throughout the day, you receive ticks (trading data) which consists of 
product name and its traded volume of stocks. Eg: {name: vodafone, volume: 20}. What data structure will you 
maintain if:
* You have to sell top k products traded by volume at end of day.
* You have to sell top k products traded by volume throughout the day.

if we kept a dict like:
{
    vodafone: 20
}
-> as stocks tick in during the day 
make more sense to keep a sorted set?
But that would mean we have to at least partially re-sort on every new tick

{ vodafone: 20, max: 40, ff: 60}

if we get a new vodafone tic for an additional 20 shares then we need to move it (swap/sort)


----
BY END OF DAY:

If we keep a simple dictionary:
{
    vodafone: 20,
    max: 40,
    ff: 60
}
Then at the end of day, we can convert it to a list, and sort to get the top K products.
We end up with a NLogN time complexity due to sorting.

----
THROUGHOUT DAY:

This requires maintaining a record of the top K products at all times.
We can maintain a min-heap of size K, and a hash map.

hashmap:
{
    vodafone: 20,
    max: 40,
    ff: 60
}
minheap (size 2):
{
    [60, ff],
    [40, max]
}

on any tick update, if the current total value of the company in the hashmap
exceeds the minimum value in the minheap, that company replaces the minimum
value company in the minheap

"""