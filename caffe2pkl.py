#!/usr/bin/env python
from __future__ import print_function
import argparse
import caffe
import six


def caffe2pkl(caffe_prototxt, caffemodel_path):
    savename = caffemodel_path[:caffemodel_path.rfind(".")] + "_W_and_b.pkl"
    net = caffe.Net(caffe_prototxt, caffemodel_path, caffe.TEST)
    data = {}
    n_layers = len(net.params.keys())
    for i in range(0, n_layers):
        name = net.params.keys()[i]
        param = net.params[name]
        has_bias = False if len(param) == 1 else True
        print('{0}:'.format(name))
        print('  - W:', param[0].data.shape)
        k = name + "_W"
        data[k] = param[0].data
        # bias
        if has_bias:
            print('  - b:', param[1].data.shape)
            k = name + "_b"
            data[k] = param[1].data
    with open(savename, 'wb') as output:
        six.moves.cPickle.dump(data, output, -1)
    return data


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--prototxt', '-p', type=str, help='.prototxt file of caffe model')
    parser.add_argument('--model', '-m', type=str, help='.caffemodel file')
    args = parser.parse_args()
    caffe2pkl(args.prototxt, args.model)


