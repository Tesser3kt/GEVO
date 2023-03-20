import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

function Index() {
	const navigate = useNavigate();

	useEffect(() => {
		fetch('/api/current-user', {
			method: 'GET',
			headers: { 'Content-Type': 'application/json' }
		}).then(res => {
			if (res.ok) {
				return res.json();
			}
		}).then(data => {
			if (data.id) {
				const state = {
					userData: data
				};
				navigate('/dashboard', { state: state });
			}
			else {
				navigate('/login');
			}
		}).catch(err => {
			console.log(err);
		});
	}, [navigate]);

	return null;
}

export default Index;