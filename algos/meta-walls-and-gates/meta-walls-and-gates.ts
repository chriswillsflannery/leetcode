
const emp = Infinity
const WAL = -1
const GAT = 0

const matrix = [
  [emp, WAL, GAT, emp],
  [emp, emp, emp, WAL],
  [emp, WAL, emp, WAL],
  [GAT, WAL, emp, emp]
];

// LC 286
// task: replace every empty space with its distance to the nearest gate (2):
{/**
const matrix = [
  [iii, -1, 0, i],
  [ii, ii, i, -1],
  [i, -1, ii, -1],
  [0, -1, iii, iv]
];
*/}

// BFS from each of the gates
// first find all the spaces which are 1 away from a gate.
// then find all the spaces which are 2 away from a gate. etc.

function wallsAndGates(rooms: number[][]): void {
  const ROWS = rooms.length;
  const COLS = rooms[0].length;
  const visit: Set<string> = new Set();
  const q: number[][] = [];

  function addRoom(r: number, c: number) {
    if (r < 0 || r === ROWS || c < 0 || c === COLS || visit.has(encode(r,c)) || rooms[r][c] == -1) {
      return;
    }
    visit.add(encode(r,c));
    q.push([r,c]);
  }

  for (let r = 0; r < ROWS; r++) {
    for (let c = 0; c < COLS; c++) {
      if (rooms[r][c] === WAL) {
        q.push([r,c]);
        visit.add(encode(r,c));
      }
    }
  }

  let dist = 0;
  while (q.length) {
    for (let i = 0; i < q.length; i++) {
      const layer = q.shift();
      if (!layer) continue;

      const [r, c] = layer;
      rooms[r][c] = dist;

      addRoom(r+1, c)
      addRoom(r-1, c)
      addRoom(r, c+1)
      addRoom(r, c-1)
    }
    dist += 1;
  }
}

function encode(x: number, y: number) {
  return `${x},${y}`;
}
