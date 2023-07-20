import {Vec2} from "./vec.js"

function Viewer(){

    let pos = Vec2(0, 0)
    const observers = []
    let scale = 1
	
	function go(x, z, s){
		pos = Vec2(x, z)
		scale = s
		update()
	}

    function scaleUp(){
        if(scale >= 16) return
        scale *= 2
        update()
    }

    function scaleDown(){
        if (scale <= 1) return
        scale /= 2
        update()
    }

    function scrolling(opt){
        document.documentElement.style.overflow = 'hidden';  // firefox, chrome
        document.body.scroll = "no"; // ie only
    }

    const getWidth = () => document.documentElement.clientWidth
    const getHeight = () => document.documentElement.clientHeight
    const listen = (callback) => observers.push(callback)

    const computedSize = () => Vec2(getWidth() * scale, getHeight() * scale)
    const computedCenter = () => Vec2(Math.floor(getWidth() / 2), Math.floor(getHeight() / 2))

    const update = function(){
        observers.forEach(function(listener){
            listener()
        })
    }
    
    const move = (offset) => {
        pos = pos.add(offset)
		update()
    }
    const moveTo = (p) => {
        pos = p
		update()
    }

    window.addEventListener('resize', update)

    const obj = {
		go: go,
        pos: () => pos,
        scale: () => scale,
        size: computedSize,
        center: computedCenter,
        scrolling: scrolling,
        listen: listen,
        update: update,
        move: move,
        moveTo: moveTo,
        scaleUp: scaleUp,
        scaleDown: scaleDown
    }

    return obj
}

export {Viewer}
