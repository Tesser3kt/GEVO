interface AddArticleFormProps {
  onSubmitClick: (heading: string, content: string) => void;
}

const AddArticleForm = ({ onSubmitClick }: AddArticleFormProps) => {
  let heading = "";
  let content = "";

  return (
    <div className="form-container">
      <form className="add-article-form">
        <label htmlFor="heading">Nadpis</label>
        <input
          id="heading"
          name="heading"
          type="text"
          className="heading"
          onChange={(e) => (heading = e.target.value)}
        />
        <label htmlFor="content">Obsah</label>
        <textarea
          name="content"
          id="content"
          cols={30}
          rows={10}
          onChange={(e) => (content = e.target.value)}
        ></textarea>
        <button
          type="submit"
          onClick={(e) => {
            e.preventDefault();
            onSubmitClick(heading, content);
          }}
        >
          Přidat
        </button>
      </form>
    </div>
  );
};

export default AddArticleForm;
