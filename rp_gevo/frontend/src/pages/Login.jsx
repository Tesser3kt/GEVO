import { GoogleLogin } from '@react-oauth/google';
import jwtDecode from 'jwt-decode';
import { useNavigate } from 'react-router-dom';

import logo from '../imgs/logo.png';

function Login() {
	const navigate = useNavigate();

	function onSuccess(credentialResponse) {
		if (credentialResponse.credential) {
			const userCredential = jwtDecode(credentialResponse.credential);

			if (!userCredential.hd || userCredential.hd !== 'gevo.cz') {
				onError('Přihlášení je možné pouze pomocí účtu GEVO.');
				return;
			};

			fetch('/api/login', {
				method: 'POST',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify(userCredential)
			}).then(res => {
				if (res.ok) {
					return res.json();
				}
				onError('Chyba serveru.');
			}).then(data => {
				if (data.id) {
					const state = {
						userData: data
					};
					navigate('/dashboard', { state: state, replace: true });
				}
				else {
					onError('Uživatel nenalezen.');
				}
			}).catch(err => {
				onError(err);
			});
		}
	}

	function onError(err) {
		const state = {
			message: 'Přihlášení neúspěšné.',
			err: err
		};
		navigate('/error', { state: state });
	}

	return (
		<div className="container mx-auto min-h-screen flex flex-col items-center justify-center">
			<div className="container mx-auto flex flex-col items-center">
				<img className="logo w-60" src={logo} alt="Logo" />
				<h1 className="app-title px-10 border-b-2 border-burnt-sienna">RP GEVO</h1>
				<div className="my-8">
					<GoogleLogin
						onSuccess={onSuccess}
						onError={onError}
						useOneTap
						size="large"
					/>
				</div>
			</div>
		</div>
	);
}

export default Login;