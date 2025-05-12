from dinov2.data.datasets import ImageNet


data_root = r'/root/dinov2_data'

for split in ImageNet.Split:
    dataset = ImageNet(split=split, root=data_root, extra=data_root)
    dataset.dump_extra()