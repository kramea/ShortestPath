# ShortestPath
##Bi-objective time-dependent dynamic shortest path problem for modal choice application for the SF bay area

Shortest path problems have a numerous applications in the transportation field. When it comes to mode choice problems, there are number of factors that are taken into account while choosing the optimal mode between two points. Typically, the factors include total travel time, cost of travel, inconvenience, resource consumption and so on, and the importance of each factor may vary from person to person. This project will limit the number of objectives to two, and will compare the optimal mode choices for different income groups for the Bay Area Rapid Transit (BART) network in the San Francisco Bay Area. It will also limit the study for ‘peak hours’, since the off-peak mode competition can give an unfair advantage to driving as the train schedule intervals are wide and no congestion delays happen to driving.
	
This project will focus on the competition between the three modes of choice (Driving alone, Carpooling, taking transit) for the different income groups ranging from minimum wage to top 5%, for the BART train network in the Bay Area. The objective function is two-fold in this case, it is designed to first minimize the total travel time, and second, it is designed to minimize the total travel cost, and the optimal mode based on these two is then selected.  

The shortest path algorithm was developed in Python and the BART network and shortest path were determined using networkx package.
