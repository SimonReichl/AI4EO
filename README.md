# AI4EO
Repo for my report

Notebooks for automatic flood detection from Sentinel-1 SAR satellite data, based on the MMFlood dataset.
Includes two classical baselines (Otsu Thresholding, Random Forest) and three deep learning models (DeepLabV3+, U-Net with ResNet50, U-Net with MiT-B2), using SAR, DEM, and optionally a hydrology layer as input.
The notebooks run in Google Colab. Data needs to be placed in Google Drive as mmflood_tiled.zip or mmflood_tiled_hydro.zip. Those were created using this repo https://github.com/edornd/mmflood/tree/main
and the activations.json aswell as the activations_europe_only.json. tiled_hydro was created in the notebook itself or using the hydro.py
download of dataset https://zenodo.org/records/6534637
