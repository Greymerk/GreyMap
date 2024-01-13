import {Vec2} from './vec.js'

const MarkerManager = function(container){
	
	const markers = []
	
	const update = function(pos, size, scale){
		
		markers.forEach((m) => {
			m.update(pos, size, scale)
		})
	}
	
	const add = function(sign){
		markers.push(Marker(container, sign))
	}
	
	return{
		update: update,
		add: add
	}
}


const Marker = function(container, sign){
	
	const markBack = document.createElement('span')
	container.appendChild(markBack)
	const mark = document.createElement('span')
	container.appendChild(mark)
	
	const indicator = sign.front()[0]
	const name = indicator.substring(1, indicator.length - 1)
	const icon =  `markers/${getIcon(name)}`
	
	const markBackSize = 10
	
	markBack.style.width = `${markBackSize}px`
	markBack.style.height = `${markBackSize}px`
	markBack.style.borderRadius = `${markBackSize/2}px`
	markBack.style.zIndex = '1'
	markBack.style.backgroundColor = 'black'
	markBack.style.outline = "1px solid LightGrey"
	markBack.style.position = "absolute"
	markBack.style.boxShadow = "2px 2px 3px black"
	
	mark.style.width = '8px'
	mark.style.height = '8px'
	mark.style.position = "absolute"
	mark.style.backgroundImage = `url('${icon}')`
	mark.style.backgroundSize = 'contain'
	mark.style.backgroundRepeat = 'no-repeat'
	mark.style.zIndex = "2"
	
	const label = document.createElement('span')
	container.appendChild(label)
	label.style.position = "absolute"
	label.style.width = '10em'
	label.style.fontSize = "8px"
	label.style.fontWeight = "bold"
	label.style.fontFamily = "monospace"
	label.style.textShadow = "-1px -1px 1px #000, 0 -1px 1px #000, 1px -1px 1px #000, 1px 0 1px #000, 1px  1px 1px #000, 0 1px 1px #000, -1px 1px 1px #000, -1px 0 1px #000"
	label.style.color = "white"
	label.style.whiteSpace = "nowrap"
	label.style.textAlign = "center"
	label.style.opacity = "1"
	label.style.zIndex = "3"
	
	const labelText = document.createTextNode(sign.front()[1])
	label.appendChild(labelText)
	
	const region_size = 512
	const offset = sign.pos()
	

	
	const update = function(pos, size, scale){
		
		const scaledSize = size.div(Vec2(scale, scale))
		const halfScaledSize = scaledSize.div(Vec2(2,2))
		const blockPos = pos.div(Vec2(scale, scale))
		const topLeft = halfScaledSize.sub(blockPos)
		
		markBack.style.marginLeft = `${Math.floor(topLeft.x + offset.x/scale) - markBackSize/2}px`
		markBack.style.marginTop = `${Math.floor(topLeft.y + offset.y/scale) - markBackSize/2}px`
		
		mark.style.marginLeft = `${Math.floor(topLeft.x + offset.x/scale) - 4}px`
		mark.style.marginTop = `${Math.floor(topLeft.y + offset.y/scale) - 4}px`
		
		label.style.marginLeft = `${Math.floor(topLeft.x + offset.x/scale) - 40}px`
		label.style.marginTop = `${Math.floor(topLeft.y + offset.y/scale) - 17}px`

	}
	
	return {
		update: update
	}
}

const icons = {
	amethyst:		"amethyst.png",
	anchor: 		"anchor.png",
	apple:			"apple.png",
	bank: 			"bank.png",
	base:			"bed.png",
	battlefield:	"sword.png",
	basket: 		"basket.png",
	bed:			"bed.png",
	bee:			"bee.png",
	beer:			"beer.png",
	bell:			"bell.png",
	bighouse:		"bighouse.png",
	blueflag:		"blueflag.png",
	bomb:			"bomb.png",
	bone:			"bone.png",
	bookshelf:		"bookshelf.png",
	bricks:			"bricks.png",
	bronzemedal:	"bronzemedal.png",
	bronzestar:		"bronzestar.png",
	building:		"building.png",
	cake:			"cake.png",
	camera:			"camera.png",
	cart:			"cart.png",
	caution:		"caution.png",
	chest:			"chest.png",
	church:			"church.png",
	coins:			"coins.png",
	comment:		"comment.png",
	compass:		"compass.png",
	cookie:			"cookie.png",
	construction:	"construction.png",
	cross:			"cross.png",
	cup:			"cup.png",
	cutlery:		"cutlery.png",
	default:		"default.png",
	diamond:		"diamond.png",
	dog:			"dog.png",
	door:			"door.png",
	down:			"down.png",
	drink:			"drink.png",
	emerald:		"emerald",
	endereye:		"endereye.png",
	enchantedbook:	"enchantedbook.png",
	exclamation:	"exclamation.png",
	factory:		"factory.png",
	farm:			"hoe.png",
	fire:			"fire.png",
	flower:			"flower.png",
	gear:			"gear.png",
	goldenapple:	"goldenapple.png",
	goldmedal:		"goldmedal.png",
	goldstar:		"goldstar.png",
	greenflag:		"greenflag.png",
	gunpowder:		"gunpowder.png",
	hammer:			"hammer.png",
	heart:			"heart.png",
	hoe:			"hoe.png",
	home:			"bed.png",
	house:			"house.png",
	hostile:		"warning.png",
	key:			"key.png",
	king:			"king.png",
	left:			"left.png",
	lightbulb:		"lightbulb.png",
	lighthouse:		"lighthouse.png",
	lock:			"lock.png",
	mine:			"pickaxe.png",
	minecart:		"minecart.png",
	nautilus:		"nautilus.png",
	netherite:		"netherite.png",
	offlineuser:	"offlineuser.png",
	orangeflag:		"orangeflag.png",
	pickaxe:		"pickaxe.png",
	pinkflag:		"pinkflag.png",
	pin:			"pin.png",
	pirateflag:		"pirateflag.png",
	pointdown:		"pointdown.png",
	pointleft:		"pointleft.png",
	pointright:		"pointright.png",
	pointup:		"pointup.png",
	portal:			"portal.png",
	purpleflag:		"purpleflag.png",
	queen:			"queen.png",
	redflag:		"redflag.png",
	right:			"right.png",
	ruby:			"ruby.png",
	ruin:			"ruin.png",
	scales:			"scales.png",
	shield:			"shield.png",
	shop:			"emerald.png",
	sign:			"sign.png",
	silvermedal:	"silvermedal.png",
	silverstar:		"silverstar.png",
	skull:			"skull.png",
	spawn:			"world.png",
	star:			"star.png",
	stronghold:		"endereye.png",
	sun:			"sun.png",
	sword:			"sword",
	temple:			"temple.png",
	theater:		"theater.png",
	tornado:		"tornado.png",
	tower:			"tower.png",
	tree:			"tree.png",
	truck:			"truck.png",
	up:				"up.png",
	village:		"bell.png",
	walk:			"walk.png",
	warning:		"warning.png",
	world:			"world.png",
	wrench:			"wrench.png",
	yellowflag:		"yellowflag.png"
}

const getIcon = function(key){
	
	if(!(key in icons)) return icons["pin"]
	
	return icons[key]
}

export {MarkerManager}
