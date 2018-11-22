# User configurations
workspace_dir = '/path/to/workspace/'  # Note the / at the end
tensorimage_path = '/path/to/tensorimage/'  # Note the / at the end

predictions_base_filename = 'predictions'

# Program configurations
training_metafile_path = workspace_dir+'metadata/training/meta.json'
classification_metafile_path = workspace_dir+'metadata/classification/meta.json'
dataset_metafile_path = workspace_dir+'metadata/data/meta.json'
id_management_file_path = workspace_dir+'metadata/id.json'
nid_names_metafile_path = workspace_dir+'metadata/nid_names.json'

base_training_data_store_path = workspace_dir+'user/training_datasets/'
base_unclassified_data_store_path = workspace_dir+'user/unclassified_datasets/'
base_predictions_store_path = workspace_dir+'user/predictions/'
base_trained_models_store_path = workspace_dir+'user/trained_models/'
