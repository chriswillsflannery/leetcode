/*

Given an array of arrays like the following:
[
    ['icr_2', 'icr_3'],
    ['icr_2', 'icr_3', 'icr_5'],
    ['icr_5', 'icr_4']
]

return a Map which reflects unique pairings;
Map() {
    icr2 => 2 (because 3 and 5)
    icr3 => 2 (because 2 and 5)
    icr4 => 1 (because 5)
    icr5 => 3 (because 2, 3, and 4)
}

// is there a way to do this in linear time?

*/