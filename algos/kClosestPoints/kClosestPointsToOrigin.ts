// given an array of points [x,y] on a grid
// and given a K int
// return the K closest points to the origin [0,0]

/**
 input [[1,3],[-2,2]]
 k = 1

 euclydian distance : d =√[(x2 – x1)2 + (y2 – y1)2]
 distance bt (1,3) and origin is sqrt(10)
 √[1 – 0)2 + (3 – 0)2]
  √[1 + 9]

 distance bt (-2,2) and origin is sqrt(8)
  √[-2)2 + (2)2]
  √[4 + 4]

  [-2,2] is closer to the origin since sqrt(8) is smaller val.
 */

  function getEuclideanDist(x1: number, y1: number, x2: number, y2: number) {
    const difOfXs = x1 - x2;
    const difOfYs = y1 - y2;
  
    const additionOfDiffs = (difOfXs * difOfXs) + (difOfYs * difOfYs);
    return Math.sqrt(additionOfDiffs);
  }
  
  type PointsByDist = Map<number[], number>;
  
  function kClosest(points: number[][], k: number): number[][] {
  
    const pointsByDist: PointsByDist = new Map();
    points.forEach(point => {
      pointsByDist.set(point, getEuclideanDist(point[0], point[1], 0, 0));
    });

    const keyValueArray = Array.from(pointsByDist.entries());
    keyValueArray.sort((a, b) => a[1] - b[1]);
  
  
    const closestPoints: number[][] = [];
    for (let i = 0; i < k; i++) {
      closestPoints.push(keyValueArray[i][0]);
    }
    return closestPoints;
  
  }

