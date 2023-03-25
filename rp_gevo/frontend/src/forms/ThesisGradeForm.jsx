function ThesisGradeForm(props) {
	const tableData = props.viewingSupervisor ? [
		{
			description: 'Úvod',
			points: 5
		},
		{
			description: 'Literární rešerše',
			points: 5
		},
		{
			description: 'Metoda',
			points: 5
		},
		{
			description: 'Analýza',
			points: 5
		},
		{
			description: 'Zhodnocení',
			points: 5
		},
		{
			description: 'Jazyk',
			points: 3
		},
		{
			description: 'Citace',
			points: 2
		},
		{
			description: 'Formátování',
			points: 2
		},
		{
			description: 'Logická struktura',
			points: 3
		}
	] : [
		{
			description: 'Úvod',
			points: 5
		},
		{
			description: 'Literární rešerše',
			points: 5
		},
		{
			description: 'Metoda',
			points: 5
		},
		{
			description: 'Analýza',
			points: 5
		},
		{
			description: 'Zhodnocení',
			points: 5
		},
		{
			description: 'Jazyk',
			points: 3
		},
		{
			description: 'Citace',
			points: 2
		},
		{
			description: 'Formátování',
			points: 2
		},
		{
			description: 'Logická struktura',
			points: 3
		}
	];

	function getTotalPoints() {
		return props.grades.reduce((total, item) => total + item, 0);
	}

	function onGradeChange(event) {
		const target = event.target;
		const index = parseInt(target.id);
		const maxPoints = tableData[index].points;
		let grade = parseInt(target.value);

		if (isNaN(grade)) {
			return;
		}

		if (grade < 0) {
			grade = 0;
		}
		if (grade > maxPoints) {
			grade = maxPoints;
		}

		const newGrades = [...props.grades];
		newGrades[index] = grade;

		props.setGrades(newGrades);
	}

	return (
		<div className="container mx-auto px-6 w-3/5">
			<div className="container flex justify-center min-w-full">
				<form id="thesis-grade-form" className="thesis-grade-form min-w-full" method="POST">
					<table id="thesis-grade-table" className="thesis-grade-table min-w-full">
						<thead>
							<tr>
								<th></th>
								<th>Hodnocení ročníkové práce</th>
								<th>Max. bodů</th>
								<th>Body</th>
							</tr>
						</thead>
						<tbody>
							{tableData.map((item, index) => (
								<tr key={index}>
									<td>{index + 1}</td>
									<td>{item.description}</td>
									<td>{item.points}</td>
									<td className="flex items-center justify-center">
										{props.userCanEdit ?
											<>
												<input id={index} type="number" min="0" max="100" value={props.grades[index]} onChange={onGradeChange} />
											</> :
											<span>{props.grades[index]}</span>
										}
									</td>
								</tr>
							))}
						</tbody>
					</table>
					<div className="container mx-auto mt-4 text-center">
						<span className="weighted-mean">Celkem bodů: {getTotalPoints()}</span>
					</div>
					<div className="container mt-8 flex flex-col justify-center items-center min-w-full">
						{(props.editStatus === 'success' && props.showEditMessage) &&
							<p className="edit-status-message mb-4 text-green-500">{props.editStatusMessage}</p>
						}
						{(props.editStatus === 'failure' && props.showEditMessage) &&
							<p className="edit-status-message mb-4 text-red-500">{props.editStatusMessage}</p>
						}
						{props.userCanEdit &&
							<button className="btn save-edits-button p-2 w-52 rounded-md" type="submit" onClick={props.onSaveButtonClick}>Uložit změny</button>
						}
					</div>
				</form>
			</div>
		</div>
	)
}

export default ThesisGradeForm;