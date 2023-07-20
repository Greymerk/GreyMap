const Mapurl = function(){
	
	let state = "@"
	const defaultState = "@0,0,z1"
	
	const init = function(view){
		state = getUrlState()
		const args = parse(state)
		const x = args[0]
		const z = args[1]
		const s = args[2]
		
		view.go(x, z, s)
		update(x, z, s)
	}
	
	const update = function(x, z, scale){
		state = `@${x},${z},z${scale}`
	}
	
	const getUrlState = function(){
		const p = document.location.pathname
		const s = p.includes('@') ? '@' + p.split('@')[1] : defaultState
		return s
	}
	
	const updateURL = function(){
		const p = document.location.pathname
		const basePath = p.includes('@') ? p.split('@', 1)[0] : p
		const newPath = basePath + state
		window.history.replaceState(null, null, newPath)
		setTimeout(updateURL, 1000)
	}
	
	const parse = function(strg){
		const params = strg.substring(1)
		const parr = params.split(',')
		const x = parseInt(parr[0])
		const z = parseInt(parr[1])
		const s = parseInt(parr[2].substring(1))
		
		const xzs = [x, z, s]
		return xzs
	}
	
	setTimeout(updateURL, 500)
	
	return {
		update: update,
		init: init,
		state: () => state
	}
}

export {Mapurl}