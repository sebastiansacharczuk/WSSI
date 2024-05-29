import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class Neuron:  
    def __init__(self, n_inputs, bias = 0., weights = None):  
        self.b = bias
        if weights: self.ws = np.array(weights)
        else: self.ws = np.random.rand(n_inputs)

    def _f(self, x): #activation function (here: leaky_relu)
        return max(x*.1, x)   

    def __call__(self, xs): #calculate the neuron's output: multiply the inputs with the weights and sum the values together, add the bias value,
                            # then transform the value via an activation function
        return self._f(xs @ self.ws + self.b) 

class NeuralNetwork:
    def __init__(self, layers):
        self.layers = layers
        self.network = self._build()

    def _build(self):
        network = []
        for i, (n_inputs, n_neurons) in enumerate(self.layers):
            layer = [Neuron(n_inputs) for neuron_index in range(n_neurons)]
            network.append(layer)
        return network

    def visualize(self):
        G = nx.DiGraph()
        pos = {}
        node_counter = 0
        color_map = {f'layer {i}': 'blue' for i in range(1, len(self.network) - 1)}
        color_map['input'] = 'red'
        color_map['output'] = 'green'
        layer_names = ['input'] + [f'layer {i}' for i in range(1, len(self.network) - 1)] + ['output']

        for i, layer in enumerate(self.network):
            for j, neuron in enumerate(layer):
                node_name = f'L{i}N{j}'
                G.add_node(node_name, layer=layer_names[i])
                pos[node_name] = (i, j - len(layer) / 2)
                node_counter += 1

            if i > 0:
                for k in range(len(self.network[i - 1])):
                    for j in range(len(layer)):
                        G.add_edge(f'L{i - 1}N{k}', f'L{i}N{j}')

        plt.figure(figsize=(9, 6))
        nx.draw(G, pos, with_labels=False, node_size=5000,
                node_color=[color_map[data['layer']] for node, data in G.nodes(data=True)], edge_color='gray')

        for node, data in G.nodes(data=True):
            plt.text(pos[node][0], pos[node][1], data['layer'], ha='center', va='center', fontsize=12, color='white', weight='bold',
                    bbox=dict(color=color_map[data['layer']], edgecolor='none', boxstyle='round,pad=0.3'))

        plt.show()



layers = [(3, 4), (4, 5), (5, 4),(4, 1)]
nn = NeuralNetwork(layers)
nn.visualize()
