#### SOFT-NMS

cd nms/

python setup.py build_ext --inplace

##### Usage in   nms_wrapper.py

in soft_nms(dets, sigma=0.5, Nt=0.3, threshold=0.001, method=1)

The threshold needs to be set by yourself, generally threshold=0.5
