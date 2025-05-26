const API_URL = "http://localhost:8000/api/v1/purchases";

export interface Purchase {
  id: number;
  asset_id: number;
  base_id: number;
  quantity: number;
  notes?: string;
  purchased_by?: number;
  purchase_date: string;
}

export async function fetchPurchases(): Promise<Purchase[]> {
  const response = await fetch(API_URL);
  if (!response.ok) {
    throw new Error(`Failed to fetch purchases: ${response.statusText}`);
  }
  return response.json();
}
