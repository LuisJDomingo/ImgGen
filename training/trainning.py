import torch
from torch.utils.data import DataLoader
from transformers import CLIPTextModel, CLIPTokenizer
from diffusers import StableDiffusionPipeline, UNet2DConditionModel, PNDMScheduler
from datasets import load_dataset

# Cargar el conjunto de datos
dataset = load_dataset("Rapidata/text-2-image-Rich-Human-Feedback")

# Tokenizador y modelo de texto
tokenizer = CLIPTokenizer.from_pretrained("openai/clip-vit-base-patch32")
text_encoder = CLIPTextModel.from_pretrained("openai/clip-vit-base-patch32")

# Modelo de difusión
model_id = "CompVis/stable-diffusion-v1-4"
unet = UNet2DConditionModel.from_pretrained(model_id, subfolder="unet")
scheduler = PNDMScheduler.from_pretrained(model_id, subfolder="scheduler")

# Pipeline de Stable Diffusion
pipe = StableDiffusionPipeline(
    text_encoder=text_encoder,
    vae=None,  # Puedes usar un VAE preentrenado si lo tienes
    unet=unet,
    scheduler=scheduler,
    tokenizer=tokenizer,
    safety_checker=None,
    feature_extractor=None,
)

# Configurar el optimizador
optimizer = torch.optim.AdamW(pipe.unet.parameters(), lr=1e-5)

# Configurar el DataLoader
def collate_fn(batch):
    texts = [item["text"] for item in batch]
    images = [item["image"] for item in batch]
    inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True)
    return inputs, images

dataloader = DataLoader(dataset, batch_size=4, shuffle=True, collate_fn=collate_fn)

# Entrenamiento
pipe.unet.train()
for epoch in range(10):  # Número de épocas
    for batch in dataloader:
        inputs, images = batch
        optimizer.zero_grad()
        outputs = pipe(**inputs, images=images)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        print(f"Epoch {epoch}, Loss: {loss.item()}")

# Guardar el modelo ajustado
pipe.save_pretrained(r"ImgGen\training")