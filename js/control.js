import {Vec2} from "./vec.js"

function Control(view, world){

    let mouseDown = false
    let lastMouse = Vec2(0,0)
	let counter = 0

	let region_outline = false

    document.body.style.overflow = "hidden"
    document.body.style.touchAction = "none"

    const getTouch = function(touch, i){
        const x = touch.clientX
        const y = touch.clientY
        return Vec2(x, y)
    }

    window.addEventListener("touchstart", function(e){
		mouseDown = true
        const touch = e.touches[0]
        lastMouse = getTouch(touch, 0)
        e.preventDefault()
    })

    window.addEventListener("touchmove", function(e){
		counter += 1
		console.log(counter)
		e.preventDefault()
		if(!mouseDown) return
		const touch = e.touches[0]
        const current = getTouch(touch, 0)
        const offset = lastMouse.sub(current)
		const pos = view.pos().add(offset.mul(Vec2(view.scale(), view.scale())))
        view.moveTo(pos)
        lastMouse = current
	})

    window.addEventListener("touchend", function(e){
        mouseDown = false
		touch = null
        e.preventDefault()
    })

    window.addEventListener("mousedown", function(e){
        mouseDown = true
        lastMouse = Vec2(e.clientX, e.clientY)
        e.preventDefault()
    })

    window.addEventListener("mousemove", function(e){
        if(!mouseDown) return
        counter += 1
		const current = Vec2(e.clientX, e.clientY)
        const offset = lastMouse.sub(current)
        const pos = view.pos().add(offset.mul(Vec2(view.scale(), view.scale())))
        view.moveTo(pos)
        lastMouse = current
        e.preventDefault()
    })

    window.addEventListener("mouseup", function(e){
        mouseDown = false
        const current = Vec2(e.clientX, e.clientY)
        const offset = lastMouse.sub(current)
        const pos = view.pos().add(offset.mul(Vec2(view.scale(), view.scale())))
        view.moveTo(pos)
        e.preventDefault()
    })

    const move = (x, y) => view.move(Vec2(x, y))

    const codes = {
        'ArrowUp':      () => move(0, -64),
        'ArrowDown':    () => move(0, 64),
        'ArrowLeft':    () => move(-64, 0),
        'ArrowRight':   () => move(64, 0),
        'PageUp':       () => view.scaleUp(),
        'PageDown':     () => view.scaleDown(),
		'g':			() => {
			region_outline = !region_outline
			const settings = getSettings()
			//console.log(settings)
			world.configure(settings)
		}
    }
    
    window.addEventListener("keydown", function(e){
        codes.hasOwnProperty(e.key) && codes[e.key]()
    })
	
	const getSettings = function(){
		return {
			region_outline: region_outline
		}
	}
	
	return {
		lastMouse: () => lastMouse,
		mpos: () => view.pos().add(lastMouse)
	}
}

export {Control}
