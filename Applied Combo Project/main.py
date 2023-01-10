print('\n\n')
"""""""""""""""""""""""""""""""""""""""""""""""""""
Math 3012 Project
Student: Rishit Sarkar, Srirag Tatavarti, Anish Kayarthodi
"""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""
CycleOfLengthThree method checks if this is a cycle 
of length 3. If there is, then 1 is returned. Otherwise, 0 is returned.
"""""""""""""""""""""""""""""""""""""""""""""""""""
def CycleOfLengthThree(lon, iMaxVer):
	iRet = 0 
	iCount = 0 

	for i in range(1, iMaxVer+1):

		if iRet == 1:
			break 
		iCount = len(lon[i])

		if iCount < 2:
			continue
		else:
			for j in range(iCount-1):
				iSecond = list(lon[i])[j] 
				iThird = list(lon[i])[j+1] 

				if iThird in lon[iSecond]:
					print("\nFound a triangle (cycle of length 3):", i, iSecond, iThird)
					iRet = 1
					break
	return iRet 

"""""""""""""""""""""""""""""""""""""""""""""""""""
IsGraphPlanar method checks if a graph is Planar 
or not. If planar, 1 is returned. Otherwise, 0 is returned.
"""""""""""""""""""""""""""""""""""""""""""""""""""
def IsGraphPlanar(lon, iMaxVer, iEdges, faces):
	iPlanar = 0

	if iMaxVer < 3:
		iPlanar = 1 
		return iPlanar
	if iMaxVer - iEdges + faces == 2:
		if CycleOfLengthThree(lon, iMaxVer) == 1:
			# Theorem 1. e <= 3v - 6
			if iEdges <= (3*iMaxVer - 6):
				print(f"\nSatisfies e ≤ 3v - 6: {int(iEdges)} ≤ 3 * {iMaxVer} - 6 = {int(3 * iMaxVer - 6)}")
				print(f"\nSatisfies Euler's Formula (v - e + f = 2): {iMaxVer} - {int(iEdges)} + {faces} = 2")
				iPlanar = 1
			else:
				print(f"Does not satisfy e ≤ 3v - 6: {int(iEdges)} ≤ 3 * {iMaxVer} - 6 = {int(3 * iMaxVer - 6)}")
		else:
			# Theorem 2. e <= 2v - 4
			if iEdges <= (2*iMaxVer - 4):
				print(f"\nSatisfies e ≤ 2v - 4: {int(iEdges)} ≤ 2 * {iMaxVer} - 4 = {int(2 * iMaxVer - 4)}")
				print(f"\nSatisfies Euler's Formula (v - e + f = 2): {iMaxVer} - {int(iEdges)} + {faces} = 2")
				iPlanar = 1
			else:
				print(f"\nDoes not satisfy e ≤ 2v - 4: {int(iEdges)} ≤ 2 * {iMaxVer} - 4 = {int(2 * iMaxVer - 4)}")
	else:
		print(f"\nDoes not satisfy Euler's Formula (v - e + f = 2): {iMaxVer} - {int(iEdges)} + {faces} = {int(iMaxVer - iEdges + faces)}")
		
	return iPlanar			

"""""""""""""""""""""""""""""""""""""""""""""""""""
PrintConnectedVertices method to print all the 
nodes that are connected with other nodes.
"""""""""""""""""""""""""""""""""""""""""""""""""""
def PrintConnectedVertices(lon, iMaxVer):
	for i in range(1, iMaxVer+1):
		print(f"\nDegree of Node {i}: {len(lon[i])}")
		print(f"Connected Vertices from Node {i}:") 
		for j in range(len(lon[i])):
			print(list(lon[i])[j]) 
	return

"""""""""""""""""""""""""""""""""""""""""""""""""""
AddEdge method to add edges to the graph.
"""""""""""""""""""""""""""""""""""""""""""""""""""
def AddEdge(lon, iNode1, iNode2):
	lon[iNode1].add(iNode2)
	lon[iNode2].add(iNode1)

"""""""""""""""""""""""""""""""""""""""""""""""""""
NumFaces method to find the number of faces on the graph.
"""""""""""""""""""""""""""""""""""""""""""""""""""
def NumFaces(edges):
	counter = 0
	numFaces = 1
	firstvert = 1
	tempcycle = [firstvert]
	tempvert = -1
	while True:
		if tempvert * -1 <= len(edges[firstvert]):
			secondvert = edges[firstvert][tempvert]
		else:
			x = edges[tempcycle[-2]].index(tempcycle[-1])
			del edges[firstvert][0]
			firstvert = tempcycle[-2]
			if edges[firstvert] != []:
				del edges[firstvert][edges[firstvert].index(tempcycle[-1])]
				del tempcycle[-1]
				if not any(edges):
					break
				else:
					secondvert = edges[firstvert][x - 1]
			else:
				firstvert += 1
				tempcycle = [firstvert]
				tempvert = -1
				secondvert = edges[firstvert][tempvert]
		if secondvert not in tempcycle:
			tempcycle += [secondvert]
			tempvert = -1
		elif secondvert != tempcycle[-1] and secondvert != tempcycle[-2]:
			finalcycle = tempcycle[tempcycle.index(secondvert):]
			for i in range(len(finalcycle) - 1):
				del edges[finalcycle[i]][edges[finalcycle[i]].index(finalcycle[i+1])]
			del edges[finalcycle[-1]][edges[finalcycle[-1]].index(finalcycle[0])]
			numFaces += 1
			if not any(edges):
				break
			firstvert = 1
			while True:
				if edges[firstvert] == []:
					firstvert += 1
				else:
					break
			tempvert = -1
			tempcycle = [firstvert]
			secondvert = firstvert
			counter += 1
			if counter == 7:
				break
		else:
			tempvert -= 1
			secondvert = firstvert
		firstvert = secondvert
	return numFaces

"""""""""""""""""""""""""""""""""""""""""""""""""""
This is the logic method that incorporates all previous functions.
"""""""""""""""""""""""""""""""""""""""""""""""""""
def logic(file):
	print(f'{file}')
	check = True
	inputgraph = open(file).read().strip().split('\n')
	iMaxVertices = int(inputgraph[0])
	print(f"Vertices: {iMaxVertices}")
	print(f"Edges: {len(inputgraph) - 1}")
	print("\nEdge entries:")

	# Creating a set of TotalVertices+1.
	listOfNode = [set() for i in range(iMaxVertices + 1)]
	edgenum = 0
	for edge in inputgraph[1:]:
		edgenum += 1
		if list(edge)[0].isdigit():
			node1, node2 = edge.split()
			node1 = int(node1) 
			node2 = int(node2) 
			# We assume node index number can't be more than number of vertices.
			if node1 > iMaxVertices or node2 > iMaxVertices:
				print("\nInvalid entry (node number is higher than vertices.)")
				check = False
				break
			else:
				print(node1, node2)
				AddEdge(listOfNode, node1, node2)
		else:
			print(f"\nPlease enter valid positive integers for edge {edgenum}.")
			check = False
			break

	if check:
		# PrintConnectedVertices(listOfNode, iMaxVertices)
		edgelist = [sorted(list(i)) for i in listOfNode]
		if IsGraphPlanar(listOfNode, iMaxVertices, len(inputgraph) - 1, NumFaces(edgelist)) == 1:
			print("Graph is planar\n\n\n")
		else:
			print("Graph is not planar\n\n")

"""""""""""""""""""""""""""""""""""""""""""""""""""
This is the main method that tests logic with different graphs.
"""""""""""""""""""""""""""""""""""""""""""""""""""
def main():
	logic("k5.txt")
	logic("k33.txt")
	logic("test-graph1.txt")
	logic("test-graph2.txt")
	logic("test-graph3.txt")
	logic("test-graph4.txt")
	logic("test-graph5.txt")
	logic("test-graph6.txt")
	logic("test-graph7.txt")
	logic("test-graph8.txt")

if __name__ == "__main__":
	main()