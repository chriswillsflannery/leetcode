// given a list of socks like:
/*

[
[101, 'FFAAFF'],
[102, 'FFAAFF'],
[103, 'FFEEEE'],
[104, 'FFEEEE'],
]

group the socks such that each pair has the same hex color, like the following:
[[101, 102], [103, 104]]

We should loop over each sock and build an object like this:
{
    'FFAAFF': '101'
}
Each time we see a particular color, we look to see if there is a sock with that color in the object.
If there is not, we add that sock to the object.
If there is, we can remove that sock from the object, and add the pair to some "results" array.

Expansion: the socks also have a size

[
[101: 'FFAAFF', '9']
[102: 'FFAAFF', '10']
[103: 'FFAAFF', '9']
[104: 'FFAAFF', '10']
]

pair the socks off such that they are paired by both size and color

Here we can do a similar pattern to the above, but build the object like this:
{
    9: {
        'FFAAFF':101
    },
    10: {
        'FFAAFF':102
    }
}

Here, we would follow the same pattern as before - as we see a new color of sock for that size,
add it to the appropriate object.
When a match is found for that sock both by size and by color, remove that sock from the object,
and add the pair to a results array.

*/

function processSockStream() {
    while (true) {
        nextBatch = getNextBatchFromKafka()
        // store raw batches in db for processing
        storeBatchInDB(nextBatch)
        // get all unpaired socks from db (previously unpaired socks + nextBatch)
        // create pairs from those so-far-unpaired socks
        pairSocks(unpairedSocks)
        // update db with pairs, and stragglers
    }
}

function pairSocks() {
    // do the same thing we were doing before, but instead of
    // building up an object to find pairs, we run a find_one
    // op on the db -> 

    /*
        SELECT * FROM socks WHERE
        color = inputColor
        AND size = inputSize
        AND paired = FALSE
        and id != inputID
        LIMIT 1
    */

    // each time a pair is found and added to a RES array
    // we also mark both socks as PAIRED = TRUE in db
}

// spin up multiple instances of this process
// ex force multithreading in NodeJS or use Go routines etc.
function () {
    // for each avail thread...
        processSockStream()
}