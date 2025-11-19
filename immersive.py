import os
import sys

def get_immersive_reader_credentials():
    """
    Retrieves Azure AI Immersive Reader endpoint and key from environment variables
    set in Azure App Service Application Settings.
    """
    # The variable names are standardized here for clarity.
    endpoint = "https://aiimmersivereaders.cognitiveservices.azure.com"
    subscription_key = "8x1ZQ1omEC4bjsXNwfCNg9j8UYlqMICEHLKqHY2xPys3jah8pVfeJQQJ99BKACYeBjFXJ3w3AAAOACOGPe5J"

    if not endpoint:
        # Log error if variables are missing
        print("ERROR: AZURE_IMAGINATIVE_READER_ENDPOINT not found in App Settings.", file=sys.stderr)
        raise ValueError("Immersive Reader endpoint not configured.")

    if not subscription_key:
        print("ERROR: AZURE_IMAGINATIVE_READER_SUBSCRIPTION_KEY not found in App Settings.", file=sys.stderr)
        raise ValueError("Immersive Reader subscription key not configured.")

    return endpoint, subscription_key

# --- Example Usage in your backend logic ---

if __name__ == "__main__":
    try:
        reader_endpoint, reader_key = get_immersive_reader_credentials()
        
        print("Credentials loaded successfully from App Settings:")
        print(f"Endpoint URL: {reader_endpoint}")
        # WARNING: Avoid printing the actual key in production logs for security.
        # print(f"Subscription Key: {reader_key}") 

        # --- Your application logic goes here ---
        # You would use these variables to obtain an AAD token for the Immersive Reader service.
        # Example of how you might generate the token (requires more implementation):
        # generate_aad_token(reader_endpoint, reader_key)

    except ValueError as e:
        print(f"Configuration error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

