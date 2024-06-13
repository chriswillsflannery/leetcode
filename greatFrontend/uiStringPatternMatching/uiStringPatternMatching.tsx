/*

React challenge.
For each of the above items, we want to render a JSX element.
The JSX element should display the name and description of the item.
If any of the terms in the description of the item match any of the terms above,
that term should be rendered in the UI with an underline, and when the user
hovers on that item, a dialogue box should appear which shows the description of the item.

*/

import React from "react";
import "./App.css";

const terms = {
  brownie: "A delicious dessert made with chocolate and nuts",
  "root beer":
    "A sweet, carbonated beverage made from the root of the sassafras tree",
  chocolate: "A sweet, brown food made from cacao seeds",
  tempura:
    "A Japanese dish of seafood or vegetables that have been battered and deep-fried",
  mondo: "A large or great thing",
};

const items = [
  {
    id: "1",
    name: "Maine Root-Beer",
    description: "A classic root beer made with fair trade sugar.",
  },
  {
    id: "2",
    name: "Tempura layered Brownie",
    description: "A delicious brownie covered in a tempura layer",
  },
];

const Tooltip = ({ description, children }) => {
  return (
    <span className="tooltip">
      {children}
      <span className="tooltiptext">{description}</span>
    </span>
  );
};

const processDescription = (
  description,
  terms
): (React.JSX.Element | string)[] => {
  const termKeys = Object.keys(terms);
  const parts: (React.JSX.Element | string)[] = [];
  let lastIndex = 0;

  termKeys.forEach((term) => {
    // match whole term, case insensitive
    const regex = new RegExp(`\\b${term}\\b`, "gi");
    let match = regex.exec(description);

    while (match !== null) {
      const before = description.slice(lastIndex, match.index);
      if (before) parts.push(before);
      parts.push(<Tooltip description={terms[term]}>{match[0]}</Tooltip>);
      lastIndex = regex.lastIndex;
      match = regex.exec(description);
    }
  });

  parts.push(description.slice(lastIndex));

  return parts;
};

const Item = ({ item }) => {
  const { name, description } = item;

  const processedDescription = processDescription(description, terms);

  return (
    <div className="item">
      <h2>{name}</h2>
      <p>{processedDescription}</p>
    </div>
  );
};

const App = () => {
  return (
    <div className="app">
      {items.map((item) => (
        <Item item={item} />
      ))}
    </div>
  );
};

export default App;
