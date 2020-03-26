from MapsAreasCalculator import MapsAreasCalculator


def main():

    calculator = MapsAreasCalculator(2, "layer", ".ari", ".ver", ".car")
    calculator.get_intersecctions()


if __name__ == "__main__":
    main()
