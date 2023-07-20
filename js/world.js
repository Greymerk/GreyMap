import {Vec2} from "./vec.js"
import {Region} from "./region.js"
import {MarkerManager} from "./markers.js"

function World(container){

    const regions = new Map()
	let regionOutlines = false

	const markers = MarkerManager(container)

	const addRegions = function(toAdd, pos, size, scale){
		toAdd.forEach(function(rpos){
			const key = `${rpos.x}.${rpos.y}`
			if(!regions.has(key)){
				const rbox = document.createElement('div')
				container.appendChild(rbox)
				const region = Region(rpos, rbox)
				//console.log(regionOutlines)
				region.setOutline(regionOutlines)
				regions.set(key, region)
				
				region.addMarkers(markers, () => {
					markers.update(Vec2(pos.x, pos.y), size, scale)
				})
			}
		})
	}

	const visible = function(pos, size, scale){
		const offsetX = size.x/2
		const offsetY = size.y/2
        let x = pos.x - offsetX
        let y = pos.y - offsetY
        
        const toAdd = []
		
        for(let x=pos.x - Math.floor(offsetX); x < pos.x + Math.floor(offsetX) + 512; x += 512){
            for(let y=pos.y - Math.floor(offsetY); y < pos.y + Math.floor(offsetY)+ 512; y += 512){
                toAdd.push(Vec2(Math.floor(x/512), Math.floor(y/512)))
            }
        }
        
        addRegions(toAdd, pos, size, scale)
    }

    const update = function(pos, size, scale){
		visible(pos, size, scale)
        regions.forEach(function(region){
            region.update(Vec2(pos.x, pos.y), size, scale)
        })
		markers.update(Vec2(pos.x, pos.y), size, scale)
    }

	const configure = function(settings){
		regionOutlines = settings.region_outline
		console.log(settings)
		regions.forEach((r) => r.configure(settings))
	}

    return {
        update: update,
		configure: configure
    }

}

export {World}
