import { Link } from 'react-router-dom';

import logo from '../imgs/logo.png';

function Header({ userName, onLogout }) {
	return (
		<header className="header min-w-full">
			<div className="container grid grid-cols-3 m-0 px-10 py-2 min-w-full">
				<div className="container header-left flex justify-left items-center">
					<Link to ="/dashboard">
						<img className="header-logo h-20" src={logo} alt="logo" />
					</Link>
				</div>
				<div className="container header-center flex justify-center items-center">
					<h1 className="app-title">RP GEVO</h1>
				</div>
				<div className="container header-right flex justify-end items-center">
					<div className="header-user">
						<span className="header-user-name">{userName}</span>
					</div>
					<button className="btn header-logout ml-4 rounded-md p-2" onClick={onLogout}>
						<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-8 h-8 header-logout-icon">
							<path strokeLinecap="round" strokeLinejoin="round" d="M15.75 9V5.25A2.25 2.25 0 0013.5 3h-6a2.25 2.25 0 00-2.25 2.25v13.5A2.25 2.25 0 007.5 21h6a2.25 2.25 0 002.25-2.25V15m3 0l3-3m0 0l-3-3m3 3H9" />
						</svg>
					</button>
				</div>
			</div>
		</header>
	)
}

export default Header;