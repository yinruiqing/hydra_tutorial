# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from omegaconf import DictConfig, MissingMandatoryValue, open_dict
from omegaconf import OmegaConf
from pytest import raises

import hydra


@hydra.main(version_base=None, config_path=".", config_name="config")
def my_app(cfg: DictConfig) -> None:
    OmegaConf.resolve(cfg)
    print(cfg.node.waldo)
    print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    my_app()
