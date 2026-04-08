"""
caller.py  –  Real Model API Caller with Full Provenance Logging
================================================================
Supports: Anthropic (Claude), OpenAI (GPT), Ollama (local LLaMA/Mistral)

EVERY call logs:
  - UUID (unique per call)
  - UTC timestamp
  - Exact prompt sent
  - Full raw response
  - Token counts (proof of real execution)
  - Latency in ms
  - Model name + provider
"""

import os, time, uuid, json
from datetime import datetime, timezone
from pathlib import Path


LOG_DIR = Path("logs/raw_calls")
LOG_DIR.mkdir(parents=True, exist_ok=True)
RUNLOG   = None   # set by experiment.py


def _write_log(record: dict):
    """Write one JSON file per call (crash-safe) + append to run log."""
    call_path = LOG_DIR / f"{record['call_id']}.json"
    with open(call_path, "w") as f:
        json.dump(record, f, indent=2)
    if RUNLOG:
        with open(RUNLOG, "a") as f:
            f.write(json.dumps(record) + "\n")


# ─────────────────────────────────────────────────────────────────────────────
# Anthropic  (Claude)
# ─────────────────────────────────────────────────────────────────────────────
def call_anthropic(messages: list[dict], model: str, temperature: float, max_tokens: int) -> dict:
    import anthropic
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        raise EnvironmentError("Set ANTHROPIC_API_KEY environment variable.")
    client = anthropic.Anthropic(api_key=api_key)
    call_id  = str(uuid.uuid4())
    ts       = datetime.now(timezone.utc).isoformat()
    t0       = time.perf_counter()
    try:
        r = client.messages.create(
            model=model, max_tokens=max_tokens,
            messages=messages, temperature=temperature,
        )
        latency_ms = round((time.perf_counter() - t0) * 1000)
        record = {
            "call_id": call_id, "timestamp_utc": ts,
            "provider": "anthropic", "model": model,
            "temperature": temperature, "max_tokens": max_tokens,
            "prompt_messages": messages,
            "response_text": r.content[0].text.strip(),
            "input_tokens":  r.usage.input_tokens,
            "output_tokens": r.usage.output_tokens,
            "latency_ms": latency_ms, "error": None,
        }
    except Exception as e:
        latency_ms = round((time.perf_counter() - t0) * 1000)
        record = {
            "call_id": call_id, "timestamp_utc": ts,
            "provider": "anthropic", "model": model,
            "temperature": temperature, "max_tokens": max_tokens,
            "prompt_messages": messages,
            "response_text": "", "input_tokens": 0, "output_tokens": 0,
            "latency_ms": latency_ms, "error": str(e),
        }
    _write_log(record)
    return record


# ─────────────────────────────────────────────────────────────────────────────
# OpenAI  (GPT-4o, GPT-3.5-Turbo)
# ─────────────────────────────────────────────────────────────────────────────
def call_openai(messages: list[dict], model: str, temperature: float, max_tokens: int) -> dict:
    import openai
    api_key = os.environ.get("OPENAI_API_KEY", "")
    if not api_key:
        raise EnvironmentError("Set OPENAI_API_KEY environment variable.")
    client = openai.OpenAI(api_key=api_key)
    call_id  = str(uuid.uuid4())
    ts       = datetime.now(timezone.utc).isoformat()
    t0       = time.perf_counter()
    try:
        r = client.chat.completions.create(
            model=model, messages=messages,
            temperature=temperature, max_tokens=max_tokens,
        )
        latency_ms = round((time.perf_counter() - t0) * 1000)
        record = {
            "call_id": call_id, "timestamp_utc": ts,
            "provider": "openai", "model": model,
            "temperature": temperature, "max_tokens": max_tokens,
            "prompt_messages": messages,
            "response_text": r.choices[0].message.content.strip(),
            "input_tokens":  r.usage.prompt_tokens,
            "output_tokens": r.usage.completion_tokens,
            "latency_ms": latency_ms, "error": None,
        }
    except Exception as e:
        latency_ms = round((time.perf_counter() - t0) * 1000)
        record = {
            "call_id": call_id, "timestamp_utc": ts,
            "provider": "openai", "model": model,
            "temperature": temperature, "max_tokens": max_tokens,
            "prompt_messages": messages,
            "response_text": "", "input_tokens": 0, "output_tokens": 0,
            "latency_ms": latency_ms, "error": str(e),
        }
    _write_log(record)
    return record


