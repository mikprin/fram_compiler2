// Generated for: spectre
// Generated on: Feb  1 23:20:28 2021
// Design library name: fram_cells3
// Design cell name: all_cells
// Design view name: schematic
simulator lang=spectre
global 0
include "models.scs"

// Library name: fram_cells3
// Cell name: memory_cell
// View name: schematic
.subckt memory_cell bl gnd pl wn
M0 (net6 wn bl gnd) nsvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 \
        mismatch=1
    I0 (pl net6) conder Ec=1.9 dT=1e-09 l=5e-07 w=5e-07 p00=0.25
.ends memory_cell
// End of subcircuit definition.

// Library name: fram_cells3
// Cell name: off_driver
// View name: schematic
.subckt off_driver BL IN VDD
M1 (BL IN VDD VDD) psvt25 w=0.4 l=0.28 nfing=1 mult=1 srcefirst=1 \
        mismatch=1
.ends off_driver
// End of subcircuit definition.

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

// Library name: fram_cells3
// Cell name: all_cells
// View name: schematic
I0 (BL 0 PL net2) memory_cell
I1 (BL net7 VDD) off_driver
I2 (0 BL net11 net10 net13 net14 VDD) sense_amp
I3 (0 net010 PL VDD) fram_cells5_1u_invertor_schematic
simulatorOptions options reltol=1e-3 vabstol=1e-6 iabstol=1e-12 temp=27 \
    tnom=27 scalem=1.0 scale=1.0 gmin=1e-12 rforce=1 maxnotes=5 maxwarns=5 \
    digits=5 cols=80 pivrel=1e-3 sensfile="../psf/sens.output" \
    checklimitdest=psf
modelParameter info what=models where=rawfile
element info what=inst where=rawfile
outputParameter info what=output where=rawfile
designParamVals info what=parameters where=rawfile
primitives info what=primitives where=rawfile
subckts info what=subckts where=rawfile
saveOptions options save=allpub subcktprobelvl=2
ahdl_include "/home/solovyanov_m/work_shell/fram_cells/conder/veriloga/veriloga.va"