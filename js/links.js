
function Links(box){
	
	box.style.position = "absolute"
	box.style.marginTop = "5px"
	box.style.marginLeft = "5px"
	box.style.width = "128px"
	box.style.height = "16px"
	box.style.zIndex = 2
	box.appendChild(Link("markers/house.png", window.location.origin))
	box.appendChild(Link("markers/world.png", `${getPath()}@0,0,z1`))
	
}

function Link(icon, href){
	
	const a = document.createElement("a")
	a.href = href
	a.style.display = "inline-block"
	a.style.marginRight = "5px"
	
	const container = document.createElement("div")
	a.appendChild(container)
	//container.style.display = "flex"
	container.style.width = "16px"
	container.style.height = "16px"
	container.style.outline = "1px solid LightGrey"
	container.style.backgroundColor = "black"
	container.style.backgroundImage = `url('${icon}')`
	container.style.borderRadius = '5px'
	
	return a
}

function getPath(){
	
	const p = document.location.pathname
	const basePath = p.includes('@') ? p.split('@', 1)[0] : p
	return window.location.origin + basePath
}

export {Links}

