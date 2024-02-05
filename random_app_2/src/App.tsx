import { useState } from "react";
import "./App.css";

function App() {
  const title = "Random Title";
  const content = "lkqkwdndlqwn ekjqehi u`3iu3g p73f 93g ug";
  const [list, setList] = useState([
    {
      name: "vec jedna",
      crossedOut: false,
    },
    {
      name: "vec dva",
      crossedOut: true,
    },
    {
      name: "vec tri",
      crossedOut: false,
    },
  ]);

  return (
    <>
      <h1 className="text-xl font-bold">{title}</h1>
      <p>{content}</p>
      <ul>
        {list.map(({ name, crossedOut }, index) => (
          <li
            className={
              crossedOut ? "cursor-pointer line-through" : "cursor-pointer"
            }
            key="index"
            onClick={() =>
              console.log("Item " + index.toString() + " clicked.")
            }
          >
            {name}
          </li>
        ))}
      </ul>
    </>
  );
}

export default App;