# ─────────────────────────────────────────────────────────────────────────────
# Ollama  (local LLaMA-3, Mistral — FREE, no API key needed)
# ─────────────────────────────────────────────────────────────────────────────
def call_ollama(messages: list[dict], model: str, temperature: float, max_tokens: int,
                base_url: str = "http://localhost:11434") -> dict:
    import requests
    prompt   = "\n\n".join(m["content"] for m in messages)
    call_id  = str(uuid.uuid4())
    ts       = datetime.now(timezone.utc).isoformat()
    t0       = time.perf_counter()
    try:
        resp = requests.post(
            f"{base_url}/api/generate",
            json={"model": model, "prompt": prompt, "stream": False,
                  "options": {"temperature": temperature, "num_predict": max_tokens}},
            timeout=180,
        )
        resp.raise_for_status()
        data = resp.json()
        latency_ms = round((time.perf_counter() - t0) * 1000)
        record = {
            "call_id": call_id, "timestamp_utc": ts,
            "provider": "ollama", "model": model,
            "temperature": temperature, "max_tokens": max_tokens,
            "prompt_messages": messages,
            "response_text": data.get("response", "").strip(),
            "input_tokens":  data.get("prompt_eval_count", 0),
            "output_tokens": data.get("eval_count", 0),
            "latency_ms": latency_ms, "error": None,
        }
    except Exception as e:
        latency_ms = round((time.perf_counter() - t0) * 1000)
        record = {
            "call_id": call_id, "timestamp_utc": ts,
            "provider": "ollama", "model": model,
            "temperature": temperature, "max_tokens": max_tokens,
            "prompt_messages": messages,
            "response_text": "", "input_tokens": 0, "output_tokens": 0,
            "latency_ms": latency_ms, "error": str(e),
        }
    _write_log(record)
    return record


# ─────────────────────────────────────────────────────────────────────────────
# Unified Dispatcher
# ─────────────────────────────────────────────────────────────────────────────
SUPPORTED_MODELS = {
    # Anthropic
    "claude-sonnet-4-20250514": ("anthropic", "claude-sonnet-4-20250514"),
    "claude-3-haiku-20240307":  ("anthropic", "claude-3-haiku-20240307"),
    # OpenAI
    "gpt-4o":          ("openai", "gpt-4o"),
    "gpt-3.5-turbo":   ("openai", "gpt-3.5-turbo"),
    # Ollama (local, free)
    "llama3:8b":       ("ollama", "llama3:8b"),
    "llama3:70b":      ("ollama", "llama3:70b"),
    "mistral:7b":      ("ollama", "mistral:7b"),
    "mistral:latest":  ("ollama", "mistral:latest"),
}


def call_model(messages: list[dict], model_id: str,
               temperature: float = 0.0, max_tokens: int = 1024,
               ollama_url: str = "http://localhost:11434") -> dict:
    """
    Unified model call. Returns a provenance record dict.
    Raises ValueError if model_id is not in SUPPORTED_MODELS.
    """
    if model_id not in SUPPORTED_MODELS:
        raise ValueError(
            f"Unknown model: {model_id!r}\n"
            f"Supported: {list(SUPPORTED_MODELS.keys())}"
        )
    provider, model_name = SUPPORTED_MODELS[model_id]
    if provider == "anthropic":
        return call_anthropic(messages, model_name, temperature, max_tokens)
    elif provider == "openai":
        return call_openai(messages, model_name, temperature, max_tokens)
    elif provider == "ollama":
        return call_ollama(messages, model_name, temperature, max_tokens, ollama_url)
