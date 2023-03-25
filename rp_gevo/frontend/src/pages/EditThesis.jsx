import { useState } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';

import Header from '../dashboard/Header';
import Title from '../thesis-editor/Title';
import Navbar from '../thesis-editor/Navbar';
import ThesisEditor from '../thesis-editor/ThesisEditor';

function EditThesis() {
	const navigate = useNavigate();
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

	function onTabClick(event) {
		event.stopPropagation();
		const target = event.target;
		if (!target.id) {
			return;
		}
		if (target.className.includes('disabled')) {
			return;
		}

		const tabId = parseInt(target.id);
		setOpenTab(tabId);
	}

	const { state } = useLocation();
	const userData = state.userData;
	const thesisData = state.thesisData;
	const userJob = state.userJob;

	const enabledTabs = {
		supervisor: userJob === 'supervisor' || userData.role === 'admin',
		opponent: userJob === 'opponent' || userData.role === 'admin'
	}
	let defaultOpenTab = null;
	if (enabledTabs.opponent) {
		defaultOpenTab = 2;
	}
	if (enabledTabs.supervisor) {
		defaultOpenTab = 1;
	}
	const [openTab, setOpenTab] = useState(defaultOpenTab);

	if (!enabledTabs.supervisor && !enabledTabs.opponent) {
		const state = {
			message: "Nemáte oprávnění k zobrazení posudků.",
			err: "Ani jeden z autorů posudků jej nezveřejnil."
		}
		navigate('/error', { state: state, replace: true });
	}

	const [title, setTitle] = useState(thesisData.title);
	const [supervisor, setSupervisor] = useState(thesisData.supervisor);
	const [opponent, setOpponent] = useState(thesisData.opponent);
	const [newThesisData, setNewThesisData] = useState(thesisData);

	const [grades, setGrades] = useState([0, 0, 0, 0, 0, 0, 0, 0, 0]);

	const [review, setReview] = useState('');

	const [questions, setQuestions] = useState([]);

	return (
		<>
			<Header userName={userData?.name} onLogout={onLogout} />
			<Title thesisTitle={title} />
			<Navbar openTab={openTab} enabledTabs={enabledTabs} onTabClick={onTabClick} />
			<ThesisEditor
				userData={userData}
				userJob={userJob}
				openTab={openTab}
				thesisData={thesisData}
				title={title}
				setTitle={setTitle}
				supervisor={supervisor}
				setSupervisor={setSupervisor}
				opponent={opponent}
				setOpponent={setOpponent}
				newThesisData={newThesisData}
				setNewThesisData={setNewThesisData}
				grades={grades}
				setGrades={setGrades}
				review={review}
				setReview={setReview}
				questions={questions}
				setQuestions={setQuestions}
			/>
		</>
	)
}

export default EditThesis;