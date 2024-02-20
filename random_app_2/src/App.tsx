import { useState } from "react";
import "./App.css";
import ArticleList from "./components/ArticleList";

function App() {
  const totalLikes = () => {
    let total = 0;
    articles.forEach((article) => {
      total += article.likes;
    });

    return total;
  };

  const [articles, setArticles] = useState([
    {
      id: 1,
      heading: "Heading 1",
      content: [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nisl tincidunt eget nullam non nisi est sit. Amet tellus cras adipiscing enim eu. Nisl vel pretium lectus quam id leo in vitae turpis. Vitae et leo duis ut diam quam. Morbi tincidunt ornare massa eget egestas purus viverra accumsan. Turpis in eu mi bibendum neque egestas congue quisque. Est velit egestas dui id ornare arcu odio ut. Ornare suspendisse sed nisi lacus sed. Cras semper auctor neque vitae. Vulputate enim nulla aliquet porttitor lacus luctus accumsan. Lacus laoreet non curabitur gravida. Sit amet consectetur adipiscing elit pellentesque. Tristique risus nec feugiat in fermentum posuere urna nec.",
        "Dignissim cras tincidunt lobortis feugiat vivamus at augue. Quam adipiscing vitae proin sagittis nisl rhoncus mattis rhoncus. Amet justo donec enim diam vulputate ut. Non curabitur gravida arcu ac tortor. In est ante in nibh. Eu turpis egestas pretium aenean pharetra magna ac. Vestibulum morbi blandit cursus risus at ultrices mi tempus. Id aliquet risus feugiat in ante metus. Ultrices vitae auctor eu augue ut lectus. Fringilla urna porttitor rhoncus dolor purus non enim praesent elementum. Pellentesque massa placerat duis ultricies.",
      ],
      likes: 3,
    },
    {
      id: 2,
      heading: "Heading 2",
      content: [
        "Gravida cum sociis natoque penatibus et magnis dis parturient montes. Augue interdum velit euismod in pellentesque massa. Magna eget est lorem ipsum dolor sit. Potenti nullam ac tortor vitae. Nisl nunc mi ipsum faucibus vitae. Habitasse platea dictumst vestibulum rhoncus est pellentesque elit. Sed nisi lacus sed viverra tellus in hac habitasse. Netus et malesuada fames ac turpis egestas integer eget aliquet. Metus vulputate eu scelerisque felis. Lectus magna fringilla urna porttitor rhoncus dolor.",
        "Turpis egestas integer eget aliquet nibh praesent tristique. Aliquet sagittis id consectetur purus ut faucibus pulvinar elementum. Ut tortor pretium viverra suspendisse potenti nullam ac tortor. Urna nunc id cursus metus aliquam eleifend mi in. Augue lacus viverra vitae congue eu consequat ac felis donec. Odio ut sem nulla pharetra diam sit amet nisl suscipit. Convallis a cras semper auctor neque vitae. Elit at imperdiet dui accumsan sit. Egestas integer eget aliquet nibh praesent tristique. Sed pulvinar proin gravida hendrerit. Volutpat consequat mauris nunc congue. Tincidunt lobortis feugiat vivamus at. Facilisis magna etiam tempor orci eu lobortis elementum nibh. Posuere ac ut consequat semper. Habitasse platea dictumst quisque sagittis. Eget aliquet nibh praesent tristique magna sit. Justo donec enim diam vulputate. Volutpat sed cras ornare arcu dui vivamus arcu felis bibendum. Aliquet eget sit amet tellus cras.",
      ],
      likes: 6,
    },
  ]);

  const title = "Články";
  const subtitle = "Liky: " + totalLikes().toString();

  return (
    <div className="app p-8 min-w-full min-h-screen">
      <header className="header">
        <h1 className="text-center text-3xl font-bold">{title}</h1>
        <h2 className="text-center text-xl text-gray-600">({subtitle})</h2>
      </header>
      <ArticleList articles={articles} />
    </div>
  );
}

export default App;
