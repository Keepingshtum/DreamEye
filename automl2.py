## To do: Uncomment and set the following variables
project_id = 'plsgoogol'
compute_region = 'us-central1'
model_id = 'IOD1766646904998854656'
file_path = r'D:\GCloud\20191005_204349046_iOS.jpg'

from google.cloud import automl_v1beta1 as automl

automl_client = automl.AutoMlClient()

# Get the full path of the model.
model_full_id = automl_client.model_path(project_id, compute_region, model_id)

prediction_client = automl.PredictionServiceClient()
with open(file_path, 'rb') as f_in:
  image_bytes = f_in.read()
payload = {'image': {'image_bytes': image_bytes}}
result = prediction_client.predict(model_full_id, payload)
print('Result of online predict: ', result)
for result in result.payload:
    print("Predicted class name: {}".format(result.display_name))
    print("Predicted class score: {}".format(result.classification.score))
r1=result.display_name;
r2=result.classification.score