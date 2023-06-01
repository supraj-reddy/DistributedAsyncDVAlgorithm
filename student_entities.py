"""
CPSC 5510, Seattle University, Project #3
:Author: Sai Supraj Reddy M
:Version: s23
"""

# YOU MAY NOT ADD ANY IMPORTS
from entity import Entity
from student_utilities import to_layer_2


def common_init(self):
    """
    You may call a common function like this from your individual __init__ 
    methods if you want.
    """
    print("Entity: {} initializing".format(self.node))
    print(self.__str__())

    if self.node == 0:
        to_layer_2(self.node, 1, self.distance_table[self.node])
        to_layer_2(self.node, 2, self.distance_table[self.node])
        to_layer_2(self.node, 3, self.distance_table[self.node])
    elif self.node == 1:
        to_layer_2(self.node, 0, self.distance_table[self.node])
        to_layer_2(self.node, 2, self.distance_table[self.node])
    elif self.node == 2:
        to_layer_2(self.node, 0, self.distance_table[self.node])
        to_layer_2(self.node, 1, self.distance_table[self.node])
        to_layer_2(self.node, 3, self.distance_table[self.node])
    elif self.node == 3:
        to_layer_2(self.node, 0, self.distance_table[self.node])
        to_layer_2(self.node, 2, self.distance_table[self.node])


def common_update(self, packet):
    """
    You may call a common function like this from your individual update 
    methods if you want.
    """
    src = packet.src
    dest = packet.dest
    mincost = packet.mincost
    changes = False

    print("node {}: Update from {} received".format(self.node,src))

    # Update distance table based on received packet
    for i in range(len(mincost)):
        self.distance_table[src][i] = mincost[i]
        if mincost[i] < float('inf') and mincost[i] + self.distance_table[src][dest] < self.distance_table[dest][i]:
            self.distance_table[dest][i] = mincost[i] + self.distance_table[src][dest]
            changes = True

    if changes:
        print("changes based on the update")

        print(self.__str__())

        print("sending mincost updates to neighbors..")

        # Send updated minimum costs to all other nodes
        if self.node == 0:
            to_layer_2(self.node, 1, self.distance_table[self.node])
            to_layer_2(self.node, 2, self.distance_table[self.node])
            to_layer_2(self.node, 3, self.distance_table[self.node])
        elif self.node == 1:
            to_layer_2(self.node, 0, self.distance_table[self.node])
            to_layer_2(self.node, 2, self.distance_table[self.node])
        elif self.node == 2:
            to_layer_2(self.node, 0, self.distance_table[self.node])
            to_layer_2(self.node, 1, self.distance_table[self.node])
            to_layer_2(self.node, 3, self.distance_table[self.node])
        elif self.node == 3:
            to_layer_2(self.node, 0, self.distance_table[self.node])
            to_layer_2(self.node, 2, self.distance_table[self.node])

    else:
        print("no changes in node {}, so nothing to do".format(self.node))
        print(self.__str__())

    


def common_link_cost_change(self, to_entity, new_cost):
    """
    You may call a common function like this from your individual 
    link_cost_change methods if you want.
    Note this is only for extra credit and only required for Entity0 and 
    Entity1.
    """
    self.distance_table[self.node][to_entity] = new_cost

    if self.node == 0:
        to_layer_2(self.node, 1, self.distance_table[self.node])
        to_layer_2(self.node, 2, self.distance_table[self.node])
        to_layer_2(self.node, 3, self.distance_table[self.node])
    elif self.node == 1:
        to_layer_2(self.node, 0, self.distance_table[self.node])
        to_layer_2(self.node, 2, self.distance_table[self.node])


class Entity0(Entity):
    """Router running a DV algorithm at node 0"""
    def __init__(self):
        super().__init__()
        self.node = 0
        self.distance_table[0] = [0,1,3,7]
        common_init(self)

    def update(self,packet):
        common_update(self,packet)

    def link_cost_change(self,to_entity,new_cost):
        common_link_cost_change(self,to_entity,new_cost)


class Entity1(Entity):
    """Router running a DV algorithm at node 1"""
    def __init__(self):
        super().__init__()
        self.node = 1
        self.distance_table[1] = [1,0,1,float('inf')]
        common_init(self)

    def update(self,packet):
        common_update(self,packet)

    def link_cost_change(self,to_entity,new_cost):
        common_link_cost_change(self,to_entity,new_cost)


class Entity2(Entity):
    """Router running a DV algorithm at node 2"""
    def __init__(self):
        super().__init__()
        self.node = 2
        self.distance_table[2] = [3,1,0,2]
        common_init(self)

    def update(self,packet):
        common_update(self,packet)


class Entity3(Entity):
    """Router running a DV algorithm at node 3"""
    def __init__(self):
        super().__init__()
        self.node = 3
        self.distance_table[3] = [7,float('inf'),2,0]
        common_init(self)

    def update(self,packet):
        common_update(self,packet)
