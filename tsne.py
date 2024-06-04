import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from transformers import RobertaTokenizer, RobertaModel
import torch
from mpl_toolkits.mplot3d import Axes3D

# Load the JSONL file
file_path = 'test/data/train.jsonl'
commit_messages = []
labels = []

# Read JSONL file
with open(file_path, 'r') as file:
    for line in file:
        data = json.loads(line)
        commit_messages.append(data['commit_message'])
        labels.append(data['target'])

# Ensure we have the required number of messages and labels
commit_messages = commit_messages[:2000]
labels = labels[:2000]

# Verify that the length of commit_messages and labels are the same
assert len(commit_messages) == len(labels), "The number of commit messages and labels must be the same."

# Load RoBERTa model and tokenizer
tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
model = RobertaModel.from_pretrained('roberta-base')

# Function to get embeddings from RoBERTa
def get_roberta_embeddings(texts):
    inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    # Use the embeddings from the [CLS] token
    embeddings = outputs.last_hidden_state[:, 0, :].numpy()
    return embeddings

# Get embeddings for commit messages
X = get_roberta_embeddings(commit_messages)

# Step 3: Apply t-SNE with adjusted parameters
tsne = TSNE(n_components=2, perplexity=50, n_iter=2000, init='pca', learning_rate=200, random_state=42)
X_embedded = tsne.fit_transform(X)

# Step 4: 2D Visualization
plt.figure(figsize=(12, 8))
# Convert labels to a numpy array for easier indexing
labels = np.array(labels)
# Plot group 0
plt.scatter(X_embedded[labels == 0, 0], X_embedded[labels == 0, 1], c='blue', label='Not Performance Related (0)')
# Plot group 1
plt.scatter(X_embedded[labels == 1, 0], X_embedded[labels == 1, 1], c='red', label='Performance Related (1)')
plt.title('t-SNE Visualization of Commit Message Embeddings (2D)')
plt.xlabel('t-SNE Dimension 1')
plt.ylabel('t-SNE Dimension 2')
plt.legend()
# Save the plot to a file
plt.savefig('tsne_commit_messages_2000_2D_before.png')
plt.close()

# Step 5: 3D Visualization
tsne_3d = TSNE(n_components=3, perplexity=30, n_iter=2000, init='pca', learning_rate=200, random_state=42)
X_embedded_3d = tsne_3d.fit_transform(X)

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
# Plot group 0
ax.scatter(X_embedded_3d[labels == 0, 0], X_embedded_3d[labels == 0, 1], X_embedded_3d[labels == 0, 2], c='blue', label='Not Performance Related (0)')
# Plot group 1
ax.scatter(X_embedded_3d[labels == 1, 0], X_embedded_3d[labels == 1, 1], X_embedded_3d[labels == 1, 2], c='red', label='Performance Related (1)')
ax.set_title('t-SNE Visualization of Commit Message Embeddings (3D)')
ax.set_xlabel('t-SNE Dimension 1')
ax.set_ylabel('t-SNE Dimension 2')
ax.set_zlabel('t-SNE Dimension 3')
ax.legend()
# Save the plot to a file
plt.savefig('tsne_commit_messages_2000_3D.png')
plt.close()
