import { useState } from "react";
import Card from "./Card";

const CardList = () => {
  const handleDoneClick = (index: number) => {
    console.log("Switching card " + index + " to " + !cards[index].done);
    setCards((cards) => {
      const newCards = [...cards];
      newCards[index] = {
        ...cards[index],
        done: !cards[index].done,
      };
      return newCards;
    });
  };

  const [cards, setCards] = useState([
    {
      title: "Tit(s)-kulkus💀",
      content: "OᴡO ᴛᴏʜʟᴇ ᴊᴇ ᴅᴏᴄᴇʟᴀ ᴋᴏɴᴛᴇɴᴛ ᴋᴀʀᴛɪčᴋʏ ᴜᴡᴜ",
      author: "Aďa Klepajznů",
      date: "6. 9. 4269",
      done: false,
    },
    {
      title: "Tit(s)-kulkus💀",
      content: "OᴡO ᴛᴏʜʟᴇ ᴊᴇ ᴅᴏᴄᴇʟᴀ ᴋᴏɴᴛᴇɴᴛ ᴋᴀʀᴛɪčᴋʏ ᴜᴡᴜ",
      author: "Aďa Klepajznů",
      date: "6. 9. 4269",
      done: true,
    },
  ]);

  return (
    <div className="cards-container">
      {cards.map((card, index) => (
        <Card
          key={index}
          title={card.title}
          content={card.content}
          author={card.author}
          date={card.date}
          done={card.done}
          onDoneClick={() => handleDoneClick(index)}
        />
      ))}
    </div>
  );
};

export default CardList;
