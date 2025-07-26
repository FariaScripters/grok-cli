"""Model configurations and pricing information for Grok models."""
from dataclasses import dataclass
from typing import Optional


@dataclass
class ModelPricing:
    text_input: float
    text_output: float
    image_input: Optional[float] = None
    image_output: Optional[float] = None


MODELS = {
    "grok-4": ModelPricing(
        text_input=3.00,
        text_output=15.00,
    ),
    "grok-3": ModelPricing(
        text_input=3.00,
        text_output=15.00,
    ),
    "grok-3-fast": ModelPricing(
        text_input=5.00,
        text_output=25.00,
    ),
    "grok-3-mini": ModelPricing(
        text_input=0.30,
        text_output=0.50,
    ),
    "grok-3-mini-fast": ModelPricing(
        text_input=0.60,
        text_output=4.00,
    ),
    "grok-2-vision": ModelPricing(
        text_input=2.00,
        text_output=10.00,
        image_input=2.00,
    ),
    "grok-2": ModelPricing(
        text_input=2.00,
        text_output=10.00,
    ),
    "grok-2-image": ModelPricing(
        text_output=0.07,  # per image
    ),
}

DEFAULT_MODEL = "grok-3"
FAST_MODEL = "grok-3-fast"
VISION_MODEL = "grok-2-vision"
IMAGE_MODEL = "grok-2-image"

def get_model_pricing(model: str) -> ModelPricing:
    """Get pricing information for a model."""
    return MODELS.get(model, MODELS[DEFAULT_MODEL])

def list_available_models():
    """Return a list of available model IDs."""
    return list(MODELS.keys())
