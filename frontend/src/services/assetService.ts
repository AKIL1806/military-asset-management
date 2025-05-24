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
  try {
    const response = await fetch(API_URL);

    if (!response.ok) {
      throw new Error(`Failed to fetch assets: ${response.statusText}`);
    }

    const data: Asset[] = await response.json();
    return data;
  } catch (error) {
    console.error("fetchAssets error:", error);
    throw error;
  }
}

// Create new asset
export async function createAsset(data: {
  name: string;
  description: string;
}): Promise<Asset> {
  try {
    const response = await fetch(API_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw new Error(`Failed to create asset: ${response.statusText}`);
    }

    const created: Asset = await response.json();
    return created;
  } catch (error) {
    console.error("createAsset error:", error);
    throw error;
  }
}
