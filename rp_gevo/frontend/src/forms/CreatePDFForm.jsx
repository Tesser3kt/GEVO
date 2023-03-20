function CreatePDFForm(props) {
	return (
		<div className="container mt-8 flex flex-col justify-center items-center min-w-full">
			{(props.editStatus === 'success' && props.showEditMessage) &&
				<p className="edit-status-message mb-4 text-green-500">{props.editStatusMessage}</p>
			}
			{(props.editStatus === 'failure' && props.showEditMessage) &&
				<p className="edit-status-message mb-4 text-red-500">{props.editStatusMessage}</p>
			}
			{props.userCanPrint &&
				<button className="btn save-edits-button p-2 w-52 rounded-md" type="submit" onClick={props.onCreatePDFClick}>Vygenerovat PDF</button>
			}
		</div>
	);
}

export default CreatePDFForm;