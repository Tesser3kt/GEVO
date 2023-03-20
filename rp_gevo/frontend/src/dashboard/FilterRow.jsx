function FilterRow({ userRole, filters, onFilterInputChange }) {
	return (
		<div className="filter-row text-center grid grid-rows-1 grid-cols-6 gap-x-8 items-center">
			<div className="filter-row-item">
				<input type="text" name="class" value={filters['class']} placeholder="např. 5.A" onChange={onFilterInputChange} />
			</div>
			<div className="filter-row-item">
				<input type="text" name="student" value={filters['student']} placeholder="např. Jára Cimrman" onChange={onFilterInputChange} />
			</div>
			<div className="filter-row-item">
				<input type="text" name="title" value={filters['title']} placeholder="např. opereta Proso" onChange={onFilterInputChange} />
			</div>
			<div className="filter-row-item">
				{userRole === 'admin' ?
					<input type="text" name="supervisor" value={filters['supervisor']} placeholder="např. inspektor Trachta" onChange={onFilterInputChange} /> :
					<input type="checkbox" checked={filters['supervisor-check']} name="supervisor-check" onChange={onFilterInputChange} />
				}
			</div>
			<div className="filter-row-item">
				{userRole === 'admin' ?
					<input type="text" name="opponent" value={filters['opponent']} placeholder="např. Béla Puskás" onChange={onFilterInputChange} /> :
					<input type="checkbox" checked={filters['opponent-check']} name="opponent-check" onChange={onFilterInputChange} />
				}
			</div>
			<div className="filter-row-item">
				<select name="year" onChange={onFilterInputChange}>
					<option value="23">2022/23</option>
				</select>
			</div>
		</div>
	)
}

export default FilterRow;