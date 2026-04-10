from glob import glob
from pathlib import Path
import os

for subset in ['train', 'val', 'test']:
    sar_files = sorted(glob(f'/Users/simon.reichl/Desktop/mmflood_tiled_hydro/{subset}/sar/*.tif'))
    removed = 0
    for sar_path in sar_files:
        name = Path(sar_path).name
        hyd_path = Path(f'/Users/simon.reichl/Desktop/mmflood_tiled_hydro/{subset}/hydro/{name}')
        if not hyd_path.exists():
            for mod in ['sar', 'dem', 'mask']:
                p = Path(f'/Users/simon.reichl/Desktop/mmflood_tiled_hydro/{subset}/{mod}/{name}')
                if p.exists():
                    os.remove(p)
            removed += 1
    print(f'{subset}: {removed} Tiles ohne Hydro entfernt')
