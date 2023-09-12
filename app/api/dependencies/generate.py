import torch
from diffusers import DiffusionPipeline

enable_cuda = False
model_id = "runwayml/stable-diffusion-v1-5"
# pipeline = DiffusionPipeline.from_pretrained(model_id, use_safetensors=True)

# if torch.cuda.is_available() and enable_cuda:
#     pipeline = pipeline.to("cuda")

def create_image(prompt: str) -> bytes:
    # Generate an image based on the received text
    generator = torch.Generator("cuda").manual_seed(0)
    image = pipeline(prompt, generator=generator).images[0]
    return image
