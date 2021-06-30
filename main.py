from network.routing import RoutingMapTree
import argparse

def parse_args():
	parser = argparse.ArgumentParser(description="Mobile Tracking")
	parser.add_argument(
	    "--actions",
	    default="actions/actions1.txt",
	    type=str,
	    help="which actions file to use",
	)
	args = parser.parse_args()
	return args.actions

def main():
	filename = parse_args()
	database = RoutingMapTree()
	f = open(filename, "r")
	for line in f:
		database.performAction(line)
	print(database)

if __name__ == "__main__":
    main()