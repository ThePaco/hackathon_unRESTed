import React, { useEffect } from 'react';
import './Floor.css';

var FloorPlanEngine;

const floorPlanStartupSettings = {
  hideElements: [],
  panZoom: true,
  planRotation: 0,
  roomStampSize: null,
  spaceLabelMapping: {
    bedroom: 'Office',
    residential: 'Open',
    balcony: 'Office',
    storage: 'Conference',
    bathroom: 'nesto'
  },
  hideElements: ['interior'],
  ui: {
      menu: false,
      scale: false,
      coordinates: false
  },
  theme: {
      background: {
          color: '#f3f5f8',
          showGrid: false
      },
      wallContours: false,
      elements: {
          roomstamp: { showArea: false }
      }
  },
  units: {
      system: 'metric',
      digits: 0,
      roomDimensions: 'area'
  }
}

const colorMap = {
  red: [227, 108, 100],
  green: [177, 204, 136],
  blue: [0, 100, 255],
  gold: [250, 173, 20]
};

const Floor = (props) => {
  let active = {};
  function highlightResources(evt) {
    const pos = evt.pos
    let { assets, spaces } = this.getResourcesFromPosition(pos)
    highlight(spaces, 'space', [150, 200, 250])
    highlight(assets, 'asset', [250, 150, 50])
  }

  function highlight(items, type, color) {
    if (!items.length) {
      if (active[type]) active[type].node.setHighlight()
      delete active[type]
      return
    }
    let item = items[0]
    if (active[type]?.id === item.id) return
    else if (active[type]) active[type].node.setHighlight()
    item.node.setHighlight({ fill: color })
    active[type] = item
  }

  useEffect(() => {
    const container = document.getElementById('floorplan')
    const fp = new FloorPlanEngine(container, floorPlanStartupSettings)
    const publishableToken = 'e8e6cce9-788f-4866-b53d-a1a145325a76'

    fp.loadScene(props.sceneId, { publishableToken }).then(() => {
      console.log(fp)
      fp.on('mousemove', highlightResources, fp);
      fp.on("click", (ev) => onRoomClick(ev,fp));
      //comment
    })

    // eslint-disable-next-line react-hooks/exhaustive-deps
}, [props.sceneId]);
const onRoomClick = (event, floorPlan) => {
  const { spaces } = floorPlan.getResourcesFromPosition(event.pos);
  if (spaces.length === 0) return;
  spaces[0].node.setHighlight({fill: [0,200,0]});
}

  return (<>
  <div id='floorplan' style={{ height: '100%', width: '100%' }}></div>
  </>)
}

Floor.propTypes = {};

Floor.defaultProps = {};

export default Floor;
