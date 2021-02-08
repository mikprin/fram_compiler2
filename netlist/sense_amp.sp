// Library name: fram_cells3
// Cell name: sense_amp
// View name: schematic
.subckt sense_amp gnd in nb nt ref seb vdd
M3 (nb seb gnd gnd) nsvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 \
        mismatch=1
M2 (gnd seb nt gnd) nsvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 \
        mismatch=1
M1 (nt nb gnd gnd) nsvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 \
        mismatch=1
M0 (gnd nt nb gnd) nsvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 \
        mismatch=1
M8 (net25 seb vdd vdd) psvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 \
        mismatch=1
M7 (net25 ref net33 vdd) psvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 \
        mismatch=1
M6 (net29 in net25 vdd) psvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 \
        mismatch=1
M5 (nt nb net33 vdd) psvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 \
        mismatch=1
M4 (net29 nt nb vdd) psvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 \
        mismatch=1
.ends sense_amp
// End of subcircuit definition.