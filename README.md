# STATUS

*  **[Working]** lstm.py **Haven't been Tested yet !**

* **[Working]** main.py **Haven't been Tested yet !**

* **[Broken]** notebooks (Falta modificar las referencias a las clases en los imports. Y están pensados en ejecutarlos en Colaboratory)


# TODO List


### main --> Crear Main en Root

* Testear modelo en lstm.py

* Agregar modelo al main y testear el main


### Testear archivos y clases

* **[Tested]** utils.py

* **[Tested]** perplexity.py

* **[Tested]** TokenSelector.py

* Corpus.py

* RNN.py

* Generators.py


### Crear archivo requirements.txt

* Hacer lista de paquetes y crear archivo requirements.txt


### perplexity

* Implementar perplexity


### Clase Generators

* Verificar que clase Generators se ajusta al uso de L y Lprima


---



# Data

## Syllable-aware tests

Spanish data for tests obtained from [HERE](https://github.com/yoonkim/lstm-char-cnn/blob/master/get_data.sh)


## Spanish Billion Words Corpus

Raw Data down obtained from [Spanish Billion Words Corpus](http://cs.famaf.unc.edu.ar/~ccardellino/SBWCE/clean_corpus.tar.bz2)

> Cristian Cardellino: Spanish Billion Words Corpus and Embeddings (March 2016), http://crscardellino.me/SBWCE/


## getData

```
wget http://cs.famaf.unc.edu.ar/~ccardellino/SBWCE/clean_corpus.tar.bz2

tar xf clean_corpus.tar.bz2

mv spanish_billion_words ./data/
```


# Conda Environment


## Create Environment (example name = venv1)

```
conda create -n venv1 python=3.6 theano=1.0 anaconda
```

## Activate Environment

```
source activate venv1
```

## Theano Install

```
pip install theano --upgrade
```

## Keras Install

```
pip install keras --upgrade
```

## Switch KERAS Backend to Theano

Keras Documentation: [Switching from one backend to another](https://keras.io/backend/#switching-from-one-backend-to-another)


```
cd ~/.keras/
nano keras.json

```

Edit keras.json, and change the field "backend" to "theano"

```
{
    "image_data_format": "channels_last",
    "epsilon": 1e-07,
    "floatx": "float32",
    "backend": "theano"
}
```

## Theano Configuration (GPU)

From [Theano Configuration](http://deeplearning.net/software/theano/library/config.html)

Create a config file at home dir

```
cd ~
nano .theanorc
```

And copy and paste this configuration

```
[global]
device = cuda
force_device = True
floatX = float32
mode=FAST_RUN
optimizer_including=cudnn

[dnn]
enabled = True
include_path = /usr/local/cuda/include
library_path = /usr/local/cuda/lib64

[gpuarray]
preallocate = 1

[lib]
cnmem = 1
```

And save it.

---

## Extras

```
conda install -n venv1 mkl
conda install -n venv1 mkl-service
conda install -n venv1 openblas
conda install -n venv1 -c anaconda pygpu
```

