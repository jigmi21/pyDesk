import argparse
from core.stats import run_stats

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type = str, help= "The path to the directory")
    arg = parser.parse_args()