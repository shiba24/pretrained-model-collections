Pre-trained model links of recent neural network papers
====

A list of available pre-trained neural network. In particular caffe and chainer models.

For the users who haven't installed caffe, I made up some files where weight and bias are saved as pickle.

You can re-construct neural networks if you know the model structure.

Note 1: this is in progress and we need your help! Thank you.

Note 2: Please be careful about the LICENCE for each model of your own usage.

## TODOs

 - Adding more models
 - List the LICENCE for each model
 - Scripts for reading caffe model without caffe?


## Contributing

If you want to inform and add the new pre-trained models available, feel free for Issues and PRs.

Also if you have installed caffe and want to contribute, please see [Caffe model weight and bias export for non-caffe users](#Caffe model weight and bias export for non-caffe users).

## Table of Contents

 - [Caffe models](#Caffe models and/or weight and bias pkls)
 - [Chainer models](#Chainer models)


## Caffe models and/or weight and bias pkls


 - [ResNet]()


## Chainer models

 - [ResNet]()


## Tips

### Users who haven't installed caffe

If you want to use caffe pre-trained models in chainer or keras, please see [Reading pkl](#Reading pkl). You need .pkl file exported or downloaded beforehand.


### Users who want to copy pre-trained chainer model

See the function ```copy_model``` in [this web site](http://qiita.com/tabe2314/items/6c0c1b769e12ab1e2614).

Although this is in Japanese, but you will find the function very useful. (No need to understanding the Japanese explanation exactly!)


### Caffe model weight and bias export for non-caffe users

#### Why exporting pickles for non-caffe users?

Recently the framework that have plenty of pre-trained models is [Caffe](http://caffe.berkeleyvision.org/), particularly in the academic papers.

However, the installation of caffe is a bit complicated. Those who use other frameworks might not want to install caffe only for the pre-trained models.

This kind of exclusive possession of models for specific frameworks prevent open improvement for deep learning communities including students, academic fields, and industries.

So, I wrote ```caffe2pkl.py```. This script works only caffe installed evironment and makes pickles of weights and biases.

#### Usage

```
python caffe2pkl.py --prototxt PATH_TO_PROTOTXT --model PATH_TO_MODEL
```

#### Reading pkl

In python, 

```
with open(PATH_TO_PKL, 'rb') as d_pickle:
    data = six.moves.cPickle.load(d_pickle)
```

```data``` is dict and has *_W and *_b keys for each layer. W ans b is np.ndarray.


## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Author

[shiba24](https://github.com/shiba24)
