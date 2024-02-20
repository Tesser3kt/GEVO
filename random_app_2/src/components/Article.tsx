interface ArticleProps {
  id: number;
  heading: string;
  content: Array<string>;
  likes: number;
}

const Article = ({ id, heading, content, likes }: ArticleProps) => {
  return (
    <div className="article-container bg-blue-400 pt-3 mt-8 rounded-lg">
      <div key={id} className="article p-6 shadow-sm rounded-lg bg-gray-50">
        <h3 className="w-1/3 p-2 font-bold text-xl border-b border-gray-400">
          {heading}
        </h3>
        {content.map((par, index) => (
          <p key={index} className="mt-4 text-justify">
            {par}
          </p>
        ))}
        <p className="text-right mt-2 italic">Počet liků: {likes}</p>
      </div>
    </div>
  );
};

export default Article;
