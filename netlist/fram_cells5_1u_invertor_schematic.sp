// Library name: fram_cells5
// Cell name: 1u_invertor
// View name: schematic
.subckt fram_cells5_1u_invertor_schematic gnd in out vdd
M0 (out in gnd gnd) nsvt25 w=1.0 l=0.28 nfing=1 mult=1 srcefirst=1 \
        mismatch=1
M1 (out in vdd vdd) psvt25 w=1.0 l=0.28 nfing=1 mult=1 srcefirst=1 \
        mismatch=1
.ends fram_cells5_1u_invertor_schematic
// End of subcircuit definition.