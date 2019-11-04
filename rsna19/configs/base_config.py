class BaseConfig:
    train_dir = '/kolos/storage/ct/data/rsna/stage_1_train_images'
    test_dir = '/kolos/storage/ct/data/rsna/stage_1_test_images'
    labels_path = "/kolos/storage/ct/data/rsna/stage_1_train.csv"
    nb_folds = 5

    data_root = "/kolos/m2/ct/data/rsna/"

    # Used for Dmytro's models
    checkpoints_dir = "../output/checkpoints"
    tensorboard_dir = "../output/tensorboard"
    oof_dir = "../output/oof"

    # Used for Brainscan models
    model_outdir = '/kolos/m2/ct/models/classification/rsna/'

    n_classes = 6
    csv_root_dir = None
