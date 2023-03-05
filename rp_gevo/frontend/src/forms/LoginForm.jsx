import { useState } from 'react';

import LoginInput from '../inputs/LoginInput.jsx';

function LoginForm() {
	const [email, setEmail] = useState('');
	const [password, setPassword] = useState('');

	return (
		<form method="POST">
			<LoginInput
				type="email"
				name="email"
				value={email}
				onChange={e => setEmail(e.target.value)}
				placeholder="Email"
			/>
			<LoginInput
				type="password"
				name="password"
				value={password}
				onChange={e => setPassword(e.target.value)}
				placeholder="Password"
			/>
		</form>
	);
}

export default LoginForm;