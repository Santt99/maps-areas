import subprocess
import concurrent.futures


class MapsAreasCalculator(object):
    def __init__(self, number_of_layers, prefix_on_layers_files, edges_file_extension, vertices_file_extension, faces_file_extension):
        self.layer_extensions = [edges_file_extension,
                                 vertices_file_extension, faces_file_extension]
        self.number_of_layers = number_of_layers
        self.prefix_on_layers_files = prefix_on_layers_files

    def get_areas(self):
        print("Getting Areas")

    def get_interseccions_in_one_layer(self, layer):
        print("Getting intersecctions for layer {}".format(layer))

    def get_intersecctions(self):
        with concurrent.futures.ProcessPoolExecutor() as executor:
            for layer in range(self.number_of_layers):
                executor.submit(get_interseccions_in_one_layer, layer)

    get_areas()
