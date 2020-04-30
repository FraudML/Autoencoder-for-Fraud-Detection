class AutoencoderArnProvider:
    
    @staticmethod
    def get_algorithm_arn(current_region):
        mapping = {
          "us-east-2" : "arn:aws:sagemaker:us-east-2:587740566727:algorithm/autoencoder-1588167541"
        }
        return mapping[current_region]
