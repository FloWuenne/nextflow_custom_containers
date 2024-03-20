## Import the the vitessce html body template
from vitessce_template import html_template
import json

###################
#### Molkart config
from vitessce import (
    VitessceConfig,
    OmeTiffWrapper,
    Component as cm
)
vc = VitessceConfig(schema_version="1.0.15", name='Nextflow vitessce test', description='Test')
dataset = vc.add_dataset(name='Spraggins').add_object(
    OmeTiffWrapper(
      img_url = "https://assets.hubmapconsortium.org/a4be39d9c1606130450a011d2f1feeff/ometiff-pyramids/processedMicroscopy/VAN0012-RK-102-167-PAS_IMS_images/VAN0012-RK-102-167-PAS_IMS-registered.ome.tif"
    )
)
spatial = vc.add_view(cm.SPATIAL, dataset=dataset)
lc = vc.add_view(cm.LAYER_CONTROLLER, dataset=dataset)
vc.layout(spatial | lc)

###################
#### MCMICRO config

config_dict = vc.export(to='files', base_url='http://localhost')
config_json = json.dumps(config_dict)

# Replace the CONFIG_JSON placeholder in the html template with our actual vitessce json view config
html_content = html_template.replace("%CONFIG_JSON%", config_json)

# Write the HTML content to a static html file
with open("vitessce_test.html", "w") as file:
    file.write(html_content)

# Print a message to let the user know the html has been produced.
print("Static HTML file for vitessce generated successfully.")