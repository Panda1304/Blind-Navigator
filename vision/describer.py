from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

print("Loading TinyLLaMA on CPU...")
tokenizer = AutoTokenizer.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")
model = AutoModelForCausalLM.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, device=0)

def describe_position(x_center, frame_width):
    if x_center < frame_width / 3:
        return "on your left"
    elif x_center < 2 * frame_width / 3:
        return "ahead"
    else:
        return "on your right"

def estimate_distance(x1, x2):
    width_pixels = x2 - x1
    return round(2.0 * (1 / (width_pixels / 100)), 1)  

def describe_scene_tinyllama(detections, frame_width, use_llm=True):
    if not detections:
        return "I couldn't detect anything in your surroundings."

    if not use_llm:
        description = []
        for det in detections:
            label = det["label"]
            x1, _, x2, _ = det["bbox"]
            x_center = (x1 + x2) / 2
            position = describe_position(x_center, frame_width)
            distance = estimate_distance(x1, x2)
            description.append(f"{label} {position}, about {distance} meters away")
        return ". ".join(description)

    summary_parts = []
    for det in detections:
        label = det["label"]
        x1, _, x2, _ = det["bbox"]
        x_center = (x1 + x2) / 2
        pos = describe_position(x_center, frame_width)
        dist = estimate_distance(x1, x2)
        summary_parts.append(f"{label} {pos} approximately {dist} meters")
    grounded_summary = ", ".join(summary_parts)

    prompt = f"""<|system|>.Be brief and factual. You are describing surroundings in points to a blind user in real-time.</s>
<|user|>Describe all these facts: {grounded_summary}</s>
<|assistant|>"""




    response = pipe(prompt, max_new_tokens=60, do_sample=False, temperature=0.7)[0]["generated_text"]
    description = response.split("<|assistant|>")[-1].strip()

    # ✅ Clean up response
    return description
