function ThesisGradeForm(props) {
	const tableData = props.viewingSupervisor ? [
		{
			description: 'Problematika a cíl práce jsou zformulovány a odpovídají zadání a názvu práce.',
			weight: 1
		},
		{
			description: 'Metodika práce vede k naplnění cílů, je správně a logicky zvolená a kvalitně provedená.',
			weight: 3
		},
		{
			description: 'Autor se opírá o relevantní prameny a literaturu.',
			weight: 2
		},
		{
			description: 'Struktura práce je logická a vyvážená a předepsané části práce naplňují svůj účel i obsah.',
			weight: 4
		},
		{
			description: 'Práce je originální a obsahuje jednoznačně definovatelný vlastní přínos studenta zvolené tématice.',
			weight: 4
		},
		{
			description: 'Práce používá správnou odbornou terminologii, obrazový doprovod je kvalitní a odpovídá tématu.',
			weight: 1
		},
		{
			description: 'Formální stránka práce – autor správně cituje, má správně vedený seznam literatury, nic podstatného neopominul.',
			weight: 3
		},
		{
			description: 'Jazyková stránka práce.',
			weight: 2
		},
		{
			description: 'Grafická stránka práce (formátování). Hodnotí pověřený učitel.',
			weight: 2
		},
		{
			description: 'Cíle práce byly splněny.',
			weight: 4
		}
	] : [
		{
			description: 'Problematika a cíl práce jsou zformulovány a odpovídají zadání a názvu práce.',
			weight: 1
		},
		{
			description: 'Metodika práce vede k naplnění cílů, je správně a logicky zvolená a kvalitně provedená.',
			weight: 3
		},
		{
			description: 'Autor se opírá o relevantní prameny a literaturu.',
			weight: 2
		},
		{
			description: 'Struktura práce je logická a vyvážená a předepsané části práce naplňují svůj účel i obsah.',
			weight: 4
		},
		{
			description: 'Práce je originální a obsahuje jednoznačně definovatelný vlastní přínos studenta zvolené tématice.',
			weight: 4
		},
		{
			description: 'Práce používá správnou odbornou terminologii, obrazový doprovod je kvalitní a odpovídá tématu.',
			weight: 1
		},
		{
			description: 'Cíle práce byly splněny.',
			weight: 4
		}
	];

	function getWeightedMean() {
		let weightedMean = 0;
		let sumOfWeights = 0;

		for (let i = 0; i < tableData.length; i++) {
			weightedMean += props.grades[i] * tableData[i].weight;
			sumOfWeights += tableData[i].weight;
		}

		return Math.round(weightedMean / sumOfWeights);
	}

	function onGradeChange(event) {
		const target = event.target;
		const index = parseInt(target.id);
		let grade = parseInt(target.value);

		if (isNaN(grade)) {
			return;
		}

		if (grade < 0) {
			grade = 0;
		}
		if (grade > 100) {
			grade = 100;
		}

		const newGrades = [...props.grades];
		newGrades[index] = grade;

		props.setGrades(newGrades);
	}

	return (
		<div className="container mx-auto px-6 min-w-full">
			<div className="container flex justify-center min-w-full">
				<form id="thesis-grade-form" className="thesis-grade-form min-w-full" method="POST">
					<table id="thesis-grade-table" className="thesis-grade-table min-w-full">
						<thead>
							<tr>
								<th></th>
								<th>Hodnocení ročníkové práce</th>
								<th>Váha</th>
								<th>Známka</th>
							</tr>
						</thead>
						<tbody>
							{tableData.map((item, index) => (
								<tr key={index}>
									<td>{index + 1}</td>
									<td>{item.description}</td>
									<td>{item.weight}</td>
									<td className="flex items-center justify-center">
										{props.userCanEdit ?
											<>
												<input id={index} type="number" min="0" max="100" value={props.grades[index]} onChange={onGradeChange} />
												<span>&nbsp;%</span>
											</> :
											<span>{props.grades[index]} %</span>
										}
									</td>
								</tr>
							))}
						</tbody>
					</table>
					<div className="container mx-auto mt-4 text-center">
						<span className="weighted-mean">Výsledná známka (vážený průměr): {getWeightedMean()} %</span>
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