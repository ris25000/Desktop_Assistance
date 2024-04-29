
def gpt_response(prompt, client):
    """
    Generate a response using OpenAI's GPT-4 model based on the given prompt.

    Args:
    - prompt (str): The prompt to be used for generating the response.
    - client: An instance of the OpenAI API client.

    Returns:
    - str: The generated response.
    """
    # Generate a response using OpenAI's GPT-4 model
    response = client.chat.completions.create(
        model="gpt-4",  # Specify the GPT-4 model for response generation
        messages=[{"role": "user", "content": prompt}],  # Provide the prompt as user input
    )

    # Extract and return the content of the generated response
    return response.choices[0].message.content
