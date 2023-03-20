function ThesisRow({ thesisData, onEditClick }) {
	function getTitleExcerpt() {
		const title = thesisData.title;
		if (title.length > 20) {
			return title.substring(0, 20) + '...';
		}
		return title;
	}

	function getNameShorter(name) {
		if (name.length < 2) {
			return name;
		}

		const nameArray = name.split(' ');
		if (nameArray.length === 3) {
			return nameArray[0].substring(0, 1) + '. ' + nameArray[1].substring(0, 1) + '. ' + nameArray[2];
		}
		else {
			return nameArray[0].substring(0, 1) + '. ' + nameArray[1];
		}
	}

	return (
		<div id={thesisData.id} className="thesis-row grid grid-rows-1 grid-cols-6 gap-x-8 items-center" onClick={onEditClick}>
			<div className="thesis-row-item">{thesisData.author_class}</div>
			<div className="thesis-row-item">{getNameShorter(thesisData.author)}</div>
			<div className="thesis-row-item">{getTitleExcerpt()}</div>
			<div className="thesis-row-item">{getNameShorter(thesisData.supervisor)}</div>
			<div className="thesis-row-item">{getNameShorter(thesisData.opponent)}</div>
			<div className="thesis-row-item">{thesisData.academic_year}</div>
		</div>
	);
}

export default ThesisRow;