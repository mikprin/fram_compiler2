// Library name: fram_cells3
// Cell name: memory_cell
// View name: schematic
.subckt memory_cell bl gnd pl wn
M0 (net6 wn bl gnd) nsvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 \
        mismatch=1
I0 (pl net6) conder Ec=1.9 dT=1e-09 l=5e-07 w=5e-07 p00=0.25
.ends memory_cell
// End of subcircuit definition.