from util import *
from termcolor import colored


class DFA():
  def __init__ (self):
    self.number_of_nodes = 0
    self.q0 = 0
    self.final_states = []
    self.node_dictionary = {}
    self.keys = []
    
def RunThroughDFA(language, dfa):
  if language == "":
    if NodeIsInFinalState(dfa.q0, dfa):
       print("The DFA accepts this string", language)
    else:
      print("The DFA rejects this string", language)
  if ValidString(language):
    current_node = dfa.q0
    for i, c in enumerate(language):
      next_node = dfa.node_dictionary[current_node][int(c)]
      current_node = next_node
      if i == len(language) - 1:
        if NodeIsInFinalState(current_node, dfa):
          print("The DFA accepts this string", language)
        else:
          print("The DFA rejects this string", language)
  else:
    print("The language is not within the alphabet - REJECT")
    
########################## MAIN FUNCTION###############################################

def main():

	print("------------Let's Construct a DFA------------")
	dfa = DFA()
	print("----", colored("(1)", 'blue'), "---- Let's Pick the Number of Nodes")

	EstablishNumberOfNodes(dfa)

	for node in range(int(dfa.number_of_nodes)):
  		dfa.node_dictionary[node] = []

	dfa.keys = list(dfa.node_dictionary.keys())

	print(colored("Created nodes", 'magenta'), colored(dfa.keys, 'magenta'))

# picks a start state
	print("----", colored("(2)", 'blue'), "---- Let's Establish the Start States (q0)")
	EstablishStartState(dfa.keys, dfa)

# picks final states.
	print("----", colored("(3)", 'blue'), "---- Let's Establish the Final States ({0..1..})")
	EstablishFinalStates(dfa)

	for node in dfa.keys:
  		dfa.node_dictionary[node] = [-1, -1] #key = node, value = list [edge 0 node, edge 1 node]

# picks nodes edges connect to.
	print("----", colored("(4)", 'blue'), "---- Connect Edges to Nodes (node 0: edge 0 --> node 1 || edge 1 --> node 2)  --> = 'goes to'")
	ConnectEdgesToNodes(dfa)

# Completed DFA
	print("----", colored("(4)", 'blue'), "---- DFA Completed. Now we can run strings through the DFA!")
	
#####################################################################
# test out strings

	# DFA that accepts strings with an even # of 0s and 1s
	#s1 = "01110110100" # REJECT
	#s2 = "00001111" # ACCEPT
	#s3 = "0110010010" # ACCEPT
	#s4 = "1110" # REJECT
	#s5 = "000s11r"# REJECT
	#s6 = "" # ACCEPT
	
	# DFA that accepts strings that starts with 1 and contains 10 or starts with 0 and contains the 01
	s1 = "1000101" # ACCEPT
	s2 = "00101010111" # ACCEPT
	s3 = "1111011" # ACCEPT
	s4 = "111" # REJECT
	s5 = "0000" # REJECT
	s6 = "10" # ACCEPT
	
	#TEST OUT YOUR OWN STRINGS BELOW:
	#s1 =
	#s2 = 
	#s3 = 
	

	RunThroughDFA(s1, dfa)
	RunThroughDFA(s2, dfa)
	RunThroughDFA(s3, dfa)
	RunThroughDFA(s4, dfa)
	RunThroughDFA(s5, dfa)
	RunThroughDFA(s6, dfa)
	
if __name__ == '__main__':
    main()
