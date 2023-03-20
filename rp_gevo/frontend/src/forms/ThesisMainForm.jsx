import { useState } from 'react';

function ThesisMainForm(props) {
	const canEdit = props.userCanEdit;
	const thesisData = props.thesisData;
	const [editingTitle, setEditingTitle] = useState(false);
	const author = thesisData.author;
	const authorClass = thesisData.author_class;
	const [editingSupervisor, setEditingSupervisor] = useState(false);
	const [editingOpponent, setEditingOpponent] = useState(false);

	return (
		<div className="container mx-auto px-6 min-w-full">
			<div className="flex justify-center min-w-full">
				<form id="thesis-main-form" className="thesis-main-form min-w-full" method="POST">
					<div className="container thesis-main-form-grid min-w-full grid grid-cols-1 auto-rows-fr">
						<div className="container thesis-main-form-row grid grid-rows-1 grid-cols-4 gap-x-8 min-w-full">
							<span className="thesis-main-form-text">
								Téma práce:
							</span>
							{(editingTitle && canEdit) ?
								<input className="col-span-2" type="text" name="title" value={props.title} onChange={(e) => props.setTitle(e.target.value)} /> :
								<span className="thesis-editable thesis-main-form-text col-span-2">{props.title}</span>
							}
							<button className={canEdit ? 'btn edit-btn' : 'btn edit-btn disabled'} type="button" onClick={() => setEditingTitle(!editingTitle)}>
								{(editingTitle && canEdit) &&
									<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
										<path strokeLinecap="round" strokeLinejoin="round" d="M20.25 7.5l-.625 10.632a2.25 2.25 0 01-2.247 2.118H6.622a2.25 2.25 0 01-2.247-2.118L3.75 7.5m8.25 3v6.75m0 0l-3-3m3 3l3-3M3.375 7.5h17.25c.621 0 1.125-.504 1.125-1.125v-1.5c0-.621-.504-1.125-1.125-1.125H3.375c-.621 0-1.125.504-1.125 1.125v1.5c0 .621.504 1.125 1.125 1.125z" />
									</svg>
								}
								{(!editingTitle && canEdit) &&
									<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
										<path strokeLinecap="round" strokeLinejoin="round" d="M16.862 4.487l1.687-1.688a1.875 1.875 0 112.652 2.652L10.582 16.07a4.5 4.5 0 01-1.897 1.13L6 18l.8-2.685a4.5 4.5 0 011.13-1.897l8.932-8.931zm0 0L19.5 7.125M18 14v4.75A2.25 2.25 0 0115.75 21H5.25A2.25 2.25 0 013 18.75V8.25A2.25 2.25 0 015.25 6H10" />
									</svg>
								}
								{!canEdit &&
									<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
										<path strokeLinecap="round" strokeLinejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z" />
									</svg>
								}
							</button>
						</div>
						<div className="container thesis-main-form-row grid grid-rows-1 grid-cols-4 gap-x-8 min-w-full">
							<span className="thesis-main-form-text">Jméno žáka, třída:</span>
							<span className="thesis-editable thesis-main-form-text col-span-2">{author + ", " + authorClass}</span>
							<button className="btn edit-btn disabled" type="button">
								<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
									<path strokeLinecap="round" strokeLinejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z" />
								</svg>
							</button>
						</div>
						<div className="container thesis-main-form-row grid grid-rows-1 grid-cols-4 gap-x-8 min-w-full">
							<span className="thesis-main-form-text">Jméno vedoucího:</span>
							{(editingSupervisor && canEdit) ?
								<input className="col-span-2" type="text" name="supervisor" value={props.supervisor} onChange={(e) => props.setSupervisor(e.target.value)} /> :
								<span className="thesis-editable thesis-main-form-text col-span-2">{props.supervisor}</span>
							}
							<button className={canEdit ? 'btn edit-btn' : 'btn edit-btn disabled'} type="button" onClick={() => setEditingSupervisor(!editingSupervisor)}>
								{(editingSupervisor && canEdit) &&
									<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
										<path strokeLinecap="round" strokeLinejoin="round" d="M20.25 7.5l-.625 10.632a2.25 2.25 0 01-2.247 2.118H6.622a2.25 2.25 0 01-2.247-2.118L3.75 7.5m8.25 3v6.75m0 0l-3-3m3 3l3-3M3.375 7.5h17.25c.621 0 1.125-.504 1.125-1.125v-1.5c0-.621-.504-1.125-1.125-1.125H3.375c-.621 0-1.125.504-1.125 1.125v1.5c0 .621.504 1.125 1.125 1.125z" />
									</svg>
								}
								{(!editingSupervisor && canEdit) &&
									<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
										<path strokeLinecap="round" strokeLinejoin="round" d="M16.862 4.487l1.687-1.688a1.875 1.875 0 112.652 2.652L10.582 16.07a4.5 4.5 0 01-1.897 1.13L6 18l.8-2.685a4.5 4.5 0 011.13-1.897l8.932-8.931zm0 0L19.5 7.125M18 14v4.75A2.25 2.25 0 0115.75 21H5.25A2.25 2.25 0 013 18.75V8.25A2.25 2.25 0 015.25 6H10" />
									</svg>
								}
								{!canEdit &&
									<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
										<path strokeLinecap="round" strokeLinejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z" />
									</svg>
								}
							</button>
						</div>
						<div className="container thesis-main-form-row grid grid-rows-1 grid-cols-4 gap-x-8 min-w-full">
							<span className="thesis-main-form-text">Jméno oponenta:</span>
							{(editingOpponent && canEdit) ?
								<input className="col-span-2" type="text" name="opponent" value={props.opponent} onChange={(e) => props.setOpponent(e.target.value)} /> :
								<span className="thesis-editable thesis-main-form-text col-span-2">{props.opponent}</span>
							}
							<button className={canEdit ? 'btn edit-btn' : 'btn edit-btn disabled'} type="button" onClick={() => setEditingOpponent(!editingOpponent)}>
								{(editingOpponent && canEdit) &&
									<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
										<path strokeLinecap="round" strokeLinejoin="round" d="M20.25 7.5l-.625 10.632a2.25 2.25 0 01-2.247 2.118H6.622a2.25 2.25 0 01-2.247-2.118L3.75 7.5m8.25 3v6.75m0 0l-3-3m3 3l3-3M3.375 7.5h17.25c.621 0 1.125-.504 1.125-1.125v-1.5c0-.621-.504-1.125-1.125-1.125H3.375c-.621 0-1.125.504-1.125 1.125v1.5c0 .621.504 1.125 1.125 1.125z" />
									</svg>
								}
								{(!editingOpponent && canEdit) &&
									<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
										<path strokeLinecap="round" strokeLinejoin="round" d="M16.862 4.487l1.687-1.688a1.875 1.875 0 112.652 2.652L10.582 16.07a4.5 4.5 0 01-1.897 1.13L6 18l.8-2.685a4.5 4.5 0 011.13-1.897l8.932-8.931zm0 0L19.5 7.125M18 14v4.75A2.25 2.25 0 0115.75 21H5.25A2.25 2.25 0 013 18.75V8.25A2.25 2.25 0 015.25 6H10" />
									</svg>
								}
								{!canEdit &&
									<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
										<path strokeLinecap="round" strokeLinejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z" />
									</svg>
								}
							</button>
						</div>
					</div>
					<div className="container mt-8 flex flex-col justify-center items-center min-w-full">
						{(props.editStatus === 'success' && props.showEditMessage) &&
							<p className="edit-status-message mb-4 text-green-500">{props.editStatusMessage}</p>
						}
						{(props.editStatus === 'failure' && props.showEditMessage) &&
							<p className="edit-status-message mb-4 text-red-500">{props.editStatusMessage}</p>
						}
						{canEdit &&
							<button className="btn save-edits-button p-2 w-52 rounded-md" type="submit" onClick={props.onSaveButtonClick}>Uložit změny</button>
						}
					</div>
				</form>
			</div>
		</div>
	)
}

export default ThesisMainForm;