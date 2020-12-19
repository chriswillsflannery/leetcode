/*

PROVIDED:
1) You will be given an array of objects

THE TASK:
1) Please write a function named `generateGreeting` 
2) The function must take in an Array as a parameter
3) The function will return a NEW Array of objects
4) Each object within the new Array must have a new property with the label `greeting`
5) The value of `greeting` will be the following string:

Hi <firstName here>, what do you like the most about <language here>?

6) Make sure to inject the proper values for `firstName` and `language`

*/

// Array of meeting attendees
const attendees = [
  {
    firstName: "John",
    lastName: "Snow",
    house: "Stark",
    age: 35,
    language: "Java",
  },
  {
    firstName: "Cersei",
    lastName: "Lannister",
    house: "Lannister",
    continent: "Europe",
    age: 35,
    language: "Python",
  },
  {
    firstName: "Aerys",
    lastName: "Targaryen",
    house: "Targaryen",
    age: 32,
    language: "Ruby",
  },
];

function generateGreeting(array) {
  return array.map((obj) => {
    return {
      greeting: `Hi ${obj.firstName}, what do you like the most about ${obj.language}?`,
    };
  });
}

console.log(generateGreeting(attendees));
