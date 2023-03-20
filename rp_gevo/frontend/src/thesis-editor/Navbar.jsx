function Navbar({ openTab, enabledTabs, onTabClick }) {
	let supervisorTabClass = 'mr-1';
	let supervisorItemClass = 'nav-item';
	let opponentTabClass = 'mr-1';
	let opponentItemClass = 'nav-item';

	if (openTab === 1 && enabledTabs.supervisor) {
		supervisorTabClass += ' -mb-1';
		supervisorItemClass += ' active';
	}
	if (openTab === 2 && enabledTabs.opponent) {
		opponentTabClass += ' -mb-1';
		opponentItemClass += ' active';
	}
	if (!enabledTabs.supervisor) {
		supervisorTabClass += ' disabled';
		supervisorItemClass += ' disabled';
	}
	if (!enabledTabs.opponent) {
		opponentTabClass += ' disabled';
		opponentItemClass += ' disabled';
	}

	return (
		<div className="container mx-auto px-10 min-w-full navbar-container">
			<ul className="flex border-b-2 border-powder-blue justify-center navbar">
				<li className={supervisorTabClass}>
					<button id="1" className={supervisorItemClass} onClick={onTabClick}>Posudek vedoucího</button>
				</li>
				<li className={opponentTabClass}>
					<button id="2" className={opponentItemClass} onClick={onTabClick}>Posudek oponenta</button>
				</li>
			</ul>
		</div>
	);
}

export default Navbar;