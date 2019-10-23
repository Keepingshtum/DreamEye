# TODO(developer): Uncomment and set the following variables
project_id = 'plsgoogol'
compute_region = 'us-central1'
model_id = 'IOD1766646904998854656'
file_path = r'D:\GCloud\20191005_204349046_iOS.jpg'
score_threshold = '0.5'

from google.cloud import automl_v1beta1 as automl
import json
from google.protobuf.json_format import MessageToJson
import config
import smtplib


def send_email(subject, msg):
        server = smtplib.SMTP('smtp.gmail.com:587')

        server.ehlo()

        server.starttls()

        server.login(config.EMAIL_ADDRESS, config.PASSWORD)

        message = 'Subject: {}\n\n{}'.format(subject, msg)

        server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS, message)

        server.quit()

        print("Success: Email sent!")












automl_client = automl.AutoMlClient()

# Get the full path of the model.
model_full_id = automl_client.model_path(
    project_id, compute_region, model_id
)

# Create client for prediction service.
prediction_client = automl.PredictionServiceClient()

# Read the image and assign to payload.
with open(file_path, "rb") as image_file:
    content = image_file.read()
payload = {"image": {"image_bytes": content}}

# params is additional domain-specific parameters.
# score_threshold is used to filter the result
# Initialize params
params = {}
if score_threshold:
    params = {"score_threshold": score_threshold}

response = prediction_client.predict(model_full_id, payload, params)
print("Prediction results:")
for result in response.payload:
    print("Predicted class name: {}".format(result.display_name))
    print("Predicted class score: {0:f}".format(result.classification.score))
r1=result.display_name;
r2=result.classification.score


subject = "Test subject"

msg =response
send_email(subject, msg)
serialized = MessageToJson(response)
with open('results.txt','w') as outfile:
	json.dump(serialized,outfile)
