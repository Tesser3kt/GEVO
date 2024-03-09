interface ButtonProps {
  id: number;
  text: string;
  color: string;
  onClick: (e: React.SyntheticEvent) => void;
}

const Button = ({ id, text, color, onClick }: ButtonProps) => {
  return (
    <button
      id={id.toString()}
      className="button bg-red-100 py-2 px-4 rounded-md ring ring-red-400 hover:bg-red-200"
      onClick={(e) => onClick(e)}
    >
      {text}
    </button>
  );
};

export default Button;
