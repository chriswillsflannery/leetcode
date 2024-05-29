/*
Implement a function chunk(array, [size=1]) that splits the input array
into groups of length size and returns them within a new array.
If array can't be split evenly, the final chunk will be the remaining
elements. The function should not modify the original input array.
*/

// with altering input array

export function chunka<T>(array: Array<T>, size = 1): Array<Array<T>> {
  const chunks: T[][] = [];

  while (array.length) {
    let chunk: T[] = [];
    for (let i = 0; i < size; i++) {
      const item = array.shift();
      if (!item) continue;

      chunk.push(item);
    }
    chunks.push(chunk);
  }

  return chunks;
}

// without altering input array
export function chunky<T>(array: Array<T>, size = 1): Array<Array<T>> {
  if (array.length === 0) return [];
  const chunks: T[][] = [];

  let chunk: T[] = [];
  for (let i = 0; i < array.length; i++) {
    if (chunk.length === size) {
      chunks.push(chunk);
      chunk = [];
    }
    chunk.push(array[i]);
  }

  chunks.push(chunk);

  return chunks;
}
