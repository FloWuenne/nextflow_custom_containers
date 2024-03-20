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
        img_url = "s3://nf-core-awsmegatests.s3-eu-west-1.amazonaws.com/molkart/results-7605a53092930a0b65509c64f79834a6c8449e9b/clahe/32830-Slide1_A2-2_32830-Slide1_A2-2_DAPI_gridfilled_clahe.tiff"
    )
)
spatial = vc.add_view(cm.SPATIAL, dataset=dataset)
lc = vc.add_view(cm.LAYER_CONTROLLER, dataset=dataset)
vc.layout(spatial | lc)

###################
#### MCMICRO config

config_json = json.dumps(vc.to_dict(), indent=2)

# Replace the CONFIG_JSON placeholder in the html template with our actual vitessce json view config
html_content = html_template.replace("%CONFIG_JSON%", config_json)

# Write the HTML content to a static html file
with open("vitessce_test.html", "w") as file:
    file.write(html_content)

# Print a message to let the user know the html has been produced.
print("Static HTML file for vitessce generated successfully.")