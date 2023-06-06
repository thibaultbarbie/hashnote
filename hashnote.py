import argparse
import os

if __name__== "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--recall", help="Recall the note from the hash.", type=ascii)
    
    args, unknown = parser.parse_known_args()
    args = vars(args)

    if len(unknown)>0:
        all_notes = []
        if os.path.isfile('notes.csv'):
            with open('notes.csv', 'r', newline='') as notefile:
                lines=notefile.readlines()
                for row in lines:
                    all_notes.append(row.split(" ")[1])
        with open('notes.csv', 'a', newline='') as notefile:
            for i, note in enumerate(unknown):
                # We do not add the note if it is already saved
                if note in all_notes:
                    index = all_notes.index(note)
                    print(lines[index].split(" ")[0])
                else:
                    notefile.write(f"{len(all_notes)+i:x} {note} \n")
                    print(f"{len(all_notes)+i:x}")
