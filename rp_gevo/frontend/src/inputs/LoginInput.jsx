function LoginInput(props) {
	return (
		<input
			className="login-input"
			type={props.type}
			name={props.name}
			value={props.value}
			onChange={props.onChange}
			placeholder={props.placeholder}
		/>
	);
}

export default LoginInput;