import { useState, useEffect } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';

import Header from '../dashboard/Header';
import Table from '../dashboard/Table';

function Dashboard() {
	const navigate = useNavigate();
	const { state } = useLocation();
	const [theses, setTheses] = useState({
		authored: [],
		supervised: [],
		opposed: [],
		other: []
	});

	function onLogout() {
		fetch('/api/logout', {
			method: 'GET',
			headers: { 'Content-Type': 'application/json' }
		}).then((res) => {
			if (res.status === 200) {
				console.log('Logout successful');
				navigate('/', { replace: true });
			} else {
				const state = {
					message: "Odhlášení se nezdařilo.",
					err: res.statusText + ' (' + res.status + ')'
				};
				navigate('/error', { state: state, replace: true });
			}
		});
	}

	function onEditClick(event) {
		const target = event.target;
		let thesisId = null;
		if (target.id) {
			thesisId = parseInt(target.id);
		} else {
			thesisId = parseInt(target.parentElement.id);
		}

		if (!thesisId) {
			return;
		}

		let thesisById = null;
		let userJob = null;
		if (userData.role === 'student') {
			thesisById = theses.authored.find((thesis) => thesis.id === thesisId);
			userJob = 'author';
		} else if (userData.role === 'teacher') {
			thesisById = [...theses.supervised, ...theses.opposed].find((thesis) => thesis.id === thesisId);
			if (thesisById.supervisor_id === userData.id) {
				userJob = 'supervisor';
			} else {
				userJob = 'opponent';
			}
		} else if (userData.role === 'admin') {
			thesisById = [...theses.authored, ...theses.supervised, ...theses.opposed, ...theses.other].find((thesis) => thesis.id === thesisId);
			if (thesisById.author_id === userData.id) {
				userJob = 'author';
			} else if (thesisById.supervisor_id === userData.id) {
				userJob = 'supervisor';
			} else if (thesisById.opponent_id === userData.id) {
				userJob = 'opponent';
			} else {
				userJob = 'viewer';
			}
		}

		if (!thesisById) {
			const state = {
				message: "Práce nebyla nalezena.",
				err: "Práce s ID " + thesisId + " neexistuje.",
			};
			navigate('/error', { state: state, replace: true });
			return;
		}

		const state = {
			thesisData: thesisById,
			userData: userData,
			userJob: userJob
		}
		navigate('/edit/' + thesisId, { state: state });
	}

	useEffect(() => {
		if (!state) {
			navigate('/', { replace: true });
		} else {
			fetch('/api/theses', {
				method: 'GET',
				headers: { 'Content-Type': 'application/json' }
			}).then((res) => {
				if (res.ok) {
					return res.json();
				} else {
					const state = {
						message: "Nepodařilo se načíst seznam prací.",
						err: res.statusText + ' (' + res.status + ')',
					};
					navigate('/error', { state: state, replace: true });
				}
			}).then((data) => {
				setTheses(data);
			});
		}
	}, [state, navigate, setTheses]);

	if (!state) {
		return null;
	}
	const userData = state.userData;

	return (
		<>
			<Header userName={userData?.name} onLogout={onLogout} />
			<Table userData={userData} theses={theses} onEditClick={onEditClick} />
		</>
	);
}

export default Dashboard;