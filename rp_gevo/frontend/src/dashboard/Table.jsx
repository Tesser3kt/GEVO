import { useState } from 'react';
import FilterRow from './FilterRow';
import ThesisRow from './ThesisRow';
import unidecode from 'unidecode';

function Table({ userData, theses, onEditClick }) {
	const [filters, setFilters] = useState({
		'class': '',
		'student': '',
		'title': '',
		'supervisor-check': true,
		'supervisor': '',
		'opponent-check': true,
		'opponent': ''
	});

	function onFilterInputChange(event) {
		const target = event.target;
		const value = target.type === 'checkbox' ? target.checked : target.value;

		setFilters({
			...filters,
			[target.name]: value
		});
	}

	function userTheses() {
		if (userData.role === 'student') {
			return theses.authored;
		}
		if (userData.role === 'teacher') {
			let userTheses = [];
			if (filters['supervisor-check']) {
				userTheses = [...userTheses, ...theses.supervised];
			}
			if (filters['opponent-check']) {
				userTheses = [...userTheses, ...theses.opposed];
			}
			return userTheses;
		}
		if (userData.role === 'admin') {
			return [...theses.authored, ...theses.supervised, ...theses.opposed, ...theses.other];
		}
	}

	function decodedString(string) {
		return unidecode(string.toLowerCase());
	}

	function filterTheses(userTheses) {
		const filteredTheses = userTheses.filter(thesis => {
			return (
				decodedString(thesis.author_class).includes(decodedString(filters['class']))
				&& decodedString(thesis.author).includes(decodedString(filters['student']))
				&& decodedString(thesis.title).includes(decodedString(filters['title']))
				&& decodedString(thesis.supervisor).includes(decodedString(filters['supervisor']))
				&& decodedString(thesis.opponent).includes(decodedString(filters['opponent']))
			);
		});
		return filteredTheses;
	}

	return (
		<div className="container min-w-full px-10">
			<div id="theses-grid-container" className="container theses-grid-container my-8 min-w-full">
				<div className="theses-grid-head grid grid-cols-6 grid-rows-1 gap-x-8 min-w-full">
					<span>Třída</span>
					<span>Student</span>
					<span>Název</span>
					<span>Vedoucí</span>
					<span>Oponent</span>
					<span>Rok práce</span>
				</div>
				<div className="theses-grid-filter grid grid-cols-1 grid-rows-1">
					<FilterRow
						userRole={userData.role}
						filters={filters}
						onFilterInputChange={onFilterInputChange}
					/>
				</div>
				<div className="theses-grid-body grid grid-cols-1 auto-rows-fr gap-y-6">
					{filterTheses(userTheses()).map(thesis => {
						return (
							<ThesisRow
								key={thesis.id}
								thesisData={thesis}
								onEditClick={onEditClick}
							/>
						);
					})}
				</div>
			</div>
		</div>
	)
}

export default Table;