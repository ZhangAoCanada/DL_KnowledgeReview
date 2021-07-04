# Popular Detection Heads for Object Detection

## Content

* [One-Stage Anchor-Based Detectors](#OneAnchor)
    * [YOLO](#YOLO)
    * [SSD](#SSD)
* [One-Stage Anchor-Free Detectors](#OneFree)
    * [FCOS](#FCOS)
* [Two-Stage Detectors](#Two)
    * [Faster R-CNN](#FerRCNN)

## One-Stage Anchor-Based Detectors<a name="OneAnchor"/>

### [You Look Only Once (YOLO)](https://arxiv.org/pdf/1612.08242.pdf) (2016)<a name="YOLO"/>

- History of YOLO Detector: [YOLOv1](https://arxiv.org/abs/1506.02640), [YOLOv2](https://arxiv.org/abs/1612.08242), [YOLOv3](https://arxiv.org/abs/1804.02767), [YOLOv4](https://arxiv.org/abs/2004.10934), [YOLO web: DarkNet](https://pjreddie.com/darknet/).

- The box decoding system of [YOLO](https://arxiv.org/pdf/1612.08242.pdf) is shown as below.

<p align="center">
  <img src="./images/YOLO.png" height="400">
</p>

- Anchor boxes for [YOLO](https://arxiv.org/pdf/1612.08242.pdf) is defined by K-means Clustering on the entire dataset. All anchor boxes only consist of size info with format `[w, h]`. For [COCO](https://cocodataset.org/#home), [YOLOv2](https://arxiv.org/pdf/1612.08242.pdf) claims using `9` anchor boxes can achieve optimal performance.

- The original [YOLOv2](https://arxiv.org/pdf/1612.08242.pdf) performs the box decoding on a single-stage feature maps. Therefore, the output shape before the box decoding system is
```yaml
raw features shape: [B, H, W, K, (5 + num_classes)]
B: batch size
H: height
W: width
K: number of anchor boxes
(5 + num_classes): box info [x, y, w, h] + objectness + num_classes
```

- Starting from [YOLOv3](https://arxiv.org/abs/1804.02767), with the combination of [FPN](https://arxiv.org/abs/1612.03144), multi-stage feature maps are employed. Therefore, the output shape are orgnized in the following way. The detections of small objects are thus enriched.
```yaml
raw features shape: [B, 3, H, W, K/3, (5 + num_classes)]
B: batch size
H: height
W: width
3: 3 hierarchical stage from FPN
K: number of anchor boxes
(5 + num_classes): box info [x, y, w, h] + objectness + num_classes
```

### [Single Shot Detector (SSD)](https://arxiv.org/abs/1512.02325) (2016)<a name="SSD"/>

<p align="center">
  <img src="./images/SSD.png">
</p>
