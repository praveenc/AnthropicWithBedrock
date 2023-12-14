import boto3

def get_inference_parameters(
    model,
):  # return a default set of parameters based on the model's provider
    bedrock_model_provider = model.split(".")[
        0
    ]  # grab the model provider from the first part of the model id

    if bedrock_model_provider == "anthropic":  # Anthropic model
        return {  # anthropic
            "max_tokens_to_sample": 1000,
            "temperature": 0.0,
            "top_k": 250,
            "top_p": 0.999,
            "stop_sequences": ["\n\nHuman:"],
        }

    elif bedrock_model_provider == "ai21":  # AI21
        return {  # AI21
            "maxTokens": 512,
            "temperature": 0,
            "topP": 0.5,
            "stopSequences": [],
            "countPenalty": {"scale": 0},
            "presencePenalty": {"scale": 0},
            "frequencyPenalty": {"scale": 0},
        }

    elif bedrock_model_provider == "cohere":  # COHERE
        return {
            "max_tokens": 512,
            "temperature": 0,
            "p": 0.01,
            "k": 0,
            "stop_sequences": [],
            "return_likelihoods": "NONE",
        }

    else:  # Amazon
        # For the LangChain Bedrock implementation, these parameters will be added to the
        # textGenerationConfig item that LangChain creates for us
        return {
            "maxTokenCount": 512,
            "stopSequences": [],
            "temperature": 0,
            "topP": 0.9,
        }


def get_model_ids(provider, output_modality):
    """
    Fetch model IDs from AWS Bedrock for specified provider and output modality.

    Args:
    provider (str): The provider of the model.
    output_modality (str): The output modality of the model.

    Returns:
    list: A list of model IDs that match the criteria.
    """
    b_client = boto3.client("bedrock", region_name="us-west-2")
    models = b_client.list_foundation_models()['modelSummaries']
    model_ids = [model['modelId'] for model in models if model['providerName'] == provider and model['outputModalities'] == [output_modality]]
    
    return model_ids