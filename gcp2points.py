#!/usr/bin/env python
import asciitable,sys
import numpy as np
Fichero=sys.argv[1]
datos=asciitable.read(Fichero)#,delimiter=',')
enable=np.int8(np.ones(len(datos.col1)))
asciitable.write({'mapX': datos.col3,'mapY': datos.col4,'pixelX': datos.col1, 'pixelY': datos.col2*-1,'enable':enable}, Fichero.split('.')[0]+'.jpg.points', names=['mapX','mapY','pixelX','pixelY','enable'],delimiter=",")
