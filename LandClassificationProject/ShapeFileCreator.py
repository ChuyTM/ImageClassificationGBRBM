import pandas as pd
import shapefile as sf

class ShapeFileCreator:

    #variable = 'canine'  # class variable shared by all instances

    def __init__(self):
        self.csv_path = ""
        self.save_path = ""
        # variable no pública
        self._non_public = None

    def create_shapefile(self, csv_path, save_path):
        self.csv_path = csv_path
        self.save_path = save_path
        csv_coord = pd.read_csv(self.csv_path)
        w = sf.Writer(self.save_path, shapeType=5)
        w.field('name', 'C')
        list_coords = csv_coord.iloc[:,1:].values.tolist()
        w.poly([
            list_coords
            # [[122, 37], [117, 36], [115, 32], [118, 20], [113, 24]],  # poly 1
            # [[15, 2], [17, 6], [22, 7]],  # hole 1
            # [[122, 37], [117, 36], [115, 32]]  # poly 2
        ])
        w.record('polygon1')

        w.close()

        # Finally,if you would prefer to work with the entire shapefile in a
        # different format, you can convert all of it to a GeoJSON dictionary,
        # although you may lose some information in the process, such as z-
        # and m-values:
        #
        # sf.__geo_interface__['type']
        # Result: 'FeatureCollection'
        return 0

    def otra_funcion(self):
        # llamar a otra función
        self.create_shapefile()

# Testing
point = pd.read_csv("coordinates.csv")
print(point)
print(type(point))
coords = point.iloc[:,1:].values.tolist()
print(coords)

sfc = ShapeFileCreator()
test = sfc.create_shapefile(csv_path="coordinates.csv", save_path="shapefiles/test/test2")