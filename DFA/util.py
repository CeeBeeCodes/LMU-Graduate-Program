from termcolor import colored
# VERIFICATION FUNCTIONS: Used To help the validity of the task at hand. 

# returns 0,1, and -1 if it is an invalid input. Checks if the input is either a "no" or "yes"
def GetCondition(prompt):
  if prompt == "yes" or prompt == "YES" or prompt == "Yes" or prompt == "Y" or prompt == "y":
    return 1
  if prompt == "no" or prompt == "NO" or prompt == "No" or prompt == "N" or prompt == "n":
    return 0
  return -1

# checks if the string can be in numeral form.
def ValidInt(analyzed_str):
  if analyzed_str.isnumeric():
    return True
  else:
    return False

# checks if the node parameter is inside the DFA.
def NodeInDFA(node, dfa):
  for i in dfa.keys:
    if node == i:
      return True
  return False

# Prints out the status of the node and its connecting edges.
def PrintOutNodesAndEdges(dfa):
      for node in dfa.keys:
        edges = dfa.node_dictionary[node]
        edge0 = str(edges[0])
        edge1 = str(edges[1])
        if edge0 == "-1":
          edge0 = "??"
        if edge1 == "-1":
          edge1 = "??"

        print(colored("[  Node " + str(node) + ": " + "edge 0" + "--> " + "Node " + edge0 + " || " + "edge 1" + "--> "  + "Node " + edge1 + "  ]", "magenta"))

# DFA BUILDER FUNCTIONS: Functions that collect the information to create a working DFA.  

def EstablishNumberOfNodes(dfa):
  valid_input = False
  while valid_input == False:
    num_of_nodes = input('Please enter number of nodes: ')
    if num_of_nodes.isnumeric() == True:
      dfa.number_of_nodes = num_of_nodes
      valid_input = True   
    else:
      print(colored("Not a Valid Number. Please Try Again.", 'red'))

def EstablishStartState(list_of_nodes, dfa):
  valid_input = False
  while valid_input == False:
    start_node = input("Out of the nodes " + str(list_of_nodes) + ", pick the starting node: ")
    if ValidInt(start_node) == True:
      for node in list_of_nodes:
        if node == int(start_node):
            dfa.q0 = int(start_node)
            valid_input = True
            break
    if valid_input == False:
      print(colored("Invalid start node. Please pick from the list.", 'red'))

def EstablishFinalStates(dfa):
  for node in dfa.keys:
    valid_input = False
    while valid_input == False:
      final_state = input("Is node " + str(node) + " a final state? [Y/n] ")
      value = GetCondition(final_state)
      if value == 1:
        dfa.final_states.append(True)
        valid_input = True;
      elif value == 0:
        dfa.final_states.append(False)
        valid_input = True;
      else:
        print(colored("Invalid Input: Please try again.", "red"))

def ConnectEdgesToNodes(dfa):
  avail_nodes = dfa.keys
  for node in avail_nodes:  
    for edge in range(2):
      valid_input = False
      while valid_input == False:
        PrintOutNodesAndEdges(dfa)
        print("Choose out of the available nodes: ", avail_nodes)
        proposed_node = input("What node does edge " + str(edge) + " of node " + str(node) + " go to? ")
        if ValidInt(proposed_node) and NodeInDFA(int(proposed_node), dfa):
          dfa.node_dictionary[node][edge] = int(proposed_node)
          valid_input = True
        else:
          print(colored("Invalid Input. Please try again", 'red'))

 # LANGUAGE VALIDITY FUNCTIONS: After DFA is created these functions check the validity of the language.

def ValidString(language):
  for c in language:
    if c != "1" and c != "0":
      return False
  return True

def NodeIsInFinalState(node, dfa):
  return dfa.final_states[node]
