const API_URL = "http://localhost:8000/api/v1/assets";

export interface Asset {
  id?: number;
  name: string;
  type?: string;
  status?: string;
  description?: string;
  quantity?: number;
  base_id?: number;
}

export async function fetchAssets(): Promise<Asset[]> {
  const response = await fetch(API_URL);
  if (!response.ok) {
    throw new Error(`Failed to fetch assets: ${response.statusText}`);
  }
  return response.json();
}

export async function createAsset(asset: Asset): Promise<Asset> {
  const response = await fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(asset),
  });

  if (!response.ok) {
    throw new Error(`Failed to create asset: ${response.statusText}`);
  }

  return response.json();
}
