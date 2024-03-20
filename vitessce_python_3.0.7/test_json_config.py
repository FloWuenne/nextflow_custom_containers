vitessce_config = {
  "version": "1.0.1",
  "name": "Neumann et al., 2020",
  "description": "Four registered imaging modalities (PAS, IMS, AF) from HuBMAP collection HBM876.XNRH.336",
  "datasets": [
    {
      "uid": "A",
      "name": "Spraggins",
      "files": [
        {
          "fileType": "raster.json",
          "options": {
            "images": [
              {
                "metadata": {
                  "isBitmask": False
                },
                "name": "molkart.tiff",
                "type": "ome-tiff",
                "url": "s3://nf-core-awsmegatests.s3-eu-west-1.amazonaws.com/molkart/results-7605a53092930a0b65509c64f79834a6c8449e9b/clahe/32830-Slide1_A2-2_32830-Slide1_A2-2_DAPI_gridfilled_clahe.tiff"
              }
            ],
            "schemaVersion": "0.0.2",
            "usePhysicalSizeScaling": False
          }
        }
      ]
    }
  ],
  "coordinationSpace": {},
  "layout": [
    {
      "component": "spatial",
      "coordinationScopes": {},
      "x": 0,
      "y": 0,
      "w": 9,
      "h": 12
    },
    {
      "component": "layerController",
      "coordinationScopes": {},
      "x": 9,
      "y": 0,
      "w": 3,
      "h": 12
    }
  ],
  "initStrategy": "auto"
}
