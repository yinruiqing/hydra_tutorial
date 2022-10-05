from omegaconf import OmegaConf
conf = OmegaConf.from_cli()
print(OmegaConf.to_yaml(conf))