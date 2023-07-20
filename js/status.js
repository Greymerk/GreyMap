import {StatusItem} from './status-item.js'

function Status(box){

	const entryList = document.createElement("ul")
	entryList.style.listStyleType = 'none'
	entryList.style.margin = '5px'
	entryList.style.padding = '0'
	entryList.style.minWidth = '12em'  

	box.appendChild(entryList)
	box.style.position = "fixed"
	box.style.zIndex = 10
	box.style.marginTop = "25px"
	box.style.marginLeft = "5px"
	box.style.border = "1"
	box.style.backgroundColor = "PapayaWhip"
	box.style.borderRadius = '5px'
	box.style.fontFamily = 'Verdana'
	box.style.fontSize = '0.8em'

	const entries = {}

	//console.log(entries)

	const update = function(name, val){
		entries[name].update(val)
	}
	
	const add = function(name){
		const box = document.createElement('li')
		entryList.appendChild(box)
		const entry = StatusItem(name, box)
		entries[name] = entry
		return entry	   
	}

	return {
		update: update,
		add: add,
		get: name => entries[name]
	}
}

export {Status}
