import { Link } from "react-router-dom";

function NotFound() {
	return (
		<div className="container mx-auto min-h-screen flex flex-col items-center justify-center" >
			<div className="container mx-auto flex flex-col items-center">
				<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-20 h-20 not-found-icon">
					<path strokeLinecap="round" strokeLinejoin="round" d="M9.879 7.519c1.171-1.025 3.071-1.025 4.242 0 1.172 1.025 1.172 2.687 0 3.712-.203.179-.43.326-.67.442-.745.361-1.45.999-1.45 1.827v.75M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-9 5.25h.008v.008H12v-.008z" />
				</svg>

				<h2 className="error-message">Stránka nenalezena.</h2>

				<button className="btn rounded-md p-4 my-10">
					<Link to="/">Zpět na hlavní stránku</Link>
				</button>
			</div>
		</div>
	);
}

export default NotFound;