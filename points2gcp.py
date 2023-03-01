#!/usr/bin/env python
import asciitable,sys
Fichero=sys.argv[1]
datos=asciitable.read(Fichero)#,delimiter=',')
asciitable.write({'X': datos.pixelX, 'Y': datos.pixelY*-1,'lat': datos.mapY, 'long': datos.mapX}, Fichero.split('.')[0]+'points.gcp', names=['X','Y','long','lat'],delimiter=",",Writer=asciitable.NoHeader)
print Fichero.split('.')[0]+'points.gcp'
