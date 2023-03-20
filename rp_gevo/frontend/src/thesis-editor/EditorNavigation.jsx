function EditorNavigation({ active, setActive }) {
	return (
		<div className="container mx-auto min-w-full pills-container">
			<ul className="flex justify-between pills">
				<li className={active === 1 ? 'pill active' : 'pill'}>
					<button
						className="btn pill-item"
						onClick={() => setActive(1)}
					>
						Údaje
					</button>
				</li>
				<li className={active === 2 ? 'pill active' : 'pill'}>
					<button
						className="btn pill-item"
						onClick={() => setActive(2)}
					>
						Známka
					</button>
				</li>
				<li className={active === 3 ? 'pill active' : 'pill'}>
					<button
						className="btn pill-item"
						onClick={() => setActive(3)}
					>
						Slovní hodnocení
					</button>
				</li>
				<li className={active === 4 ? 'pill active' : 'pill'}>
					<button
						className="btn pill-item"
						onClick={() => setActive(4)}
					>
						Otázky k obhajobě
					</button>
				</li>
				<li className={active === 5 ? 'pill active' : 'pill'}>
					<button
						className="btn pill-item"
						onClick={() => setActive(5)}
					>
						Zveřejnění a tisk
					</button>
				</li>
			</ul>
		</div>
	)
}

export default EditorNavigation;