/**
[[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
 */

function insert(intervals: number[][], newInterval: number[]): number[][] {
  const jak: number[][] = [];
  let i = 0;

  // push into new array any intervals lower and not conflicting with newInterval
  while (i < intervals.length && intervals[i][1] < newInterval[0]) {
      jak.push(intervals[i]);
      i++;
  }

  // while current interval start time <= new interval end time
  while (i < intervals.length && intervals[i][0] <= newInterval[1]) {
    // reassign newInterval to take:
    // [ min of new interval start time or current interval start time,
    // max of new interval end time or current interval start time
      newInterval = [
          Math.min(newInterval[0], intervals[i][0]),
          Math.max(newInterval[1], intervals[i][1])
      ];
      i++;
  }
  jak.push(newInterval);

  // push in remainder of intervals higher than newInterval and not conflicting
  while (i < intervals.length) {
      jak.push(intervals[i]);
      i++;
  }

  return jak;
};
