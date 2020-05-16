
/*
Write a function called dayMapper. It will accept three parameters: arr (bitcoinData), property1, property2.
It should use map to return a new array of objects with only the passed in properties on each object.
If the passed in properties are not present in arr's objects, then it should ignore that property name and it should not appear in the returned array.
*/

function dayMapper(arr, ...properties) {
  return arr.map(day => {
    const newDay = {};
    properties.forEach(prop => {
      if (day.hasOwnProperty(prop)) {
        newDay[prop] = day[prop];
      }
    });
    return newDay;
  });
}

// console.log(dayMapper(bitcoinData, 'date', 'price(USD)'));

/*
averageValueOf________ (follow up to challenge 7)
for each property that has numeric values in bitcoin data, write a function that takes in an array (bitcoinData in this case) and a property name and will return the property's average value in the array.
*/

function getAverageValue(arr, prop) {
  const total = arr.reduce((acc, cur) => {
    acc += cur[prop];
    return acc;
  }, 0);
  return Math.floor(total / arr.length);
}

function getAveragesForEachNumericProp(day) {
  const totals = {};
  for (let key in day) {
    if (typeof day[key] === 'number') {
      totals[key] = getAverageValue(bitcoinData, key);
    }
  }
  return totals;
}

console.log(getAveragesForEachNumericProp(bitcoinData[0]));
