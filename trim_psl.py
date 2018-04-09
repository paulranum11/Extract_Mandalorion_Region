MANDALORION_PSL_PATH = "/Shared/MORL/Analysis/ranum/Nanopore/OHC_12_04052018_Shortened/Cell_1/2D_trimmed_l_gmapoutput_filtered.psl"

write_psl = open("trimmed_output.psl", "w")
write_readIDs = open("trimmed_readIDs", "w")

with open(MANDALORION_PSL_PATH) as file:
    for line in file:
        splitted_line = line.split()
        if splitted_line[13] == '9' and int(splitted_line[15]) >= 54535269 and int(splitted_line[16]) <= 54567739:
            out_line = '\t'.join(splitted_line)
            write_psl.write(out_line + "\n")
write_psl.close()

with open("trimmed_output.psl", "r") as file:
    for line in file:
        splitted_line = line.split()
        readID = splitted_line[9]
        write_readIDs.write(readID + "\n")
write_readIDs.close()
