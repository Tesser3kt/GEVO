function ThesisReviewForm(props) {
	return (
		<div className="container mx-auto px-6 min-w-full">
			<div className="container flex justify-center min-w-full">
				<form id="thesis-review-form" className="thesis-review-form min-w-full" method="POST">
					<label htmlFor="review" className="block mb-2">
						Slovní hodnocení výsledné práce (klady a nedostatky)
					</label>
					<textarea
						name="review"
						id="review"
						className={
							props.userCanEdit ?
								"w-full h-96 block" :
								"w-full h-96 block disabled"
						}
						value = {props.review}
						onChange={(e) => props.setReview(e.target.value)}
						disabled={!props.userCanEdit}
					/>
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
				</form>
			</div>
		</div>
	)
}

export default ThesisReviewForm;