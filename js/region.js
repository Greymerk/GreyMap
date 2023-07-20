
import {Vec2} from './vec.js'
import {Sign} from './sign.js'

function Region(offset, container){

	const region_size = 512

	const src = `regions/${offset.x}.${offset.y}.png`
	const p = document.location.pathname
	const pathname = p.includes('@') ? p.split('@', 1)[0] : p
	const imgurl = `${document.location.origin}${pathname}${encodeURI(src)}`
	container.style.width =  `${region_size}px`
	container.style.height = `${region_size}px`
	container.style.backgroundColor = 'black'
	container.style.backgroundImage = `url('${imgurl}')`
	container.style.position = "absolute"

	container.style.outline = "1px solid yellow"
	container.style.outlineOffset =  "-4px;"
	const label = `${offset.x},${offset.y}`
	const labelBox = document.createElement('span')
	container.appendChild(labelBox)
	const labelText = document.createTextNode(label)
	labelBox.appendChild(labelText)
	labelBox.style.color = "white"
	labelBox.style.margin = "1em"
	labelBox.style.fontFamily = "monospace"
	labelBox.style.fontSize = "small"

	const update = function(pos, size, scale){
		const scaledSize = size.div(Vec2(scale, scale))
		const halfScaledSize = scaledSize.div(Vec2(2,2))
		const blockPos = pos.div(Vec2(scale, scale))
		const topLeft = halfScaledSize.sub(blockPos)
		
		container.style.marginLeft = `${Math.floor(topLeft.x + offset.x*(region_size/scale))}px`
		container.style.marginTop = `${Math.floor(topLeft.y + offset.y*(region_size/scale))}px`
		container.style.width =  `${Math.floor(region_size/scale)}px`
		container.style.height = `${Math.floor(region_size/scale)}px`
		container.style.backgroundSize = "cover"
	}
	
	const setOutline = function(state){
		container.style.outline = state ? "1px solid yellow" : "none"
		labelBox.style.visibility = state ? "visible" : "hidden"
	}
	
	const configure = function(settings){
		setOutline(settings.region_outline)
	}
	
	const addMarkers = function(markers, callback){
		const signFile = `signs/${offset.x}.${offset.y}.json`
		fetch(signFile)
			.then(response => response.ok ? response.json() : Promise.reject('404'))
			.then(obj => loadMarkers(obj, markers))
			.then(callback)
	}
	
	const loadMarkers = function(list, markers){
		list.forEach((e) => {
			const s = Sign(e)
			if(s.isMarker()) markers.add(s)
		})
	}
	
	return {
		update: update,
		configure: configure,
		setOutline: setOutline,
		addMarkers: addMarkers
	}

}

export {Region}
