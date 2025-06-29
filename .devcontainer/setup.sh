#!/bin/bash

# Update package list
sudo apt update -y

# Install dependencies
sudo apt install -y curl

# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Verify installation
ollama --version

# Ensure Ollama service is running
sudo systemctl enable --now ollama || echo "Ollama service may require manual start."