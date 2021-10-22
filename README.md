# Update Gene Symbols
> Update gene symbols to official HGNC gene symbols.


## Install

`pip install update_gs_hgnc`

## How to use

Use this package to get the official gene symbol as follows:

```
from update_gs_hgnc import core as update_gs

off_gs = update_gs.get_official_gene_symbol('VARS')
off_gs
```




    'VARS1'


