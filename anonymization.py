from cn.protect import Protect
from cn.protect.privacy import KAnonymity
from cn.protect.quality import Loss
from cn.protect.hierarchy import DataHierarchy, OrderHierarchy, IntervalHierarchy
import pandas as pd
import argparse

def parse_arguments():
    """Manage input arguments for program"""
    ap = argparse.ArgumentParser()    
    ap.add_argument("-k", "--anonymity_level", required=True, help="first operand")
    ap.add_argument("-d", "--input_file", required=True, help="second operand")
    ap.add_argument("-o", "--output_file", required=True, help="second operand")
    args = vars(ap.parse_args())
    return args

def main(args):
    """Main function actually do the anonymization and save result to specified file"""
    dataset = pd.read_csv(args["input_file"])
    print(dataset.head())

    prot = Protect(dataset,KAnonymity(args["anonymity_level"]))
    prot.quality_model = Loss()

    prot.supression = .2

    for col in dataset.columns:        
        prot.itypes[col] = 'quasi'

    prot.hierarchies.Age = OrderHierarchy('interval',5,2,2,2,2)
    prot.hierarchies.Nationality = DataHierarchy(pd.read_csv("data/Nationality.csv"))
    prot.hierarchies.Condition = DataHierarchy(pd.read_csv("data/Condition.csv"))
    prot.hierarchies.Gender = DataHierarchy(pd.read_csv("data/Gender.csv"))
    prot.hierarchies.ZipCode = OrderHierarchy('interval',1000,2,2,2,2)

    priv = prot.protect()
    print(priv)
    priv.to_csv(args["output_file"],index=False)
    print(prot.stats)

if __name__ == '__main__':
    arguments = parse_arguments()
    main(arguments)