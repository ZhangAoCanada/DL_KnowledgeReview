# Popular Architectures for Semantic Segmentation

## Content 

- [FCN](#FCN)
- [SegNet](#SegNet)
- [DeepLab](#DeepLab)
    - [DeepLab V1](#DeepLabV1)
    - [DeepLab V2](#DeepLabV2)
    - [DeepLab V3](#DeepLabV3)
    - [Auto-DeepLab](#AutoDeepLab)
- [U-Net](#U-Net)
    - [Attention U-Net](#AttentionUNet)
    - [TransUNet](#TransUNet)
- [Swin-Transformer](#SwinTransformer)

## DeepLab<a name="DeepLab"/>

### [DeepLab V1](https://arxiv.org/abs/1412.7062) (2016)<a name="DeepLabV1"/>

[DeepLab V1](https://arxiv.org/abs/1412.7062) is the first to introduce *Atrous Convolution* (shown as the left of the figure below), which is later viewed as the most outstanding property of the DeepLab series.
<p align="center">
  <img src="./images/deeplabv1.png">
</p>

For the explanation of fully-connected CRF, the following equations shows the original explanation from the paper. As can be seen, the calculation of CRF model is based on its Energy function. The connect between two different pixel locations is based on Gaussian Kernel.
<p align="center">
  <img src="./images/deeplab_CRF.png">
</p>

### [DeepLab V2](https://arxiv.org/abs/1606.00915) (2017)<a name="DeepLabV2"/>

Compared to [DeepLab V1](https://arxiv.org/abs/1412.7062), [DeepLab V2](https://arxiv.org/abs/1606.00915) introduces another practical method, called Atrous Spatial Pyramid Pooling (ASPP). The block is added to the end of the backbone and thus the performance of [DeepLab V2](https://arxiv.org/abs/1606.00915) exceeds [DeepLab V1](https://arxiv.org/abs/1412.7062). All other implementations including fully-connected CRF are kept the same.
<p align="center">
  <img src="./images/ASPP.png">
</p>

### [DeepLab V3](https://arxiv.org/abs/1706.05587) (2017)<a name="DeepLabV3"/>

Starting from [DeepLab V3](https://arxiv.org/abs/1706.05587), the fully-connected CRF is removed. Instead, Atrous Convolutional layers are fully explored. Different stride rates are applied in the entire model which the backbone itself can keep a certain large feature maps resolution.
<p align="center">
  <img src="./images/deeplabv3.png">
</p>

### [Auto-DeepLab](https://arxiv.org/abs/1901.02985) (2019)<a name="AutoDeepLab"/>

Using Neural Architecture Search (NAS), the model is designed by Deep Learning itself and thus outperforms previous DeepLab versions.
<p align="center">
  <img src="./images/autodeeplab.png">
</p>