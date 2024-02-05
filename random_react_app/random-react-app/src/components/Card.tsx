import { ChangeEventHandler } from "react";

interface CardProps {
  title: string;
  content: string;
  author: string;
  date: string;
  done: boolean;
  onDoneClick: ChangeEventHandler;
}

const Card = ({
  title,
  content,
  author,
  date,
  done,
  onDoneClick,
}: CardProps) => {
  const cardContainerBg: string = done ? " bg-green-500/50" : " bg-red-500/50";
  return (
    <div
      className={
        "event-card-container max-width-md border border-white rounded-md p-3 border-opacity-30 shadow-sm shadow-gray-400" +
        cardContainerBg
      }
    >
      <div className="event-card">
        <h3 className="mb-2 text-2xl font-bold">{title}</h3>
        <div className="card-content">{content}</div>
        <div className="mt-2 author-date flex justify-between text-gray-100">
          <span className="author">{author}</span>
          <span className="date">{date}</span>
        </div>
        <div className="status">
          <span>Hotovo?</span>
          <input type="checkbox" defaultChecked={done} onChange={onDoneClick} />
        </div>
        <button className="border border-red rounded-md p-4 border-opacity-30 bg-emerald-700/30">
          Odebrat
        </button>
      </div>
    </div>
  );
};

export default Card;
