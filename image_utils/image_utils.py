import torch
from diffusers import StableDiffusionXLPipeline
from dotenv

class ImageGen:
    def generate_image(self,prompt):
        pipeline = StableDiffusionXLPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0",torch_dtype=torch.float16)
        image = pipeline(prompt=self.prompt).images
        return image

    def url_gen(self,api_key):
