import {Vec2} from "./vec.js"
import {Viewer} from "./viewer.js"
import {Status} from "./status.js"
import {World} from "./world.js"
import {Control} from "./control.js"
import {Mapurl} from "./mapurl.js"

window.addEventListener("load", main, false);

function main(){

	const body = document.body
	
	const statBox = document.createElement('div')
	body.appendChild(statBox)

	const mbox = document.createElement('div')
	mbox.style.backgroundColor = 'black'
	body.appendChild(mbox)

	const world = World(mbox)

	body.style.padding = '0px'
	body.style.margin = '0px'
	body.style.backgroundColor = 'black'
	const view = Viewer()
	view.scrolling(false)
	const size = view.size
	
	const url = Mapurl()
	url.init(view)
	
	const stats = Status(statBox)
	const statsCam = stats.add('camera')
	const statsMouse = stats.add('mouse')
	statsCam.update(size.x + ', ' + size.y)
	
	view.listen(function(){
		statsCam.update(view.pos().x + ', ' + view.pos().y)
		world.update(view.pos(), view.size(), view.scale())
		url.update(view.pos().x, view.pos().y, view.scale())
	})
	
	window.addEventListener('mousemove', (e) => {
		const m = Vec2(e.clientX, e.clientY)
		const mOff = m.sub(view.center())
		const scaledMOff = mOff.mul(Vec2(view.scale(), view.scale()))
		const mpos = scaledMOff.add(view.pos())
		statsMouse.update(mpos.x + ', ' + mpos.y)
	})
	
	statsMouse.update('0, 0')

	const control = Control(view, world)

	view.update()

}
