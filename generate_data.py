from random import randint
import argparse

def parse_arguments():
    """Manage input arguments for program"""
    ap = argparse.ArgumentParser()
    ap.add_argument("-n", "--samples", required=True, help="first operand")
    ap.add_argument("-o", "--output_file", required=True, help="second operand")
    args = vars(ap.parse_args())
    return args

def main(args):
    """Main function, generate data"""
    nationalities = ["english","russian","french","spanish","italian","swedish","colombian",\
        "mexican","canadian","costarican","argentinian","brazilian","japanese","chinese",\
        "korean","vietnamese","taiwanese","mongolian"]
    conditions = ["heart","viral","cancer","bacteria","kidney","diabetes"]
    gender = ["male","female"]

    with open(args["output_file"],"w") as f:
        f.write("ZipCode,Nationality,Condition,Gender,Age\n")
        for elemento in range(int(args["samples"])):
            zcode = randint(10000,19000)
            nationality = nationalities[randint(0,len(nationalities)-1)]
            condition = conditions[randint(0,len(conditions)-1)]
            gen = gender[randint(0,len(gender)-1)]
            f.write("{},{},{},{},{}\n".format(zcode,nationality,condition,gen,randint(10,80)))

if __name__ == '__main__':
    arguments = parse_arguments()
    main(arguments)
