Pre-trained model links of latest neural network papers
====

A list of available pre-trained neural network, in particular caffe and chainer models. Like [model zoo](https://github.com/BVLC/caffe/wiki/Model-Zoo) of caffe, but this repository aims to offer you framework-free collections of the latest paper implements.

Recently many deep-learning frameworks exist such as caffe, theano, chainer, tensorflow, keras and so on.
However, each pre-trained models are sometimes not compatible each other (i.e. cannot be loaded with other frameworks). This kind of exclusion of models for specific frameworks might prevent open improvement for deep learning communities including students, academic fields, and industries.

For the users who haven't installed caffe, I made up some files where weight and bias are saved as pickle. You can re-construct neural networks of your own framework, if you know the model structure. See also [Loading Caffe model without Caffe](#loading-caffe-model-without-caffe)

## Notice
1. Please be careful about the LICENSE for each model of your own usage.
2. This is in progress and we [need your help](#contributing)! Thank you.

## Contributing
If you want to inform and add the new pre-trained models available, feel free for Issues and PRs. Also if you have installed caffe and want to contribute, please see [Caffe model weight and bias export for non-caffe users](#caffe-model-weight-and-bias-export-for-non-caffe-users).


## TODOs
 - Add more models and implementations
 - List the LICENSE for each model
 - Scripts for chainer2pkl

## Table of Contents

 - [Models](#models)
 - [Caffe](#caffe)
    - [Loading Caffe model with Caffe](#loading-caffe-model-with-caffe) 
    - [Loading Caffe model without Caffe](#loading-caffe-model-without-caffe) 
 - [Chainer](#chainer)
    - [Loading Chainer model with Chainer](#loading-chainer-model-with-chainer) 
    - [Loading Chainer model without Chainer](#loading-chainer-model-without-chainer) 
 - [Theano](#theano)
    - [Loading Theano model with Theano](#loading-theano-model-with-theano) 
    - [Loading Theano model without Theano](#loading-theano-model-without-theano) 
 - [Tips](#tips)
     - [Who has not installed caffe](#who-has-not-installed-caffe)
     - [Who wants to copy pre-trained chainer model](#who-wants-to-copy-pre-trained-chainer-model)
     - [Caffe model weight and bias export for non-caffe users](#caffe-model-weight-and-bias-export-for-non-caffe-users)
 - [LICENSE](#license)
 - [Author](#author)


## Models

Models are sorted for each tasks or competitions.

### ILSVRC
 - ResNet
    - [Original paper](http://arxiv.org/abs/1512.03385) "Deep Residual Learning for Image Recognition" by Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun
    - [Caffe model and prototxt](https://onedrive.live.com/?authkey=%21AAFW2-FVoxeVRck&id=4006CBB8476FF777%2117887&cid=4006CBB8476FF777) uploaded by [@KaimingHe](https://github.com/KaimingHe). MIT LICENSE. For the details see  [https://github.com/KaimingHe/deep-residual-networks](https://github.com/KaimingHe/deep-residual-networks).
    - [Exported pkl](https://drive.google.com/open?id=0BxSyYt1jT6Lhc2xVUFgzQThpcXM) You can know the structure of model by reading prototxt above. Only ResNet50 is available for now. MIT LICENSE. Exported by [@shiba24](https://github.com/shiba24)

### Pascal datasets
 - Fully Convolutional Network 
    - [Original paper](http://www.cv-foundation.org/openaccess/content_cvpr_2015/html/Long_Fully_Convolutional_Networks_2015_CVPR_paper.html) "Fully Convolutional Networks for Semantic Segmentation" by Jonathan Long, Evan Shelhamer, Trevor Darrell
    - [Caffe model](http://dl.caffe.berkeleyvision.org/fcn8s-heavy-pascal.caffemodel) from [https://github.com/shelhamer/fcn.berkeleyvision.org/tree/master/voc-fcn8s](https://github.com/shelhamer/fcn.berkeleyvision.org/tree/master/voc-fcn8s). However deploy.prototxt is incorrect. Please ```wget https://raw.githubusercontent.com/shelhamer/fcn.berkeleyvision.org/master/voc-fcn8s/deploy.prototxt``` for prototxt.
    - [Exported pkl](https://drive.google.com/open?id=0BxSyYt1jT6LhUlhITjdicDFyNHM) You can know the structure of model by reading prototxt above. Only ResNet50 is available for now. MIT LICENSE. Exported by [@shiba24](https://github.com/shiba24)

### VOC 2010 datasets
 - Fully Convolutional Network 
    - now in prep

### FLIC dataset for human pose estimation
 - AlexNet
    - [Original paper](http://arxiv.org/abs/1312.4659)
    - [Chainer implementation](https://github.com/mitmul/deeppose) by [@mitmul](https://github.com/mitmul). [GPL v2 LICENSE](https://opensource.org/licenses/GPL-2.0).
    - [Chainer model](https://drive.google.com/file/d/0BxSyYt1jT6LhS2dKSUtIV1Z4eGM/view?usp=sharing) trained by [@shiba24](https://github.com/shiba24). [GPL v2 LICENSE](https://opensource.org/licenses/GPL-2.0). Trained epoch = 90 and the validation loss = 0.0187835. This file is .npy format so you may read without chainer (though not tested yet).
 - ResNet50
    - [Chainer model](https://drive.google.com/open?id=0BxSyYt1jT6LhS2dKSUtIV1Z4eGM) trained by [@shiba24](https://github.com/shiba24). [GPL v2 LICENSE](https://opensource.org/licenses/GPL-2.0). Trained epoch = 40 and the validation loss = 0.00374945877117. This file is .npy format so you may read without chainer (though not tested yet).

## Caffe
### Loading Caffe model with Caffe
See the [Caffe documentation](http://caffe.berkeleyvision.org/) for loading caffe models with caffe.

### Loading Caffe model without Caffe

There are few ways for loading caffe model without caffe. Currently my best practices are two below:

#### 1. Loading from chaner.CaffeFunction

Chainer is compatible to Caffe model to some extent. Please see [Caffe function in Chainer](http://docs.chainer.org/en/stable/reference/caffe.html)

#### 2. Loading pickles

Chainer doesn't support yet some functions and layers (e.g. Deconvolution layer) and might output some error messages. In that case, it might be possible to [load pkls](#Loading pkl) exported from caffe. The pkl file should be exported by those who DO have caffe! (To caffe users: please see [Caffe model weight and bias export for non-caffe users](#caffe-model-weight-and-bias-export-for-non-caffe-users))

## Chainer

### Loading Chainer model with Chainer

See the [Chainer documentation](http://docs.chainer.org/en/stable/index.html) for loading chainer model with chainer.
See also [how to copy model to another model](#who-wants-to-copy-pre-trained-chainer-model).

### Loading Chainer model without Chainer

#### The best practice

Currently the best practice might be installing chainer on your own environment because of its easy installation.
```pip install chainer```
For more details, please see [chainer installation guide](http://docs.chainer.org/en/stable/install.html).

#### chainer2pkl

Now I am implementing ```chainer2pkl.py``` for exporting W and b of chainer model. Please wait for a while.

## Theano

### Loading Theano model with Theano
See the [Theano documentation](http://deeplearning.net/software/theano/) for loading theano models with theano.

### Loading Theano model without Theano
Now in prep

## Tips

### Who has not installed caffe

If you want to use caffe pre-trained models in chainer or keras, please see [Loading pkl](#loading-pkl). You need .pkl file exported or downloaded beforehand.

### Caffe model weight and bias export for non-caffe users

#### Why exporting pickles for non-caffe users?

Recently the framework that has plenty of pre-trained models is [Caffe](http://caffe.berkeleyvision.org/), particularly in the academic papers.

However, the installation of caffe is a bit complicated. Those who use other frameworks might not want to install caffe only for the pre-trained models. This kind of exclusive possession of models for specific frameworks prevent open improvement for deep learning communities including students, academic fields, and industries.

So, I wrote ```caffe2pkl.py```. This script works only caffe installed evironment and makes pickles of weights and biases.

#### Usage

```
python caffe2pkl.py --prototxt PATH_TO_PROTOTXT --model PATH_TO_MODEL
```

#### Loading pkl

In python, 

```
with open(PATH_TO_PKL, 'rb') as d_pickle:
    data = six.moves.cPickle.load(d_pickle)
```

```data``` is dict and has *_W and *_b keys for each layer. W ans b is np.ndarray.


### Who wants to copy pre-trained chainer model

See the function ```copy_model``` in [this web site](http://qiita.com/tabe2314/items/6c0c1b769e12ab1e2614)

Although this is in Japanese, but you will find the function very useful. (No need to understanding the Japanese explanation exactly!)


## Licence

[MIT LICENSE](https://github.com/tcnksm/tool/blob/master/LICENSE)

## Author

[shiba24](https://github.com/shiba24)
