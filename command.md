## From .weights to .onnx
```python demo_darknet2onnx.py <cfgFile> <namesFile> <weightFile> <imageFile> <batchSize>```

## From .onnx to .trt
```
docker run --gpus all -it --rm -v /home/tiga/Develop/GDP/CodeSpace/onnx_engine_conversion:/workspace/onnx_engine_conversion nvcr.io/nvidia/tensorrt:22.02-py3
trtexec --onnx=yolo_v4.onnx --explicitBatch --saveEngine=yolov4_480_static.trt --workspace=2048 --fp16
```

