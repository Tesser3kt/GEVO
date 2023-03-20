function ThesisQuestionsForm(props) {
	return (
		<div className="container mx-auto px-6 min-w-full">
			<div className="container flex flex-col items-center min-w-full">
				<form id="thesis-questions-form" className="thesis-questions-form min-w-full" method="POST">
					{props.questions.map((question, index) => {
						return (
							<div key={index} className="container flex justify-between items-center text-right min-w-full mb-8">
								<label htmlFor={"question-" + (index + 1)} className="block">
									Otázka&nbsp;{index + 1}:
								</label>
								<input
									name={"question-" + (index + 1)}
									id={index}
									className={
										props.userCanEdit ?
											"w-full block question-input" :
											"w-full block question-input disabled"
									}
									value={question.text}
									onChange={(e) => props.setQuestion(e.target.value, index)}
									disabled={!props.userCanEdit}
								/>
								<div className="flex move-question-buttons">
									{props.userCanEdit &&
										<>
											<button
												type="button"
												className="btn btn-arrow rounded-md p-2"
												onClick={() => props.onMoveQuestionDownClick(index)}
												disabled={index === props.questions.length - 1}
											>
												<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
													<path strokeLinecap="round" strokeLinejoin="round" d="M19.5 8.25l-7.5 7.5-7.5-7.5" />
												</svg>
											</button>
											<button
												type="button"
												className="btn btn-arrow rounded-md p-2 ml-2"
												onClick={() => props.onMoveQuestionUpClick(index)}
												disabled={index === 0}
											>
												<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
													<path strokeLinecap="round" strokeLinejoin="round" d="M4.5 15.75l7.5-7.5 7.5 7.5" />
												</svg>
											</button>
										</>
									}
								</div>
							</div>
						)
					})}
					{props.questions.length <= 0 &&
						<p className="text-center no-questions-text">Zatím nebyly přidány žádné otázky.</p>
					}
				</form>
				<div className="container flex justify-center items-center mt-4">
					{props.userCanEdit &&
						<button
							type="button"
							className="btn btn-primary rounded-md p-2 w-36 mr-6"
							onClick={props.onAddQuestionClick}
						>
							Přidat otázku
						</button>
					}
					{props.userCanEdit &&
						<button
							type="button"
							className="btn btn-primary rounded-md p-2 w-36"
							onClick={props.onRemoveQuestionClick}
						>
							Odebrat otázku
						</button>
					}
				</div>
				{props.questions.length > 0 &&
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
				}
			</div>
		</div>
	)
}

export default ThesisQuestionsForm;