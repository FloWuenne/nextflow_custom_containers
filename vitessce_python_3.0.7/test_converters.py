from vitessce.data_utils import multiplex_img_to_ome_tiff
import imageio
import numpy as np
img_path = "/workspace/nextflow_custom_containers/32830-Slide1_A2-2_32830-Slide1_A2-2_DAPI_gridfilled_clahe.ome.tiff"
img = imageio.imread(img_path)
multiplex_img_to_ome_tiff(img_arr = img,  output_path = "/workspace/test.ome.tiff", channel_names = "DAPI", axes = "YX")ls -lh