/*
A KBase module: kb_Msuite
This SDK module is developed to wrap the open source package CheckM which consists of a set of tools 
for assessing the quality of genomes recovered from isolates, single cells, or metagenomes. 
CheckM consists of a series of commands in order to support a number of different analyses and workflows.

References: 
CheckM in github: http://ecogenomics.github.io/CheckM/
CheckM docs: https://github.com/Ecogenomics/CheckM/wiki

Parks DH, Imelfort M, Skennerton CT, Hugenholtz P, Tyson GW. 2015. CheckM: assessing the quality of microbial genomes recovered from isolates, single cells, and metagenomes. Genome Research, 25: 1043–1055.
*/

module kb_Msuite {
    /*
    A boolean - 0 for false, 1 for true.
        @range (0, 1)
    */
    typedef int boolean;

    typedef string FASTA_format; /*".fna"*/

    /*  
        required params:
        bin_folder: folder path that holds all putative genome files with (fa as the file extension) to be checkM-ed
        out_folder: folder path that holds all putative genome files with (fa as the file extension) to be checkM-ed
        checkM_cmd_name: name of the CheckM workflow,e.g., lineage_wf or taxonomy_wf
        workspace_name: the name of the workspace it gets saved to.

        optional params:
        file_extension: the extension of the putative genome file, should be "fna"
        thread: number of threads; default 1
    */
    typedef structure {
        string bin_folder;
        string out_folder;
        string checkM_cmd_name;
        string workspace_name;

        string file_extension;
        int thread;
    } CheckMInputParams;

    /*
        checkM_results_folder: folder path that stores the CheckM results
        report_name: report name generated by KBaseReport
        report_ref: report reference generated by KBaseReport
    */
    typedef structure{
        string checkM_results_folder;
        string report_name;
        string report_ref;
    } CheckMResults;

    funcdef run_checkM(CheckMInputParams params)
        returns (CheckMResults returnVal) authentication required;
};
