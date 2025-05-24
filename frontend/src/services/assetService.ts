// src/services/assetService.ts

const API_URL = 'http://localhost:8000/api/assets';

export interface Asset {
  id: number;
  name: string;
  type: string;
  status: string;
  description?: string; 
}

// Fetch all assets
export async function fetchAssets(): Promise<Asset[]> {
  const response = await fetch(API_URL);

  if (!response.ok) {
    throw new Error('Failed to fetch assets');
  }

  const data: Asset[] = await response.json();
  return data;
}

// Create new asset
export async function createAsset(data: { name: string; description: string }) {
  const response = await fetch(API_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });

  if (!response.ok) {
    throw new Error('Failed to create asset');
  }

  return response.json();
}
