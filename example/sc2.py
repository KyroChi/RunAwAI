# Originally written by Kyle Chickering, Taaha Chaudhry, Xin Jin, Alex Mirov and
# Simon Wu for ECS 170 @ UC Davis, Spring 2018.

if __name__ == "__main__":
    import sys
    sys.path.insert(0, './../')

    from ga import Individual
    from ga import EvolutionaryController
    from nn import NeuralNetwork

    def run_simulation(A):
        pass

    # We define an Individual implementation to run evolution on through an
    # EvolutionaryController object
    class NN(object):

        def __init__(self):
            """ We store a neural network as a member of the NN class since
            the neural network itself doesn't implement Individual and we have
            to do some administrative wrapping to get everything working """

            self.network = None


        def individual_print(self):
            return ""


        def fitness_function(self):
            """ The fitness function is where the heavy lifting for the
            implementation is done. This section can be tweaked in several ways
            to either speed up or slow down convergence. The fitness function
            will vary widely from problem to problem """

            fitness = 0

            fitness = 1 - run_simulation(self.network)

            if self.network.node_id > 10:
                fitness += 10*self.network.node_id
            elif self.network.node_id < 10:
                fitness += 10*(5 - self.network.node_id)

            return fitness


        def breed_parents(self, parent_tuple, child, reproduction_constant):
            """ Simply calls the network's breeding function to generate a
            child. """

            child.network = parent_tuple[0][1].network.breed(
                parent_tuple[1][1].network,
                parent_tuple[0][0],
                parent_tuple[1][0]
            )

            return


        def mutate(self, mutation_constant):
            """ We preform two types of network mutations, structural and
            non-structural. The structural mutations add nodes to the network
            and the non-structural mutations add connections between previously
            disconnected nodes. """

            self.network.structural_mutation()
            self.network.non_structural_mutation()

            return


        def generate_random(self):
            """ Generate a "seed" network. We create a two input, one output
            network which is the basis for our XOR evolution. We can manipulate
            the magic numbers in the initialization to get different behavior
            out of our network."""

            self.network = NeuralNetwork(2, 1, ['a', 'b'], ['o'],
                                          struct_mut_new_rate=0.2,
                                          struct_mut_con_rate=0.2,
                                          n_struct_mut_rate=0.2)

            self.network.build_network()

            return


        def __lt__(self, other):
            """ Required so that the heap can compare NN objects """

            return self


    # Create a new Evolutionary controller
    EC = EvolutionaryController(NN)

    # How many iterations to run?
    gen_lim = int(input("How many iterations: "))

    # Run the evolution simulation and return the most fit individual from the
    # final iteration
    nn = EC.run_evolution(10, 1, 1, printing='minimal', generation_limit=gen_lim)
