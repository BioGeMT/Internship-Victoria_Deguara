import pandas as pd 
import argparse
from Bio import Align
aligner = Align.PairwiseAligner()
aligner.mode = "global"

def get_seed6mer(noncodingRNA):
    return [noncodingRNA[1:7],noncodingRNA[2:8],'A'+noncodingRNA[1:6]]

def get_seed7mer(noncodingRNA) :
    return [noncodingRNA[1:8],'A'+noncodingRNA[1:7]]

def get_seed8mer(noncodingRNA):
    return ['A'+noncodingRNA[1:8]]

aligner.open_left_deletion_score = 0.000
aligner.extend_left_deletion_score = 0.000
aligner.open_right_deletion_score = 0.000
aligner.extend_right_deletion_score = 0.000

def check_match(row, seed_function):
    seeds = seed_function(row["noncodingRNA"])
    return max(aligner.score(row["gene"], seed) for seed in seeds)

def check_match_6mer(row):
    return check_match(row, get_seed6mer)

def check_match_7mer(row):
    return check_match(row, get_seed7mer)

def check_match_8mer(row):
    return check_match(row, get_seed8mer)

def seed_match_df():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    args = parser.parse_args()

    dfi = pd.read_csv(args.input_file)[["gene", "noncodingRNA", "label"]]

    dfi["seed6mer"] = dfi.apply(check_match_6mer, axis=1)
    dfi["seed7mer"] = dfi.apply(check_match_7mer, axis=1)
    dfi["seed8mer"] = dfi.apply(check_match_8mer, axis=1)

    dfi.to_csv(args.output_file, sep="\t", index=False)

if __name__ == "__main__":
    seed_match_df()