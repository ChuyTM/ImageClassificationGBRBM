from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
import geopandas as gpd
import os, zipfile, glob


class GetImage():

    def __init__(self):
        self.api = None
        self._connect_to_api()

    def _connect_to_api(self):
        user = 'chuytm'
        password = "nick4252"
        self.api = SentinelAPI(user, password, 'https://scihub.copernicus.eu/dhus')

    def _create_footprint(self, sf):
        footprint = None
        for i in sf['geometry']:
            footprint = i
        return footprint

    def _get_product(self, footprint, num_images, start_date=0, end_date=0, processing_level='Level-2A'):
        products = self.api.query(footprint,
                                  date=('20190601', '20190626'),
                                  platformname='Sentinel-2',
                                  processinglevel='Level-2A',
                                  cloudcoverpercentage=(0, 10))
        products_gdf = self.api.to_geodataframe(products)
        best_products = products_gdf.sort_values(['cloudcoverpercentage', 'ingestiondate'],
                                                 ascending=[True, True]).head(num_images)
        print(best_products[['title', 'cloudcoverpercentage']])
        return best_products

    def _download_image(self, products):
        save_path = "products/"
        extension = ".zip"

        origin_path = os.getcwd()
        os.makedirs(save_path, exist_ok=True)
        os.chdir(save_path)
        current_path = os.getcwd()
        self.api.download_all(products.index)

        for item in os.listdir(current_path):
            if item.endswith(extension):
                file_name = os.path.abspath(item)
                zip_ref = zipfile.ZipFile(file_name)
                zip_ref.extractall(current_path)
                zip_ref.close()
                os.remove(file_name)
        print(current_path)
        directories = [x for x in glob.glob(current_path+'/*/')]
        os.chdir(origin_path)

        return directories

    def get_image(self, shp_path, num_images):
        sf = gpd.read_file(shp_path)
        footprint = self._create_footprint(sf)
        products = self._get_product(footprint, num_images)
        list_images = self._download_image(products)
        print(list_images)
        return 0


# testing
sf_location = "shapefiles/test/sfile.shp"
gi = GetImage()
products = gi.get_image(sf_location, 1)
# print(products)
