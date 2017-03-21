import math
import heapq
import re
'''
this algorithm uses a minimum spaning tree followed by a traversal with raidial sorting 
to build an approximate solution to the traveling salesman problem in n dimensions in approximately n squared time.
'''
#get the magnitude of the vector.
def get_magnitude(vector):
    mag = 0
    for i in vector:
        mag += i**2
        
    return math.sqrt(mag)

#get the angle between two vectors
def get__angle(vector1,vector2):
    
    dot = 0
    for i,x in zip(vector1,vector2):
        dot+=i*x
    #return large integer instead of float for python's sorting comparison.
    return int(10000*math.acos(dot/(get_magnitude(vector1)*get_magnitude(vector2))))

#computes differnce of angle of point2 from point1 and angle of point3 from point1
def get_angle(point1,point2,point3):
    vector1 = []
    vector2 = []
    vector3 = []
    
    for i in xrange(len(point1)):
        vector1.append(point2[i] - point1[i])
        vector2.append(point3[i] - point1[i])
        vector3.append(1)
    
    
    return get__angle(vector1, vector3) - get__angle(vector2, vector3)
        

    
def distance(point1,point2):
    d = 0
    for i in xrange(len(point1)):
        d+=(point1[i] - point2[i])**2
        
    #math.sqrt returns float
    return math.sqrt(d)


#graph that makes a complete(fully connected) graph from list of points.
class graph:
    m_points = []
    edge_lengths ={}
    
    def __init__(self,points):
        self.m_points = points
        for i in xrange(len(self.m_points)):
            for x in xrange(i+1,len(self.m_points)):
                self.edge_lengths[(i,x)] = distance(self.m_points[i],self.m_points[x])
                
    def get_edge_length(self,x,y):
        #make order not matter.
        if y < x:
            x,y=y,x
        if (x,y) in self.edge_lengths:    
            return self.edge_lengths[x,y]
        else:
            return None
            
        



def traveling_salesman(points):
    #Use prim's algorithm to make to minimal spanning tree.
    #https://en.wikipedia.org/wiki/Prim's_algorithm
    
    #init complete graph.
    G = graph(points)
    current_point = 0
    
    #start from first point in the list
    visited = [current_point]
    edges = []
    #heap to keep track of smallest edges.
    edge_heap = []
    
    #provides lookup table for nodes with odd degree.
    odd_vertices = []
    odd_vertex_counter = {i:0 for i in xrange(len(points))}
    
    #this section should run in approximately n squared time.
    while len(visited) < len(points):
        for i in xrange(len(points)):
            if i not in visited:
                #add each edge from the current node whose end is not in the tree
                e = G.get_edge_length(current_point,i)
                #Only first item in a tuple is compared
                heapq.heappush(edge_heap,(e,current_point,i))
                #should create pairs where edge[1]->edge[2] and edge[1]==0 is the root
                
                    

        #update the current edge
        edge_info = heapq.heappop(edge_heap)
        #find the smallest edge that is not in the tree.
        while edge_info[2] in visited:
            edge_info = heapq.heappop(edge_heap)
    
            
        visited.append(edge_info[2])
        #add the edge
        edges.append((edge_info[1],edge_info[2]))
        
        
        
        for e in [edge_info[1],edge_info[2]]:
            if e in odd_vertices:
                odd_vertices.remove(e)
                
            else:
                odd_vertices.append(e)
        
        
        current_point = edge_info[2]
   

     
    #end prim's algorithm.
    
    #get smallest perfect matching from the odd vertices
    #use heap to order all possible edges.
    match_heap = []
    
    for i in odd_vertices:
        for x in odd_vertices:
            if i != x:
                l = G.get_edge_length(i,x)
                heapq.heappush(match_heap,(l,i,x))
    
    #create a matching                                 
    used_vertices = []
    perfect_matching = []
    while len(used_vertices) < len(odd_vertices):
        edge_info = heapq.heappop(match_heap)
        if (edge_info[1] not in used_vertices) and (edge_info[2] not in used_vertices):
            used_vertices.append(edge_info[1])
            used_vertices.append(edge_info[2])
            perfect_matching.append((edge_info[1],edge_info[2]))
        
    
    #combine the two graphs to create a graphs with vertices of even degree, Which can have a hamiltonian cycle.
    new_graph = perfect_matching + edges
    edge_table = {}
    for i in xrange(len(points)):
        edge_table[i]=[]
        
    hamiltonian_cycle = [0]
    for e in new_graph:
        edge_table[e[0]].append(e[1])
        edge_table[e[1]].append(e[0])

    
    #randomly traverse the edges of the new graph    
    current_vertex  = 0
    not_disconnected = []
    while len(hamiltonian_cycle) < len(points):
        
        #delete edges as we go
        last_vertex = current_vertex
        #check if node is connected
        if edge_table[current_vertex]:
            current_vertex = edge_table[last_vertex].pop()
            edge_table[current_vertex].remove(last_vertex)
            #if there will still more edges left after we leave this node mark it
            if edge_table[current_vertex] > 1:
                not_disconnected.append(current_vertex)
        else:
            #If the current node is disconnected.
            #Try the next connected node.
            current_vertex = not_disconnected.pop()
            
        
        
        if current_vertex not in hamiltonian_cycle:
            hamiltonian_cycle.append(current_vertex)
        
                
    
        
    return (hamiltonian_cycle, edges)

     

lines = open('points.txt').readlines()
points = []
for line in lines:
    point = re.findall(r"[-+]?\d*\.\d+|\d+",line)
    for i in xrange(len(point)):
        point[i] = float(point[i])
    if len(point):
        points.append(point)

#store points for h. cycle.
pe= traveling_salesman(points)

h_file = open('hamiltonian_cycle.txt','w')
for i in pe[0]:
    h_file.write(str(points[i][0]) + ' ' + str(points[i][1]) + '\n')
h_file.close()


#store edge for mst.
h_file = open('minimum_spanning_tree.txt','w')
for i in pe[1]:
    h_file.write(str(points[i[0]][0]) + ' ' + str(points[i[0]][1]) + ' '+ str(points[i[1]][0]) + ' '+ str(points[i[1]][1])  + '\n')
h_file.close()



            
