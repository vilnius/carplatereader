# Car plate reader server API

This document describes API of server. It tries to capture all details, but some of the endpoints are optional and
could be replaced by simple text files (like `/lanes`, `/transports`).
Also, as long as we have single camera, `/cameras` is optional.

```
/auth  # Authorization

/lanes
  query(lat,lng)  # Is GPS position inside some lane_id or 404?

/lanes/:id
  [{lat,lng}, ...]  # Area of A-lane as polygon on map

/transports
  query(plate='abc123')  # Is plate white-listed or 404?

/transports/:id
  plate: 'BUS123'
  type: [bus/trolley/metro :)]
  route: '3G'

/cameras/:id
  transport: id

/videos/:id
  status: [new/processed]
  camera: id
  time
  location: (lat, lng)  # GPS coordinates
  content: URL
  snapshots: [IMAGE_URL, IMAGE_URL]
  metadata: {length, fps, encoding, etc.}

/penalties/:id
  status: [new/ignored/confirmed]
  video: id
  plate: 'CAR123'
  log

```
