class Noode {
  val: number;
  neighbors: Noode[];
  constructor(val?: number, neighbors?: Noode[]) {
    this.val = val === undefined ? 0 : val;
    this.neighbors = neighbors === undefined ? [] : neighbors;
  }
}

type OldToNew = Map<Noode, Noode>;

function cloneGraph(node: Noode | null): Noode | null {
  if (!node) return null;

  const oldToNew: OldToNew = new Map();
  const stack = [node];

  while (stack.length) {
    const cur = stack.pop();
    if (!cur) continue;
    let clone: Noode;

    if (!oldToNew.has(cur)) {
      clone = new Noode(cur.val);
      oldToNew.set(cur, clone);
    } else {
      clone = oldToNew.get(cur)!;
    }

    for (let neighbor of cur.neighbors) {
      if (!oldToNew.has(neighbor)) {
        const newNeighbor = new Noode(neighbor.val);
        oldToNew.set(neighbor, newNeighbor);
        stack.push(newNeighbor);
      }
      clone.neighbors.push(oldToNew.get(neighbor)!);
    }
  }

  return oldToNew.get(node)!;
}
