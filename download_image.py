import requests

"""
"""
def download_png_image(url, save_path):
    """
    Downloads a PNG image from the given URL and saves it to the specified file path.

    Args:
        url (str): The URL of the PNG image to download.
        save_path (str): The local file path where the image will be saved.

    Returns:
        bool: True if the download was successful, False otherwise.
    """
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Get the content of the response (the PNG image data)
            image_data = response.content

            # Save the image data to the specified file
            with open(save_path, 'wb') as file:
                file.write(image_data)

            print(f"Image downloaded and saved to {save_path}")
            return True
        else:
            print(f"Failed to download the image. Status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False
