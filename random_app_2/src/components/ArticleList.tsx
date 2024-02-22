import Article from "./Article";

interface ArticleType {
  id: number;
  heading: string;
  content: Array<string>;
  likes: number;
}
interface ArticleListProps {
  articles: Array<ArticleType>;
  onLikeButtonClick: (id: number) => void;
  onDeleteButtonClick: (id: number) => void;
}

const ArticleList = ({
  articles,
  onLikeButtonClick,
  onDeleteButtonClick,
}: ArticleListProps) => {
  return (
    <div className="article-list m-auto max-w-screen-lg">
      {articles.map((article) => (
        <Article
          key={article.id}
          id={article.id}
          heading={article.heading}
          content={article.content}
          likes={article.likes}
          onLikeButtonClick={onLikeButtonClick}
          onDeleteButtonClick={onDeleteButtonClick}
        />
      ))}
    </div>
  );
};

export default ArticleList;
