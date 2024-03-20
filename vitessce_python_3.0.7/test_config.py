## Small test to see if vitessce can produce proper layouts
from vitessce import (
    VitessceConfig,
    Component as cm,
    CoordinationType as ct,
    OmeTiffWrapper,
    MultiImageWrapper,
)
from os.path import join
vc = VitessceConfig(schema_version="1.0.15", name='Spraggins Multi-Modal', description='PAS + IMS + AF From https://portal.hubmapconsortium.org/browse/collection/6a6efd0c1a2681dc7d2faab8e4ab0bca')
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

config_dict = vc.export(to='files', base_url='http://localhost')
config_json = json.dumps(config_dict)

# vc.export(to="files", base_url=f"http://localhost:{8080}", out_dir="/workspace")

# with open("/workspace/vitessce_test.html", "w") as f:
#     config_dict = vc.to_dict(base_url=f"http://localhost:8000")
#     json.dump(config_dict, f)
    