import { useEffect } from 'react';

function AutoSaveQuestions({ thesisId, userFrom, questions }) {
	useEffect(() => {
		const timer = setTimeout(() => {
			fetch('/api/thesis-questions', {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({
				id: thesisId,
				from: userFrom,
				questions: questions
			})
		}).then((res) => {
			if (!res.ok) {
				console.log('Chyba při automatickém ukládání otázek.');
			}
		}).catch((err) => {
			console.log('Chyba při automatickém ukládání otázek.');
		});
	}, 5000);
		return () => clearTimeout(timer);
	}, [thesisId, userFrom, questions]);
}

export default AutoSaveQuestions;