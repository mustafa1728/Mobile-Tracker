from network.routing import RoutingMapTree

def main():
	database = RoutingMapTree()
	f = open("actions/actions1.txt", "r")
	for line in f:
		database.performAction(line)
	print(database)

if __name__ == "__main__":
    main()