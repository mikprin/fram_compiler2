// Library name: fram_cells3
// Cell name: off_driver
// View name: schematic
.subckt off_driver BL IN VDD
M1 (BL IN VDD VDD) psvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 \
        mismatch=1
.ends off_driver
// End of subcircuit definition.