import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

def stablelm_initialization():
    # Preload the torch model here
    model_name = "stabilityai/stablelm-tuned-alpha-7b"  # @param ["stabilityai/stablelm-tuned-alpha-7b", "stabilityai/stablelm-base-alpha-7b", "stabilityai/stablelm-tuned-alpha-3b", "stabilityai/stablelm-base-alpha-3b"]

    print(f"Using `{model_name}`")

    # Select "big model inference" parameters
    torch_dtype = "float16"  # @param ["float16", "bfloat16", "float"]
    load_in_8bit = False  # @param {type:"boolean"}
    device_map = "auto"

    print(f"Loading with: `{torch_dtype=}, {load_in_8bit=}, {device_map=}`")

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=getattr(torch, torch_dtype),
        load_in_8bit=load_in_8bit,
        device_map=device_map,
        offload_folder="./offload",
    )
    return tokenizer, model