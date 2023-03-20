import { useState, useEffect, useCallback } from 'react';
import { useNavigate } from 'react-router-dom';

import EditorNavigation from './EditorNavigation';
import ThesisMainForm from '../forms/ThesisMainForm';
import ThesisGradeForm from '../forms/ThesisGradeForm';
import ThesisReviewForm from '../forms/ThesisReviewForm';
import ThesisQuestionsForm from '../forms/ThesisQuestionsForm';
import CreatePDFForm from '../forms/CreatePDFForm';

import AutoSaveGrades from './AutoSaveGrades';
import AutoSaveReview from './AutoSaveReview';
import AutoSaveQuestions from './AutoSaveQuestions';

function ThesisEditor(props) {
	const { userData,
		userJob,
		openTab,
		thesisData,
		title,
		setTitle,
		supervisor,
		setSupervisor,
		opponent,
		setOpponent,
		newThesisData,
		setNewThesisData,
		grades,
		setGrades,
		review,
		setReview,
		questions,
		setQuestions
	} = props;

	const navigate = useNavigate();
	const [active, setActive] = useState(1);

	const [editStatus, setEditStatus] = useState({
		basicData: 'none',
		grade: 'none',
		review: 'none',
		questions: 'none',
		pdf: 'none'
	});
	const [editStatusMessage, setEditStatusMessage] = useState({
		basicData: '',
		grade: '',
		review: '',
		questions: '',
		pdf: ''
	});
	const [showEditMessage, setShowEditMessage] = useState({
		basicData: false,
		grade: false,
		review: false,
		questions: false,
		pdf: false
	});

	const canEditStuff = (userData.id === thesisData.supervisor_id && openTab === 1) ||
		(userData.id === thesisData.opponent_id && openTab === 2);
	const userFrom = openTab === 1 ? 'supervisor' : 'opponent';

	const getGrades = useCallback((dataFor) => {
		fetch('/api/thesis-evaluation?' + new URLSearchParams({
			'id': newThesisData.id,
			'for': dataFor
		})).then((res) => {
			if (res.ok) {
				return res.json();
			} else {
				const state = {
					'message': 'Hodnocení se nepodařilo načíst.',
					'error': res.statusText + ' (' + res.status + ')'
				};
				navigate('/error', { state: state, replace: true });
			}
		}).then((data) => {
			if (data) {
				if (data.success) {
					setGrades(data.grades);
				} else {
					const state = {
						'message': 'Hodnocení se nepodařilo načíst.',
						'error': data.message
					};
					navigate('/error', { state: state, replace: true });
				}
			} else {
				const state = {
					'message': 'Hodnocení se nepodařilo načíst.',
					'error': 'Chybná odpověď serveru.'
				};
				navigate('/error', { state: state, replace: true });
			}
		}).catch((err) => {
			const state = {
				'message': 'Hodnocení se nepodařilo načíst.',
				'error': err.message
			};
			navigate('/error', { state: state, replace: true });
		});
	}, [newThesisData.id, navigate, setGrades]);

	const getReview = useCallback((dataFor) => {
		fetch('/api/thesis-review?' + new URLSearchParams({
			'id': newThesisData.id,
			'for': dataFor
		})).then((res) => {
			if (res.ok) {
				return res.json();
			} else {
				const state = {
					'message': 'Slovní hodnocení se nepodařilo načíst.',
					'error': res.statusText + ' (' + res.status + ')'
				};
				navigate('/error', { state: state, replace: true });
			}
		}).then((data) => {
			if (data) {
				if (data.success) {
					setReview(data.review);
				} else {
					const state = {
						'message': 'Slovní hodnocení se nepodařilo načíst.',
						'error': data.message
					};
					navigate('/error', { state: state, replace: true });
				}
			} else {
				const state = {
					'message': 'Slovní hodnocení se nepodařilo načíst.',
					'error': 'Chybná odpověď serveru.'
				};
				navigate('/error', { state: state, replace: true });
			}
		}).catch((err) => {
			const state = {
				'message': 'Recenze se nepodařilo načíst.',
				'error': err.message
			};
			navigate('/error', { state: state, replace: true });
		});
	}, [newThesisData.id, navigate, setReview]);

	const getQuestions = useCallback((dataFor) => {
		fetch('/api/thesis-questions?' + new URLSearchParams({
			'id': newThesisData.id,
			'for': dataFor
		})).then((res) => {
			if (res.ok) {
				return res.json();
			} else {
				const state = {
					'message': 'Otázky k obhajobě se nepodařilo načíst.',
					'error': res.statusText + ' (' + res.status + ')'
				};
				navigate('/error', { state: state, replace: true });
			}
		}).then((data) => {
			if (data) {
				if (data.success) {
					setQuestions(data.questions);
				} else {
					const state = {
						'message': 'Otázky k obhajobě se nepodařilo načíst.',
						'error': data.message
					};
					navigate('/error', { state: state, replace: true });
				}
			} else {
				const state = {
					'message': 'Otázky k obhajobě se nepodařilo načíst.',
					'error': 'Chybná odpověď serveru.'
				};
				navigate('/error', { state: state, replace: true });
			}
		}).catch((err) => {
			const state = {
				'message': 'Otázky k obhajobě se nepodařilo načíst.',
				'error': err.message
			};
			navigate('/error', { state: state, replace: true });
		});
	}, [newThesisData.id, navigate, setQuestions]);

	function commitBasicData() {
		fetch('/api/thesis-data', {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({
				id: newThesisData.id,
				title: title,
				supervisor: supervisor,
				opponent: opponent
			})
		}).then((res) => {
			if (res.ok) {
				return res.json();
			} else {
				setEditStatus({
					...editStatus,
					basicData: 'failure'
				});
				setEditStatusMessage({
					...editStatusMessage,
					basicData: 'Údaje se nepodařilo uložit. Chybná odpověď serveru.'
				});
			}
		}).then((data) => {
			if (data) {
				if (data.success) {
					setEditStatus({
						...editStatus,
						basicData: 'success'
					});
					setEditStatusMessage({
						...editStatusMessage,
						basicData: data.message
					});
					setNewThesisData(data.new_thesis_data);
				} else {
					setEditStatus({
						...editStatus,
						basicData: 'failure'
					});
					setEditStatusMessage({
						...editStatusMessage,
						basicData: data.message
					});
				}
			} else {
				setEditStatus({
					...editStatus,
					basicData: 'failure'
				});
				setEditStatusMessage({
					...editStatusMessage,
					basicData: 'Údaje se nepodařilo uložit. Chybná odpověď serveru.'
				});
			}
		}).catch((err) => {
			setEditStatus({
				...editStatus,
				basicData: 'failure'
			});
			setEditStatusMessage({
				...editStatusMessage,
				basicData: 'Údaje se nepodařilo uložit. Chyba při komunikaci se serverem.'
			});
		});
	}

	function commitGrades() {
		fetch('/api/thesis-evaluation', {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({
				id: newThesisData.id,
				from: userFrom,
				grades: grades
			})
		}).then((res) => {
			if (res.ok) {
				return res.json();
			} else {
				setEditStatus({
					...editStatus,
					grade: 'failure'
				});
				setEditStatusMessage({
					...editStatusMessage,
					grade: 'Údaje se nepodařilo uložit. Chybná odpověď serveru.'
				});
			}
		}).then((data) => {
			if (data) {
				if (data.success) {
					setEditStatus({
						...editStatus,
						grade: 'success'
					});
					setEditStatusMessage({
						...editStatusMessage,
						grade: data.message
					});
				} else {
					setEditStatus({
						...editStatus,
						grade: 'failure'
					});
					setEditStatusMessage({
						...editStatusMessage,
						grade: data.message
					});
				}
			} else {
				setEditStatus({
					...editStatus,
					grade: 'failure'
				});
				setEditStatusMessage({
					...editStatusMessage,
					grade: 'Údaje se nepodařilo uložit. Chybná odpověď serveru.'
				});
			}
		}).catch((err) => {
			setEditStatus({
				...editStatus,
				grade: 'failure'
			});
			setEditStatusMessage({
				...editStatusMessage,
				grade: 'Údaje se nepodařilo uložit. Chyba při komunikaci se serverem.'
			});
		});
	}

	function commitReview() {
		fetch('/api/thesis-review', {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({
				id: newThesisData.id,
				from: userFrom,
				review: review
			})
		}).then((res) => {
			if (res.ok) {
				return res.json();
			} else {
				setEditStatus({
					...editStatus,
					review: 'failure'
				});
				setEditStatusMessage({
					...editStatusMessage,
					review: 'Údaje se nepodařilo uložit. Chybná odpověď serveru.'
				});
			}
		}).then((data) => {
			if (data) {
				if (data.success) {
					setEditStatus({
						...editStatus,
						review: 'success'
					});
					setEditStatusMessage({
						...editStatusMessage,
						review: data.message
					});
				} else {
					setEditStatus({
						...editStatus,
						review: 'failure'
					});
					setEditStatusMessage({
						...editStatusMessage,
						review: data.message
					});
				}
			} else {
				setEditStatus({
					...editStatus,
					review: 'failure'
				});
				setEditStatusMessage({
					...editStatusMessage,
					review: 'Údaje se nepodařilo uložit. Chybná odpověď serveru.'
				});
			}
		}).catch((err) => {
			setEditStatus({
				...editStatus,
				review: 'failure'
			});
			setEditStatusMessage({
				...editStatusMessage,
				review: 'Údaje se nepodařilo uložit. Chyba při komunikaci se serverem.'
			});
		});
	}

	function commitQuestions() {
		fetch('/api/thesis-questions', {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({
				id: newThesisData.id,
				from: userFrom,
				questions: questions
			})
		}).then((res) => {
			if (res.ok) {
				return res.json();
			} else {
				setEditStatus({
					...editStatus,
					questions: 'failure'
				});
				setEditStatusMessage({
					...editStatusMessage,
					questions: 'Údaje se nepodařilo uložit. Chybná odpověď serveru.'
				});
			}
		}).then((data) => {
			if (data) {
				if (data.success) {
					setEditStatus({
						...editStatus,
						questions: 'success'
					});
					setEditStatusMessage({
						...editStatusMessage,
						questions: data.message
					});
				} else {
					setEditStatus({
						...editStatus,
						questions: 'failure'
					});
					setEditStatusMessage({
						...editStatusMessage,
						questions: data.message
					});
				}
			} else {
				setEditStatus({
					...editStatus,
					questions: 'failure'
				});
				setEditStatusMessage({
					...editStatusMessage,
					questions: 'Údaje se nepodařilo uložit. Chybná odpověď serveru.'
				});
			}
		}).catch((err) => {
			setEditStatus({
				...editStatus,
				questions: 'failure'
			});
			setEditStatusMessage({
				...editStatusMessage,
				questions: 'Údaje se nepodařilo uložit. Chyba při komunikaci se serverem.'
			});
		});
	}

	function setQuestion(value, index) {
		const newQuestions = [...questions];
		newQuestions[index].text = value;
		setQuestions(newQuestions);
	}

	function onAddQuestionClick() {
		setQuestions([
			...questions,
			{
				text: '',
				order: questions.length + 1
			}
		]);
	}

	function onRemoveQuestionClick() {
		setQuestions(questions.slice(0, -1));
	}

	function onMoveQuestionUpClick(questionIndex) {
		if (questionIndex > 0) {
			const newQuestions = [...questions];
			const temp = newQuestions[questionIndex - 1];
			newQuestions[questionIndex - 1] = newQuestions[questionIndex];
			newQuestions[questionIndex] = temp;
			setQuestions(newQuestions);
		}
	}

	function onMoveQuestionDownClick(questionIndex) {
		if (questionIndex < questions.length - 1) {
			const newQuestions = [...questions];
			const temp = newQuestions[questionIndex + 1];
			newQuestions[questionIndex + 1] = newQuestions[questionIndex];
			newQuestions[questionIndex] = temp;
			setQuestions(newQuestions);
		}
	}

	function onSaveButtonClick(event) {
		event.preventDefault();
		if (active === 1) {
			commitBasicData();
			setShowEditMessage({
				basicData: true,
				grade: false,
				review: false,
				questions: false,
				pdf: false
			});
		}
		if (active === 2) {
			commitGrades();
			setShowEditMessage({
				basicData: false,
				grade: true,
				review: false,
				questions: false,
				pdf: false
			});
		}
		if (active === 3) {
			commitReview();
			setShowEditMessage({
				basicData: false,
				grade: false,
				review: true,
				questions: false,
				pdf: false
			});
		}
		if (active === 4) {
			commitQuestions();
			setShowEditMessage({
				basicData: false,
				grade: false,
				review: false,
				questions: true,
				pdf: false
			});
		}
	}

	function onCreatePDFClick(event) {
		event.preventDefault();
		const temp = userFrom === 'supervisor' ?
			'PV' : 'PO';
		const filename = newThesisData.author_class + '_' +
			newThesisData.author.replace(' ', '_') +
			'_RP' +
			'_' + temp +
			'_' + newThesisData.academic_year.substring(0, 2) +
			newThesisData.academic_year.substring(5) +
			'.pdf';
		setShowEditMessage({
			basicData: false,
			grade: false,
			review: false,
			questions: false,
			pdf: true
		});
		fetch('/api/thesis-pdf?' + new URLSearchParams({
			id: newThesisData.id,
			from: userFrom
		})).then((res) => {
			if (res.ok) {
				return res.blob();
			} else {
				setEditStatus({
					...editStatus,
					pdf: 'failure'
				});
				setEditStatusMessage({
					...editStatusMessage,
					pdf: 'PDF se nepodařilo vytvořit. Chybná odpověď serveru.'
				});
			}
		}).then((blob) => {
			const url = window.URL.createObjectURL(
				new Blob([blob]),
				{ type: 'application/pdf', encoding: 'UTF-8' }
			);
			const link = document.createElement('a');
			link.href = url;
			link.setAttribute('download', filename);
			document.body.appendChild(link);
			link.click();
			link.remove();

			setEditStatus({
				...editStatus,
				pdf: 'success'
			});
			setEditStatusMessage({
				...editStatusMessage,
				pdf: 'PDF bylo úspěšně vytvořeno.'
			});
		}).catch((err) => {
			console.log(err);
			setEditStatus({
				...editStatus,
				pdf: 'failure'
			});
			setEditStatusMessage({
				...editStatusMessage,
				pdf: 'PDF se nepodařilo vytvořit. Chyba při komunikaci se serverem.'
			});
		});
	}

	useEffect(() => {
		if (openTab === 1) {
			getGrades('supervisor');
			getReview('supervisor');
			getQuestions('supervisor');
		}
		if (openTab === 2) {
			getGrades('opponent');
			getReview('opponent');
			getQuestions('opponent');
		}
		setShowEditMessage({
			basicData: false,
			grade: false,
			review: false,
			questions: false
		});
	}, [
		getGrades,
		getReview,
		getQuestions,
		openTab
	]);

	return (
		<div className="container mx-auto w-4/5 pb-20">
			<EditorNavigation active={active} setActive={setActive} />
			{active === 1 &&
				<ThesisMainForm
					userCanEdit={userJob === 'supervisor'}
					thesisData={newThesisData}
					title={title}
					setTitle={setTitle}
					supervisor={supervisor}
					setSupervisor={setSupervisor}
					opponent={opponent}
					setOpponent={setOpponent}
					editStatus={editStatus.basicData}
					editStatusMessage={editStatusMessage.basicData}
					showEditMessage={showEditMessage.basicData}
					onSaveButtonClick={onSaveButtonClick}
				/>
			}
			{active === 2 &&
				<ThesisGradeForm
					userCanEdit={canEditStuff}
					viewingSupervisor={openTab === 1}
					grades={grades}
					setGrades={setGrades}
					editStatus={editStatus.grade}
					editStatusMessage={editStatusMessage.grade}
					showEditMessage={showEditMessage.grade}
					onSaveButtonClick={onSaveButtonClick}
				/>
			}
			{active === 3 &&
				<ThesisReviewForm
					userCanEdit={canEditStuff}
					review={review}
					setReview={setReview}
					editStatus={editStatus.review}
					editStatusMessage={editStatusMessage.review}
					showEditMessage={showEditMessage.review}
					onSaveButtonClick={onSaveButtonClick}
				/>
			}
			{active === 4 &&
				<ThesisQuestionsForm
					userCanEdit={canEditStuff}
					thesisData={newThesisData}
					questions={questions}
					setQuestion={setQuestion}
					onAddQuestionClick={onAddQuestionClick}
					onRemoveQuestionClick={onRemoveQuestionClick}
					onMoveQuestionUpClick={onMoveQuestionUpClick}
					onMoveQuestionDownClick={onMoveQuestionDownClick}
					editStatus={editStatus.questions}
					editStatusMessage={editStatusMessage.questions}
					showEditMessage={showEditMessage.questions}
					onSaveButtonClick={onSaveButtonClick}
				/>
			}
			{active === 5 &&
				<CreatePDFForm
					userCanPrint={canEditStuff || userData.role === 'admin'}
					onCreatePDFClick={onCreatePDFClick}
					editStatus={editStatus.pdf}
					editStatusMessage={editStatusMessage.pdf}
					showEditMessage={showEditMessage.pdf}
				/>
			}
			<AutoSaveGrades
				grades={grades}
				thesisId={newThesisData.id}
				userFrom={userFrom}
			/>
			<AutoSaveReview
				review={review}
				thesisId={newThesisData.id}
				userFrom={userFrom}
			/>
			<AutoSaveQuestions
				questions={questions}
				thesisId={newThesisData.id}
				userFrom={userFrom}
			/>
		</div>
	)
}

export default ThesisEditor;