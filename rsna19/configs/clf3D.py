from rsna19.configs.base_config import BaseConfig


class Config(BaseConfig):
    train_out_dir = '/home/ec2-user/SageMaker/rsna/0024_3d/0_1_2_3'

    dataset_file = '5fold.csv'
    data_version = '3d'  # '3d', 'npy', 'npy256' etc.
    train_folds = [0, 1, 2, 3]
    val_folds = [4]

    backbone = 'resnet18'
    pretrained = '/home/ec2-user/SageMaker/rsna/pretrained_3d/resnet18_23dataset.pth'
    resnet_shortcut = 'A'   # 'A' or 'B'
    new_layer_names = ['fc']

    lr = 1e-4
    new_params_lr_boost = 10
    batch_size = 32  # 16 (3, 512, 512) images fits on TITAN XP
    dropout = 0.5
    weight_decay = 0.001
    optimizer = 'radam'

    gpus = [0, 1]
    num_workers = 3 * len(gpus)

    max_epoch = 20

    num_slices = 11  # must be odd
    pre_crop_size = 400
    crop_size = 384
    random_crop = True
    vertical_flip = True
    pixel_augment = False
    elastic_transform = True
    use_cdf = True
    augment = True

    # used only if use_cdf is False
    min_hu_value = 20
    max_hu_value = 100

    balancing = False
    # 'epidural', 'intraparenchymal', 'intraventricular', 'subarachnoid', 'subdural', no_bleeding
    probas = [0.1, 0.14, 0.14, 0.14, 0.14, 0.34]


assert (not Config.pretrained) or (Config.backbone in Config.pretrained), \
    "The backbone depth and the pretrained model depth should be equal."
