import { useState } from "react";
import Card from "./Card";

const CardList = () => {
	const handleDoneClick = (index: number) => {
		const newCards = cards;
		for (let i = 0; i < cards.length; i++) {
			const card = cards[i];
			if (i === index) {
				card.done = !card.done;
			}
			newCards[i] = card;
		}
		setCards(newCards);
	}

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
