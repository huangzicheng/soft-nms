# ----------------------------------------------------------
# Soft-NMS: Improving Object Detection With One Line of Code
# Copyright (c) University of Maryland, College Park
# Licensed under The MIT License [see LICENSE for details]
# Written by Navaneeth Bodla and Bharat Singh
# ----------------------------------------------------------

# from fast_rcnn.config import cfg
# from nms.gpu_nms import gpu_nms
from nms.cpu_nms import cpu_nms, cpu_soft_nms
import numpy as np


def soft_nms(dets, sigma=0.5, Nt=0.3, threshold=0.001, method=1):

    keep = cpu_soft_nms(np.ascontiguousarray(dets, dtype=np.float32),
                        np.float32(sigma), np.float32(Nt),
                        np.float32(threshold),
                        np.uint8(method))
    return keep


# Original NMS implementation
# def nms(dets, thresh, force_cpu=False):
#     """Dispatch to either CPU or GPU NMS implementations."""
#     if dets.shape[0] == 0:
#         return []
#     if cfg.USE_GPU_NMS and not force_cpu:
#         return gpu_nms(dets, thresh, device_id=cfg.GPU_ID)
#     else:
#         return cpu_nms(dets, thresh)


if __name__=='__main__':

# boxes and scores
    boxes = np.array([[200, 200, 400, 400, 0.9], [220, 220, 420, 420,0.8], [200, 240, 400, 440, 0.7 ], [240, 200, 440, 400,0.6], [1, 1, 2, 2, 0.5]], dtype=np.float32)
    boxscores = np.array([0.9, 0.8, 0.7, 0.6, 0.5], dtype=np.float32)
    index = soft_nms(boxes, sigma=0.5, Nt=0.3, threshold=0.1, method=1)
    print(index)