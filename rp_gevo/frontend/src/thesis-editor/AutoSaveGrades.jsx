import { useEffect } from 'react';

function AutoSaveGrades({ thesisId, userFrom, grades }) {
	useEffect(() => {
		const timer = setTimeout(() => {
			fetch('/api/thesis-evaluation', {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({
				id: thesisId,
				from: userFrom,
				grades: grades
			})
		}).then((res) => {
			if (!res.ok) {
				console.log('Chyba při automatickém ukládání hodnocení.');
			}
		}).catch((err) => {
			console.log('Chyba při automatickém ukládání hodnocení.');
		});
	}, 5000);
		return () => clearTimeout(timer);
	}, [thesisId, userFrom, grades]);
}

export default AutoSaveGrades;