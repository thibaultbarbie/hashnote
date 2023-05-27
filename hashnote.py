import argparse

if __name__== "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--recall", type=ascii)
    
    args, unknown = parser.parse_known_args()
    print(unknown)
    print(args)
