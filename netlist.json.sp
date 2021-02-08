.subckt sense_amp gnd in nb nt ref seb vdd
M3 (nb seb gnd gnd) nsvt25w=0.4 l=0.28 nfing=1.0 mult=1.0 srcefirst=1.0 mismatch=1.0 
M2 (gnd seb nt gnd) nsvt25w=0.4 l=0.28 nfing=1.0 mult=1.0 srcefirst=1.0 mismatch=1.0 
M1 (nt nb gnd gnd) nsvt25w=0.4 l=0.28 nfing=1.0 mult=1.0 srcefirst=1.0 mismatch=1.0 
M0 (gnd nt nb gnd) nsvt25w=0.4 l=0.28 nfing=1.0 mult=1.0 srcefirst=1.0 mismatch=1.0 
M8 (net25 seb vdd vdd) psvt25w=0.4 l=0.28 nfing=1.0 mult=1.0 srcefirst=1.0 mismatch=1.0 
M7 (net25 ref net33 vdd) psvt25w=0.4 l=0.28 nfing=1.0 mult=1.0 srcefirst=1.0 mismatch=1.0 
M6 (net29 in net25 vdd) psvt25w=0.4 l=0.28 nfing=1.0 mult=1.0 srcefirst=1.0 mismatch=1.0 
M5 (nt nb net33 vdd) psvt25w=0.4 l=0.28 nfing=1.0 mult=1.0 srcefirst=1.0 mismatch=1.0 
M4 (net29 nt nb vdd) psvt25w=0.4 l=0.28 nfing=1.0 mult=1.0 srcefirst=1.0 mismatch=1.0 
.ends sense_amp


.subckt fram_cells5_1u_invertor_schematic gnd in out vdd
M0 (out in gnd gnd) nsvt25w=1.0 l=0.28 nfing=1.0 mult=1.0 srcefirst=1.0 mismatch=1.0 
M1 (out in vdd vdd) psvt25w=1.0 l=0.28 nfing=1.0 mult=1.0 srcefirst=1.0 mismatch=1.0 
.ends fram_cells5_1u_invertor_schematic


.subckt off_driver BL IN VDD
M1 (BL IN VDD VDD) psvt25w=0.4 l=0.28 nfing=1.0 mult=1.0 srcefirst=1.0 mismatch=1.0 
.ends off_driver


.subckt memory_cell bl gnd pl wn
M0 (net6 wn bl gnd) nsvt25w=0.4 l=0.28 nfing=1.0 mult=1.0 srcefirst=1.0 mismatch=1.0 
I0 (pl net6) conder Ec=1.9 dT=1e-09 l=5e-07 w=5e-07 p00=0.25 
.ends memory_cell


