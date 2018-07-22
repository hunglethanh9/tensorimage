import click

import nnir.trainer as nt
import nnir.classifier as nc
import image.loader as iml
import image.writer as iw
import sound.loader as sl
import sound.writer as sw
import man.label_path_writer as mlpw


class Config:
    def __init__(self):
        with open('tmp/opt') as temp:
            self.opt = temp.readline()


config = Config()

if config.opt == 'train':
    @click.command()
    @click.argument('sess_id', required=True)
    @click.argument('trained_model_path', required=True)
    @click.argument('trained_model_name', required=True)
    @click.argument('n_perceptrons_per_layer', default=(100, 51, 51, 51))
    @click.argument('optimizer', default='GradientDescent')
    @click.argument('n_epochs', default=150)
    @click.argument('learning_rate', default=0.2)
    @click.argument('train_test_split', default=0.1)
    def train(sess_id: int, trained_model_path: str, trained_model_name: str, n_perceptrons_per_layer: tuple,
              optimizer: str, n_epochs: int, learning_rate: float, train_test_split: float):
        trainer = nt.Train(sess_id, trained_model_path, trained_model_name,
                           optimizer=optimizer, n_perceptrons_layer=n_perceptrons_per_layer,
                           epochs=n_epochs, learning_rate=learning_rate, train_test_split=train_test_split)
        trainer.train()
    train()

elif config.opt == 'im_man1':
    @click.command()
    @click.argument('path_file_path', required=True)
    @click.argument('method', required=True)
    @click.argument('file_name', required=True)
    @click.argument('label_file_path', required=True)
    def im_man_1(path_file_path: str, method: str, file_name: str, label_file_path: str):
        loader = iml.ImageLoader(path_file_path, method=method)
        data = loader.main()
        writer = iw.TrainDataWriter(data, file_name, label_file_path)
        writer.main()
    im_man_1()

elif config.opt == 'im_man2':
    @click.command()
    @click.argument('path_file_path', required=True)
    @click.argument('method', required=True)
    @click.argument('file_name', required=True)
    def im_man_2(path_file_path: str, method: str, file_name: str):
        loader = iml.ImageLoader(path_file_path, method=method)
        data = loader.main()
        writer = iw.DataWriter(data, file_name)
        writer.main()
    im_man_2()

elif config.opt == 'snd_man_1':
    @click.command()
    @click.argument('path_file_path')
    @click.argument('file_name')
    def snd_man_1(path_file_path, file_name):
        loader = sl.Loader(path_file_path)
        data = loader.main()
        writer = sw.DataWriter(data, file_name)
        writer.main()
    snd_man_1()

elif config.opt == 'snd_man_2':
    @click.command()
    @click.argument('path_file_path')
    @click.argument('label_file_path')
    @click.argument('file_name')
    def snd_man_2(path_file_path: str, label_file_path: str, file_name: str):
        loader = sl.Loader(path_file_path)
        data = loader.main()
        writer = sw.TrainDataWriter(data, file_name, label_file_path)
        writer.main()
    snd_man_2()

elif config.opt == 'classify':
    @click.command()
    @click.argument('sess_id', required=True)
    @click.argument('model_path', required=True)
    @click.argument('model_name', required=True)
    @click.argument('dataset_name', required=True)
    @click.argument('prediction_fname', default='predictions')
    @click.argument('show_image', default=True)
    def predict(sess_id: int, model_path: str, model_name: str, dataset_name: str, prediction_fname: str, show_image: bool):
        predicter = nc.Predict(sess_id, model_path, model_name, dataset_name,
                               prediction_fname=prediction_fname, show_im=False)
        predicter.main()
    predict()
elif config.opt == 'write_paths':
    @click.command()
    @click.argument('main_directory_path')
    @click.argument('dataset_name')
    def path_writer(main_directory_path, dataset_name):
        mlpw.write_paths(main_directory_path, dataset_name)
    path_writer()
elif config.opt == 'write_labels':
    @click.command()
    @click.argument('main_directory_path')
    @click.argument('dataset_name')
    def label_writer(main_directory_path, dataset_name):
        mlpw.write_labels(main_directory_path, dataset_name)
    label_writer()
