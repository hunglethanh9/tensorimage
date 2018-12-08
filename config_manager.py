import tensorimage.src.file.writer as tsfw
import tensorimage.src.file.reader as tsfr
import os


def set_config(**config):
    config_writer = tsfw.JSONWriter("user", os.getcwd()+'/config.json')

    for key, val in zip(config.keys(), config.values()):
        eval("config_writer.update("+key+"='"+str(val)+"')")
        config_writer.write()


def view_config():
    config_reader = tsfr.JSONReader("user", os.getcwd()+'/config.json')
    config_reader.bulk_read()
    config_reader.select()
    return config_reader.selected_data