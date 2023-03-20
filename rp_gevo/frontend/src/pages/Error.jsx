import { useLocation } from "react-router-dom";
import { Link } from "react-router-dom";

function Error() {
	const { state } = useLocation();

	return (
		<div className="container mx-auto min-h-screen flex flex-col items-center justify-center" >
			<div className="container mx-auto flex flex-col items-center">
				<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="error-triangle w-20 h-20">
					<path strokeLinecap="round" strokeLinejoin="round" d="M12 9v3.75m-9.303 3.376c-.866 1.5.217 3.374 1.948 3.374h14.71c1.73 0 2.813-1.874 1.948-3.374L13.949 3.378c-.866-1.5-3.032-1.5-3.898 0L2.697 16.126zM12 15.75h.007v.008H12v-.008z" />
				</svg>
				<h2 className="error-message">{state.message}</h2>
				<p className="error-detail rounded-md p-4 my-4 bg-gray-100 ring-2 ring-burnt-sienna">{state.err}</p>

				<button className="btn rounded-md p-4 my-10">
					<Link to="/">Zpět na hlavní stránku</Link>
				</button>
			</div>
		</div>
	);
}

export default Error;