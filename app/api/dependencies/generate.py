import torch
from diffusers import DiffusionPipeline

device = "cpu"
model_id = "runwayml/stable-diffusion-v1-5"
pipeline = DiffusionPipeline.from_pretrained(model_id, use_safetensors=True)

def create_image(prompt: str) -> bytes:
    # Generate an image based on the received text
    generator = torch.Generator(device="cpu").manual_seed(0)
    image = pipeline(prompt, generator=generator).images[0]
    return image
