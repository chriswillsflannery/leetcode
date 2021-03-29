// Filter movie list by average rating, name.
// Sort filtered list by any field inside movie object

const movies = [
  {
    name: 'Sharknado',
    rating: 10,
    blurb: 'sharks and tornados',
  },
  {
    name: 'Casino Royale',
    rating: 4,
    blurb: 'something vegas - bond',
  },
];

const fourOrHigher = movies.filter(movie => movie.rating >= 4);
const sortLowToHigh = fourOrHigher.sort((a,b) => {
  if (a.rating > b.rating) return 1;
  if (b.rating > a.rating) return -1;
  return 0;
});
console.log(sortLowToHigh);