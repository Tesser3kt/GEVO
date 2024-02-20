import Article from "./Article";

interface ArticleType {
  id: number;
  heading: string;
  content: Array<string>;
  likes: number;
}
interface ArticleListProps {
  articles: Array<ArticleType>;
}

const ArticleList = ({ articles }: ArticleListProps) => {
  return (
    <div className="article-list m-auto max-w-screen-lg">
      {articles.map((article) => (
        <Article
          id={article.id}
          heading={article.heading}
          content={article.content}
          likes={article.likes}
        />
      ))}
    </div>
  );
};

export default ArticleList;
