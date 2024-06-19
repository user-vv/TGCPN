### 1. Recommended Environment

- Linux (tested on Ubuntu 16.04)
- Python 3.7
- PyTorch 1.4 or higher (tested on PyTorch 1.10.1)
- CUDA 9.0 or higher (tested on CUDA 10.2)

### 2. Set the Environment

```shell
pip install -r requirement.txt
python setup.py build_dist --inplace 
```
The [torch_scatter](https://github.com/rusty1s/pytorch_scatter) package is required



### 3. Data Preparation

- Prepare [KITTI](http://www.cvlibs.net/datasets/kitti/eval_object.php?obj_benchmark=3d) dataset and [road planes](https://drive.google.com/file/d/1d5mq0RXRnvHPVeKx6Q612z0YRO1t2wAp/view?usp=sharing)

```shell
# Download KITTI and organize it into the following form:
├── data
│   ├── kitti
│   │   │── ImageSets
│   │   │── training
│   │   │   ├──calib & velodyne & label_2 & image_2 & (optional: planes)
│   │   │── testing
│   │   │   ├──calib & velodyne & image_2

# Generatedata infos:
python -m pcdet.datasets.kitti.kitti_dataset create_kitti_infos tools/cfgs/dataset_configs/kitti_dataset.yaml
```

### 4. Pretrain model
You can download the pretrain model [here](https://drive.google.com/file/d/1CdSWpxU03pdd0gQXLw3x5PMj7h_vifLW/view?usp=sharing) and the log file [here](https://drive.google.com/file/d/1_n50FBxFmGjyHvbBiqUSvbqF3WzCRIIt/view?usp=sharing).

The performance (using 11 recall poisitions) on KITTI validation set is as follows:
```
Car  AP@0.70, 0.70, 0.70:
bev  AP:90.1572, 88.0972, 86.8397
3d   AP:88.8694, 78.7660, 77.5758

Pedestrian AP@0.50, 0.50, 0.50:
bev  AP:63.1125, 58.5591, 55.1318
3d   AP:60.2515, 55.5535, 50.1888

Cyclist AP@0.50, 0.50, 0.50:
bev  AP:85.6768, 71.9008, 67.1551
3d   AP:85.4238, 70.2774, 64.9804
```
The runtime is about **33 ms** per sample.

### 5. Train

- Train with a single GPU （cfg文件为voxset_context_awar，3Dbackbone在VoxSeT\pcdet\models\backbones_3d\vfe）

```shell
python train.py --cfg_file tools/cfgs/kitti_models/voxset_context_awar.yaml
```

- Train with multiple GPUs 

```shell
cd VoxSeT/tools
bash scripts/dist_train.sh --cfg_file ./cfgs/kitti_models/voxset_context_awar.yaml
```
### 6. Test with a pretrained model

```shell
cd VoxSeT/tools
python test.py --cfg_file --cfg_file ./cfgs/kitti_models/voxset.yaml --ckpt ${CKPT_FILE}
```
