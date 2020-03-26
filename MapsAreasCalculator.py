import subprocess
import concurrent.futures
import os
from Arista import Arista
from algoritmo import AlgoritmoBarrido
from Vertice import Vertice
from Cara import Cara
from Segmento import Segmento
from Punto import Punto


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

        # Extract edges
        input_directory = "input/"
        input_file_name = "{}{}".format(
            self.prefix_on_layers_files, layer if layer >= 10 else "0{}".format(layer))
        verices_file = os.path.join(
            input_directory, input_file_name + self.layer_extensions[1])
        edges_file = os.path.join(
            input_directory, input_file_name + self.layer_extensions[0])

        vertices = self.__get_vertices(verices_file)
        edges = self.__get_edges(vertices, edges_file)

        points = {}
        for key, value in vertices.items():
            points[key] = Punto(value.x, value.y)

        segments = {}
        for key, value in edges.items():
            segments[key] = Segmento(
                points[value.inicio], points[edges[value.siguiente_arista].inicio])

        barr = AlgoritmoBarrido(list(segments.values()))

        barr.barrer()
        intersections = barr.R
        print("Hola")
        print(intersections)

    def __clean_lines(self, lines):
        clean_lines = []
        for line in lines:
            new_line = line.replace("\n", "").split("   ")
            items = []
            for item in new_line:
                if item != "":
                    items.append(item.replace(" ", ""))
            new_line = items
            clean_lines.append(new_line)
        return clean_lines

    def __get_edges(self, verices, edges_file):
        with open(edges_file, "r") as input_file:
            lines = input_file.readlines()
            util_lines = lines[4:]
            edges = self.__extract_edges(util_lines)

        return edges

    def __extract_edges(self, lines):
        clean_lines = self.__clean_lines(lines)
        edges = {}
        for edge in clean_lines:
            edges[edge[0]] = Arista(
                edge[3], edge[1], edge[2], edge[4], edge[5])
        return edges

    def __get_vertices(self, verices_file):
        with open(verices_file, "r") as input_file:
            lines = input_file.readlines()
            util_lines = lines[4:]
            vertices = self.__extract_verices(util_lines)

        return vertices

    def __extract_verices(self, lines):
        from Vertice import Vertice
        clean_lines = self.__clean_lines(lines)
        vertices = {}
        for vertex in clean_lines:
            vertices[vertex[0]] = Vertice(vertex[1], vertex[2], vertex[3])
        return vertices

    def get_intersecctions(self):
        with concurrent.futures.ProcessPoolExecutor() as executor:
            for layer in range(1, self.number_of_layers + 1):
                executor.submit(self.get_interseccions_in_one_layer, layer)
