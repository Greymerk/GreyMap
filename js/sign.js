
import {Vec2} from "./vec.js"

const Sign = function(obj){
	
	const pos = Vec2(obj.x, obj.z)
	
	const isMarker = function(){
		const line = obj.front_text.messages[0]
		if(line.length < 3) return false
		if(line.charAt(line.length - 1) != '~') return false
		if(line.charAt(0) != '~') return false
		return true
	}
	
	return {
		front: () => obj.front_text.messages,
		back: () => obj.front_text.messages,
		pos: () => pos,
		isMarker: isMarker
	}
	
}

export{Sign}