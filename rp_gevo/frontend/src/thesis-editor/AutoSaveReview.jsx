import { useEffect } from 'react';

function AutoSaveReview({ thesisId, userFrom, review }) {
	useEffect(() => {
		const timer = setTimeout(() => {
			fetch('/api/thesis-review', {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({
				id: thesisId,
				from: userFrom,
				review: review
			})
		}).then((res) => {
			if (!res.ok) {
				console.log('Chyba při automatickém ukládání slovního hodnocení.');
			}
		}).catch((err) => {
			console.log('Chyba při automatickém ukládání slovního hodnocení.');
		});
	}, 5000);
		return () => clearTimeout(timer);
	}, [thesisId, userFrom, review]);
}

export default AutoSaveReview;