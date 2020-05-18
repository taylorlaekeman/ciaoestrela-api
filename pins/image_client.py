from google.cloud import storage


class ImageClient():
    def __init__(self):
        client = storage.Client()
        self.bucket = client.bucket('images.ciaoestrela.co')

    def upload(self, name, image):
        blob = self.bucket.blob(name)
        blob.upload_from_file(image)
        return 'https://images.ciaoestrela.co/{}'.format(name)
