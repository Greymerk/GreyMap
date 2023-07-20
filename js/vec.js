const Vec2 = function(x, y){
	return {
		x: x,
		y: y,
		add: (other) => Vec2(x + other.x, y + other.y),
		sub: (other) => Vec2(x - other.x, y - other.y),
		mul: (other) => Vec2(x * other.x, y * other.y),
		div: (other) => Vec2(x / other.x, y / other.y),
		equals: function(other){
			if(other.x != x) return false
			if(other.y != y) return false
			return true
		},
		string: () => `x:${x}, y:${y}`,
		log: () => console.log(x, y)
	}
}

export {Vec2}
