import json

# Configuration for Vitessce, defined as a Python dictionary
vitessce_config = {
    "version": "1.0.16",
    "name": "Example configuration",
    "description": "",
    "datasets": [],
    "initStrategy": "auto",
    "coordinationSpace": {},
    "layout": [{
        "component": "description",
        "props": {"description": "Hello, world!"},
        "x": 0, "y": 0, "w": 6, "h": 6,
    }],
}

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
          "type": "raster",
          "fileType": "raster.json",
          "options": {
            "schemaVersion": "0.0.2",
            "images": [
              {
                "name": "PAS",
                "type": "ome-tiff",
                "url": "s3://nf-core-awsmegatests.s3-eu-west-1.amazonaws.com/molkart/results-7605a53092930a0b65509c64f79834a6c8449e9b/clahe/32830-Slide1_A2-2_32830-Slide1_A2-2_DAPI_gridfilled_clahe.tiff"
              },
            ],
            "usePhysicalSizeScaling": True,
            "renderLayers": [
              "PAS",
              "AF",
              "IMS PosMode",
              "IMS NegMode"
            ]
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

# HTML template with a placeholder for the Vitessce configuration
html_template = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>Vitessce main page</title>
  </head>
  <body>
    <h1>Vitessce</h1>
    <div id="root"></div>

    <script type="importmap">
      {
        "imports": {
          "react": "https://esm.sh/react@18.2.0?dev",
          "react-dom": "https://esm.sh/react-dom@18.2.0?dev",
          "react-dom/client": "https://esm.sh/react-dom@18.2.0/client?dev",
          "vitessce": "https://unpkg.com/vitessce@latest"
        }
      }
    </script>
    <script type="module">
      import React from 'react';
      import { createRoot } from 'react-dom/client';
      import { Vitessce } from 'vitessce';

      const config = %CONFIG_JSON%;

      function MyApp() {
        return React.createElement(
          Vitessce,
          {
            height: 500,
            theme: 'light',
            config: config,
          }
        );
      }

      const container = document.getElementById('root');
      const root = createRoot(container);
      root.render(React.createElement(MyApp));
    </script>
  </body>
</html>
"""

## Small test to see if vitessce can produce proper layouts
from vitessce import (
    VitessceConfig,
    Component as cm,
    CoordinationType as ct,
    OmeTiffWrapper,
    MultiImageWrapper,
)
from os.path import join
vc = VitessceConfig(schema_version="1.0.16", name='Spraggins Multi-Modal', description='PAS + IMS + AF From https://portal.hubmapconsortium.org/browse/collection/6a6efd0c1a2681dc7d2faab8e4ab0bca')
dataset = vc.add_dataset(name='Spraggins').add_object(
    MultiImageWrapper(
        image_wrappers=[
            OmeTiffWrapper(img_url='https://assets.hubmapconsortium.org/f4188a148e4c759092d19369d310883b/ometiff-pyramids/processedMicroscopy/VAN0006-LK-2-85-PAS_images/VAN0006-LK-2-85-PAS_registered.ome.tif?token=', name='PAS'),
            OmeTiffWrapper(img_url='https://assets.hubmapconsortium.org/2130d5f91ce61d7157a42c0497b06de8/ometiff-pyramids/processedMicroscopy/VAN0006-LK-2-85-AF_preIMS_images/VAN0006-LK-2-85-AF_preIMS_registered.ome.tif?token=', name='AF'),
            OmeTiffWrapper(img_url='https://assets.hubmapconsortium.org/be503a021ed910c0918842e318e6efa2/ometiff-pyramids/ometiffs/VAN0006-LK-2-85-IMS_PosMode_multilayer.ome.tif?token=', name='IMS Pos Mode'),
            OmeTiffWrapper(img_url='https://assets.hubmapconsortium.org/ca886a630b2038997a4cfbbf4abfd283/ometiff-pyramids/ometiffs/VAN0006-LK-2-85-IMS_NegMode_multilayer.ome.tif?token=', name='IMS Neg Mode')
        ],
        use_physical_size_scaling=True,
 )
)
spatial = vc.add_view(cm.SPATIAL, dataset=dataset)
status = vc.add_view(cm.STATUS, dataset=dataset)
lc = vc.add_view(cm.LAYER_CONTROLLER, dataset=dataset).set_props(disableChannelsIfRgbDetected=True)
vc.layout(spatial | (lc / status))


# Convert the configuration to a JSON string
config_json = json.dumps(vitessce_config)

# Replace the placeholder with the actual JSON configuration
html_content = html_template.replace("%CONFIG_JSON%", config_json)

# Write the HTML content to a file
with open("vitessce_test.html", "w") as file:
    file.write(html_content)

print("HTML file generated successfully.")