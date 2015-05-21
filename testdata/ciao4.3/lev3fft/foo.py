#!/usr/bin/env python
from sherpa.astro.utils._region import region_parse
print region_parse(r'region(acisf07999_000N001_r0035_reg3.fits[SRCREG])', 0)
