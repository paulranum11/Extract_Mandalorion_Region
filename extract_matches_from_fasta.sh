grep --group-separator "" -A 1 -h -f trimmed_readIDs ./Cell_1/2D_trimmed_l_filtered.fasta | sed '/^\s*$/d' > trimmed_output.fasta
