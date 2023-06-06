import argparse
import csv
import os

if __name__== "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--recall", help="Recall the note from the hash.", type=ascii)
    
    args, unknown = parser.parse_known_args()
    args = vars(args)

    if len(unknown)>0:
        if os.path.isfile('notes.csv'): 
            num_lines = sum(1 for _ in open('notes.csv'))
        else:
            num_lines = 0
        with open('notes.csv', 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            
            for i, note in enumerate(unknown):
                spamwriter.writerow([f'{num_lines+i:x}', note])
