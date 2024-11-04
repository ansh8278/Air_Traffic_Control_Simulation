import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import tkinter as tk
from tkinter import messagebox

# Modify create_airport_graph to accept user-defined distances and names
def create_airport_graph(num_airports):
    distances = np.zeros((num_airports, num_airports))
    airport_names = []

    # Create a window to collect distances and names
    input_window = tk.Toplevel()
    input_window.title("Define Airport Names and Distances")

    # Collect airport names
    name_labels = []
    name_entries = []

    for i in range(num_airports):
        label = tk.Label(input_window, text=f"Name for Airport {i}:")
        label.grid(row=i, column=0)
        entry = tk.Entry(input_window)
        entry.grid(row=i, column=1)
        name_labels.append(label)
        name_entries.append(entry)

    # Collect distances
    distance_labels = []
    distance_entries = []

    for i in range(num_airports):
        for j in range(i + 1, num_airports):
            label = tk.Label(input_window, text=f"Distance between Airport {i} and Airport {j}:")
            label.grid(row=len(name_entries) + len(distance_labels), column=0)
            entry = tk.Entry(input_window)
            entry.grid(row=len(name_entries) + len(distance_labels), column=1)
            distance_labels.append(label)
            distance_entries.append(entry)

    def submit_data():
        nonlocal distances
        try:
            # Get airport names
            names = [entry.get() for entry in name_entries]
            airport_names.extend(names)

            # Get distances
            index = 0
            for i in range(num_airports):
                for j in range(i + 1, num_airports):
                    distance = float(distance_entries[index].get())
                    distances[i][j] = distance
                    distances[j][i] = distance  # Symmetrical matrix
                    index += 1
            
            input_window.destroy()  # Close the window when done
            return airport_names
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for distances and valid names for airports.")

    submit_button = tk.Button(input_window, text="Submit", command=submit_data)
    submit_button.grid(row=len(name_entries) + len(distance_labels), column=1)

    input_window.wait_window()  # Wait for the user to input data
    return distances, airport_names

# Implementing Prim's algorithm
def prims_algorithm(distances):
    num_airports = distances.shape[0]
    visited = [False] * num_airports
    edges = []
    total_cost = 0

    visited[0] = True  # Start from the first airport
    for _ in range(num_airports - 1):
        min_edge = float('inf')
        min_edge_pair = (-1, -1)

        for i in range(num_airports):
            if visited[i]:
                for j in range(num_airports):
                    if not visited[j] and distances[i][j] < min_edge:
                        min_edge = distances[i][j]
                        min_edge_pair = (i, j)

        edges.append(min_edge_pair)
        total_cost += min_edge
        visited[min_edge_pair[1]] = True

    return edges, total_cost

# Visualization function with airport names
def visualize_airports(distances, edges, airport_names):
    G = nx.Graph()
    num_airports = distances.shape[0]

    # Add nodes for airports
    for i in range(num_airports):
        G.add_node(i, label=airport_names[i])

    # Add edges representing distances
    for edge in edges:
        G.add_edge(edge[0], edge[1], weight=distances[edge[0]][edge[1]])

    # Positioning of airports
    pos = nx.spring_layout(G)

    # Draw edges (routes between airports)
    nx.draw(G, pos, with_labels=True, labels={i: airport_names[i] for i in range(num_airports)}, node_size=0)

    # Draw custom markers for airports (square markers for buildings)
    airport_x, airport_y = zip(*pos.values())
    plt.scatter(airport_x, airport_y, s=1000, c='lightgray', marker='s', label='Airport (Building)')

    # Draw edges labels (distances)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("Air Traffic Control: Minimum Spanning Tree with Airport Names")
    plt.legend()
    plt.show()

# Function to run the simulation
def run_simulation(num_airports):
    distances, airport_names = create_airport_graph(num_airports)
    edges, total_cost = prims_algorithm(distances)

    result_message = f"Minimum Spanning Tree Edges: {edges}\nTotal Cost: {total_cost:.2f}"
    messagebox.showinfo("Simulation Results", result_message)
    visualize_airports(distances, edges, airport_names)

# Setting up the GUI
def setup_gui():
    root = tk.Tk()
    root.title("Air Traffic Control Simulation")

    label = tk.Label(root, text="Enter the number of airports:")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    button = tk.Button(root, text="Run Simulation", command=lambda: run_simulation(int(entry.get())))
    button.pack()

    root.mainloop()

if __name__ == "__main__":
    setup_gui()
