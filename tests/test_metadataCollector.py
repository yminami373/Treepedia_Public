import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

import unittest
from collections import OrderedDict
from Treepedia import metadataCollector


class TestMetadataCollector(unittest.TestCase):

    def test_get_pano_items(self):
        # Boston
        test_data_1 = OrderedDict([('@image_width', '16384'), ('@image_height', '8192'), ('@tile_width', '512'), ('@tile_height', '512'), ('@image_date', '2019-08'), ('@pano_id', 'Z12uXTZKc7-CkGZI27rzjw'), ('@imagery_type', '1'), ('@num_zoom_levels', '5'), ('@lat', '42.400560'), ('@lng', '-71.151165'), ('@original_lat', '42.400584'), ('@original_lng', '-71.151152'), ('@elevation_wgs84_m', '-27.212080'), ('@best_view_direction_deg', '164.39876'), ('@elevation_egm96_m', '1.335211'), ('copyright', '© 2020 Google'), ('text', 'MA-2'), ('region', 'Cambridge, Massachusetts'), ('country', 'United States')])
        panoDate, panoId, panoLat, panoLon = metadataCollector.getPanoItems(test_data_1)
        
        self.assertEqual(panoDate, '2019-08')
        self.assertEqual(panoId, 'Z12uXTZKc7-CkGZI27rzjw')
        self.assertEqual(panoLat, '42.400560')
        self.assertEqual(panoLon, '-71.151165')

        # Shibuya
        test_data_2 = OrderedDict([('@image_width', '16384'), ('@image_height', '8192'), ('@tile_width', '512'), ('@tile_height', '512'), ('@image_date', '2020-01'), ('@pano_id', 'Hgpbe7YandLTAkTt191Hfw'), ('@imagery_type', '1'), ('@num_zoom_levels', '5'), ('@lat', '35.661628'), ('@lng', '139.708112'), ('@original_lat', '35.661685'), ('@original_lng', '139.708116'), ('@elevation_wgs84_m', '71.271167'), ('@best_view_direction_deg', '119.61822'), ('@elevation_egm96_m', '34.677269'), ('copyright', '© 2020 Google'), ('text', 'Aoyama-dori Ave'), ('region', 'Shibuya City, Tokyo'), ('country', 'Japan')])
        panoDate, panoId, panoLat, panoLon = metadataCollector.getPanoItems(test_data_2)
        
        self.assertEqual(panoDate, '2020-01')
        self.assertEqual(panoId, 'Hgpbe7YandLTAkTt191Hfw')
        self.assertEqual(panoLat, '35.661628')
        self.assertEqual(panoLon, '139.708112')

        # Shibuya, with different data format
        test_data_3 = OrderedDict([('@image_width', '13312'), ('@image_height', '6656'), ('@tile_width', '512'), ('@tile_height', '512'), ('@image_date', '2018-05'), ('@pano_id', 'Y37nf692NCU2nEAn7OFqmw'), ('@scene', '1'), ('@imagery_type', '5'), ('@level_id', '7137976d59905955'), ('@num_zoom_levels', '5'), ('@lat', '35.669549'), ('@lng', '139.702947'), ('@original_lat', '35.669549'), ('@original_lng', '139.702947'), ('@elevation_wgs84_m', '1.193989'), ('@best_view_direction_deg', '41.73935'), ('@elevation_egm96_m', '-35.458862'), ('copyright', '© 2020 Google'), ('text', None), ('country', 'Japan'), ('attribution_name', None)])
        panoDate, panoId, panoLat, panoLon = metadataCollector.getPanoItems(test_data_3)
        
        self.assertEqual(panoDate, '2018-05')
        self.assertEqual(panoId, 'Y37nf692NCU2nEAn7OFqmw')
        self.assertEqual(panoLat, '35.669549')
        self.assertEqual(panoLon, '139.702947')


if __name__ == '__main__':
    unittest.main()