I0 (bl_v_0 gnd pl_h_0 wn_h_0) memory_cell 
I1 (bl_v_1 gnd pl_h_0 wn_h_0) memory_cell 
I2 (bl_v_2 gnd pl_h_0 wn_h_0) memory_cell 
I3 (bl_v_3 gnd pl_h_0 wn_h_0) memory_cell 
I4 (bl_v_4 gnd pl_h_0 wn_h_0) memory_cell 
I5 (bl_v_5 gnd pl_h_0 wn_h_0) memory_cell 
I6 (bl_v_6 gnd pl_h_0 wn_h_0) memory_cell 
I7 (bl_v_7 gnd pl_h_0 wn_h_0) memory_cell 
I8 (bl_v_0 gnd pl_h_1 wn_h_1) memory_cell 
I9 (bl_v_1 gnd pl_h_1 wn_h_1) memory_cell 
I10 (bl_v_2 gnd pl_h_1 wn_h_1) memory_cell 
I11 (bl_v_3 gnd pl_h_1 wn_h_1) memory_cell 
I12 (bl_v_4 gnd pl_h_1 wn_h_1) memory_cell 
I13 (bl_v_5 gnd pl_h_1 wn_h_1) memory_cell 
I14 (bl_v_6 gnd pl_h_1 wn_h_1) memory_cell 
I15 (bl_v_7 gnd pl_h_1 wn_h_1) memory_cell 
I16 (bl_v_0 gnd pl_h_2 wn_h_2) memory_cell 
I17 (bl_v_1 gnd pl_h_2 wn_h_2) memory_cell 
I18 (bl_v_2 gnd pl_h_2 wn_h_2) memory_cell 
I19 (bl_v_3 gnd pl_h_2 wn_h_2) memory_cell 
I20 (bl_v_4 gnd pl_h_2 wn_h_2) memory_cell 
I21 (bl_v_5 gnd pl_h_2 wn_h_2) memory_cell 
I22 (bl_v_6 gnd pl_h_2 wn_h_2) memory_cell 
I23 (bl_v_7 gnd pl_h_2 wn_h_2) memory_cell 
I24 (bl_v_0 gnd pl_h_3 wn_h_3) memory_cell 
I25 (bl_v_1 gnd pl_h_3 wn_h_3) memory_cell 
I26 (bl_v_2 gnd pl_h_3 wn_h_3) memory_cell 
I27 (bl_v_3 gnd pl_h_3 wn_h_3) memory_cell 
I28 (bl_v_4 gnd pl_h_3 wn_h_3) memory_cell 
I29 (bl_v_5 gnd pl_h_3 wn_h_3) memory_cell 
I30 (bl_v_6 gnd pl_h_3 wn_h_3) memory_cell 
I31 (bl_v_7 gnd pl_h_3 wn_h_3) memory_cell 
I32 (bl_v_0 gnd pl_h_4 wn_h_4) memory_cell 
I33 (bl_v_1 gnd pl_h_4 wn_h_4) memory_cell 
I34 (bl_v_2 gnd pl_h_4 wn_h_4) memory_cell 
I35 (bl_v_3 gnd pl_h_4 wn_h_4) memory_cell 
I36 (bl_v_4 gnd pl_h_4 wn_h_4) memory_cell 
I37 (bl_v_5 gnd pl_h_4 wn_h_4) memory_cell 
I38 (bl_v_6 gnd pl_h_4 wn_h_4) memory_cell 
I39 (bl_v_7 gnd pl_h_4 wn_h_4) memory_cell 
I40 (bl_v_0 gnd pl_h_5 wn_h_5) memory_cell 
I41 (bl_v_1 gnd pl_h_5 wn_h_5) memory_cell 
I42 (bl_v_2 gnd pl_h_5 wn_h_5) memory_cell 
I43 (bl_v_3 gnd pl_h_5 wn_h_5) memory_cell 
I44 (bl_v_4 gnd pl_h_5 wn_h_5) memory_cell 
I45 (bl_v_5 gnd pl_h_5 wn_h_5) memory_cell 
I46 (bl_v_6 gnd pl_h_5 wn_h_5) memory_cell 
I47 (bl_v_7 gnd pl_h_5 wn_h_5) memory_cell 
I48 (bl_v_0 gnd pl_h_6 wn_h_6) memory_cell 
I49 (bl_v_1 gnd pl_h_6 wn_h_6) memory_cell 
I50 (bl_v_2 gnd pl_h_6 wn_h_6) memory_cell 
I51 (bl_v_3 gnd pl_h_6 wn_h_6) memory_cell 
I52 (bl_v_4 gnd pl_h_6 wn_h_6) memory_cell 
I53 (bl_v_5 gnd pl_h_6 wn_h_6) memory_cell 
I54 (bl_v_6 gnd pl_h_6 wn_h_6) memory_cell 
I55 (bl_v_7 gnd pl_h_6 wn_h_6) memory_cell 
I56 (bl_v_0 gnd pl_h_7 wn_h_7) memory_cell 
I57 (bl_v_1 gnd pl_h_7 wn_h_7) memory_cell 
I58 (bl_v_2 gnd pl_h_7 wn_h_7) memory_cell 
I59 (bl_v_3 gnd pl_h_7 wn_h_7) memory_cell 
I60 (bl_v_4 gnd pl_h_7 wn_h_7) memory_cell 
I61 (bl_v_5 gnd pl_h_7 wn_h_7) memory_cell 
I62 (bl_v_6 gnd pl_h_7 wn_h_7) memory_cell 
I63 (bl_v_7 gnd pl_h_7 wn_h_7) memory_cell 
I64 (bl_v_0 gnd pl_h_8 wn_h_8) memory_cell 
I65 (bl_v_1 gnd pl_h_8 wn_h_8) memory_cell 
I66 (bl_v_2 gnd pl_h_8 wn_h_8) memory_cell 
I67 (bl_v_3 gnd pl_h_8 wn_h_8) memory_cell 
I68 (bl_v_4 gnd pl_h_8 wn_h_8) memory_cell 
I69 (bl_v_5 gnd pl_h_8 wn_h_8) memory_cell 
I70 (bl_v_6 gnd pl_h_8 wn_h_8) memory_cell 
I71 (bl_v_7 gnd pl_h_8 wn_h_8) memory_cell 
I72 (bl_v_0 gnd pl_h_9 wn_h_9) memory_cell 
I73 (bl_v_1 gnd pl_h_9 wn_h_9) memory_cell 
I74 (bl_v_2 gnd pl_h_9 wn_h_9) memory_cell 
I75 (bl_v_3 gnd pl_h_9 wn_h_9) memory_cell 
I76 (bl_v_4 gnd pl_h_9 wn_h_9) memory_cell 
I77 (bl_v_5 gnd pl_h_9 wn_h_9) memory_cell 
I78 (bl_v_6 gnd pl_h_9 wn_h_9) memory_cell 
I79 (bl_v_7 gnd pl_h_9 wn_h_9) memory_cell 
I80 (bl_v_0 gnd pl_h_10 wn_h_10) memory_cell 
I81 (bl_v_1 gnd pl_h_10 wn_h_10) memory_cell 
I82 (bl_v_2 gnd pl_h_10 wn_h_10) memory_cell 
I83 (bl_v_3 gnd pl_h_10 wn_h_10) memory_cell 
I84 (bl_v_4 gnd pl_h_10 wn_h_10) memory_cell 
I85 (bl_v_5 gnd pl_h_10 wn_h_10) memory_cell 
I86 (bl_v_6 gnd pl_h_10 wn_h_10) memory_cell 
I87 (bl_v_7 gnd pl_h_10 wn_h_10) memory_cell 
I88 (bl_v_0 gnd pl_h_11 wn_h_11) memory_cell 
I89 (bl_v_1 gnd pl_h_11 wn_h_11) memory_cell 
I90 (bl_v_2 gnd pl_h_11 wn_h_11) memory_cell 
I91 (bl_v_3 gnd pl_h_11 wn_h_11) memory_cell 
I92 (bl_v_4 gnd pl_h_11 wn_h_11) memory_cell 
I93 (bl_v_5 gnd pl_h_11 wn_h_11) memory_cell 
I94 (bl_v_6 gnd pl_h_11 wn_h_11) memory_cell 
I95 (bl_v_7 gnd pl_h_11 wn_h_11) memory_cell 
I96 (bl_v_0 gnd pl_h_12 wn_h_12) memory_cell 
I97 (bl_v_1 gnd pl_h_12 wn_h_12) memory_cell 
I98 (bl_v_2 gnd pl_h_12 wn_h_12) memory_cell 
I99 (bl_v_3 gnd pl_h_12 wn_h_12) memory_cell 
I100 (bl_v_4 gnd pl_h_12 wn_h_12) memory_cell 
I101 (bl_v_5 gnd pl_h_12 wn_h_12) memory_cell 
I102 (bl_v_6 gnd pl_h_12 wn_h_12) memory_cell 
I103 (bl_v_7 gnd pl_h_12 wn_h_12) memory_cell 
I104 (bl_v_0 gnd pl_h_13 wn_h_13) memory_cell 
I105 (bl_v_1 gnd pl_h_13 wn_h_13) memory_cell 
I106 (bl_v_2 gnd pl_h_13 wn_h_13) memory_cell 
I107 (bl_v_3 gnd pl_h_13 wn_h_13) memory_cell 
I108 (bl_v_4 gnd pl_h_13 wn_h_13) memory_cell 
I109 (bl_v_5 gnd pl_h_13 wn_h_13) memory_cell 
I110 (bl_v_6 gnd pl_h_13 wn_h_13) memory_cell 
I111 (bl_v_7 gnd pl_h_13 wn_h_13) memory_cell 
I112 (bl_v_0 gnd pl_h_14 wn_h_14) memory_cell 
I113 (bl_v_1 gnd pl_h_14 wn_h_14) memory_cell 
I114 (bl_v_2 gnd pl_h_14 wn_h_14) memory_cell 
I115 (bl_v_3 gnd pl_h_14 wn_h_14) memory_cell 
I116 (bl_v_4 gnd pl_h_14 wn_h_14) memory_cell 
I117 (bl_v_5 gnd pl_h_14 wn_h_14) memory_cell 
I118 (bl_v_6 gnd pl_h_14 wn_h_14) memory_cell 
I119 (bl_v_7 gnd pl_h_14 wn_h_14) memory_cell 
I120 (bl_v_0 gnd pl_h_15 wn_h_15) memory_cell 
I121 (bl_v_1 gnd pl_h_15 wn_h_15) memory_cell 
I122 (bl_v_2 gnd pl_h_15 wn_h_15) memory_cell 
I123 (bl_v_3 gnd pl_h_15 wn_h_15) memory_cell 
I124 (bl_v_4 gnd pl_h_15 wn_h_15) memory_cell 
I125 (bl_v_5 gnd pl_h_15 wn_h_15) memory_cell 
I126 (bl_v_6 gnd pl_h_15 wn_h_15) memory_cell 
I127 (bl_v_7 gnd pl_h_15 wn_h_15) memory_cell 
I128 (gnd in pl_v_0 vdd) fram_cells5_1u_invertor_schematic 
I129 (gnd in pl_v_1 vdd) fram_cells5_1u_invertor_schematic 
I130 (gnd in pl_v_2 vdd) fram_cells5_1u_invertor_schematic 
I131 (gnd in pl_v_3 vdd) fram_cells5_1u_invertor_schematic 
I132 (gnd in pl_v_4 vdd) fram_cells5_1u_invertor_schematic 
I133 (gnd in pl_v_5 vdd) fram_cells5_1u_invertor_schematic 
I134 (gnd in pl_v_6 vdd) fram_cells5_1u_invertor_schematic 
I135 (gnd in pl_v_7 vdd) fram_cells5_1u_invertor_schematic 
I136 (gnd in pl_v_8 vdd) fram_cells5_1u_invertor_schematic 
I137 (gnd in pl_v_9 vdd) fram_cells5_1u_invertor_schematic 
I138 (gnd in pl_v_10 vdd) fram_cells5_1u_invertor_schematic 
I139 (gnd in pl_v_11 vdd) fram_cells5_1u_invertor_schematic 
I140 (gnd in pl_v_12 vdd) fram_cells5_1u_invertor_schematic 
I141 (gnd in pl_v_13 vdd) fram_cells5_1u_invertor_schematic 
I142 (gnd in pl_v_14 vdd) fram_cells5_1u_invertor_schematic 
I143 (gnd in pl_v_15 vdd) fram_cells5_1u_invertor_schematic 
I144 (bl_h_0 IN VDD) off_driver 
I145 (bl_h_1 IN VDD) off_driver 
I146 (bl_h_2 IN VDD) off_driver 
I147 (bl_h_3 IN VDD) off_driver 
I148 (bl_h_4 IN VDD) off_driver 
I149 (bl_h_5 IN VDD) off_driver 
I150 (bl_h_6 IN VDD) off_driver 
I151 (bl_h_7 IN VDD) off_driver 
I152 (gnd bl_h_0 nb nt ref seb vdd) sense_amp 
I153 (gnd bl_h_1 nb nt ref seb vdd) sense_amp 
I154 (gnd bl_h_2 nb nt ref seb vdd) sense_amp 
I155 (gnd bl_h_3 nb nt ref seb vdd) sense_amp 
I156 (gnd bl_h_4 nb nt ref seb vdd) sense_amp 
I157 (gnd bl_h_5 nb nt ref seb vdd) sense_amp 
I158 (gnd bl_h_6 nb nt ref seb vdd) sense_amp 
I159 (gnd bl_h_7 nb nt ref seb vdd) sense_amp 
