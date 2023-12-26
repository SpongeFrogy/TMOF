# Preprocessing

!! rename Preprocessing

## Structure

### vectorization of QMOF database

- [load_qmof](/preprocesing/qmof/load_qmof.ipynb) -- loading QMOF database
- [QMOF Mordred](/preprocesing/qmof/get_mordred_qmof.ipynb) - extract Mordred data
- [QMOF Mordred](/preprocesing/qmof/get_node_qmof.ipynb) -- extract Node vectorization
- [cif2vec_qmof](cif2vec_qmof.ipynb)
  - Node encoding
  - concatenation and cleaning
  - fitting `Preprocessing model`
- [QMOF dataset](/preprocesing/datasets/)

### vectorization of main database

- [getting mofid](/preprocesing/mofid)
  - [get mofid](/preprocesing/mofid/get_mofid.py) - function that saves mofid data
  - [mofid data](/preprocesing/mofid/mofid_data.csv) - file with extracted mofid data for main database
- [getting zeo](/preprocesing/zeopp)
  - [!NAME](/preprocesing/zeopp/README.md) - description of using Zeo++
  - [zeo data](/preprocesing/zeopp/zeo_data.csv) - file with extracted Zeo++ data for main database
- [cif2vec_main](cif2vec_main.ipynb) - getting MOF vector representation
  - extract Mordred data
  - Node encoding
  - concatenation and cleaning
- [Preprocessing model](preproc_model.py) - cleaning vector representation of `Nan` values and normalization
- [main dataset](/preprocesing/datasets/main_dataset.csv)
- [2pt structures](/preprocesing/datasets/2pt_dataset.csv) - structures that have both types of phase transmission
