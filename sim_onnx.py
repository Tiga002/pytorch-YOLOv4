from onnxsim import simplify
import onnx

onnx_model = onnx.load("/home/tiga/Develop/GDP/CodeSpace/onnx_engine_conversion/yolov4_1_3_480_480_static.onnx")
model_simp, check = simplify(onnx_model)
assert check, "Simplified ONNX model could not be validated"
onnx.save(model_simp, "yolo_v4_sim_v1.onnx")
print("Finish exporting simplifed onnx")
