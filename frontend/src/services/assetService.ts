const API_URL = "http://localhost:8000/api/v1/assets";

export interface Asset {
  id: number;
  name: string;
  type: string;
  status: string;
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
