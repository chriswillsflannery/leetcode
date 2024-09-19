function minimalHeaviestSetA (arr) {
    const sum = (arr) => {
        if (Array.isArray(arr) && arr.length) {
            return arr.reduce((a,b) => a+b)
        } else { return 0 }
    }

    // sort ascending
    arr.sort((a,b) => a - b)

    const arrLength = arr.length;

    let n = 1
    const A = []
    let B = []
    const pivot = Math.floor(sum(arr) / 2)

    while (n <= arrLength) {
        const w = arr.pop()
        A.push(w)
        B = [...arr]

        n++
        sumA += w

        if (sumA > pivot) {
            // check element is not in both sets
            if (B.includes(w)) continue
            break
        }
    }
    return A
}