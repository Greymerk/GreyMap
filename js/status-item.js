
const StatusItem = function(name, entry){

	const label = document.createTextNode(`${name}: `)
	const tn = document.createTextNode("")	

	entry.appendChild(label)
	entry.appendChild(tn)

	const update = function(data){
		tn.nodeValue = data
	}


	return {
		update: update
	}

}


export {StatusItem}
