Project Overview
This project simulates an air traffic control system that determines the optimal routes between airports to minimize total travel distance using Prim's Algorithm. The project uses Python libraries such as NumPy, NetworkX, Matplotlib, and Tkinter for building a user-friendly interface, algorithm implementation, and visual representation of the results.

Key Features:
Collect user-defined airport names and distances via a GUI.
Compute the minimum spanning tree (MST) to ensure the shortest connection between all airports.
Visualize the network of airports and the routes with custom markers.
Display results in a message box, including the edges of the MST and total cost.
Prerequisites
Ensure the following Python libraries are installed:

NumPy (pip install numpy)
Matplotlib (pip install matplotlib)
NetworkX (pip install networkx)
Tkinter (standard Python library)
Code Structure
1. create_airport_graph(num_airports)
Collects user inputs for airport names and distances.
Displays a Tkinter window to input data.
Returns a distance matrix and a list of airport names.
2. prims_algorithm(distances)
Implements Prim's algorithm to find the MST.
Outputs a list of edges in the MST and the total cost.
3. visualize_airports(distances, edges, airport_names)
Visualizes the airports and MST using NetworkX and Matplotlib.
Customizes node markers to depict airports as squares.
4. run_simulation(num_airports)
Orchestrates the entire workflow:
Collects input data.
Runs Prim's algorithm.
Displays results and calls the visualization function.
5. setup_gui()
Sets up the main window to collect the number of airports and trigger the simulation.


How to Run the Project
1. Download the Code: Save the code in a Python file (e.g., air_traffic_control.py).
2. Run the Script: Run the script using a Python interpreter:
python air_traffic_control.py
3. Enter Inputs:
Enter the number of airports in the initial input field.
Provide airport names and pairwise distances in the Tkinter window that appears.
4. View Results:
A message box displays the MST edges and total cost.
A graphical representation of the MST is shown in a Matplotlib window.


Example Workflow
User inputs 4 for the number of airports.
The script prompts for:
Airport names: A1, A2, A3, A4.
Distances between the airports (e.g., A1 to A2 = 15, A1 to A3 = 20, etc.).
After input:
The script runs Prim's algorithm.
Results are shown in a message box.
A plot of the airport network and MST is displayed.
Customization
Node markers: Adjust the plt.scatter properties in visualize_airports() to change marker size, color, or shape.
Algorithm tweaks: Modify prims_algorithm() if a different MST approach is needed.
Error Handling
If non-numeric values are entered for distances, a message box alerts the user to input valid data.
Ensure that all fields are filled to prevent runtime errors.
Future Enhancements
Include validation for symmetric distance entry.
Add more complex graph algorithms (e.g., Dijkstra's for shortest path).
Support weighted graphs with multiple criteria (e.g., cost, time).
License
This project is open-source and available for educational and personal use.
